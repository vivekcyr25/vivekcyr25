#!/usr/bin/env python3
"""Unit tests for scripts/export_stats.py."""

import os
import sys
import json
import csv
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.export_stats import export_stats_json, export_stats_csv


class TestExportStats(unittest.TestCase):
    """Tests for profile statistics export functions."""

    def test_export_stats_json(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as tf:
            tf_path = tf.name

        try:
            export_stats_json(tf_path)
            with open(tf_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            self.assertIn("timestamp", data)
            self.assertIn("username", data)
        finally:
            os.remove(tf_path)

    def test_export_stats_csv(self):
        with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as tf:
            tf_path = tf.name

        try:
            export_stats_csv(tf_path)
            with open(tf_path, "r", encoding="utf-8") as f:
                reader = list(csv.reader(f))
            self.assertGreater(len(reader), 0)
            self.assertEqual(reader[0], ["Metric", "Value"])
        finally:
            os.remove(tf_path)


if __name__ == "__main__":
    unittest.main()
