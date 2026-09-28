#!/usr/bin/env python3
"""Build the Mastering Copilot in Microsoft 365 workshop site (CODED workshop-builder, SPECIMEN design).

Output: ../site/ (flat, Netlify drag-and-drop). Run:  python3 build.py
Dates + live links are edited after deploy in site/site-config.js (not rebuilt).
"""
import base64, html, json, os, re, shutil, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(os.path.dirname(ROOT), 'site')
sys.path.insert(0, os.path.join(ROOT, 'content'))
from days import DAYS  # noqa: E402

M = json.load(open(os.path.join(ROOT, 'manifest.json'), encoding='utf-8'))
TITLE = M['title']


def rd(p):
    return open(os.path.join(ROOT, p), encoding='utf-8').read()


THEME = rd('css/theme.css')
BASE = rd('css/base.css')
CODED_THEME = rd('css/coded-theme.css')
COMMON = rd('static/common.js')
LOGO = rd('static/coded-logo.txt').strip()
if not LOGO.startswith('data:'):
    LOGO = 'data:image/png;base64,' + LOGO
ICON = {k: 'data:image/png;base64,' + base64.b64encode(open(os.path.join(ROOT, 'static', k + '.png'), 'rb').read()).decode()
        for k in ('word', 'excel', 'powerpoint', 'outlook')}
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">\n'
         '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '<link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600;700&family=IBM+Plex+Sans+Arabic:wght@400;500;600;700&display=swap" rel="stylesheet">')
FAVICON = ('<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns=%27http://www.w3.org/2000/svg%27 viewBox=%270 0 32 32%27%3E'
           '%3Crect width=%2732%27 height=%2732%27 rx=%278%27 fill=%27%2300112F%27/%3E%3Ccircle cx=%2716%27 cy=%2716%27 r=%277%27 fill=%27%232f74d6%27/%3E%3C/svg%3E">')


def esc(s):
    return html.escape(str(s), quote=True)


def fill_icons(s):
    return re.sub(r'\{\{ICON:(\w+)\}\}', lambda m: ICON[m.group(1)], s)


