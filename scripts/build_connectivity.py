#!/usr/bin/env python3
"""
Downloads authentic vector brand logos from jsDelivr (Simple Icons),
converts to base64, and builds core-connectivity-v4.svg as well as
individual clickable platform card SVGs in assets/.
"""

import urllib.request
import base64
import os
from colors import BRAND_COLORS, LABEL_COLORS  # noqa: F401 – available for downstream use
from svg_optimizer import normalize_svg_whitespace

LOGOS = {
    "linkedin":    "https://cdn.jsdelivr.net/npm/simple-icons@11.0.0/icons/linkedin.svg",
    "gmail":       "https://cdn.jsdelivr.net/npm/simple-icons@11.0.0/icons/gmail.svg",
    "github":      "https://cdn.jsdelivr.net/npm/simple-icons@11.0.0/icons/github.svg",
    "hackerrank":  "https://cdn.jsdelivr.net/npm/simple-icons@11.0.0/icons/hackerrank.svg",
    "hackerearth": "https://cdn.jsdelivr.net/npm/simple-icons@11.0.0/icons/hackerearth.svg",
    "orcid":       "https://cdn.jsdelivr.net/npm/simple-icons@11.0.0/icons/orcid.svg",
}

LOGO_COLORS = {
    "linkedin":    "#0A66C2",
    "gmail":       "#EA4335",
    "github":      "#FFFFFF",
    "hackerrank":  "#00EA64",
    "hackerearth": "#44BCFF",
    "orcid":       "#A6CE39",
}

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

def fetch_b64(name: str, url: str) -> str:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=15) as r:
        data_str = r.read().decode('utf-8')
    
    color = LOGO_COLORS.get(name, "#FFFFFF")
    if 'fill="' not in data_str:
        data_str = data_str.replace('<svg ', f'<svg fill="{color}" ')
    else:
        data_str = data_str.replace('fill="currentColor"', f'fill="{color}"')
        
    return base64.b64encode(data_str.encode('utf-8')).decode('utf-8')

def fetch_all_logos() -> dict[str, str]:
    print("Downloading authentic vector logos...")
    b64 = {}
    for name, url in LOGOS.items():
        try:
            b64[name] = fetch_b64(name, url)
            print(f"  ✅ {name}")
        except Exception as e:
            print(f"  ❌ {name}: {e}")
            b64[name] = ""
    return b64

def img_tag(b64_data: str, x: float, y: float, size: float = 34) -> str:
    return (
        f'<image x="{x}" y="{y}" width="{size}" height="{size}" '
        f'href="data:image/svg+xml;base64,{b64_data}" '
        f'preserveAspectRatio="xMidYMid meet" image-rendering="crisp-edges"/>'
    )

CARDS = [
    # (x, width, stroke_color, name_color, label,       logo_key)
    (  4, 142, "#0A66C2", "#4da8ff",  "LinkedIn",   "linkedin"),
    (152, 142, "#EA4335", "#ff7060",  "Gmail",      "gmail"),
    (300, 142, "#58a6ff", "#c9d1d9",  "GitHub",     "github"),
    (448, 142, "#00EA64", "#00EA64",  "HackerRank", "hackerrank"),
    (596, 152, "#44BCFF", "#44BCFF",  "HackerEarth","hackerearth"),
    (754, 142, "#A6CE39", "#b8e04a",  "ORCID",      "orcid"),
]

LINK_MAP = {
    "linkedin":    "https://www.linkedin.com/in/vivek-sharma-2bba8b398/",
    "gmail":       "mailto:viveklpu008@gmail.com",
    "github":      "https://github.com/vivekcyr25",
    "hackerrank":  "https://www.hackerrank.com/profile/viveklpu008",
    "hackerearth": "https://www.hackerearth.com/@viveklpu008/",
    "orcid":       "https://orcid.org/0009-0006-5078-9881",
}

CARD_SUBTITLES = {
    "linkedin": "Profile", "gmail": "Contact",
    "github": "Projects", "hackerrank": "Coding",
    "hackerearth": "Compete", "orcid": "Research",
}

ANIM_DUR  = [3.0, 2.8, 3.2, 3.4, 2.6, 3.0]
ANIM_BEGIN= [0.0, 0.4, 0.8, 0.2, 1.0, 1.4]

assets_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")

