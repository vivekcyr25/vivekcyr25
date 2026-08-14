#!/usr/bin/env python3
"""
VisionOS-styled animated SVG badge generator.

Generates customizable badges with glowing borders and subtle pulse animations.
"""

import os
import argparse
from typing import Optional

from scripts import colors
from scripts.utils import get_assets_dir


def generate_badge_svg(
    label: str,
    value: str,
    color: str = colors.CYAN,
    bg_color: str = colors.BG_CARD,
    border_color: str = colors.BORDER
) -> str:
    """Generate SVG string for a glowing badge.

    Args:
        label: Badge title/label text.
        value: Badge value text.
        color: Accent hex color.
        bg_color: Background hex color.
        border_color: Border hex color.

    Returns:
        SVG XML markup string.
    """
    width = 240
    height = 40
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <defs>
    <linearGradient id="badge-glow" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="{color}" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="{colors.PURPLE}" stop-opacity="0.5"/>
    </linearGradient>
    <style>
      .badge-bg {{ fill: {bg_color}; stroke: {border_color}; stroke-width: 1.5; rx: 8px; }}
      .badge-label {{ font-family: {colors.FONT_UI}; font-size: 11px; fill: {colors.TEXT_MUTED}; font-weight: 600; text-transform: uppercase; letter-spacing: 0.5px; }}
      .badge-val {{ font-family: {colors.FONT_UI}; font-size: 12px; fill: {colors.TEXT_PRIMARY}; font-weight: 700; }}
      .badge-dot {{ fill: {color}; filter: drop-shadow(0 0 4px {color}); }}
      @keyframes pulse {{
        0% {{ opacity: 0.6; }}
        50% {{ opacity: 1.0; }}
        100% {{ opacity: 0.6; }}
      }}
      .pulse-dot {{ animation: pulse 2s infinite ease-in-out; }}
    </style>
  </defs>
  <rect class="badge-bg" x="1" y="1" width="{width - 2}" height="{height - 2}" rx="8"/>
  <circle class="badge-dot pulse-dot" cx="20" cy="20" r="4"/>
  <text x="34" y="24" class="badge-label">{label}</text>
  <text x="{width - 16}" y="24" class="badge-val" text-anchor="end">{value}</text>
</svg>'''


def main(output_file: Optional[str] = None) -> None:
    """Main CLI entrypoint for badge generation."""
    parser = argparse.ArgumentParser(description="Generate VisionOS animated SVG badge")
    parser.add_argument("--label", default="STATUS", help="Badge label text")
    parser.add_argument("--value", default="ONLINE", help="Badge value text")
    parser.add_argument("--color", default=colors.CYAN, help="Accent color in hex")
    parser.add_argument("--out", help="Output filename inside assets/")
    args = parser.parse_args()

    svg_content = generate_badge_svg(args.label, args.value, args.color)
    out_path = args.out or os.path.join(get_assets_dir(), "badge-status.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated badge SVG at {out_path}")


if __name__ == "__main__":
    main()

# ui: badge font preference updated to Segoe UI
