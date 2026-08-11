#!/usr/bin/env python3
"""
Markdown tech stack & project table generator.

Formats structured dictionaries into aligned Markdown tables for READMEs.
"""

from typing import List, Dict, Any


def generate_markdown_table(headers: List[str], rows: List[List[Any]]) -> str:
    """Generate a formatted GFM Markdown table.

    Args:
        headers: List of column header strings.
        rows: List of row data lists.

    Returns:
        Formatted Markdown table string.
    """
    if not headers or not rows:
        return ""

    # Calculate column widths
    widths = [len(h) for h in headers]
    for row in rows:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))

    # Header line
    header_line = "| " + " | ".join(h.ljust(widths[i]) for i, h in enumerate(headers)) + " |"
    # Separator line
    separator_line = "|-" + "-|-".join("-" * widths[i] for i in range(len(headers))) + "-|"

    # Data rows
    row_lines = []
    for row in rows:
        formatted_cells = [str(cell).ljust(widths[i]) for i, cell in enumerate(row)]
        row_lines.append("| " + " | ".join(formatted_cells) + " |")

    return "\n".join([header_line, separator_line] + row_lines)


def main() -> None:
    """Demonstrate table generation."""
    headers = ["Tech / Tool", "Category", "Proficiency", "Status"]
    rows = [
        ["Python 3.14", "Core Language", "Expert", "Active"],
        ["VisionOS SVG", "UI Design", "Advanced", "Active"],
        ["GitHub Actions", "CI/CD", "Advanced", "Automated"],
    ]
    print(generate_markdown_table(headers, rows))


if __name__ == "__main__":
    main()
