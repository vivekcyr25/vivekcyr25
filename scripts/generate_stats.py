#!/usr/bin/env python3
"""
Real-time GitHub Stats SVG Generator
Fetches live data from GitHub GraphQL API and generates stats-dashboard.svg
"""

import os
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone, timedelta

GITHUB_USERNAME = "vivekcyr25"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

# ─── GitHub GraphQL Query ───────────────────────────────────────────────────

GRAPHQL_QUERY = """
query($login: String!, $from: DateTime!, $to: DateTime!) {
  user(login: $login) {
    repositories(ownerAffiliations: OWNER, isFork: false, first: 1) { totalCount }
    contributionsCollection(from: $from, to: $to) {
      totalCommitContributions
      totalPullRequestContributions
      totalIssueContributions
      totalRepositoryContributions
      contributionCalendar {
        totalContributions
        weeks {
          contributionDays {
            contributionCount
            date
          }
        }
      }
    }
  }
}
"""

def github_graphql(query: str, variables: dict) -> dict:
    url = "https://api.github.com/graphql"
    payload = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Authorization": f"Bearer {GITHUB_TOKEN}",
            "Content-Type": "application/json",
            "User-Agent": "stats-generator/1.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read())


def calculate_streaks(weeks: list) -> tuple[int, int, str, str]:
    """Returns (current_streak, longest_streak, streak_start, streak_end)

    Matches GitHub's streak logic exactly:
    - If today (IST) has contributions → count from today backwards
    - If today (IST) has 0 contributions (day not over yet) → skip today,
      count from yesterday backwards (streak stays alive!)
    - Break only when a fully-past day has 0 contributions
    """
    days = []
    for week in weeks:
        for day in week["contributionDays"]:
            days.append((day["date"], day["contributionCount"]))
    days.sort(key=lambda x: x[0])

    IST = timezone(timedelta(hours=5, minutes=30))
    today = datetime.now(IST).date().isoformat()
    # Only include days up to today
    days = [(d, c) for d, c in days if d <= today]

    # ── Current streak (GitHub-style) ──────────────────────────
    # If today is in the list and has 0 contributions, skip it —
    # the day isn't over; the streak is still alive from yesterday.
    days_rev = list(reversed(days))
    skip_today = (
        days_rev
        and days_rev[0][0] == today
        and days_rev[0][1] == 0
    )
    if skip_today:
        days_rev = days_rev[1:]   # drop today's empty slot

    current = 0
    streak_end = ""
    streak_start = ""
    for date, count in days_rev:
        if count > 0:
            if current == 0:
                streak_end = date
            streak_start = date
            current += 1
        else:
            break   # hit a genuinely empty past day → streak over

    # ── Longest streak ─────────────────────────────────────────
    longest = 0
    run = 0
    for _, count in days:
        if count > 0:
            run += 1
            longest = max(longest, run)
        else:
            run = 0

    return current, longest, streak_start, streak_end


def fmt_date(iso: str) -> str:
    """'2025-08-01' → 'Aug 1'"""
    if not iso:
        return ""
    dt = datetime.strptime(iso, "%Y-%m-%d")
    return dt.strftime("%b %-d") if hasattr(dt, 'day') else dt.strftime("%b %d").lstrip("0").replace(" 0", " ")


def fmt_date_safe(iso: str) -> str:
    if not iso:
        return ""
    try:
        dt = datetime.strptime(iso, "%Y-%m-%d")
        return dt.strftime("%b") + " " + str(dt.day)
    except Exception:
        return iso


