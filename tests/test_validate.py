#!/usr/bin/env python3
"""Unit tests for scripts/validate_svgs.py."""

import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.validate_svgs import validate_svg


class TestValidateSVG(unittest.TestCase):
    """Test SVG validation logic."""

    def _write_temp_svg(self, content):
        fd, path = tempfile.mkstemp(suffix=".svg")
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(content)
        return path

    def test_valid_svg_no_issues(self):
        svg = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"></svg>'
        path = self._write_temp_svg(svg)
        try:
            issues = validate_svg(path)
            self.assertEqual(issues, [])
        finally:
            os.unlink(path)

    def test_missing_viewbox(self):
        svg = '<svg xmlns="http://www.w3.org/2000/svg"></svg>'
        path = self._write_temp_svg(svg)
        try:
            issues = validate_svg(path)
            self.assertTrue(any("viewBox" in i for i in issues))
        finally:
            os.unlink(path)

    def test_invalid_xml(self):
        path = self._write_temp_svg("<not-valid-xml>")
        try:
            issues = validate_svg(path)
            self.assertTrue(len(issues) > 0)
        finally:
            os.unlink(path)


if __name__ == "__main__":
    unittest.main()