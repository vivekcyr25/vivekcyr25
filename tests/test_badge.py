#!/usr/bin/env python3
"""Unit tests for scripts/generate_badge.py."""

import os
import sys
import unittest
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.generate_badge import generate_badge_svg


class TestBadgeGenerator(unittest.TestCase):
    """Tests for badge SVG generation."""

    def test_badge_svg_valid_xml(self):
        svg_str = generate_badge_svg("BUILD", "PASSING", "#00FF88")
        try:
            root = ET.fromstring(svg_str)
            self.assertEqual(root.tag, "{http://www.w3.org/2000/svg}svg")
        except ET.ParseError as e:
            self.fail(f"Generated badge SVG is not valid XML: {e}")

    def test_badge_svg_contains_labels(self):
        svg_str = generate_badge_svg("STATUS", "ONLINE", "#00F2FF")
        self.assertIn("STATUS", svg_str)
        self.assertIn("ONLINE", svg_str)
        self.assertIn("#00F2FF", svg_str)

    def test_badge_svg_has_viewbox(self):
        svg_str = generate_badge_svg("TEST", "VALUE")
        root = ET.fromstring(svg_str)
        self.assertIn("viewBox", root.attrib)


if __name__ == "__main__":
    unittest.main()
