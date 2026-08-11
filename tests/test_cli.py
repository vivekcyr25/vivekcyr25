#!/usr/bin/env python3
"""Unit tests for scripts/profile_cli.py."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.profile_cli import run_cli


class TestProfileCLI(unittest.TestCase):
    """Tests for unified profile CLI runner."""

    def test_cli_help(self):
        code = run_cli([])
        self.assertEqual(code, 1)

    def test_cli_validate(self):
        code = run_cli(["validate"])
        self.assertEqual(code, 0)

    def test_cli_audit(self):
        code = run_cli(["audit"])
        self.assertEqual(code, 0)

    def test_cli_export(self):
        code = run_cli(["export"])
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
