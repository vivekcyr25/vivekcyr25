#!/usr/bin/env python3
"""
Replace old flat shields.io badges and komarev counter
with fully animated, self-hosted VisionOS-style SVGs.
"""

import subprocess, os

BASE = r"c:\Users\hp\Desktop\New folder (2)"

def run(cmd):
    r = subprocess.run(cmd, shell=True, cwd=BASE, capture_output=True, text=True)
    if r.returncode != 0:
        print(f"  stderr: {r.stderr.strip()}")
    return r.stdout.strip()

def write(path, content):
    full = os.path.join(BASE, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)

def read(path):
    with open(os.path.join(BASE, path), "r", encoding="utf-8") as f:
        return f.read()

def commit(files, message):
    for f in files:
        run(f'git add "{f}"')
    out = run(f'git commit -m "{message}"')
    sha = out.split()[1].rstrip("]") if out.startswith("[main") else "?"
    print(f"  ✅ [{sha}] {message}")

# ─────────────────────────────────────────────────────────────────BADGES_SVG = '''\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 36" width="720" height="36" role="img" aria-label="Profile badges: License MIT, Last Commit today, Repo Size 1.5 MiB, Made with Python and SVG">
<title>VisionOS Profile Badges</title>
<defs>
  <!-- Scanline texture -->
  <pattern id="scan" width="1" height="2" patternUnits="userSpaceOnUse">
    <rect width="1" height="1" fill="rgba(255,255,255,0.015)"/>
  </pattern>

  <!-- Soothing Glow Filters -->
  <filter id="glow-c" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="glow-p" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="glow-g" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="glow-a" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="2" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>

  <!-- Calming Nordic Pill Gradients -->
  <linearGradient id="grad-c" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#061525"/>
    <stop offset="100%" stop-color="#092237"/>
  </linearGradient>
  <linearGradient id="grad-p" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#140D28"/>
    <stop offset="100%" stop-color="#1F153D"/>
  </linearGradient>
  <linearGradient id="grad-g" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#061B16"/>
    <stop offset="100%" stop-color="#0B2A22"/>
  </linearGradient>
  <linearGradient id="grad-a" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#1C1306"/>
    <stop offset="100%" stop-color="#2C1E0A"/>
  </linearGradient>
</defs>

<!-- ═══ BADGE 1: License MIT (Glacial Ice) ═════════════════════════════════ -->
<rect x="0" y="0" width="135" height="36" rx="10" fill="url(#grad-c)"/>
<rect x="0" y="0" width="135" height="36" rx="10" fill="url(#scan)"/>
<rect x="0.75" y="0.75" width="133.5" height="34.5" rx="9.5" fill="none" stroke="#38BDF8" stroke-width="1.1">
  <animate attributeName="stroke-opacity" values="0.4;0.9;0.4" dur="4s" repeatCount="indefinite"/>
</rect>
<rect x="10" y="0.5" width="115" height="2" rx="1" fill="#38BDF8" opacity="0.6">
  <animate attributeName="opacity" values="0.35;0.75;0.35" dur="4s" repeatCount="indefinite"/>
</rect>
<circle cx="16" cy="18" r="3" fill="#38BDF8" filter="url(#glow-c)">
  <animate attributeName="r" values="2.6;3.8;2.6" dur="3s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="0.7;1;0.7" dur="3s" repeatCount="indefinite"/>
</circle>
<text x="26" y="14" font-family="'Segoe UI',Arial,sans-serif" font-size="8" font-weight="600"
      fill="#94A3B8" letter-spacing="1.2" text-anchor="start">LICENSE</text>
<rect x="25" y="18.5" width="42" height="13" rx="4" fill="#38BDF8" fill-opacity="0.12"/>
<rect x="25" y="18.5" width="42" height="13" rx="4" fill="none" stroke="#38BDF8" stroke-width="0.8" stroke-opacity="0.6"/>
<text x="46" y="28.5" font-family="'Segoe UI',Arial,sans-serif" font-size="9.5" font-weight="700"
      fill="#E0F2FE" text-anchor="middle" filter="url(#glow-c)" letter-spacing="0.5">MIT</text>
