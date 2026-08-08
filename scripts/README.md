# Scripts

Automation scripts for generating and maintaining profile README assets.

## Available Scripts

| Script | Description | Command |
|--------|-------------|---------|
| generate_stats.py | Generates the live GitHub stats dashboard SVG | make stats |
| uild_connectivity.py | Builds platform connectivity cards | make connectivity |
| generate_separator.py | Creates animated section separator | make separator |
| alidate_svgs.py | Validates all SVG files for integrity | make validate |
| svg_optimizer.py | Analyzes SVG sizes and suggests optimizations | make optimize |
| health_check.py | Verifies config, assets, and module imports | python scripts/health_check.py |

## Shared Modules

| Module | Purpose |
|--------|---------|
| colors.py | VisionOS dark theme color palette constants |
| constants.py | Centralized dimensions, thresholds, and API URLs |
| utils.py | IST timezone, config loading, date formatting, logging |

## Usage

`ash
# Generate all assets
make all

# Run a single generator
python scripts/generate_stats.py

# Analyze asset sizes
make optimize

# Run health check
python scripts/health_check.py
`

## Dependencies

All scripts use **Python standard library only** — no pip install required.
Minimum Python version: **3.10**