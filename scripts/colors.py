#!/usr/bin/env python3
"""
VisionOS dark theme color palette constants.
Centralized color definitions for all SVG generators.
"""

# ── Primary Palette ──────────────────────────────────────────────────
CYAN = "#00F2FF"
PURPLE = "#BC13FE"
GREEN = "#00FF88"
PINK = "#FF6B9D"
AMBER = "#FFB800"
BLUE = "#4499FF"

# ── Background ───────────────────────────────────────────────────────
BG_START = "#060c1e"
BG_END = "#040914"
BG_PANEL = "#060e28"
BG_DARK = "#050918"
BG_CARD = "#040e1c"

# ── Borders & Dividers ──────────────────────────────────────────────
BORDER = "#101f3e"
GRID = "#0c1a2e"
BORDER_SUBTLE = "#0a1530"

# ── Text ─────────────────────────────────────────────────────────────
TEXT_PRIMARY = "#ffffff"
TEXT_SECONDARY = "#cce0ff"
TEXT_MUTED = "#8899bb"

# ── Platform Brand Colors ────────────────────────────────────────────
BRAND_LINKEDIN = "#0A66C2"
BRAND_GMAIL = "#EA4335"
BRAND_GITHUB = "#FFFFFF"
BRAND_HACKERRANK = "#00EA64"
BRAND_HACKEREARTH = "#44BCFF"
BRAND_ORCID = "#A6CE39"

# ── Gradient Definitions ──────────────────────────────────────────────
GRADIENT_CYAN_PURPLE = (CYAN, PURPLE)
GRADIENT_AMBER_PINK = (AMBER, PINK)
GRADIENT_BLUE_GREEN = (BLUE, GREEN)
GRADIENT_NEON_GLOW = (CYAN, GREEN)

# ── Font Stack ───────────────────────────────────────────────────────
FONT_MONO = "'Courier New', Courier, monospace"
FONT_UI = "'Segoe UI', Arial, sans-serif"


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Convert hex color string (#RRGGBB) to RGB tuple."""
    hex_color = hex_color.lstrip("#")
    if len(hex_color) == 3:
        hex_color = "".join([c * 2 for c in hex_color])
    return int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)


def get_contrast_ratio(hex1: str, hex2: str) -> float:
    """Calculate approximate luminance contrast ratio between two hex colors."""
    r1, g1, b1 = hex_to_rgb(hex1)
    r2, g2, b2 = hex_to_rgb(hex2)
    l1 = (0.2126 * r1 + 0.7152 * g1 + 0.0722 * b1) / 255
    l2 = (0.2126 * r2 + 0.7152 * g2 + 0.0722 * b2) / 255
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return round((lighter + 0.05) / (darker + 0.05), 2)




# Connectivity card brand palette
BRAND_COLORS = {
    "linkedin":    "#0A66C2",
    "gmail":       "#EA4335",
    "github":      "#58a6ff",
    "hackerrank":  "#00EA64",
    "hackerearth": "#44BCFF",
    "orcid":       "#A6CE39",
}

# Label display colors (slightly lighter for readability)
LABEL_COLORS = {
    "linkedin":    "#4da8ff",
    "gmail":       "#ff7060",
    "github":      "#c9d1d9",
    "hackerrank":  "#00EA64",
    "hackerearth": "#44BCFF",
    "orcid":       "#b8e04a",
}
