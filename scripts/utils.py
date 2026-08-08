#!/usr/bin/env python3
"""
Shared utility functions for profile README automation scripts.

Provides IST timezone handling, config loading, date formatting,
and logging for all SVG generators in this project.
"""

import os
import json
from datetime import datetime, timezone, timedelta
from typing import Optional

# IST timezone constant
IST: timezone = timezone(timedelta(hours=5, minutes=30))


def get_ist_now() -> datetime:
    """Return current datetime in IST timezone."""
    return datetime.now(IST)


def get_ist_today_iso() -> str:
    """Return today's date in ISO format (IST)."""
    return get_ist_now().date().isoformat()


def get_assets_dir() -> str:
    """Return absolute path to the assets/ directory."""
    return os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "assets"
    )


def get_project_root() -> str:
    """Return absolute path to the project root directory."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_config() -> dict:
    """Load configuration from config.json.

    Returns:
        dict: Parsed configuration, or empty dict if file not found.
    """
    config_path = os.path.join(get_project_root(), "config.json")
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8-sig") as f:
            return json.load(f)
    return {}


def format_date_safe(iso_str: Optional[str]) -> str:
    """Convert ISO date string to human-readable format (e.g., 'Aug 7').

    Args:
        iso_str: Date string in YYYY-MM-DD format, or None.

    Returns:
        Formatted date string, or original input on failure.
    """
    if not iso_str:
        return ""
    try:
        dt = datetime.strptime(iso_str, "%Y-%m-%d")
        return dt.strftime("%b") + " " + str(dt.day)
    except (ValueError, TypeError):
        return iso_str


def log_sync(status: str = "success", engine: str = "generate_stats.py") -> None:
    """Write a sync log entry to .stats-sync-log.

    Args:
        status: Sync result status string.
        engine: Name of the generator script that ran.
    """
    log_path = os.path.join(get_project_root(), ".stats-sync-log")
    now = get_ist_now().strftime("%Y-%m-%d %H:%M:%S %Z")
    with open(log_path, "w", encoding="utf-8") as f:
        f.write(f"Last sync: {now}\n")
        f.write(f"Status: {status}\n")
        f.write(f"Engine: {engine}\n")