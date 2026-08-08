#!/usr/bin/env python3
"""Integration tests that validate all SVG assets in the repository."""

import os
import sys
import xml.etree.ElementTree as ET
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.utils import get_assets_dir


class TestAllSVGAssets(unittest.TestCase):
    """Run basic validation against every SVG in assets/."""

    @classmethod
    def setUpClass(cls):
        cls.assets_dir = get_assets_dir()
        cls.svg_files = [
            f for f in os.listdir(cls.assets_dir) if f.endswith(".svg")
        ]

    def test_at_least_one_svg_exists(self):
        self.assertGreater(len(self.svg_files), 0, "No SVG files found in assets/")

    def test_all_svgs_parse_as_xml(self):
        for svg_file in self.svg_files:
            path = os.path.join(self.assets_dir, svg_file)
            with self.subTest(file=svg_file):
                try:
                    ET.parse(path)
                except ET.ParseError as e:
                    self.fail(f"{svg_file} failed XML parse: {e}")

    def test_all_svgs_have_svg_root(self):
        for svg_file in self.svg_files:
            path = os.path.join(self.assets_dir, svg_file)
            with self.subTest(file=svg_file):
                tree = ET.parse(path)
                root = tree.getroot()
                self.assertIn("svg", root.tag.lower(),
                              f"{svg_file} root is not <svg>")

    def test_no_svg_exceeds_size_limit(self):
        max_kb = 500
        for svg_file in self.svg_files:
            path = os.path.join(self.assets_dir, svg_file)
            size_kb = os.path.getsize(path) / 1024
            with self.subTest(file=svg_file, size_kb=f"{size_kb:.1f}"):
                self.assertLessEqual(size_kb, max_kb,
                                     f"{svg_file} is {size_kb:.1f} KB (limit: {max_kb} KB)")


if __name__ == "__main__":
    unittest.main()