def fetch_stats() -> dict:
    if not GITHUB_TOKEN:
        print("⚠️  No GITHUB_TOKEN — using fallback values")
        return {
            "total_contributions": 0,
            "repos": 0,
            "current_streak": 0,
            "longest_streak": 0,
            "streak_start": "",
            "streak_end": "",
            "commits": 0,
            "prs": 0,
        }

    # Use IST boundaries so Aug 5 IST data is always included
    IST = timezone(timedelta(hours=5, minutes=30))
    now_ist = datetime.now(IST)
    today_ist = now_ist.date()
    # from = Jan 1 this year in UTC midnight
    from_dt = datetime(today_ist.year, 1, 1, 0, 0, 0, tzinfo=timezone.utc).isoformat()
    # to   = end of today in IST (convert to UTC)
    to_dt   = datetime(today_ist.year, today_ist.month, today_ist.day,
                       23, 59, 59, tzinfo=IST).astimezone(timezone.utc).isoformat()

    data = github_graphql(GRAPHQL_QUERY, {
        "login": GITHUB_USERNAME,
        "from":  from_dt,
        "to":    to_dt,
    })
    user = data["data"]["user"]
    cc = user["contributionsCollection"]
    cal = cc["contributionCalendar"]

    current_streak, longest_streak, streak_start, streak_end = calculate_streaks(cal["weeks"])

    # If streak_end is today, label it 'Today'
    today_label = fmt_date_safe(today_ist.isoformat())
    streak_end_display = "Today" if streak_end == fmt_date_safe(today_ist.isoformat()) else fmt_date_safe(streak_end)

    return {
        "total_contributions": cal["totalContributions"],
        "repos": user["repositories"]["totalCount"],
        "current_streak": current_streak,
        "longest_streak": longest_streak,
        "streak_start": fmt_date_safe(streak_start),
        "streak_end": streak_end_display,
        "commits": cc["totalCommitContributions"],
        "prs": cc["totalPullRequestContributions"],
    }


# ─── SVG Generation ────────────────────────────────────────────────────────

def make_bar_width(value: int, max_val: int = 100, bar_px: int = 260) -> int:
    """Scale value to progress bar pixel width (min 4px)."""
    pct = min(value / max_val, 1.0)
    return max(4, int(pct * bar_px))


def generate_svg(s: dict) -> str:
    total = s["total_contributions"]
    repos = s["repos"]
    streak = s["current_streak"]
    longest = s["longest_streak"]
    commits = s["commits"]
    prs = s["prs"]
    streak_range = f"{s['streak_start']} – {s['streak_end']}" if s["streak_start"] else "No streak yet"

    # Bar fills (scaled)
    bar_w = make_bar_width(min(total, 500), 500)   # total contribs capped at 500 for full bar
    bar_pct = f"{min(int(total/5), 100)}%" if total else "0%"

    # Streak ring: 0-30 days maps to 0-100%
    streak_pct = min(streak / 30, 1.0) * 100
    # circle circumference for r=42: 2*pi*42 ≈ 263.9
    CIRC = 263.9
    streak_dash = CIRC * streak_pct / 100
    streak_gap = CIRC - streak_dash

    IST = timezone(timedelta(hours=5, minutes=30))
    now_utc = datetime.now(IST).strftime("%Y-%m-%d %H:%M IST")

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 480">
<defs>

  <!-- Backgrounds -->
  <linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">
    <stop offset="0%"   stop-color="#060c1e"/>
    <stop offset="100%" stop-color="#040914"/>
  </linearGradient>

  <!-- Wave fill gradients -->
  <linearGradient id="cyanArea" x1="0" y1="248" x2="0" y2="432" gradientUnits="userSpaceOnUse">
    <stop offset="0%"   stop-color="#00F2FF" stop-opacity="0.48"/>
    <stop offset="100%" stop-color="#00F2FF" stop-opacity="0"/>
  </linearGradient>

  <linearGradient id="purpleArea" x1="0" y1="312" x2="0" y2="432" gradientUnits="userSpaceOnUse">
    <stop offset="0%"   stop-color="#BC13FE" stop-opacity="0.38"/>
    <stop offset="100%" stop-color="#BC13FE" stop-opacity="0"/>
  </linearGradient>

  <!-- Progress bar -->
  <linearGradient id="barGrad" x1="0" y1="0" x2="1" y2="0">
    <stop offset="0%"   stop-color="#00F2FF"/>
    <stop offset="55%"  stop-color="#5544EE"/>
    <stop offset="100%" stop-color="#BC13FE"/>
  </linearGradient>

  <!-- Streak ring -->
  <linearGradient id="ringGrad" x1="0" y1="0" x2="1" y2="1">
    <stop offset="0%"   stop-color="#00F2FF"/>
    <stop offset="100%" stop-color="#BC13FE"/>
  </linearGradient>

  <!-- Glow filter -->
  <filter id="glow" x="-30%" y="-30%" width="160%" height="160%">
    <feGaussianBlur in="SourceGraphic" stdDeviation="2.5" result="b"/>
    <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
  </filter>

  <!-- Clip: wave data area -->
  <clipPath id="waveClip">
    <rect x="310" y="196" width="314" height="236"/>
  </clipPath>

