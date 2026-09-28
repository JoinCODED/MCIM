# Before you start — setup, licence check, fallbacks (participant-facing)
CSS = SUB_CSS + '''
  .tiers{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:8px}
  @media(max-width:820px){.tiers{grid-template-columns:1fr}}
  .tiers .card h3{font-size:16.5px;font-weight:800;margin:6px 0 10px;line-height:1.3}
  .tiers .card.prem{border-color:rgba(200,50,74,.45);background:linear-gradient(180deg,rgba(200,50,74,.12),var(--surf))}
  .tiers ul{list-style:none;display:flex;flex-direction:column;gap:7px}
  .tiers li{font-size:13.5px;color:var(--ink-dim);line-height:1.45;padding-left:20px;position:relative}
  .tiers li::before{content:"✓";position:absolute;left:0;color:var(--green-lt);font-weight:800}
  .tiers li.no::before{content:"✕";color:var(--danger)}
  ol.stp{list-style:none;counter-reset:s;display:flex;flex-direction:column;gap:10px;margin-top:6px}
  ol.stp li{counter-increment:s;display:flex;gap:14px;padding:14px 16px;border:1px solid var(--line);border-radius:12px;background:var(--card);font-size:15px;color:var(--ink);line-height:1.5}
  ol.stp li::before{content:counter(s);flex:none;width:26px;height:26px;border-radius:8px;background:rgba(200,50,74,.16);color:var(--rose-lt);display:flex;align-items:center;justify-content:center;font-family:var(--mono);font-size:12px;font-weight:700}
  ol.stp li small{display:block;color:var(--ink-dim);font-size:13.5px;margin-top:3px}
  table.need{width:100%;border-collapse:collapse;font-size:14px;border:1px solid var(--line-2);border-radius:14px;overflow:hidden}
  table.need th,table.need td{padding:11px 14px;text-align:left;border-bottom:1px solid var(--line);vertical-align:top;line-height:1.45}
  table.need thead th{font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-dim);background:var(--surf2)}
  table.need td{color:var(--ink-dim)} table.need td:first-child{color:var(--ink);font-weight:700}
  .ok{color:var(--green-lt);font-weight:700}.maybe{color:var(--amber);font-weight:700}
  .fb{display:grid;grid-template-columns:1fr 1fr;gap:14px}
  @media(max-width:760px){.fb{grid-template-columns:1fr}}
  .fb .card h3{display:flex;align-items:center;gap:10px;font-size:16px;font-weight:800;margin-bottom:8px}
  .fb .card h3 img{width:24px;height:24px}
  .fb .card p{font-size:14px;color:var(--ink-dim);line-height:1.55}
  .tbl-wrap{overflow-x:auto}
  a.lk{color:var(--rose-lt);text-decoration:underline;text-underline-offset:3px}
'''