def page(title, body, css='', js='', desc='', qr=False, body_class=''):
    cls = f' class="{body_class}"' if body_class else ''
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
{FAVICON}
{FONTS}
<style>
{THEME}
{BASE}
{css}
{CODED_THEME}
</style>
<script src="site-config.js"></script>
{'<script src="qrcode.min.js"></script>' if qr else ''}
</head>
<body{cls}>
{body}
<script>
{COMMON}
</script>
{('<script>' + chr(10) + js + chr(10) + '</script>') if js else ''}
</body>
</html>
'''


def write(name, content):
    with open(os.path.join(OUT, name), 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'  {name:44s} {len(content)/1024:7.1f} KB')


def fn_day(n):
    return f'coded-copilot-day-{n}.html'


def fn_deck(n):
    return f'coded-copilot-day-{n}-deck.html'


def fn_lab(n):
    return f'coded-copilot-day-{n}-lab.html'


# ---------------------------------------------------------------- small svg icon set (Lucide-style line icons)
SVG = {
    'cal': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><rect x="3" y="4.5" width="18" height="17" rx="2.5"/><path d="M16 2.5v4M8 2.5v4M3 10h18"/></svg>',
    'clock': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7.5v5l3 2"/></svg>',
    'pin': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10.5c0 6.5-9 12.5-9 12.5s-9-6-9-12.5a9 9 0 0118 0z"/><circle cx="12" cy="10.5" r="3"/></svg>',
    'check': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"><path d="M4 12l5 5L20 6"/></svg>',
    'screen': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/></svg>',
    'flag': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/></svg>',
    'map': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 4L3 6v14l6-2 6 2 6-2V4l-6 2z"/><path d="M9 4v14M15 6v14"/></svg>',
    'setup': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 00.3 1.8l.1.1a2 2 0 11-2.8 2.8l-.1-.1a1.7 1.7 0 00-1.8-.3 1.7 1.7 0 00-1 1.5V21a2 2 0 11-4 0v-.1a1.7 1.7 0 00-1.1-1.5 1.7 1.7 0 00-1.8.3l-.1.1a2 2 0 11-2.8-2.8l.1-.1a1.7 1.7 0 00.3-1.8 1.7 1.7 0 00-1.5-1H3a2 2 0 110-4h.1a1.7 1.7 0 001.5-1.1 1.7 1.7 0 00-.3-1.8l-.1-.1a2 2 0 112.8-2.8l.1.1a1.7 1.7 0 001.8.3H9a1.7 1.7 0 001-1.5V3a2 2 0 114 0v.1a1.7 1.7 0 001 1.5 1.7 1.7 0 001.8-.3l.1-.1a2 2 0 112.8 2.8l-.1.1a1.7 1.7 0 00-.3 1.8V9a1.7 1.7 0 001.5 1H21a2 2 0 110 4h-.1a1.7 1.7 0 00-1.5 1z"/></svg>',
    'doc': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><path d="M14 2v6h6M9 13h6M9 17h4"/></svg>',
    'bank': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21l-7-5-7 5V5a2 2 0 012-2h10a2 2 0 012 2z"/></svg>',
    'sheet': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16v16H4z"/><path d="M8 8h8M8 12h8M8 16h5"/></svg>',
    'all': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l9 4-9 4-9-4z"/><path d="M3 12l9 4 9-4"/><path d="M3 17l9 4 9-4"/></svg>',
    'cap': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2l3 6 6 .9-4.5 4.3 1 6.3L12 16.5 6.5 19.5l1-6.3L3 8.9 9 8z"/></svg>',
    'survey': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 11l3 3L22 4"/><path d="M21 12v7a2 2 0 01-2 2H5a2 2 0 01-2-2V5a2 2 0 012-2h11"/></svg>',
    'out': '<svg class="out" viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 17L17 7M8 7h9v9"/></svg>',
    'coffee': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 8h13v5a5 5 0 01-5 5H9a5 5 0 01-5-5z"/><path d="M17 9h2a2.5 2.5 0 010 5h-2"/></svg>',
    'spark': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3l2.1 4.9L19 9l-4.9 2.1L12 16l-2.1-4.9L5 9l4.9-2.1z"/><path d="M18 15l.9 2.1L21 18l-2.1.9L18 21l-.9-2.1L15 18l2.1-.9z"/></svg>',
    'send': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 2L11 13"/><path d="M22 2l-7 20-4-9-9-4z"/></svg>',
    'shield': '<svg viewBox="0 0 24 24" width="{s}" height="{s}" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/><path d="M9 12l2 2 4-4"/></svg>',
}


def ic(name, s=16):
    return SVG[name].replace('{s}', str(s))


def res_row(href, label, icon):
    """Resources list row; href 'link:<key>' means a config-driven link (site-config.js)."""
    if href.startswith('link:'):
        k = href[5:]
        return (f'<a class="res" data-link="{k}"><span class="res-ic">{ic(icon)}</span>'
                f'<span class="res-nm">{esc(label)} <span class="res-soon" data-pending="· link coming soon"></span></span>{ic("out", 15)}</a>')
    ext = href.endswith(('.docx', '.xlsx', '.pptx', '.pdf'))
    dl = ' download' if ext else ''
    return f'<a class="res" href="{esc(href)}"{dl}><span class="res-ic">{ic(icon)}</span><span class="res-nm">{esc(label)}</span>{ic("out", 15)}</a>'


# ================================================================= DECK
DECK_CSS = rd('css/deck.css') + '\n' + rd('css/deck-extra.css')
DECK_JS = rd('static/deck.js')
DECK_DATA = {
    1: '''window.DECK_AC=[
 {stem:'Please find the report…',sugg:[['attached','71%'],['below','12%'],['in the shared folder','9%'],['enclosed','4%']]},
 {stem:'The meeting has been moved to…',sugg:[['tomorrow','38%'],['Thursday','21%'],['next week','17%'],['3 PM','9%']]},
 {stem:'Thank you for your…',sugg:[['patience','44%'],['email','22%'],['support','15%'],['time','11%']]}
];
window.DECK_PRED=[
 {pick:'Copilot',c:[['Copilot','62%'],['The','12%'],['Our','8%']]},
 {pick:'drafts',c:[['drafts','54%'],['writes','24%'],['reads','9%']]},
 {pick:'your',c:[['your','71%'],['the','16%'],['an','6%']]},
 {pick:'email',c:[['email','44%'],['memo','27%'],['report','15%']]},
 {pick:'in',c:[['in','58%'],['within','20%'],['before','8%']]},
 {pick:'seconds.',c:[['seconds.','66%'],['minutes.','23%'],['Arabic.','4%']]}
];''',
    2: '''window.DECK_TONES={
 concise:"Replacement boxes arrive Thursday. We're reviewing a credit note and will confirm by tomorrow. Sorry for the trouble — Tamra Sales Team.",
 warm:"Thank you for telling us — and I'm sorry. This is the second time, and it shouldn't have happened. New boxes will reach you on Thursday, and I'm personally following up on a credit note. I'll confirm it with you by tomorrow. We really value working with Darwaza Hotels. — Tamra Sales Team",
 firm:"The replacement boxes will arrive on Thursday — the warehouse has confirmed the slot. A credit note is under review, and I will confirm the outcome by tomorrow. I won't promise more than we can deliver. Thank you for your patience. — Tamra Sales Team"
};''',
}


def deck_chrome(n):
    back = fn_day(n)
    top = (f'<div class="prog-track"><div class="pt-fill" id="ptFill"></div></div>\n'
           f'<a class="deck-back" href="{back}" title="Back to the Day {n} page"><svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg><span>Day {n}</span></a>\n')
    bottom = '''
