#!/usr/bin/env python3
"""Unit tests for scripts/constants.py."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.constants import (
    DASHBOARD_WIDTH,
    DASHBOARD_HEIGHT,
    DEFAULT_SVG_VIEWBOX,
    SVG_XMLNS_NAMESPACE,
    MAX_SVG_SIZE_KB,
    MIN_SVG_SIZE_BYTES,
    GITHUB_API_BASE,
)


class TestSVGDimensions(unittest.TestCase):
    """Verify SVG dimension constants are sensible."""

    def test_dashboard_dimensions_positive(self):
        self.assertGreater(DASHBOARD_WIDTH, 0)
        self.assertGreater(DASHBOARD_HEIGHT, 0)

    def test_dashboard_wider_than_tall(self):
        self.assertGreater(DASHBOARD_WIDTH, DASHBOARD_HEIGHT)

    def test_svg_namespace_and_viewbox(self):
        self.assertEqual(SVG_XMLNS_NAMESPACE, "http://www.w3.org/2000/svg")
        self.assertIn("0 0 850 580", DEFAULT_SVG_VIEWBOX)



class TestValidationThresholds(unittest.TestCase):
    """Ensure validation thresholds are logically consistent."""

    def test_max_greater_than_min(self):
        self.assertGreater(MAX_SVG_SIZE_KB * 1024, MIN_SVG_SIZE_BYTES)


class TestAPIConstants(unittest.TestCase):
    """Check API URL constants."""

    def test_github_api_base(self):
        self.assertTrue(GITHUB_API_BASE.startswith("https://"))


if __name__ == "__main__":
    unittest.main()