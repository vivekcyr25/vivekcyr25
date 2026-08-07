# Scripts

Automation scripts for the GitHub profile README.

## `generate_stats.py`
Fetches live GitHub stats via GraphQL API and generates the
`assets/stats-dashboard.svg` with animated visualizations.

**Requirements:** `GITHUB_TOKEN` environment variable

## `build_connectivity.py`
Downloads authentic brand logos from jsDelivr (Simple Icons),
converts to base64, and builds the `core-connectivity-v4.svg`
banner and individual platform card SVGs.

## Usage

```bash
# Generate stats dashboard
export GITHUB_TOKEN=your_token
python scripts/generate_stats.py

# Build connectivity cards
python scripts/build_connectivity.py
```
