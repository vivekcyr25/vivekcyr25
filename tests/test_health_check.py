#!/usr/bin/env python3
"""Unit tests for scripts/health_check.py."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.health_check import check_config, check_readme_assets, check_scripts_import


class TestHealthCheck(unittest.TestCase):
    """Verify health check functions work correctly."""

    def test_config_is_valid(self):
        issues = check_config()
        self.assertEqual(issues, [], f"Config issues found: {issues}")

    def test_readme_assets_exist(self):
        issues = check_readme_assets()
        self.assertEqual(issues, [], f"Missing assets: {issues}")

    def test_scripts_importable(self):
        issues = check_scripts_import()
        self.assertEqual(issues, [], f"Import issues: {issues}")


if __name__ == "__main__":
    unittest.main()