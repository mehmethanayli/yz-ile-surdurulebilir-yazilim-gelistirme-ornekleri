"""Tests distinguish the planted defect from the retained settings contract."""
import argparse
import contextlib
import io
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
import reproduce
import settings_fixed
import settings_faulty


class SettingsTests(unittest.TestCase):
    def test_defaults(self):
        self.assertEqual(settings_fixed.read_settings({}), {"app_env": "development", "debug": False})

    def test_all_allowed_combinations(self):
        for env in ("development", "test", "production"):
            for raw, expected in (("true", True), ("false", False)):
                with self.subTest(env=env, raw=raw):
                    values = {"APP_ENV": env, "APP_DEBUG": raw}
                    if env == "production" and expected:
                        with self.assertRaises(ValueError): settings_fixed.read_settings(values)
                    else:
                        self.assertEqual(settings_fixed.read_settings(values), {"app_env": env, "debug": expected})

    def test_normalization(self):
        self.assertEqual(settings_fixed.read_settings({"APP_ENV": " TEST ", "APP_DEBUG": " False "}),
                         {"app_env": "test", "debug": False})

    def test_invalid_values(self):
        for key, values in (("APP_ENV", ("", "stage", "prod", "unknown")),
                            ("APP_DEBUG", ("", "0", "1", "yes", "off", "falsex"))):
            for value in values:
                with self.subTest(key=key, value=value):
                    with self.assertRaises(ValueError): settings_fixed.read_settings({key: value})

    def test_faulty_false_is_wrong_without_exception(self):
        self.assertIs(settings_faulty.read_settings({"APP_ENV": "test", "APP_DEBUG": "false"})["debug"], True)
        self.assertIs(settings_fixed.read_settings({"APP_ENV": "test", "APP_DEBUG": "false"})["debug"], False)

    def test_faulty_production_false_is_rejected(self):
        values = {"APP_ENV": "production", "APP_DEBUG": "false"}
        with self.assertRaisesRegex(ValueError, "must be false in production"):
            settings_faulty.read_settings(values)
        self.assertEqual(settings_fixed.read_settings(values), {"app_env": "production", "debug": False})

    def test_unexpected_error_is_not_swallowed(self):
        with patch.object(reproduce, "run_case", side_effect=RuntimeError("synthetic defect")):
            with self.assertRaisesRegex(RuntimeError, "synthetic defect"):
                reproduce.main([])


class CommandTests(unittest.TestCase):
    def invoke(self, *args, input_text=None):
        return subprocess.run([sys.executable, str(ROOT / "reproduce.py"), *args],
                              text=True, capture_output=True, timeout=20, input=input_text)

    def test_fixed_and_faulty_same_input(self):
        good = self.invoke("--variant", "fixed")
        bad = self.invoke("--variant", "faulty")
        self.assertEqual(good.returncode, 0, good.stderr)
        self.assertEqual(json.loads(good.stdout), {"app_env": "production", "debug": False})
        self.assertEqual(good.stderr, "")
        self.assertEqual(bad.returncode, 2)
        self.assertEqual(bad.stdout, "")
        self.assertIn("APP_DEBUG must be false in production.", bad.stderr)

    def test_guard_remains_after_fix(self):
        result = self.invoke("--debug", "true")
        self.assertEqual(result.returncode, 2)
        self.assertEqual(result.stdout, "")

    def test_trace_has_call_chain(self):
        result = self.invoke("--variant", "faulty", "--trace")
        self.assertEqual(result.returncode, 1)
        self.assertEqual(result.stdout, "")
        for frame in ("main", "run_case", "load_settings", "read_settings", "ValueError"):
            self.assertIn(frame, result.stderr)

    def test_logging_is_separate_and_does_not_echo_invalid_input(self):
        good = self.invoke("--log")
        self.assertEqual(good.returncode, 0)
        self.assertEqual(json.loads(good.stdout)["debug"], False)
        self.assertIn("event=settings_loaded", good.stderr)
        sentinel = "private-marker-93847"
        bad = self.invoke("--log", "--debug", sentinel)
        self.assertEqual(bad.returncode, 2)
        self.assertEqual(bad.stdout, "")
        self.assertIn("event=settings_rejected", bad.stderr)
        self.assertNotIn(sentinel, bad.stdout + bad.stderr)

    def test_minimal_reproduction(self):
        result = subprocess.run([sys.executable, str(ROOT / "minimal_repro.py")],
                                text=True, capture_output=True, timeout=20)
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "'false' True False")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
