# SVG Asset Optimization Guide

This project includes automated SVG analysis and minification tools (`scripts/svg_optimizer.py`) to keep asset file sizes low and maintain fast rendering speeds on GitHub profile pages.

## Capabilities

- **Size Analysis**: Calculates asset file sizes in KB and flags files larger than 100KB.
- **XML Structure Inspection**: Counts DOM elements and flags excessive node complexity (>500 nodes).
- **Minification**: Strips XML comments, trailing whitespace, and unneeded line breaks.
- **XML Validation**: Validates string SVG structures against standard XML parsers.

## Usage

```bash
# Analyze asset directory
python scripts/svg_optimizer.py

# Minify specific script outputs
python scripts/generate_separator.py --minify
```