<div class="deck-nav">
  <button class="nav-btn" id="prevBtn" aria-label="Previous slide"><svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg></button>
  <span class="deck-prog" id="prog">1 / 1</span>
  <button class="nav-btn" id="nextBtn" aria-label="Next slide"><svg viewBox="0 0 24 24"><path d="M9 5l7 7-7 7"/></svg></button>
  <button class="brk-btn" id="brkBtn" aria-label="Break timer" title="Break timer">☕</button>
</div>
<div class="kbd-hint"><kbd>→</kbd> next <kbd>←</kbd> back <kbd>F</kbd> full</div>
<div class="break-pick" id="breakPick">
  <div class="bp-card">
    <h3>Break timer</h3><p>Pick a length — the room sees a countdown.</p>
    <div class="bp-opts">
      <button class="bp-opt" data-min="5">5 min</button><button class="bp-opt" data-min="10">10 min</button>
      <button class="bp-opt" data-min="15">15 min</button><button class="bp-opt" data-min="20">20 min</button>
      <button class="bp-opt" data-min="30">30 min</button><button class="bp-opt" data-min="60">60 min</button>
    </div>
    <button class="bp-close" id="bpClose">Cancel</button>
  </div>
</div>
<div class="break-ov" id="breakOv">
  <div class="brk-wrap">
    <div class="brk-eyebrow">Break</div>
    <div class="brk-time" id="brkTime">05:00</div>
    <div class="brk-back" id="brkBack">Back at 00:00</div>
    <div class="brk-actions"><button class="brk-act" id="brkPlus">+5 min</button><button class="brk-act end" id="brkEnd">End break</button></div>
  </div>