<rect x="0" y="0" width="10" height="36" rx="10" fill="#38BDF8" opacity="0.08">
  <animateTransform attributeName="transform" type="translate" from="-10 0" to="145 0"
    dur="5s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1"/>
</rect>

<!-- ═══ BADGE 2: Last Commit (Twilight Wisteria) ═══════════════════════════ -->
<rect x="145" y="0" width="175" height="36" rx="10" fill="url(#grad-p)"/>
<rect x="145" y="0" width="175" height="36" rx="10" fill="url(#scan)"/>
<rect x="145.75" y="0.75" width="173.5" height="34.5" rx="9.5" fill="none" stroke="#A78BFA" stroke-width="1.1">
  <animate attributeName="stroke-opacity" values="0.4;0.9;0.4" dur="4.2s" repeatCount="indefinite" begin="0.5s"/>
</rect>
<rect x="155" y="0.5" width="155" height="2" rx="1" fill="#A78BFA" opacity="0.6">
  <animate attributeName="opacity" values="0.35;0.75;0.35" dur="4.2s" repeatCount="indefinite" begin="0.5s"/>
</rect>
<circle cx="161" cy="18" r="3" fill="#A78BFA" filter="url(#glow-p)">
  <animate attributeName="r" values="2.6;3.8;2.6" dur="3.2s" repeatCount="indefinite" begin="0.4s"/>
  <animate attributeName="opacity" values="0.7;1;0.7" dur="3.2s" repeatCount="indefinite" begin="0.4s"/>
</circle>
<text x="171" y="14" font-family="'Segoe UI',Arial,sans-serif" font-size="8" font-weight="600"
      fill="#94A3B8" letter-spacing="1.2">LAST COMMIT</text>
<rect x="170" y="18.5" width="56" height="13" rx="4" fill="#A78BFA" fill-opacity="0.12"/>
<rect x="170" y="18.5" width="56" height="13" rx="4" fill="none" stroke="#A78BFA" stroke-width="0.8" stroke-opacity="0.6"/>
<text x="198" y="28.5" font-family="'Segoe UI',Arial,sans-serif" font-size="9" font-weight="700"
      fill="#F3E8FF" text-anchor="middle" filter="url(#glow-p)" letter-spacing="0.3">today</text>
<rect x="145" y="0" width="10" height="36" rx="10" fill="#A78BFA" opacity="0.08">
  <animateTransform attributeName="transform" type="translate" from="-10 0" to="185 0"
    dur="5.2s" repeatCount="indefinite" begin="1s" calcMode="spline" keySplines="0.4 0 0.6 1"/>
</rect>

<!-- ═══ BADGE 3: Repo Size (Sage Jade) ═════════════════════════════════════ -->
<rect x="330" y="0" width="160" height="36" rx="10" fill="url(#grad-g)"/>
<rect x="330" y="0" width="160" height="36" rx="10" fill="url(#scan)"/>
<rect x="330.75" y="0.75" width="158.5" height="34.5" rx="9.5" fill="none" stroke="#34D399" stroke-width="1.1">
  <animate attributeName="stroke-opacity" values="0.4;0.9;0.4" dur="3.8s" repeatCount="indefinite" begin="0.8s"/>
</rect>
<rect x="340" y="0.5" width="140" height="2" rx="1" fill="#34D399" opacity="0.6">
  <animate attributeName="opacity" values="0.35;0.75;0.35" dur="3.8s" repeatCount="indefinite" begin="0.8s"/>
</rect>
<circle cx="346" cy="18" r="3" fill="#34D399" filter="url(#glow-g)">
  <animate attributeName="r" values="2.6;3.8;2.6" dur="2.8s" repeatCount="indefinite" begin="0.6s"/>
  <animate attributeName="opacity" values="0.7;1;0.7" dur="2.8s" repeatCount="indefinite" begin="0.6s"/>
</circle>
<text x="356" y="14" font-family="'Segoe UI',Arial,sans-serif" font-size="8" font-weight="600"
      fill="#94A3B8" letter-spacing="1.2">REPO SIZE</text>
