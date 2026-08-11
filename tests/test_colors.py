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


class TestGradients(unittest.TestCase):
    """Verify gradient tuple constants."""

    def test_gradient_tuples(self):
        for name in ("GRADIENT_CYAN_PURPLE", "GRADIENT_AMBER_PINK", "GRADIENT_BLUE_GREEN", "GRADIENT_NEON_GLOW"):
            grad = getattr(colors, name)
            self.assertEqual(len(grad), 2, f"{name} should be a 2-tuple")
            self.assertRegex(grad[0], HEX_PATTERN)
            self.assertRegex(grad[1], HEX_PATTERN)


if __name__ == "__main__":
    unittest.main()