</div>
<div class="qr-ov" id="qrOv"><div class="qr-big"></div><div class="qr-ov-cap">Tap anywhere to close</div></div>
'''
    return top, bottom


def build_deck(n):
    src = os.path.join(ROOT, 'content', f'day{n}-deck.html')
    if not os.path.exists(src):
        return
    slides = fill_icons(rd(f'content/day{n}-deck.html'))
    top, bottom = deck_chrome(n)
    body = top + slides + bottom
    d = DAYS[n]
    write(fn_deck(n), page(f'Day {n} Slides — {TITLE} · CODED', body, css=DECK_CSS, js=DECK_DATA.get(n, '') + '\n' + DECK_JS,
                           desc=f'Day {n} interactive slide deck — {d["title"]}.', qr=True))


# ================================================================= LAB
LAB_CSS = rd('css/lab.css')
LAB_JS = rd('static/lab.js')


def build_lab(n):
    src = os.path.join(ROOT, 'content', f'day{n}-lab.js')
    if not os.path.exists(src):
        return
    data = rd(f'content/day{n}-lab.js')
    roles = ''.join(f'<option value="{k}">{v}</option>' for k, v in M['roles'].items())
    body = f'''<aside id="rail">
  <div class="rail-brand"><span class="dot"></span>Copilot <b>Lab</b></div>
  <span class="day-chip">Day {n} · {esc(DAYS[n]['title'])}</span>
  <div class="role-pick"><label for="roleSel">Your track</label><select id="roleSel"><option value="">Pick your track…</option>{roles}</select></div>
  <div class="prog-wrap"><div class="prog-bar"><div class="prog-fill" id="progFill"></div></div><div class="prog-label" id="progLabel">0 done</div>
    <div class="prog-label" style="margin-top:9px;color:var(--amber);line-height:1.5">Finish Core, then keep going — Stretch if you're early, Boss if you're fast.</div></div>
  <nav id="navList" aria-label="Tasks"></nav>
  <div class="rail-foot"><a href="before-you-start.html">Setup help</a><button id="resetBtn" type="button">↺ Reset</button></div>
</aside>
<div id="main">
  <div id="mtop">
    <button class="ham" id="ham" aria-label="Menu" type="button"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
    <a class="back" href="{fn_day(n)}">‹ Back</a>
    <span class="crumb" id="crumb">Task 1</span>
    <a class="pbpill" href="prompt-bank.html" target="_blank" rel="noopener">{ic('bank', 14)}<span class="t">My Prompt Bank</span> <b id="pbCount">0</b></a>
    <div class="mnav"><button id="mPrev" type="button" aria-label="Previous task">‹</button><button id="mNext" type="button" aria-label="Next task">›</button></div>
  </div>
  <main id="view"></main>
</div>'''
    write(fn_lab(n), page(f'Day {n} Lab — {TITLE} · CODED', body, css=LAB_CSS, js=data + '\n' + LAB_JS,
                          desc=f'Day {n} hands-on Copilot lab.', body_class='lab'))


# ================================================================= DAY PAGES
DAY_CSS = rd('css/day.css')


def footer_row(extra=''):
    return f'''<footer class="site-foot"><div class="wrap"><div class="foot-row">
  <div class="f-lockup"><img class="coded-logo" alt="CODED" src="{LOGO}"></div>
  <span class="copy">© 2026 CODED · {esc(TITLE)}{extra}</span>
