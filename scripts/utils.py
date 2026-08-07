#!/usr/bin/env python3
"""
Shared utility functions for profile README automation scripts.
"""

import os
import json
from datetime import datetime, timezone, timedelta

# IST timezone constant
IST = timezone(timedelta(hours=5, minutes=30))


def get_ist_now():
    """Return current datetime in IST timezone."""
    return datetime.now(IST)


def get_ist_today_iso():
    """Return today's date in ISO format (IST)."""
    return get_ist_now().date().isoformat()


def get_assets_dir():
    """Return absolute path to the assets/ directory."""
    return os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "assets"
    )


def load_config():
    """Load configuration from config.json."""
    config_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "config.json"
    )
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def format_date_safe(iso_str):
    """Convert ISO date string to human-readable format (e.g., 'Aug 7')."""
    if not iso_str:
        return ""
    try:
        dt = datetime.strptime(iso_str, "%Y-%m-%d")
        return dt.strftime("%b") + " " + str(dt.day)
    except (ValueError, TypeError):
        return iso_str


def log_sync(status="success", engine="generate_stats.py"):
    """Write a sync log entry."""
    log_path = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        ".stats-sync-log"
    )
    now = get_ist_now().strftime("%Y-%m-%d %H:%M:%S %Z")
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(f"Last sync: {now}\n")
        f.write(f"Status: {status}\n")
        f.write(f"Engine: {engine}\n")
