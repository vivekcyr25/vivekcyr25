#!/usr/bin/env python3
"""
Profile statistics data exporter.

Exports configured profile metrics and statistics to JSON and CSV formats.
"""

import os
import json
import csv
from typing import Dict, Any

from scripts.utils import load_config, get_project_root, get_ist_today_iso


def export_stats_json(output_path: str) -> None:
    """Export profile configuration stats to JSON format."""
    cfg = load_config()
    stats = {
        "timestamp": get_ist_today_iso(),
        "username": cfg.get("username", "vivekcyr25"),
        "dashboard": cfg.get("dashboard", {}),
        "profile": cfg.get("profile", {})
    }
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2)


def export_stats_csv(output_path: str) -> None:
    """Export profile dashboard metrics to CSV format."""
    cfg = load_config()
    dashboard = cfg.get("dashboard", {})

    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Metric", "Value"])
        for key, val in dashboard.items():
            writer.writerow([key, val])


def main() -> None:
    """Export JSON and CSV statistics files to root."""
    root = get_project_root()
    json_path = os.path.join(root, "stats_summary.json")
    csv_path = os.path.join(root, "stats_summary.csv")

    export_stats_json(json_path)
    export_stats_csv(csv_path)
    print(f"Exported statistics to {json_path} and {csv_path}")


if __name__ == "__main__":
    main()