<rect x="355" y="18.5" width="62" height="13" rx="4" fill="#34D399" fill-opacity="0.12"/>
<rect x="355" y="18.5" width="62" height="13" rx="4" fill="none" stroke="#34D399" stroke-width="0.8" stroke-opacity="0.6"/>
<text x="386" y="28.5" font-family="'Segoe UI',Arial,sans-serif" font-size="9" font-weight="700"
      fill="#ECFDF5" text-anchor="middle" filter="url(#glow-g)" letter-spacing="0.3">1.5 MiB</text>
<rect x="330" y="0" width="10" height="36" rx="10" fill="#34D399" opacity="0.08">
  <animateTransform attributeName="transform" type="translate" from="-10 0" to="170 0"
    dur="4.8s" repeatCount="indefinite" begin="0.5s" calcMode="spline" keySplines="0.4 0 0.6 1"/>
</rect>

<!-- ═══ BADGE 4: Made with Python & SVG (Warm Amber) ═══════════════════════ -->
<rect x="500" y="0" width="220" height="36" rx="10" fill="url(#grad-a)"/>
<rect x="500" y="0" width="220" height="36" rx="10" fill="url(#scan)"/>
<rect x="500.75" y="0.75" width="218.5" height="34.5" rx="9.5" fill="none" stroke="#FBBF24" stroke-width="1.1">
  <animate attributeName="stroke-opacity" values="0.4;0.9;0.4" dur="4.4s" repeatCount="indefinite" begin="1.2s"/>
</rect>
<rect x="510" y="0.5" width="200" height="2" rx="1" fill="#FBBF24" opacity="0.6">
  <animate attributeName="opacity" values="0.35;0.75;0.35" dur="4.4s" repeatCount="indefinite" begin="1.2s"/>
</rect>
<circle cx="516" cy="18" r="3" fill="#FBBF24" filter="url(#glow-a)">
  <animate attributeName="r" values="2.6;3.8;2.6" dur="3.4s" repeatCount="indefinite" begin="1s"/>
  <animate attributeName="opacity" values="0.7;1;0.7" dur="3.4s" repeatCount="indefinite" begin="1s"/>
</circle>
<text x="526" y="14" font-family="'Segoe UI',Arial,sans-serif" font-size="8" font-weight="600"
      fill="#94A3B8" letter-spacing="1.2">MADE WITH</text>
<rect x="525" y="18.5" width="112" height="13" rx="4" fill="#FBBF24" fill-opacity="0.12"/>
<rect x="525" y="18.5" width="112" height="13" rx="4" fill="none" stroke="#FBBF24" stroke-width="0.8" stroke-opacity="0.6"/>
<text x="581" y="28.5" font-family="'Segoe UI',Arial,sans-serif" font-size="9" font-weight="700"
      fill="#FFFBEB" text-anchor="middle" filter="url(#glow-a)" letter-spacing="0.3">Python &amp; SVG</text>
<g stroke="#FBBF24" stroke-width="1.2" stroke-linecap="round" stroke-linejoin="round" opacity="0.4" fill="none">
  <path d="M648 15 L644 18 L648 21 M654 15 L658 18 L654 21"/>
</g>
<rect x="500" y="0" width="10" height="36" rx="10" fill="#FBBF24" opacity="0.08">
  <animateTransform attributeName="transform" type="translate" from="-10 0" to="230 0"
    dur="5.5s" repeatCount="indefinite" begin="1.5s" calcMode="spline" keySplines="0.4 0 0.6 1"/>
</rect>

