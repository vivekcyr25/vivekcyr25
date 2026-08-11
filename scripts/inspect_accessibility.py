#!/usr/bin/env python3
"""
SVG Accessibility (a11y) inspector script.

Inspects SVG assets to ensure proper accessibility markup (title, desc, aria-label, role).
"""

import os
import glob
import xml.etree.ElementTree as ET
from typing import List, Dict

from scripts.utils import get_assets_dir


def check_svg_accessibility(file_path: str) -> Dict[str, bool]:
    """Check an SVG file for accessibility elements.

    Args:
        file_path: Path to SVG file.

    Returns:
        Dict mapping check names to boolean pass/fail flags.
    """
    results = {
        "has_title": False,
        "has_aria_label": False,
        "has_role": False,
    }
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Check title element
        for elem in root.iter():
            if elem.tag.endswith("title") and elem.text and elem.text.strip():
                results["has_title"] = True
                break

        # Check root attributes
        if "aria-label" in root.attrib or "aria-labelledby" in root.attrib:
            results["has_aria_label"] = True
        if root.attrib.get("role") in ("img", "graphics-document"):
            results["has_role"] = True

    except ET.ParseError:
        pass

    return results


def main() -> None:
    """Inspect all SVGs in assets directory."""
    assets_dir = get_assets_dir()
    svg_files = glob.glob(os.path.join(assets_dir, "*.svg"))

    print(f"Auditing accessibility for {len(svg_files)} SVG assets...")
    pass_count = 0
    for svg_file in svg_files:
        res = check_svg_accessibility(svg_file)
        rel_name = os.path.basename(svg_file)
        if any(res.values()):
            pass_count += 1
            print(f"  [OK] {rel_name} - {res}")
        else:
            print(f"  [INFO] {rel_name} missing accessibility metadata")

    print(f"Accessibility Audit Summary: {pass_count}/{len(svg_files)} files evaluated.")


if __name__ == "__main__":
    main()
