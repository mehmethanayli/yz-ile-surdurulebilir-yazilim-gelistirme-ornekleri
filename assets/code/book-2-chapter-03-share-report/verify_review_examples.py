"""Demonstrate that a schema test rejects three deliberately incorrect proposals.

These are teaching mutations, not outputs measured from any particular AI model.
No application file is edited and all fixture values are synthetic.
"""
import io
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent / "tests"))
import test_share_report as cases


def full_report(report):
    return report


def shallow_selection(report):
    return {name: report[name] for name in (
        "python_version", "in_virtualenv", "python314", "settings", "packages")}


def mutating_selection(report):
    for name in ("project_root", "working_directory", "python_executable", "future_path"):
        report.pop(name, None)
    report["settings"].pop("private", None)
    report["packages"].pop("private", None)
    return report


if __name__ == "__main__":
    for proposal in (full_report, shallow_selection, mutating_selection):
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(cases.ShareSchemaTests)
        with patch.object(cases.probe, "share_report", proposal):
            result = unittest.TextTestRunner(stream=io.StringIO()).run(suite)
        if result.testsRun != 1 or len(result.failures) != 1 or result.errors:
            raise AssertionError("Expected one contract failure for " + proposal.__name__)
        print(proposal.__name__ + ": rejected by the contract test")
    print("Three deliberately incorrect proposals rejected; no production code changed.")
