#!/usr/bin/env python3
"""Unit tests for scripts/utils.py."""

import os
import sys
import unittest
from datetime import datetime

# Ensure project root is on path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.utils import (
    format_date_safe,
    format_number_compact,
    get_assets_dir,
    get_ist_now,
    get_ist_today_iso,
    get_project_root,
    load_config,
    IST,
)


class TestFormatNumberCompact(unittest.TestCase):
    """Tests for format_number_compact helper."""

    def test_small_numbers(self):
        self.assertEqual(format_number_compact(0), "0")
        self.assertEqual(format_number_compact(999), "999")

    def test_thousands(self):
        self.assertEqual(format_number_compact(1000), "1k")
        self.assertEqual(format_number_compact(1500), "1.5k")
        self.assertEqual(format_number_compact(25000), "25k")

    def test_millions(self):
        self.assertEqual(format_number_compact(1000000), "1M")
        self.assertEqual(format_number_compact(2400000), "2.4M")



class TestFormatDateSafe(unittest.TestCase):
    """Tests for the format_date_safe helper."""

    def test_valid_date(self):
        self.assertEqual(format_date_safe("2026-01-15"), "Jan 15")

    def test_single_digit_day(self):
        self.assertEqual(format_date_safe("2026-08-07"), "Aug 7")

    def test_empty_string(self):
        self.assertEqual(format_date_safe(""), "")

    def test_none(self):
        self.assertEqual(format_date_safe(None), "")

    def test_invalid_format(self):
        self.assertEqual(format_date_safe("not-a-date"), "not-a-date")


class TestTimezone(unittest.TestCase):
    """Tests for IST timezone utilities."""

    def test_ist_now_has_timezone(self):
        now = get_ist_now()
        self.assertIsNotNone(now.tzinfo)

    def test_ist_today_iso_format(self):
        today = get_ist_today_iso()
        # Should be YYYY-MM-DD
        datetime.strptime(today, "%Y-%m-%d")


class TestPaths(unittest.TestCase):
    """Tests for path helper functions."""

    def test_assets_dir_exists(self):
        self.assertTrue(os.path.isdir(get_assets_dir()))

    def test_project_root_contains_config(self):
        root = get_project_root()
        self.assertTrue(os.path.isfile(os.path.join(root, "config.json")))


class TestLoadConfig(unittest.TestCase):
    """Tests for config loading."""

    def test_config_has_profile(self):
        config = load_config()
        self.assertIn("profile", config)

    def test_config_has_dashboard(self):
        config = load_config()
        self.assertIn("dashboard", config)

from scripts.utils import (
    format_date_safe,
    format_number_compact,
    get_assets_dir,
    get_ist_now,
    get_project_root,
    load_config,
    sanitize_filename,
)


class TestSanitizeFilename(unittest.TestCase):
    """Tests for sanitize_filename helper."""

    def test_sanitize_spaces_and_special_chars(self):
        self.assertEqual(sanitize_filename("My Special-File Name!.svg"), "my_special-file_name_.svg")

    def test_sanitize_clean_string(self):
        self.assertEqual(sanitize_filename("valid_name.png"), "valid_name.png")


if __name__ == "__main__":
    unittest.main()