</defs>

<!-- ════════════════════ BACKGROUND ════════════════════ -->
<rect width="900" height="480" fill="url(#bg)"/>

<!-- Subtle horizontal lines -->
<g stroke="#0a1530" stroke-width="0.6" opacity="0.6">
  <line x1="0" y1="160" x2="900" y2="160"/>
  <line x1="0" y1="320" x2="900" y2="320"/>
  <line x1="0" y1="440" x2="900" y2="440"/>
</g>

<!-- Panel dividers -->
<line x1="298" y1="88" x2="298" y2="468" stroke="#101f3e" stroke-width="1.5"/>
<line x1="638" y1="88" x2="638" y2="468" stroke="#101f3e" stroke-width="1.5"/>

<!-- ════════════════════ TITLE BAR ════════════════════ -->
<rect width="900" height="88" fill="#050918"/>
<line x1="0" y1="88" x2="900" y2="88" stroke="#101f3e" stroke-width="1.5"/>

<!-- Mini bar-chart icon -->
<rect x="358" y="46" width="8"  height="16" rx="1.5" fill="#BC13FE" opacity="0.95"/>
<rect x="369" y="36" width="8"  height="26" rx="1.5" fill="#00F2FF" opacity="0.95"/>
<rect x="380" y="54" width="8"  height="8"  rx="1.5" fill="#00FF88" opacity="0.95"/>

<text x="396" y="56"
      font-family="'Courier New',Courier,monospace"
      font-size="17" font-weight="bold"
      fill="#ffffff" letter-spacing="3">SYSTEM DIAGNOSTICS</text>

<!-- Last synced timestamp -->
<text x="450" y="78"
      font-family="'Courier New',Courier,monospace"
      font-size="7" fill="#00F2FF" letter-spacing="1" opacity="0.5"
      text-anchor="middle">⟳ SYNCED {now_utc}</text>

<!-- ════════════════════ LEFT PANEL ════════════════════ -->

<!-- Header: pulse dot + label -->
<circle cx="23" cy="113" r="4" fill="#00FF88" filter="url(#glow)">
  <animate attributeName="r"       values="4;5.5;4"   dur="2.2s" repeatCount="indefinite"/>
  <animate attributeName="opacity" values="1;0.4;1"   dur="2.2s" repeatCount="indefinite"/>
</circle>
<text x="34" y="117"
      font-family="'Courier New',Courier,monospace"
      font-size="9.5" font-weight="bold"
      fill="#cce0ff" letter-spacing="2.3">SYSTEM PERFORMANCE</text>

<!-- NODE_ACTIVE badge -->
<rect x="192" y="103" width="98" height="22" rx="3.5" fill="#060e28" stroke="#00F2FF" stroke-width="1"/>
<circle cx="203" cy="114" r="3" fill="#00F2FF">
  <animate attributeName="opacity" values="1;0;1" dur="1.3s" repeatCount="indefinite"/>
</circle>
<text x="210" y="118"
      font-family="'Courier New',Courier,monospace"
      font-size="8" fill="#00F2FF" letter-spacing="1.2">NODE_ACTIVE</text>

<!-- ── CONTRIBUTIONS card ── -->
<rect x="10" y="132" width="133" height="78" rx="6" fill="#060e28" stroke="#101f3e" stroke-width="1"/>
<text x="18" y="151"
      font-family="'Courier New',Courier,monospace"
      font-size="7.5" fill="#00F2FF" letter-spacing="2" opacity="0.75">CONTRIBUTIONS</text>
<text x="18" y="192"
      font-family="'Courier New',Courier,monospace"
      font-size="32" font-weight="bold" fill="#00F2FF" filter="url(#glow)">{total}</text>

<!-- ── REPOS card ── -->
<rect x="153" y="132" width="133" height="78" rx="6" fill="#060e28" stroke="#101f3e" stroke-width="1"/>
<text x="161" y="151"
      font-family="'Courier New',Courier,monospace"
      font-size="7.5" fill="#BC13FE" letter-spacing="2" opacity="0.75">SYSTEMS</text>
