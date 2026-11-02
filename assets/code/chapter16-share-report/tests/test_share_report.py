"""Contract tests for the optional sharing view; no dependency or network needed."""
from copy import deepcopy
import json
import sys
import unittest
import test_environment as baseline

isolated_directory = baseline.isolated_directory
probe = baseline.probe


class ShareSchemaTests(unittest.TestCase):
    def test_exact_schema_excludes_future_and_nested_fields(self):
        source = {
            "project_root": "private-root", "working_directory": "private-cwd",
            "python_executable": "private-executable", "future_path": "private-future",
            "python_version": "3.13.7", "in_virtualenv": False, "python314": False,
            "settings": {"app_env": "test", "debug": False, "private": "private-setting"},
            "packages": {"Django": None, "psycopg": None, "private": "private-package"},
        }
        before = deepcopy(source)
        expected = {
            "python_version": "3.13.7", "in_virtualenv": False, "python314": False,
            "settings": {"app_env": "test", "debug": False},
            "packages": {"Django": None, "psycopg": None},
        }
        actual = probe.share_report(source)
        self.assertEqual(actual, expected)
        self.assertEqual(source, before)
        self.assertNotIn("private-", json.dumps(actual))
        actual["settings"]["debug"] = True
        self.assertEqual(source, before)


class ShareCommandTests(unittest.TestCase):
    # Reuse only the subprocess fixture, not its already collected test methods.
    invoke = baseline.CommandTests.invoke

    def test_default_and_share_differ_only_by_selected_fields(self):
        with isolated_directory() as directory:
            ordinary = self.invoke(directory)
            shared = self.invoke(directory, args=("--share",))
            self.assertEqual((ordinary.returncode, shared.returncode), (0, 0))
            local = json.loads(ordinary.stdout)
            public = json.loads(shared.stdout)
            self.assertEqual(set(local), {"project_root", "working_directory",
                "python_executable", "python_version", "in_virtualenv", "python314",
                "settings", "packages"})
            self.assertEqual(set(public), {"python_version", "in_virtualenv",
                                          "python314", "settings", "packages"})
            for key in public:
                self.assertEqual(public[key], local[key])
            for key in ("project_root", "working_directory", "python_executable"):
                self.assertNotIn(key, public)
            self.assertNotIn(directory, shared.stdout)
            self.assertEqual(shared.stderr, "")

    def test_share_preserves_both_boolean_values(self):
        with isolated_directory() as directory:
            for value, expected in (("false", False), ("true", True)):
                with self.subTest(value=value):
                    result = self.invoke(directory, {"APP_ENV": "test", "APP_DEBUG": value},
                                         args=("--share",))
                    self.assertEqual(result.returncode, 0, result.stderr)
                    self.assertIs(json.loads(result.stdout)["settings"]["debug"], expected)

    def test_invalid_settings_still_fail_without_report(self):
        with isolated_directory() as directory:
            for values in ({"APP_ENV": "production", "APP_DEBUG": "true"},
                           {"APP_DEBUG": ""}, {"APP_ENV": "private-invalid-value"}):
                with self.subTest(values=values):
                    result = self.invoke(directory, values, args=("--share",))
                    self.assertEqual(result.returncode, 2)
                    self.assertEqual(result.stdout, "")
                    self.assertNotIn("private-invalid-value", result.stderr)

    def test_share_does_not_weaken_target_check(self):
        with isolated_directory() as directory:
            expected = sys.version_info[:2] == (3, 14) and sys.prefix != sys.base_prefix
            for flags in (("--share", "--require-target"),
                          ("--require-target", "--share")):
                with self.subTest(flags=flags):
                    result = self.invoke(directory, args=flags)
                    self.assertEqual(result.returncode, 0 if expected else 1)
                    self.assertNotIn("python_executable", json.loads(result.stdout))

    def test_help_describes_share_scope(self):
        with isolated_directory() as directory:
            result = self.invoke(directory, args=("--help",))
            self.assertEqual(result.returncode, 0)
            self.assertIn("--share", result.stdout)
            self.assertIn("Omit local paths", result.stdout)
            self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
