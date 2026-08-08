#!/usr/bin/env python3
"""Pytest configuration and shared fixtures."""

import os
import sys

import pytest

# Add project root to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


@pytest.fixture
def assets_dir():
    """Return the absolute path to the assets/ directory."""
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "assets"
    )


@pytest.fixture
def config():
    """Load and return the project configuration."""
    from scripts.utils import load_config
    return load_config()


@pytest.fixture
def svg_files(assets_dir):
    """Return a sorted list of SVG file paths in assets/."""
    return sorted(
        os.path.join(assets_dir, f)
        for f in os.listdir(assets_dir)
        if f.endswith(".svg")
    )