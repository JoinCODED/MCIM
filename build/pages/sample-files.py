# Sample files — every Tamra Foods file, by day and role
import os

FILES = [
 ('Day 1', [
  ('tamra-company-profile.docx', 'Company profile', 'Who Tamra is, what it sells, its three business units. Upload it to Copilot Chat.', 'E1.4 · everyone'),
  ('tamra-annual-report-2025.docx', 'Annual report 2025', 'A 3-page report to condense into a one-page brief — and check.', 'E1.5 · everyone'),
 ]),
 ('Day 2 · Word (E2.1) — grounding files', [
  ('tamra-house-style-letter.docx', 'House-style letter', 'Tamra\'s voice: warm, clear, short sentences.', 'Sales'),
  ('tamra-supplier-notice.docx', 'Internal notice', 'New order cut-off times and payment terms from 1 Nov. Good for the summarise move.', 'Everyone · stretch'),
  ('tamra-h1-2026-business-review.docx', 'H1 2026 business review', 'The board report — its style and unit names.', 'Executive'),
  ('tamra-campaign-brief-cold-brew.docx', 'Cold-brew campaign brief', 'The brand rules: bilingual, no health claims.', 'Marketing'),
  ('tamra-pos-upgrade-project-plan.docx', 'POS upgrade project plan', 'The support plan and help-desk promise.', 'Technical'),
 ]),
 ('Day 2 · PowerPoint (E2.2, E2.3) — source documents', [
  ('tamra-h1-2026-business-review.docx', 'H1 2026 business review', '→ a 6-slide board deck.', 'Executive'),
  ('tamra-account-brief-darwaza-hotels.docx', 'Account brief: Darwaza Hotels', '→ a client-facing pitch deck. Parts are internal-only.', 'Sales'),
  ('tamra-campaign-brief-cold-brew.docx', 'Cold-brew campaign brief', '→ a 6-slide launch plan.', 'Marketing'),
  ('tamra-pos-upgrade-project-plan.docx', 'POS upgrade project plan', '→ a steering-committee deck.', 'Technical'),
  ('tamra-messy-deck.pptx', 'The messy deck', 'Out of order, a duplicate, a junk slide. Fix it.', 'Everyone · stretch'),
 ]),
 ('Day 2 · Excel (E2.4) — workbooks', [
  ('tamra-monthly-kpis.xlsx', 'Monthly KPIs', 'Three business units, Jan–Aug 2026.', 'Executive'),
  ('tamra-sales-pipeline.xlsx', 'Sales pipeline', '120 B2B deals, Jan–Sep 2026.', 'Sales'),
  ('tamra-campaign-results.xlsx', 'Campaign results', '13 weeks of campaigns by channel.', 'Marketing'),
  ('tamra-it-tickets.xlsx', 'IT tickets', '320 help-desk tickets, Jul–Sep 2026.', 'Technical'),
 ]),
 ('Day 2 · Teams (E2.6)', [
  ('tamra-leadership-meeting-transcript.docx', 'Leadership meeting transcript', 'A Teams transcript to recap into decisions, actions and owners.', 'Everyone'),
 ]),
 ('Day 3 · Agent Builder (E3.2) — Tamra HR Helper knowledge files', [
  ('tamra-employee-handbook.docx', 'Employee Handbook (2024)', 'Working hours, probation, benefits, discipline. Older than the leave policy.', 'Everyone'),
  ('tamra-leave-policy-2026.docx', 'Leave Policy 2026', 'Annual, sick and other leave. Replaces the handbook\'s leave section.', 'Everyone'),
  ('tamra-hybrid-work-policy.docx', 'Hybrid and Remote Work Policy', 'Who can work from home, and how.', 'Everyone'),
  ('tamra-expenses-travel-policy.docx', 'Expenses and Business Travel Policy', 'Claims, limits, approvals, travel allowances.', 'Everyone'),
 ]),
 ('Day 3 · Capstone inputs', [
  ('tamra-leadership-meeting-transcript.docx', 'Leadership meeting transcript', 'Step 1 input: recap it.', 'Executive'),
  ('tamra-leadership-meeting-notes.docx', 'Leadership meeting notes', 'Typed notes to cross-check against the transcript.', 'Executive'),
  ('tamra-lead-brief-mersal-tech-park.docx', 'Lead brief: Mersal Tech Park', 'A lost deal is back → pitch deck + follow-up.', 'Sales'),
  ('tamra-campaign-results.xlsx', 'Campaign results', 'Evidence for the launch plan.', 'Marketing'),
  ('tamra-it-tickets.xlsx', 'IT tickets', 'Raw data → analysis + stakeholder report.', 'Technical'),
 ]),
]


def build():
    icon = {'.docx': 'doc', '.xlsx': 'sheet', '.pptx': 'screen'}
    parts = []
    for sec, rows in FILES:
        lis = []
        for fn, name, desc, tag in rows:
            ext = os.path.splitext(fn)[1]
            size = os.path.getsize(os.path.join(OUT, fn)) if os.path.exists(os.path.join(OUT, fn)) else 0
            kb = f' · {max(1, round(size / 1024))} KB' if size else ''
            lis.append(f'<a class="res" href="{esc(fn)}" download><span class="res-ic">{ic(icon.get(ext, "doc"), 18)}</span><div class="res-body"><div class="res-nm">{esc(name)}</div>'
                       f'<div class="res-d">{esc(desc)} <span style="color:var(--ink-faint);font-family:var(--mono);font-size:11px">{esc(fn)}{kb}</span></div></div><span class="res-tag">{esc(tag)}</span></a>')
        parts.append(f'<div class="sec-label">{esc(sec)}</div><div class="res-list">{"".join(lis)}</div>')
    body = topbar('Sample <b>Files</b>', back='resources.html', back_label='← Resources') + f'''
<div class="wrap narrow">
  <span class="eyebrow">Tamra Foods Co. · Fictional</span>
  <h1>All sample files.</h1>
  <p class="intro">Every exercise uses <b>Tamra Foods Co.</b> — a fictional Kuwaiti food company with cafés, a wholesale arm and a delivery app. All names and numbers are invented, so you can practise freely. Tap a file to download it.</p>
  <p class="note"><b>Tip:</b> save a file to your <b>OneDrive</b> before you use it with Copilot in Word, Excel or PowerPoint. Some features — like building a deck from a file, or typing <code>/</code> to find it — look for it there.</p>
  {''.join(parts)}
</div>
''' + footer_row()
    return page('Sample Files — ' + TITLE + ' · CODED', body, css=SUB_CSS, desc='Download the fictional Tamra Foods sample files used in the workshop labs.')
