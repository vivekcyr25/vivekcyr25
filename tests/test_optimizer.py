#!/usr/bin/env python3
"""Unit tests for scripts/svg_optimizer.py."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.svg_optimizer import minify_svg_string, analyze_svg, validate_xml_string


class TestSVGOptimizer(unittest.TestCase):
    """Tests for SVG optimization utilities."""

    def test_minify_svg_removes_comments(self):
        raw_svg = '<!-- Comment --><svg><g></g></svg>'
        minified = minify_svg_string(raw_svg)
        self.assertNotIn("<!-- Comment -->", minified)
        self.assertIn("<svg>", minified)

    def test_minify_svg_trims_whitespace(self):
        raw_svg = "  <svg> \n   <rect/> \n </svg> "
        minified = minify_svg_string(raw_svg)
        lines = minified.split("\n")
        self.assertEqual(lines[0], "<svg>")
        self.assertEqual(lines[1], "<rect/>")
        self.assertEqual(lines[2], "</svg>")

    def test_validate_xml_string(self):
        self.assertTrue(validate_xml_string('<svg xmlns="http://www.w3.org/2000/svg"/>'))
        self.assertFalse(validate_xml_string('<invalid_xml>'))


if __name__ == "__main__":
    unittest.main()

