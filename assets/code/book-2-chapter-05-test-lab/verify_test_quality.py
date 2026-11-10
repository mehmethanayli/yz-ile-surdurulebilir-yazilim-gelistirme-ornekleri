"""Contrast weak expectations with a requirement-based regression check.

The line measurement is deliberately narrow: statement-start lines in the one
read_settings function body. It is not coverage.py or branch/path coverage.
"""
import ast
import inspect
import io
import json
from pathlib import Path
import sys
import unittest
from quality_examples import settings_faulty, settings_fixed

reader = settings_faulty.read_settings


class WeakChecks(unittest.TestCase):
    def test_defaults_have_boolean_type(self):
        self.assertIsInstance(reader({})["debug"], bool)

    def test_invalid_environment_is_rejected(self):
        with self.assertRaises(ValueError): reader({"APP_ENV": "invalid"})

    def test_invalid_debug_is_rejected(self):
        with self.assertRaises(ValueError): reader({"APP_DEBUG": "invalid"})

    def test_production_true_is_rejected(self):
        with self.assertRaises(ValueError):
            reader({"APP_ENV": "production", "APP_DEBUG": "true"})


class IndependentExpectation(unittest.TestCase):
    def test_false_means_false(self):
        self.assertIs(reader({"APP_ENV": "test", "APP_DEBUG": "false"})["debug"], False)


def run_suite(case):
    return unittest.TextTestRunner(stream=io.StringIO()).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(case))


def main():
    global reader
    path = Path(inspect.getsourcefile(settings_faulty.read_settings))
    tree = ast.parse(path.read_text(encoding="utf-8"))
    function = next(node for node in tree.body if isinstance(node, ast.FunctionDef))
    # Only this single function's statement-start lines form the denominator.
    denominator = {node.lineno for node in ast.walk(function)
                   if isinstance(node, ast.stmt) and not isinstance(node, ast.FunctionDef)}
    observed = set()
    code = settings_faulty.read_settings.__code__
    def trace(frame, event, arg):
        if frame.f_code is code and event == "line": observed.add(frame.f_lineno)
        return trace
    previous_trace = sys.gettrace()
    reader = settings_faulty.read_settings
    try:
        sys.settrace(trace)
        weak = run_suite(WeakChecks)
    finally:
        sys.settrace(previous_trace)
    strong_bad = run_suite(IndependentExpectation)
    reader = settings_fixed.read_settings
    strong_good = run_suite(IndependentExpectation)
    if not (weak.testsRun == 4 and weak.wasSuccessful()):
        raise AssertionError("Four weak checks should pass the faulty specimen")
    if not (strong_bad.testsRun == 1 and len(strong_bad.failures) == 1 and not strong_bad.errors):
        raise AssertionError("Independent expectation should reject faulty code")
    if not (strong_good.testsRun == 1 and strong_good.wasSuccessful()):
        raise AssertionError("Independent expectation should accept fixed code")
    if not denominator or denominator - observed:
        raise AssertionError("The weak checks should reach every selected statement-start line")
    summary = {"weak_checks_passed_on_faulty": weak.testsRun,
               "selected_statement_start_lines": sorted(denominator),
               "selected_lines_reached": sorted(denominator & observed),
               "selected_line_reach_percent": 100,
               "independent_check_rejected_faulty": True,
               "independent_check_passed_fixed": True,
               "scope": "One function body; not branch, path, product or coverage.py measurement"}
    print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
