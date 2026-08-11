#!/usr/bin/env python3
"""Unit tests for scripts/inspect_accessibility.py."""

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.inspect_accessibility import check_svg_accessibility


class TestAccessibilityInspector(unittest.TestCase):
    """Tests for SVG accessibility checker."""

    def test_check_svg_with_title(self):
        content = '<svg xmlns="http://www.w3.org/2000/svg"><title>Dashboard</title></svg>'
        with tempfile.NamedTemporaryFile(mode="w", suffix=".svg", delete=False) as tf:
            tf.write(content)
            tf_path = tf.name

        try:
            res = check_svg_accessibility(tf_path)
            self.assertTrue(res["has_title"])
        finally:
            os.remove(tf_path)

    def test_check_svg_with_role_and_aria(self):
        content = '<svg xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Profile Banner"></svg>'
        with tempfile.NamedTemporaryFile(mode="w", suffix=".svg", delete=False) as tf:
            tf.write(content)
            tf_path = tf.name

        try:
            res = check_svg_accessibility(tf_path)
            self.assertTrue(res["has_role"])
            self.assertTrue(res["has_aria_label"])
        finally:
            os.remove(tf_path)


if __name__ == "__main__":
    unittest.main()