</svg>'''

# ─────────────────────────────────────────────────────────────────────────────
# 2. Build the animated SYSTEM ACCESSES counter badge SVG
# ─────────────────────────────────────────────────────────────────────────────
COUNTER_SVG = '''\
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 220 42" width="220" height="42" role="img" aria-label="System Access Counter">
<title>System Accesses Counter</title>
<defs>
  <pattern id="grid" width="8" height="8" patternUnits="userSpaceOnUse">
    <path d="M 8 0 L 0 0 0 8" fill="none" stroke="rgba(0,242,255,0.05)" stroke-width="0.5"/>
  </pattern>
  <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="3" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <filter id="glow-sm" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="1.5" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>
  <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%" stop-color="#020c18"/>
    <stop offset="100%" stop-color="#040e1c"/>
  </linearGradient>
  <linearGradient id="label-bg" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#001e30"/>
    <stop offset="100%" stop-color="#002840"/>
  </linearGradient>
  <linearGradient id="val-bg" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%" stop-color="#00F2FF" stop-opacity="0.2"/>
    <stop offset="100%" stop-color="#00F2FF" stop-opacity="0.1"/>
  </linearGradient>
</defs>

<!-- Outer shell -->
<rect width="220" height="42" rx="12" fill="url(#bg)"/>
<rect width="220" height="42" rx="12" fill="url(#grid)"/>

<!-- Animated outer border -->
<rect x="0.8" y="0.8" width="218.4" height="40.4" rx="11.5" fill="none" stroke="#00F2FF" stroke-width="1.5">
  <animate attributeName="stroke-opacity" values="0.2;0.9;0.2" dur="2.5s" repeatCount="indefinite"/>
</rect>

<!-- Corner accent marks -->
<line x1="0" y1="8" x2="0" y2="0" stroke="#00F2FF" stroke-width="2.5" stroke-opacity="0.9" filter="url(#glow-sm)"/>
<line x1="0" y1="0" x2="8" y2="0" stroke="#00F2FF" stroke-width="2.5" stroke-opacity="0.9" filter="url(#glow-sm)"/>
<line x1="212" y1="0" x2="220" y2="0" stroke="#00F2FF" stroke-width="2.5" stroke-opacity="0.9" filter="url(#glow-sm)"/>
<line x1="220" y1="0" x2="220" y2="8" stroke="#00F2FF" stroke-width="2.5" stroke-opacity="0.9" filter="url(#glow-sm)"/>
<line x1="220" y1="34" x2="220" y2="42" stroke="#00F2FF" stroke-width="2.5" stroke-opacity="0.9" filter="url(#glow-sm)"/>
<line x1="220" y1="42" x2="212" y2="42" stroke="#00F2FF" stroke-width="2.5" stroke-opacity="0.9" filter="url(#glow-sm)"/>
<line x1="8" y1="42" x2="0" y2="42" stroke="#00F2FF" stroke-width="2.5" stroke-opacity="0.9" filter="url(#glow-sm)"/>
<line x1="0" y1="42" x2="0" y2="34" stroke="#00F2FF" stroke-width="2.5" stroke-opacity="0.9" filter="url(#glow-sm)"/>

<!-- Top sweep bar animation -->
<rect x="12" y="1" width="196" height="1.5" rx="1" fill="#00F2FF" opacity="0">
  <animate attributeName="opacity" values="0;0.8;0" dur="2.5s" repeatCount="indefinite"/>
</rect>

<!-- Label section -->
<rect x="8" y="6" width="120" height="30" rx="8" fill="url(#label-bg)"/>
<rect x="8" y="6" width="120" height="30" rx="8" fill="none" stroke="#00F2FF" stroke-width="0.8" stroke-opacity="0.3"/>

<!-- Pulse dot -->
<circle cx="22" cy="21" r="4" fill="#00F2FF" filter="url(#glow)">
  <animate attributeName="r" values="3.5;5;3.5" dur="1.8s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="0.6;1;0.6" dur="1.8s" repeatCount="indefinite"/>
</circle>
<circle cx="22" cy="21" r="2" fill="#ffffff" opacity="0.9"/>

<!-- Label text -->
<text x="36" y="17" font-family="'Segoe UI',Arial,sans-serif" font-size="7.5" font-weight="700"
      fill="#8899bb" letter-spacing="1.5">SYSTEM</text>
<text x="36" y="28" font-family="'Segoe UI',Arial,sans-serif" font-size="7.5" font-weight="700"
      fill="#8899bb" letter-spacing="1.5">ACCESSES</text>