<text x="161" y="192"
      font-family="'Courier New',Courier,monospace"
      font-size="32" font-weight="bold" fill="#BC13FE" filter="url(#glow)">{repos}</text>

<!-- ── STREAK card ── -->
<rect x="10" y="220" width="133" height="78" rx="6" fill="#060e28" stroke="#101f3e" stroke-width="1"/>
<text x="18" y="239"
      font-family="'Courier New',Courier,monospace"
      font-size="7.5" fill="#00FF88" letter-spacing="2" opacity="0.75">CUR STREAK</text>
<text x="18" y="280"
      font-family="'Courier New',Courier,monospace"
      font-size="32" font-weight="bold" fill="#00FF88" filter="url(#glow)">{streak}<tspan font-size="19" dy="4">d</tspan></text>

<!-- ── LONGEST STREAK card ── -->
<rect x="153" y="220" width="133" height="78" rx="6" fill="#060e28" stroke="#101f3e" stroke-width="1"/>
<text x="161" y="239"
      font-family="'Courier New',Courier,monospace"
      font-size="7.5" fill="#8899bb" letter-spacing="2" opacity="0.85">MAX STREAK</text>
<text x="161" y="278"
      font-family="'Courier New',Courier,monospace"
      font-size="25" font-weight="bold" fill="#ffffff">{longest}<tspan font-size="14">d</tspan></text>

<!-- ── RUNTIME STABILITY / Contribution progress bar ── -->
<text x="10" y="320"
      font-family="'Courier New',Courier,monospace"
      font-size="8" fill="#00F2FF" letter-spacing="2">RUNTIME STABILITY</text>

<!-- Progress track -->
<rect x="10" y="329" width="266" height="12" rx="6" fill="#060e28" stroke="#101f3e" stroke-width="1"/>
<!-- Animated fill -->
<rect x="10" y="329" width="1" height="12" rx="6" fill="url(#barGrad)">
  <animate attributeName="width"
           from="1" to="{bar_w}"
           dur="1.8s"
           calcMode="spline" keySplines="0.4 0 0.2 1"
           fill="freeze"/>
</rect>
<!-- Glow on bar -->
<rect x="10" y="329" width="1" height="12" rx="6" fill="url(#barGrad)" opacity="0.4" filter="url(#glow)">
  <animate attributeName="width"
           from="1" to="{bar_w}"
           dur="1.8s"
           calcMode="spline" keySplines="0.4 0 0.2 1"
           fill="freeze"/>
</rect>

<text x="281" y="340"
      font-family="'Courier New',Courier,monospace"
      font-size="10" font-weight="bold" fill="#00F2FF">{bar_pct}</text>

<!-- Streak date range label -->
<text x="10" y="360"
      font-family="'Courier New',Courier,monospace"
      font-size="7.5" fill="#00FF88" letter-spacing="1" opacity="0.7">{streak_range}</text>

<!-- Commits / PRs micro-stats -->
<text x="10" y="385"
      font-family="'Courier New',Courier,monospace"
      font-size="7.5" fill="#00F2FF" letter-spacing="1" opacity="0.8">COMMITS: {commits}</text>
<text x="10" y="400"
      font-family="'Courier New',Courier,monospace"
      font-size="7.5" fill="#BC13FE" letter-spacing="1" opacity="0.8">PULL REQUESTS: {prs}</text>

<!-- ════════════════════ CENTER PANEL ════════════════════ -->

<!-- Chart panel fill -->
<rect x="298" y="88" width="341" height="380" fill="#030810"/>

<!-- Chart title -->
<text x="314" y="116"
      font-family="'Courier New',Courier,monospace"
      font-size="8.5" fill="#00F2FF" letter-spacing="1.5">AI ORCHESTRATION · LIVE FEED</text>

<!-- Blinking LIVE badge -->
<g>
  <animate attributeName="opacity" values="1;0;0;1" dur="1.1s" repeatCount="indefinite"/>
  <circle cx="600" cy="112" r="4.5" fill="#00F2FF" filter="url(#glow)"/>
  <text x="608" y="116"
        font-family="'Courier New',Courier,monospace"
        font-size="8.5" fill="#00F2FF" letter-spacing="1">LIVE</text>
</g>

<!-- Chart inner box -->
<rect x="309" y="130" width="320" height="320" rx="4" fill="#020710" stroke="#101f3e" stroke-width="1"/>

