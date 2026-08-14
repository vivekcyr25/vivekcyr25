#!/usr/bin/env python3
"""Unit tests for scripts/colors.py."""

import os
import re
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts import colors


HEX_PATTERN = re.compile(r"^#[0-9A-Fa-f]{6}$")


class TestColorValues(unittest.TestCase):
    """Ensure all color constants are valid hex codes."""

    def _assert_hex(self, value, name):
        self.assertRegex(
            value, HEX_PATTERN,
            f"{name} = '{value}' is not a valid hex color"
        )

    def test_primary_palette(self):
        for name in ("CYAN", "PURPLE", "GREEN", "PINK", "AMBER", "BLUE"):
            self._assert_hex(getattr(colors, name), name)

    def test_background_colors(self):
        for name in ("BG_START", "BG_END", "BG_PANEL", "BG_DARK", "BG_CARD"):
            self._assert_hex(getattr(colors, name), name)

    def test_border_colors(self):
        for name in ("BORDER", "GRID", "BORDER_SUBTLE"):
            self._assert_hex(getattr(colors, name), name)

    def test_text_colors(self):
        for name in ("TEXT_PRIMARY", "TEXT_SECONDARY", "TEXT_MUTED"):
            self._assert_hex(getattr(colors, name), name)

    def test_brand_colors(self):
        for name in (
            "BRAND_LINKEDIN", "BRAND_GMAIL", "BRAND_GITHUB",
            "BRAND_HACKERRANK", "BRAND_HACKEREARTH", "BRAND_ORCID"
        ):
            self._assert_hex(getattr(colors, name), name)


class TestFontConstants(unittest.TestCase):
    """Verify font stack constants exist and are non-empty."""

    def test_font_mono(self):
        self.assertIn("Courier", colors.FONT_MONO)

    def test_font_ui(self):
        self.assertIn("sans-serif", colors.FONT_UI)


class TestColorContrast(unittest.TestCase):
    """Test hex_to_rgb and get_contrast_ratio functions."""

    def test_hex_to_rgb(self):
        self.assertEqual(colors.hex_to_rgb("#FFFFFF"), (255, 255, 255))
        self.assertEqual(colors.hex_to_rgb("#000000"), (0, 0, 0))
        self.assertEqual(colors.hex_to_rgb("#FFF"), (255, 255, 255))

    def test_get_contrast_ratio(self):
        ratio = colors.get_contrast_ratio("#FFFFFF", "#000000")
        self.assertGreaterEqual(ratio, 4.5)


if __name__ == "__main__":
    unittest.main()