def build_combined_banner_svg(b64_map: dict[str, str] | None = None) -> str:
    if b64_map is None:
        b64_map = {k: "" for k in LOGOS}

    parts = []
    parts.append('''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 900 100" width="900" height="100" role="img" aria-label="Core Connectivity Links">
<defs>
  <linearGradient id="panelbg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#071828"/>
    <stop offset="50%" stop-color="#06101e"/>
    <stop offset="100%" stop-color="#030c16"/>
  </linearGradient>
  <filter id="gl" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>
<rect width="900" height="100" fill="url(#panelbg)" rx="6"/>
''')

    for i, (cx, cw, stroke, label_color, label, key) in enumerate(CARDS):
        dur   = ANIM_DUR[i]
        begin = ANIM_BEGIN[i]
        href  = LINK_MAP.get(key, "#")

        logo_size = 38
        logo_x = cx + (cw - logo_size) / 2
        logo_y = 13

        card_xml = f'''
<a href="{href}" target="_blank">
  <!-- Card bg -->
  <rect x="{cx}" y="4" width="{cw}" height="92" rx="12" fill="#061424" opacity="0.98"/>

  <!-- Animated border -->
  <rect x="{cx}" y="4" width="{cw}" height="92" rx="8" fill="none"
        stroke="{stroke}" stroke-width="1.8">
    <animate attributeName="stroke-opacity" values="0.25;0.9;0.25"
             dur="{dur}s" repeatCount="indefinite" begin="{begin}s"/>
  </rect>

  <!-- Bottom accent line -->
  <rect x="{cx}" y="91" width="{cw}" height="2.5" rx="1" fill="{stroke}" opacity="0.45"/>

  <!-- Top accent bar -->
  <rect x="{cx}" y="4" width="0" height="2.5" rx="1" fill="{stroke}" opacity="0.7">
    <animate attributeName="width" from="0" to="{cw}"
             dur="1s" fill="freeze" begin="{begin + 0.1:.1f}s"
             calcMode="spline" keySplines="0.25 0.46 0.45 0.94"/>
  </rect>

  <!-- Real logo image -->
  {img_tag(b64_map.get(key, ""), logo_x, logo_y, logo_size)}

  <!-- Platform name -->
  <text x="{cx + cw / 2}" y="75"
        font-family="'Segoe UI',Arial,sans-serif"
        font-size="12.5" font-weight="700"
        fill="{label_color}" text-anchor="middle" letter-spacing="0.4">{label}</text>

  <!-- Glow layer -->
  <rect x="{cx}" y="4" width="{cw}" height="92" rx="8" fill="none"
        stroke="{stroke}" stroke-width="8" filter="url(#gl)" opacity="0">
    <animate attributeName="opacity" values="0;0.08;0"
             dur="{dur}s" repeatCount="indefinite" begin="{begin}s"/>
  </rect>
</a>
'''
        parts.append(card_xml)

    parts.append('<text x="450" y="88" font-family=\'Segoe UI\',Arial,sans-serif font-size="8" fill="#8899bb" text-anchor="middle" letter-spacing="1.5">DIRECT LINKS TO PLATFORMS</text>\n</svg>')
    return "\n".join(parts)

def build_single_card_svg(card_tuple: tuple, b64_map: dict[str, str] | None = None, dur: float = 3.0, begin: float = 0.0) -> str:
    if b64_map is None:
        b64_map = {k: "" for k in LOGOS}

    cx, cw, stroke, label_color, label, key = card_tuple
    href = LINK_MAP.get(key, "#")

    w = int(cw)
    h = 92
    logo_size = 38
    logo_x = (w - logo_size) / 2
    logo_y = 13

    return f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
<defs>
  <filter id="gl" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
</defs>
<a href="{href}" target="_blank">
  <rect x="2" y="2" width="{w-4}" height="{h-4}" rx="12" fill="#061424" opacity="0.98"/>
  <rect x="2" y="2" width="{w-4}" height="{h-4}" rx="8" fill="none" stroke="{stroke}" stroke-width="1.8">
    <animate attributeName="stroke-opacity" values="0.25;0.9;0.25" dur="{dur}s" repeatCount="indefinite" begin="{begin}s"/>
  </rect>
  <rect x="2" y="2" width="0" height="2.5" rx="1" fill="{stroke}" opacity="0.7">
    <animate attributeName="width" from="0" to="{w-4}" dur="1s" fill="freeze" begin="{begin + 0.1:.1f}s" calcMode="spline" keySplines="0.25 0.46 0.45 0.94"/>
  </rect>
  {img_tag(b64_map.get(key, ""), logo_x, logo_y, logo_size)}
  <text x="{w / 2}" y="73" font-family="'Segoe UI',Arial,sans-serif" font-size="12.5" font-weight="700" fill="{label_color}" text-anchor="middle" letter-spacing="0.4">{label}</text>
  <rect x="2" y="2" width="{w-4}" height="{h-4}" rx="8" fill="none" stroke="{stroke}" stroke-width="8" filter="url(#gl)" opacity="0">
    <animate attributeName="opacity" values="0;0.08;0" dur="{dur}s" repeatCount="indefinite" begin="{begin}s"/>
  </rect>
</a>
</svg>'''

def main() -> None:
    b64 = fetch_all_logos()
    
    # 1. Combined banner
    svg_content = build_combined_banner_svg(b64)
    for banner_name in ["core-connectivity-v4.svg", "core-connectivity-v3.svg", "core-connectivity-v2.svg"]:
        out_banner = os.path.join(assets_dir, banner_name)
        with open(out_banner, "w", encoding="utf-8") as f:
            f.write(normalize_svg_whitespace(svg_content))
        print(f"✅ Written Banner → {out_banner}")

    # 2. Individual Cards
    for i, card_tuple in enumerate(CARDS):
        key = card_tuple[5]
        single_svg = build_single_card_svg(card_tuple, b64, ANIM_DUR[i], ANIM_BEGIN[i])
        for card_name in [f"card-{key}-v4.svg", f"card-{key}-v3.svg", f"card-{key}.svg"]:
            card_out = os.path.join(assets_dir, card_name)
            with open(card_out, "w", encoding="utf-8") as f:
                f.write(single_svg)
            print(f"  ✅ Written Card → {card_name}")

if __name__ == "__main__":
    main()

