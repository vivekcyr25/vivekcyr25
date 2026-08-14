#!/usr/bin/env python3
"""
Generates the animated separator SVG used between README sections.
Creates a subtle pulsing gradient line matching the VisionOS theme.
"""

import os


def generate_separator_svg():
    """Generate the separator SVG with animated gradient."""
    return '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 20" width="600" height="20">
  <defs>
    <linearGradient id="sepGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00F2FF" stop-opacity="0"/>
      <stop offset="30%" stop-color="#00F2FF" stop-opacity="0.6"/>
      <stop offset="50%" stop-color="#BC13FE" stop-opacity="0.8"/>
      <stop offset="70%" stop-color="#00F2FF" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#00F2FF" stop-opacity="0"/>
    </linearGradient>
    <filter id="sepGlow" x="-10%" y="-50%" width="120%" height="200%">
      <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="b"/>
      <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <line x1="50" y1="10" x2="550" y2="10"
        stroke="url(#sepGrad)" stroke-width="1.5"
        filter="url(#sepGlow)">
    <animate attributeName="opacity" values="0.4;1;0.4"
             dur="3s" repeatCount="indefinite"/>
  </line>
</svg>'''


import argparse
from scripts.svg_optimizer import minify_svg


def main(args=None):
    parser = argparse.ArgumentParser(description="Generate animated SVG separator.")
    parser.add_argument("--minify", action="store_true", help="Minify output SVG")
    parsed = parser.parse_args(args)

    assets_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "assets"
    )
    out_path = os.path.join(assets_dir, "separator.svg")
    content = generate_separator_svg()
    if parsed.minify:
        content = minify_svg(content)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✅ Written separator → {out_path}")


if __name__ == "__main__":
    main()


# ui: separator gradient end color refined to neon purple #BC13FE
