"""Behavior checks for the teaching probe; no network or external packages."""
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
from contextlib import contextmanager
import shutil
import uuid
import unittest

ROOT = Path(__file__).resolve().parent.parent
SCRIPT = ROOT / "scripts" / "inspect_environment.py"
spec = importlib.util.spec_from_file_location("environment_probe", SCRIPT)
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)


@contextmanager
def isolated_directory():
    # Keep disposable fixtures inside this example, including on restricted hosts.
    directory = ROOT / (".test-work-" + uuid.uuid4().hex)
    directory.mkdir()
    try:
        yield str(directory)
    finally:
        resolved = directory.resolve()
        if resolved.parent != ROOT.resolve() or not resolved.name.startswith(".test-work-"):
            raise RuntimeError("Refusing cleanup outside the example root")
        shutil.rmtree(resolved)


class SettingsTests(unittest.TestCase):
    def test_documented_defaults(self):
        self.assertEqual(probe.read_settings({}),
                         {"app_env": "development", "debug": False})

    def test_allowed_combinations(self):
        for env in ("development", "test", "production"):
            for raw, expected in (("true", True), ("false", False)):
                with self.subTest(env=env, debug=raw):
                    values = {"APP_ENV": env, "APP_DEBUG": raw}
                    if env == "production" and expected:
                        with self.assertRaises(ValueError):
                            probe.read_settings(values)
                    else:
                        self.assertEqual(probe.read_settings(values),
                                         {"app_env": env, "debug": expected})

    def test_case_and_surrounding_whitespace(self):
        self.assertEqual(probe.read_settings(
            {"APP_ENV": " TEST ", "APP_DEBUG": " False "}),
            {"app_env": "test", "debug": False})

    def test_invalid_values_are_rejected(self):
        for key, values in (
            ("APP_ENV", ("", "stage", "prod", "unknown")),
            ("APP_DEBUG", ("", "0", "1", "yes", "off", "falsex")),
        ):
            for value in values:
                with self.subTest(key=key, value=value):
                    with self.assertRaises(ValueError):
                        probe.read_settings({key: value})


class CommandTests(unittest.TestCase):
    def invoke(self, directory, values=None, args=()):
        env = os.environ.copy()
        env.pop("APP_ENV", None)
        env.pop("APP_DEBUG", None)
        env["UNRELATED_PRIVATE_VALUE"] = "must-not-appear-987654321"
        env.update(values or {})
        return subprocess.run([sys.executable, str(SCRIPT), *args],
                              cwd=directory, env=env, text=True,
                              capture_output=True, timeout=20)

    def test_paths_and_false_value(self):
        with isolated_directory() as directory:
            result = self.invoke(directory, {"APP_DEBUG": "false"})
            self.assertEqual(result.returncode, 0, result.stderr)
            data = json.loads(result.stdout)
            self.assertEqual(Path(data["project_root"]), ROOT)
            self.assertEqual(Path(data["working_directory"]), Path(directory))
            self.assertIs(data["settings"]["debug"], False)
            self.assertEqual(data["python_executable"], sys.executable)
            self.assertEqual(set(data["packages"]), {"Django", "psycopg"})
            self.assertNotIn("must-not-appear-987654321", result.stdout + result.stderr)

    def test_invalid_setting_does_not_echo_input(self):
        sentinel = "private-invalid-setting-123456"
        with isolated_directory() as directory:
            for key in ("APP_ENV", "APP_DEBUG"):
                with self.subTest(key=key):
                    result = self.invoke(directory, {key: sentinel})
                    self.assertEqual(result.returncode, 2)
                    self.assertEqual(result.stdout, "")
                    self.assertNotIn(sentinel, result.stderr)
                    self.assertIn(key, result.stderr)

    def test_production_debug_is_rejected(self):
        with isolated_directory() as directory:
            result = self.invoke(directory,
                                 {"APP_ENV": "production", "APP_DEBUG": "true"})
            self.assertEqual(result.returncode, 2)
            self.assertEqual(result.stdout, "")

    def test_dotenv_is_not_implicitly_loaded(self):
        with isolated_directory() as directory:
            Path(directory, ".env").write_text("APP_DEBUG=true\n", encoding="utf-8")
            result = self.invoke(directory)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIs(json.loads(result.stdout)["settings"]["debug"], False)

    def test_target_check_matches_actual_interpreter(self):
        with isolated_directory() as directory:
            result = self.invoke(directory, args=("--require-target",))
            expected = sys.version_info[:2] == (3, 14) and sys.prefix != sys.base_prefix
            self.assertEqual(result.returncode, 0 if expected else 1)
            data = json.loads(result.stdout)
            self.assertEqual(data["in_virtualenv"], sys.prefix != sys.base_prefix)
            self.assertEqual(data["python314"], sys.version_info[:2] == (3, 14))
            if not expected:
                self.assertIn("Target requires", result.stderr)


if __name__ == "__main__":
    unittest.main()
