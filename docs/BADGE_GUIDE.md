# VisionOS SVG Badge Generator Guide

The `generate_badge.py` script builds customizable, animated status badges styled with VisionOS dark glassmorphism aesthetic.

## Usage

### Command Line
```bash
python -m scripts.generate_badge --label "BUILD" --value "PASSING" --color "#00FF88" --out assets/badge-status.svg
```

### Python API
```python
from scripts.generate_badge import generate_badge_svg
from scripts import colors

svg_code = generate_badge_svg(
    label="METRIC",
    value="99.9%",
    color=colors.CYAN
)
```

## Features
- **Pulse Glow Dot**: Live CSS animation with pulsing accent light.
- **Glassmorphism Border**: VisionOS standard card border with semi-transparent backdrop.
- **Flexible Palette**: Full support for standard primary colors (`CYAN`, `PURPLE`, `GREEN`, `PINK`, `AMBER`, `BLUE`).