</div></div></footer>'''


def build_day(n):
    d = DAYS[n]
    ros = []
    num = 0
    for kind, title, time, desc in d['ros']:
        if kind == 'brk':
            ros.append(f'<li class="is-brk"><span class="brk">{ic("coffee", 15)}</span><div class="rc"><div class="rt"><b>{esc(title)}</b><span class="time">{esc(time)}</span></div></div></li>')
        else:
            num += 1
            ros.append(f'<li><span class="num">{num}</span><div class="rc"><div class="rt"><b>{esc(title)}</b><span class="time">{esc(time)}</span></div><div class="rd">{esc(desc)}</div></div></li>')
    outcomes = ''.join(f'<li>{ic("check", 15)}<span>{esc(o)}</span></li>' for o in d['outcomes'])
    chips = ''.join(f'<span class="chip2">{esc(c)}</span>' for c in d['chips'])
    res = ''.join(res_row(h, l, i) for h, l, i in d['resources'])
    cap_panel = ''
    if n == 3:
        cap_panel = f'''<section class="panel cta-panel">
          <div class="cta-ico">{ic('cap', 20)}</div>
          <h3>Your capstone</h3>
          <p>Four role tracks, starter scenarios, sample inputs and a light self-check rubric. Your workflow goes home with you.</p>
          <a class="slides-btn" href="capstone.html"><span>Open the capstone</span> <span class="ar">→</span></a>
        </section>'''
    prev_next = []
    if n > 1:
        prev_next.append(f'<a class="pn" href="{fn_day(n-1)}">← Day {n-1} · {esc(DAYS[n-1]["title"])}</a>')
    if n < 3:
        prev_next.append(f'<a class="pn nx" href="{fn_day(n+1)}">Day {n+1} · {esc(DAYS[n+1]["title"])} →</a>')
    body = f'''<div class="wrap"><div class="topbar"><a class="back" href="index.html"><span class="ar">←</span> Workshop home</a></div></div>
<div class="wrap hero-wrap">
  <div class="d-hero">
    <div class="d-hero-top"><span class="cat-pill"><span class="dot"></span> Day {n} of 3 · <span data-cfg="dates.{d['cfg']}">{esc(d['date_long'])}</span></span></div>
    <h1>{esc(d['title'])}</h1>
    <p class="lede">{esc(d['lede'])}</p>
    <div class="d-meta">
      <span>{ic('cal', 15)} <span data-cfg="dates.{d['cfg']}">{esc(d['date_long'])}</span></span>
      <span>{ic('clock', 15)} {esc(d['hours'])}</span>
      <span>{ic('pin', 15)} <span data-cfg="venue">CODED, Kuwait</span></span>
    </div>
  </div>
</div>
<div class="wrap">
  <div class="d-grid">
    <div class="d-main">
      <section class="panel"><h2>Day brief</h2><p class="brief">{esc(d['brief'])}</p></section>
      <section class="panel"><h2>Run of show</h2><p class="muted">A guide, not a script — timings flex to the room.</p><ol class="ros">{''.join(ros)}</ol></section>
      <div class="pn-row">{''.join(prev_next)}</div>
    </div>
    <aside class="d-side">
      <section class="panel cta-panel">
        <div class="cta-ico">{ic('screen', 22)}</div>
        <h3>Day {n} slides</h3>
        <p>The full interactive deck — concepts, live demos and the hands-on prompts, as run in the room.</p>
        <a class="slides-btn" href="{fn_deck(n)}"><span>Open the slides</span> <span class="ar">→</span></a>
      </section>
      <section class="panel cta-panel">
        <div class="cta-ico">{ic('flag', 20)}</div>
        <h3>Day {n} hands-on lab</h3>
        <p>{esc(d['lab_blurb'])}</p>
        <a class="slides-btn" href="{fn_lab(n)}"><span>Launch the lab</span> <span class="ar">→</span></a>
      </section>
      {cap_panel}
      <section class="panel"><h3>What you'll leave able to do</h3><ul class="leave">{outcomes}</ul></section>
      <section class="panel"><h3>What we'll cover</h3><div class="chips">{chips}</div></section>
      <section class="panel"><h3>Resources</h3><div class="res-list">{res}</div></section>
    </aside>
  </div>