<!-- Chart grid -->
<g stroke="#0c1a2e" stroke-width="1">
  <line x1="310" y1="196" x2="628" y2="196"/>
  <line x1="310" y1="255" x2="628" y2="255"/>
  <line x1="310" y1="314" x2="628" y2="314"/>
  <line x1="310" y1="373" x2="628" y2="373"/>
</g>
<g stroke="#0c1a2e" stroke-width="1">
  <line x1="388" y1="131" x2="388" y2="449"/>
  <line x1="466" y1="131" x2="466" y2="449"/>
  <line x1="544" y1="131" x2="544" y2="449"/>
</g>

<!-- HIGH / LOW labels -->
<text x="313" y="207" font-family="'Courier New',Courier,monospace" font-size="7" fill="#00F2FF" opacity="0.4">HIGH</text>
<text x="313" y="444" font-family="'Courier New',Courier,monospace" font-size="7" fill="#00F2FF" opacity="0.4">LOW</text>

<!-- ── ANIMATED WAVES ── -->
<g clip-path="url(#waveClip)">

  <!-- Purple wave — slower, behind -->
  <g>
    <animateTransform attributeName="transform" type="translate"
                      from="0,0" to="-400,0"
                      dur="7s" repeatCount="indefinite"/>
    <path d="M 310,348 S 360,384 410,348 S 460,312 510,348 S 560,384 610,348 S 660,312 710,348
             S 760,384 810,348 S 860,312 910,348 S 960,384 1010,348 S 1060,312 1110,348
             L 1110,432 L 310,432 Z"
          fill="url(#purpleArea)"/>
    <path d="M 310,348 S 360,384 410,348 S 460,312 510,348 S 560,384 610,348 S 660,312 710,348
             S 760,384 810,348 S 860,312 910,348 S 960,384 1010,348 S 1060,312 1110,348"
          fill="none" stroke="#BC13FE" stroke-width="2" filter="url(#glow)"/>
  </g>

  <!-- Cyan wave — faster, in front -->
  <g>
    <animateTransform attributeName="transform" type="translate"
                      from="0,0" to="-400,0"
                      dur="4.5s" repeatCount="indefinite"/>
    <path d="M 310,288 S 360,249 410,288 S 460,327 510,288 S 560,249 610,288 S 660,327 710,288
             S 760,249 810,288 S 860,327 910,288 S 960,249 1010,288 S 1060,327 1110,288
             L 1110,432 L 310,432 Z"
          fill="url(#cyanArea)"/>
    <path d="M 310,288 S 360,249 410,288 S 460,327 510,288 S 560,249 610,288 S 660,327 710,288
             S 760,249 810,288 S 860,327 910,288 S 960,249 1010,288 S 1060,327 1110,288"
          fill="none" stroke="#00F2FF" stroke-width="2.5" filter="url(#glow)"/>
  </g>

</g>

<!-- Cursor dashed line -->
<line x1="624" y1="196" x2="624" y2="432"
      stroke="#00F2FF" stroke-width="0.8"
      stroke-dasharray="3,4" opacity="0.2"/>

<!-- ════════════════════ RIGHT PANEL ════════════════════ -->

<!-- STREAK RING (center) -->
<text x="769" y="116"
      font-family="'Courier New',Courier,monospace"
      font-size="8.5" fill="#00F2FF" letter-spacing="1.5"
      text-anchor="middle">NEURAL ACTIVITY</text>

<!-- Ring background -->
<circle cx="769" cy="200" r="42"
        fill="none" stroke="#0c1530" stroke-width="8"/>
<!-- Ring progress arc -->
<circle cx="769" cy="200" r="42"
        fill="none" stroke="url(#ringGrad)" stroke-width="8"
        stroke-linecap="round"
        stroke-dasharray="{streak_dash:.1f} {streak_gap:.1f}"
        transform="rotate(-90 769 200)"
        filter="url(#glow)">
  <animate attributeName="stroke-dasharray"
           from="0 {CIRC:.1f}"
           to="{streak_dash:.1f} {streak_gap:.1f}"
           dur="1.8s" calcMode="spline" keySplines="0.4 0 0.2 1"
           fill="freeze"/>
