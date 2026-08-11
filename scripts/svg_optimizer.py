#!/usr/bin/env python3
"""
SVG Optimizer - Reports size statistics and identifies optimization opportunities.

Analyzes SVG files in assets/ and provides recommendations for
reducing file size without affecting visual quality.
"""

import os
import xml.etree.ElementTree as ET
from scripts.utils import get_assets_dir


def analyze_svg(filepath: str) -> dict:
    """Analyze a single SVG file and return metrics.

    Args:
        filepath: Absolute path to the SVG file.

    Returns:
        Dictionary with size, element count, and optimization hints.
    """
    stats = {
        "file": os.path.basename(filepath),
        "size_kb": round(os.path.getsize(filepath) / 1024, 1),
        "elements": 0,
        "has_animation": False,
        "has_filter": False,
        "has_gradient": False,
        "hints": [],
    }

    try:
        tree = ET.parse(filepath)
        root = tree.getroot()

        for elem in root.iter():
            stats["elements"] += 1
            tag = elem.tag.split("}")[-1].lower()

            if tag in ("animate", "animatetransform", "animatemotion"):
                stats["has_animation"] = True
            if tag == "filter":
                stats["has_filter"] = True
            if tag in ("lineargradient", "radialgradient"):
                stats["has_gradient"] = True

        if stats["size_kb"] > 100:
            stats["hints"].append("Consider simplifying paths")
        if stats["elements"] > 500:
            stats["hints"].append("High element count - review for redundancy")

    except ET.ParseError:
        stats["hints"].append("XML parse error")

    return stats


def minify_svg_string(svg_content: str) -> str:
    """Minify SVG content by stripping XML comments and redundant linebreaks.

    Args:
        svg_content: Raw SVG XML string.

    Returns:
        Minified SVG string.
    """
    import re
    # Remove XML comments
    content = re.sub(r"<!--.*?-->", "", svg_content, flags=re.DOTALL)
    # Collapse multiple spaces
    lines = [line.strip() for line in content.splitlines() if line.strip()]
    return "\n".join(lines)


def main():
    """Analyze all SVGs and print a report."""
    assets_dir = get_assets_dir()
    svg_files = sorted(f for f in os.listdir(assets_dir) if f.endswith(".svg"))

    print(f"📊 SVG Asset Report ({len(svg_files)} files)\n")
    print(f"{'File':<45} {'Size':>8} {'Elements':>10} {'Anim':>6} {'Hints'}")
    print("─" * 95)

    total_size = 0
    for svg_file in svg_files:
        path = os.path.join(assets_dir, svg_file)
        stats = analyze_svg(path)
        total_size += stats["size_kb"]

        anim = "✓" if stats["has_animation"] else "—"
        hints = "; ".join(stats["hints"]) if stats["hints"] else "—"
        print(f"{stats['file']:<45} {stats['size_kb']:>7.1f}K {stats['elements']:>10} {anim:>6} {hints}")

    print("─" * 95)
    print(f"{'Total':<45} {total_size:>7.1f}K")


if __name__ == "__main__":
    main()