"""Controlled dependency outcomes; no real Django import or installation."""
import unittest
from unittest.mock import patch
import test_environment as baseline


class PackageMetadataTests(unittest.TestCase):
    def test_available_distribution_returns_version(self):
        with patch.object(baseline.probe.metadata, "version", autospec=True, return_value="5.2.8") as version:
            self.assertEqual(baseline.probe.package_version("Django"), "5.2.8")
            version.assert_called_once_with("Django")

    def test_missing_distribution_returns_none(self):
        with patch.object(baseline.probe.metadata, "version", autospec=True,
                          side_effect=baseline.probe.metadata.PackageNotFoundError("Django")):
            self.assertIsNone(baseline.probe.package_version("Django"))

    def test_unexpected_metadata_error_propagates(self):
        with patch.object(baseline.probe.metadata, "version", autospec=True,
                          side_effect=RuntimeError("synthetic metadata failure")):
            with self.assertRaisesRegex(RuntimeError, "synthetic metadata failure"):
                baseline.probe.package_version("Django")