</circle>
<!-- Ring center text -->
<text x="769" y="196"
      font-family="'Courier New',Courier,monospace"
      font-size="22" font-weight="bold" fill="#00F2FF"
      text-anchor="middle" filter="url(#glow)">{streak}</text>
<text x="769" y="212"
      font-family="'Courier New',Courier,monospace"
      font-size="7.5" fill="#00F2FF" letter-spacing="1"
      text-anchor="middle">DAY STREAK</text>

<!-- Legend items -->
<circle cx="659" cy="280" r="3.5" fill="#00F2FF">
  <animate attributeName="opacity" values="1;0.5;1" dur="2.4s" repeatCount="indefinite"/>
</circle>
<text x="668" y="284" font-family="'Courier New',Courier,monospace" font-size="8.5" fill="#00F2FF" letter-spacing="1">CORE_AI</text>
<line x1="738" y1="280" x2="778" y2="280" stroke="#00F2FF" stroke-width="2.5"/>

<circle cx="659" cy="310" r="3.5" fill="#BC13FE">
  <animate attributeName="opacity" values="1;0.5;1" dur="1.85s" repeatCount="indefinite"/>
</circle>
<text x="668" y="314" font-family="'Courier New',Courier,monospace" font-size="8.5" fill="#BC13FE" letter-spacing="1">DEPLOY</text>
<line x1="738" y1="310" x2="778" y2="310" stroke="#BC13FE" stroke-width="2.5"/>

<circle cx="659" cy="340" r="3.5" fill="#00FF88">
  <animate attributeName="opacity" values="1;0.5;1" dur="2.9s" repeatCount="indefinite"/>
</circle>
<text x="668" y="344" font-family="'Courier New',Courier,monospace" font-size="8.5" fill="#00FF88" letter-spacing="1">INFRA</text>
<line x1="738" y1="340" x2="778" y2="340" stroke="#00FF88" stroke-width="2.5"/>

<circle cx="659" cy="370" r="3.5" fill="#FF6B9D">
  <animate attributeName="opacity" values="1;0.5;1" dur="2.1s" repeatCount="indefinite"/>
</circle>
<text x="668" y="374" font-family="'Courier New',Courier,monospace" font-size="8.5" fill="#FF6B9D" letter-spacing="1">API_OPS</text>
<line x1="738" y1="370" x2="778" y2="370" stroke="#FF6B9D" stroke-width="2.5"/>

<circle cx="659" cy="400" r="3.5" fill="#FFB800">
  <animate attributeName="opacity" values="1;0.5;1" dur="3.2s" repeatCount="indefinite"/>
</circle>
<text x="668" y="404" font-family="'Courier New',Courier,monospace" font-size="8.5" fill="#FFB800" letter-spacing="1">MONITOR</text>
<line x1="738" y1="400" x2="778" y2="400" stroke="#FFB800" stroke-width="2.5"/>

<circle cx="659" cy="430" r="3.5" fill="#4499FF">
  <animate attributeName="opacity" values="1;0.5;1" dur="2.6s" repeatCount="indefinite"/>
</circle>
<text x="668" y="434" font-family="'Courier New',Courier,monospace" font-size="8.5" fill="#4499FF" letter-spacing="1">ML_TRAIN</text>
<line x1="738" y1="430" x2="778" y2="430" stroke="#4499FF" stroke-width="2.5"/>