</div>
{footer_row()}'''
    write(fn_day(n), page(f'Day {n} — {d["title"]} · {TITLE} · CODED', body, css=DAY_CSS,
                          desc=f'Day {n} of {TITLE}: {d["lede"]}'))


# ================================================================= LANDING
LANDING_CSS = rd('css/landing.css')


def build_landing():
    cards = []
    icons = {1: 'spark', 2: 'send', 3: 'shield'}
    for n in (1, 2, 3):
        d = DAYS[n]
        checks = {
            1: ['How AI and large language models work — and where not to trust them', 'What Copilot is, how it compares, and what it can do', 'The CTFT prompt recipe, practised in Copilot Chat'],
            2: ['Word — draft, rewrite, ground in a file', 'PowerPoint — document to deck', 'Excel — analysis you can check', 'Outlook & Teams — tame the thread, recap the meeting'],
            3: ['Security, compliance and Microsoft’s Responsible AI principles', 'The Prompt Gallery — find, adapt, save', 'Capstone: a Copilot workflow for your real job'],
        }[n]
        lis = ''.join(f'<li>{ic("check", 15)}<span>{esc(c)}</span></li>' for c in checks)
        cards.append(f'''<div class="dcard">
        <div class="dcard-top">
          <span class="verb-chip">{d['verb']}</span>
          <span class="top-ico">{ic(icons[n], 21)}</span>
          <span class="ghost-n">0{n}</span>
          <div class="meta-chips">
            <span class="mchip">{ic('cal', 13)}<span data-cfg="dates.{d['cfg_short']}">{esc(d['date_short'])}</span></span>
            <span class="mchip">{ic('clock', 13)}{esc(d['hours_short'])}</span>
          </div>
        </div>
        <div class="dcard-body">
          <span class="d-eyebrow">Day 0{n}</span>
          <h3>{esc(d['title'])}</h3>
          <p class="d-sub">{esc(d['sub'])}</p>
          <ul class="checks">{lis}</ul>
          <a class="open-btn" href="{fn_day(n)}">Open day {n} <span class="arr">→</span></a>
        </div>
      </div>''')
    body = f'''<header class="hero">
  <div class="glow g1"></div><div class="glow g2"></div><div class="glow g3"></div><div class="glow g4"></div>
  <div class="inner">
    <div class="pill"><span class="dot"></span> <span data-cfg="cohort">CODED · Kuwait</span></div>
    <div class="lockup"><img class="coded-logo" alt="CODED" src="{LOGO}"></div>
    <h1 class="headline"><span class="l1">Mastering Copilot</span><span class="accent">in Microsoft 365</span></h1>
    <p class="sub">A hands-on, three-day workshop for professionals who want Copilot to do real work — drafting, analysing, presenting and replying across Word, Excel, PowerPoint and Outlook. Safely.</p>
    <div class="meta">
      <span>{ic('cal', 16)} <span data-cfg="datesRange">29 Sep – 1 Oct 2026</span></span>
      <span>{ic('clock', 16)} 9:00 AM – 2:00 PM</span>
      <span>{ic('pin', 16)} <span data-cfg="venue">CODED, Kuwait</span></span>
    </div>
    <a href="#programme" class="cta">Explore the programme <span class="arr">→</span></a>
  </div>
  <a class="scrollhint" href="#programme">The three days ↓</a>
</header>

<section class="blk" id="programme">
  <div class="wrap">
    <span class="eyebrow">The Programme</span>
    <h2 class="sec-title">Three days, one <span class="hl">working habit</span>.</h2>
    <p class="sec-lede">Day 1 opens the engine and teaches the prompt recipe. Day 2 puts Copilot to work in Word, PowerPoint, Excel and Outlook — with scenarios for executive, sales, marketing and technical roles. Day 3 makes it safe, then you build a workflow for your own job. Hands-on from start to finish, on sample data.</p>
    <div class="dcards">{''.join(cards)}</div>

    <div class="res-bar">
      <div class="rb-left">
        <span class="rb-pill">Toolkit · For Participants</span>
        <h3>Resources</h3>
        <p>Setup guide, your Prompt Bank, the capstone, sample files, the cheat sheet, every deck and lab — and the official Microsoft references. One place, long after the room clears.</p>
      </div>
      <div class="rb-btns">
        <a class="rb-open ghost" href="before-you-start.html">Before you start</a>
        <a class="rb-open" href="resources.html">Open resources →</a>
      </div>
    </div>
  </div>
