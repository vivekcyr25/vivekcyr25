#!/usr/bin/env python3
"""
Unified Profile README Automation CLI tool.

Combines asset generation, SVG validation, accessibility auditing, and stats export into a single entrypoint.
"""

import sys
import argparse
from scripts import (
    generate_stats,
    build_connectivity,
    generate_separator,
    generate_badge,
    validate_svgs,
    inspect_accessibility,
    export_stats,
)


def run_cli(args=None) -> int:
    """Parse CLI arguments and dispatch commands."""
    parser = argparse.ArgumentParser(description="Unified VisionOS Profile README CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    subparsers.add_parser("build-all", help="Generate stats, connectivity cards, separator, and badge")
    subparsers.add_parser("validate", help="Validate all SVG assets")
    subparsers.add_parser("audit", help="Audit SVG accessibility metadata")
    subparsers.add_parser("export", help="Export profile statistics to JSON/CSV")

    parsed = parser.parse_args(args)

    if parsed.command == "build-all":
        print("⚡ Building all profile assets...")
        generate_stats.main()
        build_connectivity.main()
        generate_separator.main()
        generate_badge.main()
        print("✅ Built all profile assets.")
    elif parsed.command == "validate":
        validate_svgs.main()
    elif parsed.command == "audit":
        inspect_accessibility.main()
    elif parsed.command == "export":
        export_stats.main()
    else:
        parser.print_help()
        return 1
    return 0


def main() -> None:
    """Entry point for console script."""
    sys.exit(run_cli())


if __name__ == "__main__":
    main()
