#!/usr/bin/env python3
"""
Health Check - Verifies the integrity of the profile README setup.

Checks that all referenced assets exist, config is valid,
and scripts are importable.
"""

import json
import os
import sys
import importlib

# Ensure project root is in sys.path when script is executed directly
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from scripts.utils import get_assets_dir, get_project_root, load_config


def check_config() -> list:
    """Verify config.json structure."""
    issues = []
    config = load_config()
    required_keys = ["profile", "dashboard", "animation", "stats"]
    for key in required_keys:
        if key not in config:
            issues.append(f"Missing config section: {key}")
    return issues


def check_readme_assets() -> list:
    """Ensure all assets referenced in README.md actually exist."""
    issues = []
    root = get_project_root()
    readme_path = os.path.join(root, "README.md")

    if not os.path.exists(readme_path):
        return ["README.md not found"]

    with open(readme_path, "r", encoding="utf-8") as f:
        content = f.read()

    assets_dir = get_assets_dir()
    import re
    refs = re.findall(r'\./assets/([^\s"\'?]+)', content)
    for ref in refs:
        if not os.path.exists(os.path.join(assets_dir, ref)):
            issues.append(f"Missing asset: {ref}")

    return issues


def check_scripts_import() -> list:
    """Try importing all script modules."""
    issues = []
    modules = [
        "scripts.utils",
        "scripts.colors",
        "scripts.constants",
        "scripts.validate_svgs",
        "scripts.generate_separator",
        "scripts.svg_optimizer",
    ]
    for mod in modules:
        try:
            importlib.import_module(mod)
        except ImportError as e:
            issues.append(f"Cannot import {mod}: {e}")
    return issues


def main():
    print("🏥 Running health check...\n")
    all_ok = True

    for name, checker in [
        ("Config", check_config),
        ("README Assets", check_readme_assets),
        ("Script Imports", check_scripts_import),
    ]:
        issues = checker()
        if issues:
            all_ok = False
            print(f"❌ {name}:")
            for issue in issues:
                print(f"   • {issue}")
        else:
            print(f"✅ {name}")

    print()
    if all_ok:
        print("🎉 All checks passed!")
    else:
        print("⚠️  Some issues found — see above")
        sys.exit(1)


if __name__ == "__main__":
    main()