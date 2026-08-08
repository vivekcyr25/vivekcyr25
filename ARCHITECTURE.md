# Architecture

This document describes the high-level structure and design of the **vivekcyr25** GitHub profile README repository.

## Overview

```
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
│   ├── health_check.py    # System integrity checker
│   ├── colors.py          # VisionOS color palette
│   ├── constants.py       # Shared constants
│   └── utils.py           # Common utilities
├── tests/                 # Unit and integration tests
├── .github/               # GitHub configuration
│   ├── workflows/         # CI/CD automation
│   ├── ISSUE_TEMPLATE/    # Issue templates
│   └── PULL_REQUEST_TEMPLATE.md
└── docs/                  # Extended documentation
```

## Design Principles

1. **VisionOS Theme**: All visuals follow a dark-mode, cyan/purple gradient aesthetic inspired by Apple's VisionOS design language.
2. **Zero External Dependencies**: Python scripts use only the standard library to keep the project portable.
3. **Config-Driven**: Colors, animation timings, and layout parameters are centralized in `config.json` and `scripts/colors.py`.
4. **Automated Refresh**: GitHub Actions keep the stats dashboard and contribution snake animations up to date daily.

## Data Flow

```
GitHub API  ──►  generate_stats.py  ──►  assets/stats-dashboard.svg
                                              │
                 build_connectivity.py ──► core-connectivity-v4.svg
                                              │
README.md  ◄────────── references ◄───────────┘
```