<!-- Divider line -->
<line x1="131" y1="8" x2="131" y2="34" stroke="#00F2FF" stroke-width="0.8" stroke-opacity="0.4"/>

<!-- Value section -->
<rect x="134" y="6" width="78" height="30" rx="8" fill="url(#val-bg)"/>
<text x="173" y="26" font-family="'Courier New',Courier,monospace" font-size="17" font-weight="900"
      fill="#00F2FF" text-anchor="middle" filter="url(#glow)" letter-spacing="1">496</text>

<!-- Scan sweep across whole badge -->
<rect x="-20" y="0" width="30" height="42" rx="12" fill="rgba(0,242,255,0.04)">
  <animateTransform attributeName="transform" type="translate" from="-30 0" to="250 0"
    dur="3s" repeatCount="indefinite" calcMode="spline" keySplines="0.4 0 0.6 1"/>
</rect>

<!-- HUD tick marks at bottom right -->
<text x="208" y="39" font-family="'Courier New',Courier,monospace" font-size="5"
      fill="#00F2FF" text-anchor="end" letter-spacing="0.5" opacity="0.5">SYS·v4</text>

</svg>
'''

# ─────────────────────────────────────────────────────────────────────────────
# Write files, update README, commit
# ─────────────────────────────────────────────────────────────────────────────
print("\n  Writing animated badges SVG ...")
write("assets/profile-badges.svg", BADGES_SVG)

print("  Writing animated counter SVG ...")
write("assets/system-counter.svg", COUNTER_SVG)

# Update README: replace shields.io badges row with self-hosted SVG
readme = read("README.md")

# Replace the 4 img.shields.io badges with our new animated SVG
OLD_BADGES = '''  <img src="https://img.shields.io/badge/License-MIT-00F2FF?style=flat-square&logo=opensourceinitiative&logoColor=white" alt="License">
  <img src="https://img.shields.io/github/last-commit/vivekcyr25/vivekcyr25?style=flat-square&color=BC13FE&label=Last%20Commit" alt="Last Commit">
  <img src="https://img.shields.io/github/repo-size/vivekcyr25/vivekcyr25?style=flat-square&color=00FF88&label=Repo%20Size" alt="Repo Size">
  <img src="https://img.shields.io/badge/Made%20with-Python%20%26%20SVG-FFB800?style=flat-square&logo=python&logoColor=white" alt="Made with Python">'''

NEW_BADGES = '  <img src="./assets/profile-badges.svg" alt="Profile Badges: License MIT, Last Commit today, Repo Size 1.5 MiB, Made with Python and SVG" width="720">'

readme = readme.replace(OLD_BADGES, NEW_BADGES)

# Replace komarev counter with self-hosted animated counter
OLD_COUNTER = '  <img src="https://komarev.com/ghpvc/?username=vivekcyr25&color=00F2FF&style=flat-square&label=SYSTEM+ACCESSES" alt="Visitor Counter">'
NEW_COUNTER = '  <img src="./assets/system-counter.svg" alt="System Accesses Counter" width="220">'

readme = readme.replace(OLD_COUNTER, NEW_COUNTER)
write("README.md", readme)

print("  Committing 'feat: self-host animated badges bar SVG' ...")
commit(["assets/profile-badges.svg"], "feat: create animated VisionOS-style profile badges bar SVG")

print("  Committing 'feat: self-host animated SYSTEM ACCESSES counter SVG' ...")
commit(["assets/system-counter.svg"], "feat: create animated HUD-style system accesses counter SVG")

print("  Committing README update ...")
commit(["README.md"], "fix: replace flat shields.io badges and komarev counter with animated self-hosted SVGs")

print("\n  Pushing to origin/main ...")
r = subprocess.run("git push origin main", shell=True, cwd=BASE, capture_output=True, text=True)
print(r.stdout)
if r.returncode == 0:
    print("  🚀 Done! 3 commits pushed to origin/main.")
else:
    print(f"  ❌ Push failed: {r.stderr}")

import subprocess
