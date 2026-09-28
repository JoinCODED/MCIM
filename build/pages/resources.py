# Resources — everything in one place
def row(href, name, desc, tag, icon, link=None, dl=False):
    if link:
        return (f'<a class="res" data-link="{link}"><span class="res-ic">{ic(icon, 18)}</span><div class="res-body"><div class="res-nm">{esc(name)}</div>'
                f'<div class="res-d" data-pending="Link coming soon — shared in the room.">{esc(desc)}</div></div><span class="res-tag">{esc(tag)}</span></a>')
    ext = href.startswith('http')
    attrs = ' target="_blank" rel="noopener"' if ext else (' download' if dl else '')
    return (f'<a class="res" href="{esc(href)}"{attrs}><span class="res-ic">{ic(icon, 18)}</span><div class="res-body"><div class="res-nm">{esc(name)}</div>'
            f'<div class="res-d">{esc(desc)}</div></div><span class="res-tag">{esc(tag)}</span></a>')


def build():
    start = ''.join([
        row('before-you-start.html', 'Before you start', 'Sign in, check which Copilot you have, and fallbacks when a feature is missing.', 'Setup', 'setup'),
        row('prompt-bank.html', 'My Prompt Bank', 'Every prompt you saved in the labs. Export it before you leave.', 'Yours', 'bank'),
        row('cheat-sheet.html', 'Copilot cheat sheet', 'The moves that matter from all three days, on one page.', 'Reference', 'sheet'),
        row('capstone.html', 'Capstone', 'Four tracks, starter scenarios, sample inputs, the planner and the self-check.', 'Day 3', 'cap'),
        row('sample-files.html', 'All sample files', 'Every Tamra Foods file used in the labs, by day and role.', 'Files', 'doc'),
    ])
    d1 = ''.join([
        row('', 'MAP test — pre-workshop', '30 minutes at 9:00 AM. A map, not an exam.', 'Form', 'map', link='mapPre'),
        row(fn_day(1), 'Day 1 overview', 'Brief, run of show, outcomes and links.', 'Page', 'all'),
        row(fn_deck(1), 'Day 1 slides', 'The full interactive deck.', 'Deck', 'screen'),
        row(fn_lab(1), 'Day 1 lab', 'Eight hands-on tasks in Copilot Chat.', 'Lab', 'flag'),
    ])
    d2 = ''.join([
        row(fn_day(2), 'Day 2 overview', 'Brief, run of show, outcomes and links.', 'Page', 'all'),
        row(fn_deck(2), 'Day 2 slides', 'Word, PowerPoint, Excel, Outlook + Teams.', 'Deck', 'screen'),
        row(fn_lab(2), 'Day 2 lab', 'One task per app, four role scenarios each — plus a Teams recap.', 'Lab', 'flag'),
    ])
    d3 = ''.join([
        row(fn_day(3), 'Day 3 overview', 'Brief, run of show, outcomes and links.', 'Page', 'all'),
        row(fn_deck(3), 'Day 3 slides', 'Responsible AI, the Prompt Gallery and the capstone.', 'Deck', 'screen'),
        row(fn_lab(3), 'Day 3 lab', 'Classify + Redact, Judgment Calls, Gallery hunt, capstone.', 'Lab', 'flag'),
        row('day-3-classify-redact.html', 'Classify + Redact', 'Six items, four tiers — the E3.1 exercise.', 'Exercise', 'shield'),
        row('day-3-judgment-calls.html', 'Judgment calls', 'Six grey-zone requests — the E3.2 exercise.', 'Exercise', 'shield'),
        row('', 'MAP test — post-workshop', '11:10 AM. The same map as Tuesday.', 'Form', 'map', link='mapPost'),
        row('', 'Satisfaction survey', '2:00 PM, while certificates are handed out.', 'Form', 'survey', link='survey'),
    ])
    ms = ''.join([
        row('https://copilot.cloud.microsoft/', 'Microsoft Copilot', 'The Copilot app for work accounts (also m365copilot.com).', 'Microsoft', 'spark'),
        row('https://support.microsoft.com/en-us/microsoft-365-copilot/', 'Microsoft Copilot — help & learning', 'Official how-tos for Copilot in Word, Excel, PowerPoint, Outlook and Teams.', 'Microsoft', 'all'),
        row('https://support.microsoft.com/en-us/topic/learn-about-copilot-prompts-f6c3b467-f07c-4db1-ae54-ffac96184dd5', 'Learn about Copilot prompts', 'Microsoft\'s prompt guide: Goal · Context · Source · Expectations.', 'Microsoft', 'doc'),
        row('https://adoption.microsoft.com/en-us/copilot/prompt-gallery/', 'Copilot Prompt Gallery', 'Ready-made prompts to adapt and save, by role, app and task.', 'Microsoft', 'spark'),
        row('https://www.microsoft.com/en-us/ai/principles-and-approach', 'Microsoft Responsible AI principles', 'The six principles behind Copilot.', 'Microsoft', 'shield'),
    ])
    body = topbar('Workshop <b>Resources</b>') + f'''
<div class="wrap narrow">
  <span class="eyebrow">Everything In One Place</span>
  <h1>Workshop resources.</h1>
  <p class="intro">Setup, your Prompt Bank, every deck and lab, the sample files and the official Microsoft references — for the room, and for long after it clears.</p>
  <div class="sec-label">Start here</div><div class="res-list">{start}</div>
  <div class="sec-label">Day 1 · <span data-cfg="dates.d1Short">Tue 29 Sep</span> · Foundations</div><div class="res-list">{d1}</div>
  <div class="sec-label">Day 2 · <span data-cfg="dates.d2Short">Wed 30 Sep</span> · Copilot across the apps</div><div class="res-list">{d2}</div>
  <div class="sec-label">Day 3 · <span data-cfg="dates.d3Short">Thu 1 Oct</span> · Responsible AI + capstone</div><div class="res-list">{d3}</div>
  <div class="sec-label">Microsoft references</div><div class="res-list">{ms}</div>
  <p class="note"><b>Heads-up:</b> in September 2026 Microsoft renamed “Microsoft 365 Copilot” to <b>Microsoft Copilot</b>, and the chat address moved to copilot.cloud.microsoft. Older guides and screens may still use the old names.</p>
</div>
''' + footer_row()
    return page('Resources — ' + TITLE + ' · CODED', body, css=SUB_CSS, desc='All workshop resources: setup, Prompt Bank, decks, labs, sample files and Microsoft references.')
