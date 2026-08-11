#!/usr/bin/env python3
"""Unit tests for scripts/templates.py."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.templates import render_card_rect, render_glowing_dot, render_progress_bar


class TestTemplateComponents(unittest.TestCase):
    """Tests for SVG template renderers."""

    def test_render_card_rect(self):
        rect_svg = render_card_rect(10, 20, 100, 50)
        self.assertIn('x="10"', rect_svg)
        self.assertIn('width="100"', rect_svg)
        self.assertIn('rect', rect_svg)

    def test_render_glowing_dot(self):
        dot_svg = render_glowing_dot(15, 15, 5, "#00FF88")
        self.assertIn('cx="15"', dot_svg)
        self.assertIn('fill="#00FF88"', dot_svg)

    def test_render_progress_bar(self):
        bar_svg = render_progress_bar(0, 0, 200, 10, 50.0)
        self.assertIn('width="100"', bar_svg)


if __name__ == "__main__":
    unittest.main()