def build():
    body = topbar('Before you <b>start</b>') + f'''
<div class="wrap narrow">
  <span class="eyebrow">Setup · 5 minutes</span>
  <h1>Before you start.</h1>
  <p class="intro">Sign in, check which Copilot you have, and know what to do if a feature is missing. Do this once on Day 1 — it saves time in every lab.</p>

  <div class="sec-label">1 · Sign in</div>
  <ol class="stp">
    <li><span>Open <a class="lk" href="https://copilot.cloud.microsoft/" target="_blank" rel="noopener">copilot.cloud.microsoft</a><small>Or <code>m365copilot.com</code>. The old address, <code>m365.cloud.microsoft</code>, still works and forwards you.</small></span></li>
    <li><span>Sign in with your <b>work account</b> — the one you use for work email — or the <b>CODED account</b> on your card.<small>Never a personal account (Outlook.com, Hotmail) for work. Work accounts come with enterprise data protection.</small></span></li>
    <li><span>Find the label next to Copilot. It tells you which version you have — see below.<small>Microsoft renamed the product in September 2026. You may see “Microsoft Copilot” or “Microsoft 365 Copilot”. Same product.</small></span></li>
  </ol>

  <div class="sec-label">2 · Which Copilot do you have?</div>
  <div class="tiers">
    <div class="card"><span class="pill-tag">Included</span><h3>Copilot Chat (Basic)</h3><ul><li>Chat with web data</li><li>Upload files to a chat</li><li>Copilot in Outlook</li><li class="no">No Copilot inside Word, Excel or PowerPoint</li></ul></div>
    <div class="card"><span class="pill-tag">Included</span><h3>Microsoft 365 Copilot (Basic)</h3><ul><li>Everything in Copilot Chat</li><li>Copilot inside Word, Excel and PowerPoint</li><li class="no">Can be slower at busy times</li></ul></div>
    <div class="card prem"><span class="pill-tag red">Paid licence</span><h3>Microsoft 365 Copilot (Premium)</h3><ul><li>Uses your emails, files and meetings automatically</li><li>A <b>Work IQ</b> button (top left of the chat) to switch work data on or off</li><li>Researcher and Analyst agents, scheduled prompts</li></ul></div>
  </div>
  <p class="note"><b>Quick test:</b> see a <b>Work IQ</b> button in the chat? You have Premium. No button? You have a Basic version — every lab still works, using the fallbacks below.</p>

  <div class="sec-label">3 · What each day needs</div>
  <div class="tbl-wrap"><table class="need">
    <thead><tr><th>Exercise</th><th>Copilot Chat (Basic)</th><th>Microsoft 365 Copilot (Basic)</th><th>Premium</th></tr></thead>
    <tbody>
      <tr><td>Day 1 — all labs</td><td class="ok">Yes</td><td class="ok">Yes</td><td class="ok">Yes (+ the “your work” step)</td></tr>
      <tr><td>Day 2 — Word, PowerPoint, Excel</td><td class="maybe">Use the fallback</td><td class="ok">Yes</td><td class="ok">Yes</td></tr>
      <tr><td>Day 2 — Outlook</td><td class="ok">Yes</td><td class="ok">Yes</td><td class="ok">Yes</td></tr>
      <tr><td>Day 3 — Responsible AI, Prompt Gallery</td><td class="ok">Yes</td><td class="ok">Yes</td><td class="ok">Yes</td></tr>
      <tr><td>Day 3 — capstone</td><td class="maybe">Chat + fallbacks</td><td class="ok">Yes</td><td class="ok">Yes</td></tr>
    </tbody>
  </table></div>

  <div class="sec-label">4 · No Copilot in an app? Use the fallback</div>
  <p class="p">Some companies switch off Copilot inside Word, Excel and PowerPoint for staff without a licence. You can still do every exercise in <b>Copilot Chat</b>: upload the sample file with <b>+</b> → <b>Upload</b>, then use the same prompt.</p>
  <div class="fb">
    <div class="card"><h3><img src="{ICON['word']}" alt="">Word</h3><p>Ask Copilot Chat to draft or rewrite. Copy the answer into Word. To “ground” a draft, upload the sample file and say <i>“Match the tone of the attached letter.”</i></p></div>
    <div class="card"><h3><img src="{ICON['powerpoint']}" alt="">PowerPoint</h3><p>Upload the source document and ask for a slide-by-slide outline: title, three bullets and speaker notes per slide. Build the slides from the outline.</p></div>
    <div class="card"><h3><img src="{ICON['excel']}" alt="">Excel</h3><p>Upload the workbook to Copilot Chat and ask the same questions. Ask it to show the numbers behind each answer — then check them in Excel yourself.</p></div>
    <div class="card"><h3><img src="{ICON['outlook']}" alt="">Outlook</h3><p>Copilot works in Outlook for everyone. Empty inbox on a CODED account? Email the sample thread to yourself, then summarise it — or paste it into Copilot Chat.</p></div>
  </div>

  <div class="sec-label">5 · Using your own work account?</div>
  <ol class="stp">
    <li><span><b>Your company's rules come first.</b><small>If your IT team has switched a feature off — web search, image creation, agents — that is normal. Use the fallback.</small></span></li>
    <li><span><b>Use our sample files only.</b><small>Don't upload client files, company numbers or anything confidential during the workshop.</small></span></li>
    <li><span><b>Save sample files to your OneDrive</b> when an exercise says so.<small>Some features — like building a deck from a file — look for the file in your OneDrive.</small></span></li>
  </ol>

  <div class="sec-label">6 · How this site saves your work</div>
  <ol class="stp">
    <li><span>Your lab notes, your track and your <b>Prompt Bank</b> save <b>in this browser</b> — nowhere else.<small>Nobody else can see them. CODED can't see them either.</small></span></li>
    <li><span>Use the <b>same laptop and browser</b> for all three days.<small>A private or incognito window forgets everything when you close it.</small></span></li>
    <li><span>On a shared laptop? <b>Export</b> your Prompt Bank at the end of each day.<small>Open <a class="lk" href="prompt-bank.html">My Prompt Bank</a> → Export.</small></span></li>
  </ol>

  <div class="sec-label">Next</div>
  <div class="res-list">
    {res_row('sample-files.html', 'All sample files', 'doc')}
    {res_row(fn_lab(1), 'Day 1 lab', 'flag')}
    {res_row('prompt-bank.html', 'My Prompt Bank', 'bank')}
  </div>
</div>
''' + footer_row()
    return page('Before you start — ' + TITLE + ' · CODED', body, css=CSS, desc='Sign in, check which Copilot you have, and fallbacks when a feature is missing.')
