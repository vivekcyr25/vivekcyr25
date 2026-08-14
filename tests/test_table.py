#!/usr/bin/env python3
"""Unit tests for scripts/generate_table.py."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.generate_table import generate_markdown_table


class TestTableGenerator(unittest.TestCase):
    """Tests for Markdown table generator."""

    def test_empty_inputs(self):
        self.assertEqual(generate_markdown_table([], []), "")
        self.assertEqual(generate_markdown_table(["Header"], []), "")

    def test_basic_table_structure(self):
        headers = ["Col 1", "Col 2"]
        rows = [["Val 1", "Val 2"], ["A", "B"]]
        table = generate_markdown_table(headers, rows)
        lines = table.split("\n")
        self.assertEqual(len(lines), 4)
        self.assertIn("Col 1", lines[0])
        self.assertIn("|-", lines[1])
        self.assertIn("Val 1", lines[2])

    def test_column_alignment_padding(self):
        headers = ["Short", "Very Long Header Name"]
        rows = [["1", "2"]]
        table = generate_markdown_table(headers, rows)
        lines = table.split("\n")
        self.assertEqual(len(lines), 3)

    def test_bold_headers(self):
        headers = ["Tool"]
        rows = [["Python"]]
        table = generate_markdown_table(headers, rows, bold_headers=True)
        self.assertIn("**Tool**", table)


if __name__ == "__main__":
    unittest.main()

