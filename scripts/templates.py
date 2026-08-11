#!/usr/bin/env python3
"""
Reusable SVG component templates for VisionOS dashboards.

Provides standardized helper functions for rendering XML elements like cards,
glowing paths, headers, progress bars, and status text.
"""

from scripts import colors


def render_card_rect(x: int, y: int, width: int, height: int, rx: int = 12) -> str:
    """Render a standard glassmorphic card rectangle."""
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{rx}" '
        f'fill="{colors.BG_CARD}" stroke="{colors.BORDER}" stroke-width="1.5"/>'
    )


def render_glowing_dot(cx: int, cy: int, r: int = 4, color: str = colors.CYAN) -> str:
    """Render a glowing status dot SVG circle element."""
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{color}" filter="drop-shadow(0 0 4px {color})"/>'


def render_progress_bar(x: int, y: int, width: int, height: int, progress_pct: float, color: str = colors.CYAN) -> str:
    """Render a progress bar background and fill track."""
    fill_width = max(0, min(width, int(width * (progress_pct / 100.0))))
    return (
        f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{height//2}" fill="{colors.BG_DARK}"/>\n'
        f'<rect x="{x}" y="{y}" width="{fill_width}" height="{height}" rx="{height//2}" fill="{color}"/>'
    )
