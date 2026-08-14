#!/usr/bin/env python3
"""
Centralized constants for SVG generation and validation.

Keeps magic numbers and thresholds in one place so generators
and validators stay in sync.
"""

# ── SVG Dimensions ───────────────────────────────────────────────────
DASHBOARD_WIDTH = 850
DASHBOARD_HEIGHT = 580
SEPARATOR_WIDTH = 600
SEPARATOR_HEIGHT = 20
CARD_WIDTH = 200
CARD_HEIGHT = 60
DEFAULT_SVG_VIEWBOX = f"0 0 {DASHBOARD_WIDTH} {DASHBOARD_HEIGHT}"
SVG_XMLNS_NAMESPACE = "http://www.w3.org/2000/svg"


# ── Validation Thresholds ────────────────────────────────────────────
MAX_SVG_SIZE_KB = 500
MIN_SVG_SIZE_BYTES = 50

# ── Animation Defaults ───────────────────────────────────────────────
DEFAULT_PULSE_DURATION = "2.2s"
DEFAULT_WAVE_SPEED_FAST = "4.5s"
DEFAULT_WAVE_SPEED_SLOW = "7s"
DEFAULT_BAR_ANIMATION = "1.8s"

# ── GitHub API ───────────────────────────────────────────────────────
GITHUB_API_BASE = "https://api.github.com"
GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"
CONTRIBUTIONS_MAX_SCALE = 500
STREAK_RING_MAX_DAYS = 30
BAR_MAX_WIDTH_PX = 260

# VisionOS UI color palette
VISIONOS_CYAN      = "#00F2FF"
VISIONOS_PURPLE    = "#BC13FE"
VISIONOS_BG_DARK   = "#050816"
VISIONOS_BG_MID    = "#07111f"
VISIONOS_TEXT_DIM  = "#8899bb"
VISIONOS_TEXT_MAIN = "#c9d1d9"
VISIONOS_ACCENT    = "#4da8ff"
