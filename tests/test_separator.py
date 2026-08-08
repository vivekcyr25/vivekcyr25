#!/usr/bin/env python3
"""Unit tests for scripts/generate_separator.py."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.generate_separator import generate_separator_svg


class TestSeparatorSVG(unittest.TestCase):
    """Validate generated separator SVG content."""

    def setUp(self):
        self.svg = generate_separator_svg()

    def test_is_valid_svg(self):
        self.assertIn("<svg", self.svg)
        self.assertIn("</svg>", self.svg)

    def test_has_xmlns(self):
        self.assertIn('xmlns="http://www.w3.org/2000/svg"', self.svg)

    def test_has_viewbox(self):
        self.assertIn("viewBox", self.svg)

    def test_has_gradient(self):
        self.assertIn("linearGradient", self.svg)

    def test_has_animation(self):
        self.assertIn("<animate", self.svg)

    def test_uses_theme_colors(self):
        self.assertIn("#00F2FF", self.svg)
        self.assertIn("#BC13FE", self.svg)


if __name__ == "__main__":
    unittest.main()