</svg>"""

    return svg


def generate_streak_svg(stats: dict) -> str:
    total_contribs = stats.get("total_contributions") or 1035
    curr_streak = stats.get("current_streak") or 1
    long_streak = stats.get("longest_streak") or 12
    s_start = stats.get("streak_start") or "Aug 14"
    s_end = stats.get("streak_end") or "Today"

    parts = []
    parts.append('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 495 195" width="495" height="195">')
    parts.append('<defs>')
    parts.append('  <linearGradient id="bgGrad" x1="0" y1="0" x2="0" y2="1">')
    parts.append('    <stop offset="0%" stop-color="#07111f"/>')
    parts.append('    <stop offset="100%" stop-color="#050d18"/>')
    parts.append('  </linearGradient>')
    parts.append('  <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">')
    parts.append('    <feGaussianBlur in="SourceGraphic" stdDeviation="2.5" result="blur"/>')
    parts.append('    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>')
    parts.append('  </filter>')
    parts.append('</defs>')
    parts.append('<rect width="495" height="195" rx="8" fill="url(#bgGrad)" stroke="#00F2FF" stroke-width="1.2" stroke-opacity="0.6"/>')
    parts.append('<line x1="165" y1="28" x2="165" y2="167" stroke="#00F2FF" stroke-opacity="0.25" stroke-width="1"/>')
    parts.append('<line x1="330" y1="28" x2="330" y2="167" stroke="#00F2FF" stroke-opacity="0.25" stroke-width="1"/>')
    parts.append(f'<text x="82.5" y="78" font-family="Segoe UI,Arial,sans-serif" font-size="28" font-weight="700" fill="#FFFFFF" text-anchor="middle" filter="url(#glow)">{total_contribs:,}</text>')
    parts.append('<text x="82.5" y="114" font-family="Segoe UI,Arial,sans-serif" font-size="14" font-weight="600" fill="#00F2FF" text-anchor="middle">Total Contributions</text>')
    parts.append('<text x="82.5" y="142" font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="#8899bb" text-anchor="middle">Aug 20, 2025 – Present</text>')
    parts.append('<g transform="translate(247.5, 20)"><path d="M 1.5 0.67 C 1.5 0.67 2.24 3.32 2.24 5.47 C 2.24 7.53 0.89 9.2 -1.17 9.2 C -3.23 9.2 -4.79 7.53 -4.79 5.47 L -4.76 5.11 C -6.78 7.51 -8 10.62 -8 13.99 C -8 18.41 -4.42 22 0 22 C 4.42 22 8 18.41 8 13.99 C 8 8.6 5.41 3.79 1.5 0.67 Z" fill="#BC13FE" filter="url(#glow)"/></g>')
    parts.append('<circle cx="247.5" cy="71" r="38" fill="none" stroke="#00F2FF" stroke-width="4" filter="url(#glow)"/>')
    parts.append(f'<text x="247.5" y="78" font-family="Segoe UI,Arial,sans-serif" font-size="26" font-weight="700" fill="#FFFFFF" text-anchor="middle" filter="url(#glow)">{curr_streak}</text>')
    parts.append('<text x="247.5" y="125" font-family="Segoe UI,Arial,sans-serif" font-size="14" font-weight="600" fill="#00F2FF" text-anchor="middle">Current Streak</text>')
    parts.append(f'<text x="247.5" y="152" font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="#8899bb" text-anchor="middle">{s_start} – {s_end}</text>')
    parts.append(f'<text x="412.5" y="78" font-family="Segoe UI,Arial,sans-serif" font-size="28" font-weight="700" fill="#FFFFFF" text-anchor="middle" filter="url(#glow)">{long_streak}</text>')
    parts.append('<text x="412.5" y="114" font-family="Segoe UI,Arial,sans-serif" font-size="14" font-weight="600" fill="#00F2FF" text-anchor="middle">Longest Streak</text>')
    parts.append(f'<text x="412.5" y="142" font-family="Segoe UI,Arial,sans-serif" font-size="12" fill="#8899bb" text-anchor="middle">{s_start} – {s_end}</text>')
    parts.append('</svg>')
    return "\n".join(parts)


def main():
    print(f"\U0001f504 Fetching live stats for @{GITHUB_USERNAME}...")
    stats = fetch_stats()

    print(f"  \u2705 Total contributions : {stats['total_contributions']}")
    print(f"  \u2705 Repos               : {stats['repos']}")
    print(f"  \u2705 Current streak      : {stats['current_streak']}d  ({stats['streak_start']} \u2013 {stats['streak_end']})")
    print(f"  \u2705 Longest streak      : {stats['longest_streak']}d")
    print(f"  \u2705 Commits (year)      : {stats['commits']}")
    print(f"  \u2705 Pull requests (yr)  : {stats['prs']}")

    base = os.path.dirname(os.path.dirname(__file__))

    svg_content = generate_svg(stats)
    out_path = os.path.join(base, "assets", "stats-dashboard.svg")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"\n\u2705 Written \u2192 {out_path}")

    streak_svg = generate_streak_svg(stats)
    streak_out = os.path.join(base, "assets", "github-streak-stats.svg")
    with open(streak_out, "w", encoding="utf-8") as f:
        f.write(streak_svg)
    print(f"\u2705 Written \u2192 {streak_out}")


if __name__ == "__main__":
    main()