</section>

<footer class="site-foot">
  <div class="wrap">
    <div class="foot-top">
      <div class="foot-brand">
        <div class="fb-lock"><img class="coded-logo" alt="CODED" src="{LOGO}"></div>
        <p>{esc(TITLE)} — a practical, hands-on workshop by CODED for professionals in Kuwait and the Gulf.</p>
      </div>
      <div class="foot-col">
        <h4>Explore</h4>
        <a href="#programme">The programme</a>
        <a href="{fn_day(1)}">Day 1 · {esc(DAYS[1]['title'])}</a>
        <a href="{fn_day(2)}">Day 2 · {esc(DAYS[2]['title'])}</a>
        <a href="{fn_day(3)}">Day 3 · {esc(DAYS[3]['title'])}</a>
        <a href="capstone.html">Capstone</a>
      </div>
      <div class="foot-col">
        <h4>Toolkit</h4>
        <a href="before-you-start.html">Before you start</a>
        <a href="prompt-bank.html">My Prompt Bank</a>
        <a href="cheat-sheet.html">Cheat sheet</a>
        <a href="resources.html">Resources</a>
        <span class="fc-static">enterprise@joincoded.com</span>
      </div>
    </div>
    <div class="foot-divider"></div>
    <div class="foot-bottom"><span>© 2026 CODED. Built with care.</span><span>Sample company in exercises: Tamra Foods Co. (fictional)</span></div>
  </div>
</footer>'''
    write('index.html', page(f'{TITLE} — CODED', body, css=LANDING_CSS,
                             desc='A hands-on three-day CODED workshop: Copilot in Word, Excel, PowerPoint and Outlook — safely.'))


# ================================================================= SUB-PAGES (top bar)
SUB_CSS = rd('css/sub.css')


def topbar(title_html, back='index.html', back_label='← Home'):
    return f'''<div class="top"><div class="top-in">
  <a class="backlink" href="{back}">{back_label}</a>
  <div class="brand"><span class="dot"></span>{title_html}</div>
</div></div>'''


def build_subpages():
    for name in ('before-you-start', 'prompt-bank', 'capstone', 'cheat-sheet', 'resources', 'sample-files',
                 'day-3-classify-redact', 'day-3-judgment-calls'):
        mod = os.path.join(ROOT, 'pages', name + '.py')
        if os.path.exists(mod):
            ns = {'page': page, 'topbar': topbar, 'esc': esc, 'ic': ic, 'SUB_CSS': SUB_CSS, 'rd': rd, 'TITLE': TITLE,
                  'fn_day': fn_day, 'fn_deck': fn_deck, 'fn_lab': fn_lab, 'DAYS': DAYS, 'M': M, 'res_row': res_row,
                  'footer_row': footer_row, 'ICON': ICON, 'ROOT': ROOT, 'OUT': OUT}
            exec(compile(open(mod, encoding='utf-8').read(), mod, 'exec'), ns)
            write(name + '.html', ns['build']())


def main():
    os.makedirs(OUT, exist_ok=True)
    print('Building →', OUT)
    for f in ('site-config.js', 'qrcode.min.js'):
        dst = os.path.join(OUT, f)
        if f == 'site-config.js' and os.path.exists(dst) and '--reset-config' not in sys.argv:
            print(f'  {f:44s} (kept — edit it in site/)')
            continue
        shutil.copy(os.path.join(ROOT, 'static', f), dst)
        print(f'  {f:44s} copied')
    build_landing()
    for n in (1, 2, 3):
        build_day(n)
        build_deck(n)
        build_lab(n)
    build_subpages()
    print('done.')


if __name__ == '__main__':
    main()
