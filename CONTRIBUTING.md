# Architecture

This document describes the high-level structure and design of the
**vivekcyr25** GitHub profile README repository.

## Overview

`
vivekcyr25/
├── README.md              # Profile README (rendered on GitHub)
├── config.json            # Centralized theme & animation config
├── assets/                # Generated SVG and image assets
│   ├── banner-*.svg       # Animated hero banners
│   ├── stats-dashboard.*  # Live GitHub stats dashboard
│   ├── system-stack.svg   # Tech stack visualization
│   ├── operator-profile*  # Profile HUD card
│   ├── core-connectivity* # Platform link cards
│   ├── separator.svg      # Section divider
│   └── card-*.svg         # Individual platform cards
├── scripts/               # Python automation
│   ├── generate_stats.py  # Stats dashboard SVG generator
│   ├── build_connectivity # Connectivity cards builder
│   ├── generate_separator # Separator SVG generator
│   ├── validate_svgs.py   # SVG integrity checker
│   ├── svg_optimizer.py   # Asset size analyzer
│   ├── colors.py          # VisionOS color palette
│   ├── constants.py       # Shared constants
│   └── utils.py           # Common utilities
├── tests/                 # Unit and integration tests
├── .github/               # GitHub configuration
│   ├── workflows/         # CI/CD automation
│   ├── ISSUE_TEMPLATE/    # Issue templates
│   └── PULL_REQUEST_TEMPLATE.md
└── docs/                  # (future) Extended documentation
`

## Design Principles

1. **VisionOS Theme**: All visuals follow a dark-mode, cyan/purple
   gradient aesthetic inspired by Apple's VisionOS design language.

2. **Zero External Dependencies**: Python scripts use only the
   standard library to keep the project portable.

3. **Config-Driven**: Colors, animation timings, and layout
   parameters are centralized in config.json and scripts/colors.py.

4. **Automated Refresh**: GitHub Actions keep the stats dashboard
   and contribution snake animations up to date daily.

## Data Flow

`
GitHub API  ──►  generate_stats.py  ──►  assets/stats-dashboard.svg
                                              │
                 build_connectivity.py ──► core-connectivity-v4.svg
                                              │
README.md  ◄────────── references ◄───────────┘
`
"@ | Set-Content -Path "ARCHITECTURE.md" -Encoding utf8 -NoNewline

git add ARCHITECTURE.md
git commit -m "docs: add ARCHITECTURE.md documenting project structure and design"

# ══════════════════════════════════════════════════════════════════════
# COMMIT 21: Improve CONTRIBUTING.md with more detail
# ══════════════════════════════════════════════════════════════════════
@"
# Contributing

Thank you for your interest in contributing to this project!

## Getting Started

1. **Fork** the repository
2. **Clone** your fork locally
3. **Create** a feature branch: `git checkout -b feature/your-feature`
4. **Make** your changes
5. **Test** your changes: `python -m pytest tests/ -v`
6. **Commit** with a clear message (see Commit Guidelines below)
7. **Push** to your fork and submit a Pull Request

## Development Setup

`ash
# Clone and enter the project
git clone https://github.com/<your-username>/vivekcyr25.git
cd vivekcyr25

# Run tests
python -m pytest tests/ -v

# Generate assets
make all

# Analyze SVG sizes
make optimize
`

## Commit Guidelines

This project follows [Conventional Commits](https://www.conventionalcommits.org/).

| Prefix     | Use for                            |
|------------|-------------------------------------|
| `feat:`  | New features or generators          |
| `fix:`   | Bug fixes                           |
| `docs:`  | Documentation changes               |
| `style:` | Formatting, no code logic change    |
| `refactor:` | Code restructuring              |
| `test:`  | Adding or updating tests            |
| `chore:` | Build, CI, dependency updates       |
| `ci:`    | CI/CD workflow changes              |

## Code Style

- **Python**: Follow PEP 8, line length 100
- **SVG**: Keep files optimized and readable
- **Markdown**: Use consistent heading hierarchy

## Pre-Commit Hooks

You can optionally install pre-commit hooks to automatically validate SVGs and run tests before committing:

```bash
pip install pre-commit
pre-commit install
```

## Reporting Issues

Open an issue using one of the templates. Include:
- Steps to reproduce
- Expected vs actual behavior
- Screenshots if applicable