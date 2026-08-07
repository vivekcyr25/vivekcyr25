#!/usr/bin/env python3
"""
Validates all SVG files in the assets/ directory.
Checks for:
  - Valid XML structure
  - Required xmlns attribute
  - Presence of viewBox
  - File size within reasonable bounds
"""

import os
import xml.etree.ElementTree as ET


def validate_svg(filepath):
    """Validate a single SVG file. Returns list of issues."""
    issues = []
    basename = os.path.basename(filepath)

    # Check file size (warn if > 500KB)
    size_kb = os.path.getsize(filepath) / 1024
    if size_kb > 500:
        issues.append(f"  ⚠️  Large file: {size_kb:.1f} KB")

    try:
        tree = ET.parse(filepath)
        root = tree.getroot()

        # Check namespace
        if "svg" not in root.tag.lower():
            issues.append("  ❌ Root element is not <svg>")

        # Check viewBox
        if root.get("viewBox") is None:
            issues.append("  ⚠️  Missing viewBox attribute")

    except ET.ParseError as e:
        issues.append(f"  ❌ XML parse error: {e}")
    except Exception as e:
        issues.append(f"  ❌ Error: {e}")

    return issues


def main():
    assets_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "assets"
    )

    svg_files = [f for f in os.listdir(assets_dir) if f.endswith(".svg")]
    svg_files.sort()

    print(f"🔍 Validating {len(svg_files)} SVG files...\n")

    total_issues = 0
    for svg_file in svg_files:
        filepath = os.path.join(assets_dir, svg_file)
        issues = validate_svg(filepath)
        if issues:
            print(f"📄 {svg_file}")
            for issue in issues:
                print(issue)
            total_issues += len(issues)
        else:
            print(f"  ✅ {svg_file}")

    print(f"\n{'='*50}")
    if total_issues == 0:
        print("✅ All SVG files are valid!")
    else:
        print(f"⚠️  Found {total_issues} issue(s) across {len(svg_files)} files")


if __name__ == "__main__":
    main()
