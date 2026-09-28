# Capstone — "Create a workflow": four role tracks, planner, self-check (participant-facing)
CSS = SUB_CSS + '''
  .hero-c{border:1px solid var(--line);border-radius:22px;padding:34px 32px;margin-bottom:10px;
    background:linear-gradient(150deg,rgba(47,116,214,.14),rgba(0,74,163,.05)),var(--card)}
  .hero-c h1{margin-bottom:10px}
  .how{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:22px}
  @media(max-width:760px){.how{grid-template-columns:repeat(2,1fr)}}
  .how div{border:1px solid var(--line-2);border-radius:14px;padding:14px;background:var(--card);font-size:13.5px;color:var(--ink-dim);line-height:1.45}
  .how b{display:block;font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--rose-lt);margin-bottom:6px}
  .audit{border:1px dashed var(--w2);border-radius:14px;padding:16px 18px;margin-top:14px;font-size:14px;color:var(--ink-dim);line-height:1.6}
  .audit ol{margin:8px 0 0 20px}.audit li{color:var(--ink)}
  .tabs2{display:flex;flex-wrap:wrap;gap:8px;margin:6px 0 18px}
  .tab2{padding:9px 15px;border-radius:999px;font-size:13px;font-weight:700;cursor:pointer;border:1px solid var(--w1);background:var(--w06);color:var(--ink-dim);font-family:var(--f)}
  .tab2.on{border-color:rgba(47,116,214,.55);color:#fff;background:rgba(47,116,214,.22)}
  .track h2{font-size:24px;font-weight:800;letter-spacing:-.3px;margin-bottom:6px}
  .surf{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0 14px}
  .surf span{font-family:var(--mono);font-size:11px;font-weight:700;padding:5px 10px;border-radius:7px;background:rgba(47,116,214,.12);border:1px solid rgba(47,116,214,.3);color:var(--rose-lt)}
  .starter{font-size:15px;color:var(--ink);line-height:1.6;margin-bottom:14px}
  .dls{display:flex;flex-wrap:wrap;gap:10px;margin:6px 0 18px}
  .dl{display:inline-flex;align-items:center;gap:10px;padding:10px 14px;border-radius:10px;border:1px solid var(--green-bd);background:var(--green-bg);color:var(--ink);font-weight:700;font-size:13px}
  .dl small{display:block;font-weight:500;font-size:11.5px;color:var(--ink-dim)}
  .chain{display:flex;flex-direction:column;gap:12px}
  .cstep{background:linear-gradient(180deg,var(--surf2),var(--surf));border:1px solid var(--w1);border-left:3px solid var(--crimson);border-radius:14px;padding:16px 18px}
  .cstep-h{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:8px}
  .cstep-n{font-family:var(--mono);font-size:11px;font-weight:700;color:#fff;background:var(--crimson);border-radius:6px;padding:3px 8px}
  .cstep-s{font-family:var(--mono);font-size:10.5px;letter-spacing:.1em;text-transform:uppercase;color:var(--rose-lt)}
  .cstep-t{font-size:15px;font-weight:800;color:var(--ink);width:100%}
  .cstep p{font-size:13.5px;color:var(--ink-dim);line-height:1.55;margin:4px 0 8px}
  .prompt{font-family:var(--mono);font-size:12.5px;line-height:1.6;color:var(--ink);background:rgba(0,0,0,.28);border:1px solid var(--w1);border-radius:9px;padding:28px 14px 12px;position:relative;cursor:pointer;white-space:pre-wrap}
  .prompt:hover{border-color:rgba(47,116,214,.4)}
  .prompt .ct{position:absolute;top:8px;right:10px;font-size:10px;color:var(--ink-faint);font-family:var(--mono)}
  .prompt.copied{border-color:var(--green-bd)}
  .pbs{margin-top:6px;font-size:12px;font-weight:700;color:var(--ink-dim);background:none;border:1px dashed var(--w2);border-radius:8px;padding:5px 10px;cursor:pointer;font-family:var(--f)}
  .pbs:hover{color:var(--rose-lt)}
  .chk{margin-top:8px;font-size:13px;color:var(--amber);line-height:1.5}
  .yours{margin-top:14px;border:1px solid rgba(240,165,68,.3);background:rgba(240,165,68,.06);border-radius:12px;padding:12px 16px;font-size:14px;color:var(--ink);line-height:1.55}
  .yours b{color:var(--amber)}
  .planner{display:grid;gap:12px}
  .planner label{display:block;font-size:12.5px;font-weight:700;color:var(--ink-dim);margin-bottom:6px}
  .row3{display:grid;grid-template-columns:170px 1fr;gap:8px;align-items:center}
  @media(max-width:620px){.row3{grid-template-columns:1fr}}
  .surfs{display:flex;flex-wrap:wrap;gap:8px}
  .surfs label{display:inline-flex;align-items:center;gap:7px;padding:8px 12px;border:1px solid var(--w1);border-radius:9px;background:var(--base);font-size:13px;color:var(--ink);font-weight:600;margin:0;cursor:pointer}
  .surfs input{accent-color:var(--crimson)}
  .bar2{display:flex;flex-wrap:wrap;gap:10px;align-items:center}
  .rub{display:flex;flex-direction:column;gap:10px}
  .rub label{display:flex;gap:14px;align-items:flex-start;padding:15px 18px;border:1px solid var(--line);border-radius:14px;background:var(--card);cursor:pointer}
  .rub label.on{border-color:var(--green-bd);background:var(--green-bg)}
  .rub input{margin-top:3px;width:18px;height:18px;accent-color:var(--green)}
  .rub b{display:block;font-size:15px}.rub small{display:block;font-size:13px;color:var(--ink-dim);margin-top:2px}
  .times{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:12px}
  .anchor{scroll-margin-top:80px}
'''

TRACKS = {
 'executive': {
  'title': 'Teams recap → a decision-ready briefing',
  'surfaces': ['Teams or Copilot Chat', 'Word', 'PowerPoint (optional)', 'Outlook'],
  'starter': 'Sunday\'s leadership meeting ran almost two hours. You have the Teams transcript and the typed notes — and they don\'t fully agree. The CEO wants a one-page decision briefing today, the team needs to know who does what, and the board may want a short deck.',
  'files': [('tamra-leadership-meeting-transcript.docx', 'The Teams transcript (input)'), ('tamra-leadership-meeting-notes.docx', 'The typed notes (to cross-check)'), ('tamra-h1-2026-business-review.docx', 'For grounding (optional)')],
  'steps': [
   ('Teams or Copilot Chat', 'Recap and cross-check', 'Upload the transcript and the notes with + → Upload. (At work: open the meeting in Teams → Recap.)',
    'Recap the attached meeting transcript: the decisions, the open questions, and the action items with owner and due date. Then compare it with the attached notes and list every number or fact that doesn\'t match. For each point, say which document it comes from.',
    'Check: the notes say the POS budget is 102k; the transcript says 120,000 — twice. Trust the transcript (the H1 review agrees). Turn vague dates like “next week” into real dates.'),
   ('Word', 'Brief', 'Open a new Word document and use Copilot. Paste your checked recap from step 1.',
    'Draft a one-page decision briefing for our CEO from this recap: the context, the decisions needed with the options for each, my recommendation, and the risks. Under 350 words. Use the business-unit names from /tamra-h1-2026-business-review. [paste step 1]',
    'Check: every number matches the transcript; the cold-brew budget disagreement (12k vs 18k) is shown fairly.'),
   ('PowerPoint (optional)', 'Deck for the board', 'Save the briefing to your OneDrive. In PowerPoint: Copilot → Create a presentation from a file.',
    'Create a 5-slide board summary from /my decision briefing: the situation, the decisions needed with options, my recommendation, the risks, and next steps. Add speaker notes.',
    'Check: the numbers on the slides match the briefing. This makes your chain Teams → Word → PowerPoint → Outlook.'),
   ('Outlook', 'Send', 'New email in Outlook → Copilot → Draft. Attach the briefing (and the deck).',
    'Draft an email to the leadership team with the briefing attached. List each person\'s actions with due dates, and ask for corrections by Tuesday. Under 150 words. Clear and polite.',
    'Before you send: run Coaching by Copilot. Is every owner and date right?'),
  ],
  'yours': 'Use the transcript or notes from one of your own recent meetings — nothing confidential — or your weekly management report.',
 },
 'sales': {
  'title': 'Lead brief → a tailored pitch deck + follow-up email',
  'surfaces': ['Copilot Chat', 'PowerPoint', 'Outlook'],
  'starter': 'Mersal Tech Park chose another supplier in June — on price. Yesterday their new Facilities Manager called: the other supplier is often late, and staff complain. You have one meeting to win them back.',
  'files': [('tamra-lead-brief-mersal-tech-park.docx', 'The lead brief (input)'), ('tamra-sales-pipeline.xlsx', 'Deal D-1047 — the June loss (optional)')],
  'steps': [
   ('Copilot Chat', 'Find the angle', 'Upload the lead brief with + → Upload.',
    'Using the attached lead brief: what are the client\'s top three needs, the two objections they will raise, and the best angle for our pitch? We lost this deal on price in June. A short list for each.',
    'Check: is the angle about reliability and total value — not a bigger discount?'),
   ('PowerPoint', 'Build the deck', 'Save the brief to your OneDrive. In PowerPoint: Copilot → Create a presentation from a file.',
    'Create a 6-slide pitch for Mersal Tech Park from /tamra-lead-brief-mersal-tech-park: what we heard, weekly pantry supply, the monthly breakfast package, why reliability beats a cheaper price, the November trial, and next steps. It goes to the client — leave out internal notes. Add speaker notes.',
    'Check: did anything from “Watch-outs” (the 5% discount limit, why we lost) land on a client slide? Delete it.'),
   ('Outlook', 'Follow up', 'After the meeting: new email → Copilot → Draft. Attach the deck.',
    'Draft a follow-up email to Eng. Bader Al-Mutairi after our meeting: thank him, confirm the November trial, attach the deck, and propose a tasting for the tenants\' committee. Under 120 words. Warm and confident. No discounts.',
    'Before you send: Coaching by Copilot. Did you promise anything the brief doesn\'t allow?'),
  ],
  'yours': 'Use a real lead or an account you want to grow. Describe it in your own words — no client names or contract details.',
 },
 'marketing': {
  'title': 'Campaign brief → content variants + a results summary',
  'surfaces': ['Excel', 'Word or PowerPoint'],
  'starter': 'The cold-brew launch is 17 days away. Management wants two things by Sunday: launch content that follows the brand rules, and proof from past campaigns about where the money should go.',
  'files': [('tamra-campaign-results.xlsx', 'Past campaign results (input)'), ('tamra-campaign-brief-cold-brew.docx', 'The launch brief (input)')],
  'steps': [
   ('Excel', 'Find the evidence', 'Open the results workbook and click inside the table.',
    'From this table, which channels gave the best return (Revenue ÷ Spend) and the lowest cost per order (Spend ÷ Orders)? Give me three insights for our next launch, each with a number.',
    'Check: Email has the best return (4.93); Back to Office on Google Ads lost money (0.81); TikTok had the cheapest orders on Summer Iced Coffee.'),
   ('Word', 'Write the content', 'New Word document → Copilot. Paste your three insights.',
    'Using /tamra-campaign-brief-cold-brew and these insights, write launch content: three posts each for Instagram, TikTok and Snapchat, in English and Arabic. Follow the brand rules. A table: channel, English, Arabic. [paste insights]',
    'Check: no “healthy”, “sugar-free” or “good for you”. Arabic that sounds natural.'),
   ('Word or PowerPoint', 'Summarise for management', 'Same document — or PowerPoint → Copilot → create from your Word file.',
    'Write a one-page summary for management: what past campaigns tell us, the launch content plan, how we split the KWD 18,000 budget across channels, and the KPIs. Under 300 words.',
    'Check: the budget split adds up to exactly KWD 18,000, and each channel choice has a number behind it.'),
  ],
  'yours': 'Use your own brand\'s past campaign totals (no customer data) and a launch you have coming up.',
 },
 'technical': {
  'title': 'Raw data → an analysis summary + a stakeholder report',
  'surfaces': ['Excel', 'Copilot Chat', 'Word'],
  'starter': 'The Head of IT has a budget meeting next week. She needs to know where the pain is, what\'s causing it, and what to fix first — in a report non-technical managers can read.',
  'files': [('tamra-it-tickets.xlsx', 'Three months of IT tickets (input)'), ('tamra-pos-upgrade-project-plan.docx', 'The POS upgrade plan (optional)')],
  'steps': [
   ('Excel', 'Analyse', 'Open the tickets workbook and click inside the table.',
    'Analyse these tickets: the biggest spikes by site, category and month; the average hours to resolve and the reopen rate by category; and the day-of-week pattern for P1 tickets. Add one chart.',
    'Check: Fahaheel POS tickets jumped in August (13); Wi-Fi is slowest (18.8 hours); Printer is reopened most (31%); P1 app tickets cluster on Thursdays.'),
   ('Copilot Chat', 'Reason', 'Paste your checked findings into Copilot Chat.',
    'Here are my findings from our IT tickets. For each one: the likely cause, what the data proves and what it only suggests, and one recommended action with an owner. [paste findings]',
    'Check: “after firmware 4.2” in the notes suggests a cause — it doesn\'t prove it. Say so.'),
   ('Word', 'Report', 'New Word document → Copilot. Paste the output from step 2.',
    'Write a two-page stakeholder report: a five-line summary for managers, the findings with numbers, recommendations, and next steps. Plain English. Put the technical detail in an appendix.',
    'Check: could a non-technical manager act on the first five lines alone?'),
  ],
  'yours': 'Use an export from your own ticket or operations system. Remove names and personal data first.',
 },
}

JS = r'''
(function(){
  var TR = window.TRACKS, K = 'coded_copilot_capstone';
  var st = store.get(K, {}); if (!st || typeof st !== 'object') st = {};
  function save(){ store.set(K, st); }
  function esc(s){ return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
  function attr(s){ return esc(s).replace(/"/g,'&quot;'); }
  var cur = st.track || ROLE.get() || 'executive';

  // Day 1 time audit
  var p = PROFILE.get(), tasks = (p.tasks || []).filter(function(t){ return t.text; });
  document.getElementById('audit').innerHTML = tasks.length
    ? '<b>Your Day 1 time audit</b> — the biggest one is a strong capstone candidate:<ol>' + tasks.map(function(t){ return '<li>' + esc(t.text) + (t.tag ? ' · <i>' + esc(t.tag) + '</i>' : '') + (t.hours ? ' · ' + esc(t.hours) + ' h/wk' : '') + '</li>'; }).join('') + '</ol>'
    : '<b>Your Day 1 time audit</b> isn\'t in this browser. Open <a href="coded-copilot-day-1-lab.html#E1.2" style="color:var(--rose-lt);text-decoration:underline">E1.2 in the Day 1 lab</a> — or pick a real, repeating task now.';

  function drawTrack(){
    var t = TR[cur];
    document.querySelectorAll('.tab2').forEach(function(b){ b.classList.toggle('on', b.getAttribute('data-t') === cur); });
    document.getElementById('track').innerHTML =
      '<h2>' + esc(t.title) + '</h2><div class="surf">' + t.surfaces.map(function(s){ return '<span>' + esc(s) + '</span>'; }).join('') + '</div>' +
      '<p class="starter"><b>Starter scenario.</b> ' + esc(t.starter) + '</p>' +
      '<div class="dls">' + t.files.map(function(f){ return '<a class="dl" href="' + attr(f[0]) + '" download>⬇ <span>' + esc(f[0]) + '<small>' + esc(f[1]) + '</small></span></a>'; }).join('') + '</div>' +
      '<div class="chain">' + t.steps.map(function(s, i){
        return '<div class="cstep"><div class="cstep-h"><span class="cstep-n">Step ' + (i + 1) + '</span><span class="cstep-s">' + esc(s[0]) + '</span><span class="cstep-t">' + esc(s[1]) + '</span></div>' +
          '<p>' + esc(s[2]) + '</p><div class="prompt" data-copy="' + attr(s[3]) + '"><span class="ct">tap to copy</span>' + esc(s[3]) + '</div>' +
          '<button class="pbs" data-save="' + attr(s[3]) + '" data-title="Capstone · ' + attr(s[0] + ' · ' + s[1]) + '" data-app="' + attr(s[0]) + '">＋ Save to Prompt Bank</button>' +
          '<div class="chk">✔ ' + esc(s[4]) + '</div></div>';
      }).join('') + '</div>' +
      '<div class="yours"><b>Make it yours:</b> ' + esc(t.yours) + ' Keep the same chain — change the input.</div>';
    document.querySelectorAll('#track .prompt').forEach(function(el){ el.onclick = function(){ copyText(el.getAttribute('data-copy')).then(function(){ el.classList.add('copied'); el.querySelector('.ct').textContent = 'copied ✓'; setTimeout(function(){ el.classList.remove('copied'); el.querySelector('.ct').textContent = 'tap to copy'; }, 1400); }); }; });
    document.querySelectorAll('#track .pbs').forEach(function(b){ b.onclick = function(){ var r = pbAdd(b.getAttribute('data-save'), { title: b.getAttribute('data-title'), app: b.getAttribute('data-app'), day: 'Day 3', role: cur }); if (r === 'ok' || r === 'dup') b.textContent = '✓ In your Prompt Bank'; }; });
  }
  document.querySelectorAll('.tab2').forEach(function(b){ b.onclick = function(){ cur = b.getAttribute('data-t'); st.track = cur; save(); var sel = document.getElementById('pTrack'); if (sel) sel.value = cur; drawTrack(); }; });
  drawTrack();

  // planner
  var P = st.plan || {};
  function f(id){ return document.getElementById(id); }
  ['pTask','pS1','pS2','pS3','pS1s','pS2s','pS3s','pPrompt'].forEach(function(id){ if (P[id]) f(id).value = P[id]; });
  f('pTrack').value = st.track || cur;
  (P.surfs || []).forEach(function(v){ var c = document.querySelector('.surfs input[value="' + v + '"]'); if (c) c.checked = true; });
  function sync(){
    ['pTask','pS1','pS2','pS3','pS1s','pS2s','pS3s','pPrompt'].forEach(function(id){ P[id] = f(id).value; });
    P.surfs = [].slice.call(document.querySelectorAll('.surfs input:checked')).map(function(c){ return c.value; });
    st.plan = P; st.track = f('pTrack').value; save();
    f('surfN').textContent = P.surfs.length + ' surface' + (P.surfs.length === 1 ? '' : 's') + ' ticked' + (P.surfs.length < 2 ? ' — the capstone needs two or more' : ' ✓');
  }
  document.querySelectorAll('.planner input, .planner textarea, .planner select').forEach(function(el){ el.addEventListener('input', sync); el.addEventListener('change', sync); });
  f('pTrack').addEventListener('change', function(){ cur = f('pTrack').value; drawTrack(); });
  sync();
  function planText(){
    return 'MY COPILOT WORKFLOW — capstone plan\n\nTask: ' + (P.pTask || '') + '\nTrack: ' + (window.ROLES[st.track] || st.track || '') + '\nSurfaces: ' + (P.surfs || []).join(', ') +
      '\n\nStep 1 (' + (P.pS1s || '') + '): ' + (P.pS1 || '') + '\nStep 2 (' + (P.pS2s || '') + '): ' + (P.pS2 || '') + '\nStep 3 (' + (P.pS3s || '') + '): ' + (P.pS3 || '') +
      '\n\nFirst prompt:\n' + (P.pPrompt || '') + '\n\nTime by hand: ' + (st.tHand || '?') + ' · With Copilot: ' + (st.tAi || '?') + '\n';
  }
  f('pCopy').onclick = function(){ copyText(planText()).then(function(){ toast('Plan copied ✓'); }); };
  f('pDl').onclick = function(){ var blob = new Blob([planText()], { type: 'text/plain' }); var a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'my-copilot-workflow.txt'; document.body.appendChild(a); a.click(); a.remove(); };
  f('pSave').onclick = function(){ pbAdd(f('pPrompt').value, { title: 'Capstone · first prompt', app: P.pS1s || 'Copilot', day: 'Day 3', role: st.track }); };

  // rubric + times
  var R = st.rubric || {};
  document.querySelectorAll('.rub input').forEach(function(c){ c.checked = !!R[c.value]; c.closest('label').classList.toggle('on', c.checked);
    c.onchange = function(){ R[c.value] = c.checked; st.rubric = R; save(); c.closest('label').classList.toggle('on', c.checked); var n = Object.keys(R).filter(function(k){ return R[k]; }).length; if (n === 3) toast('All three checks — nice work ✓'); }; });
  ['tHand','tAi'].forEach(function(id){ f(id).value = st[id] || ''; f(id).oninput = function(){ st[id] = f(id).value; save(); }; });
})();
'''


def build():
    import json as _json
    tabs = ''.join(f'<button class="tab2" data-t="{k}">{v}</button>' for k, v in M['roles'].items())
    track_opts = ''.join(f'<option value="{k}">{v}</option>' for k, v in M['roles'].items())
    surf_opts = ''.join(f'<option>{s}</option>' for s in ['Copilot Chat', 'Word', 'PowerPoint', 'Excel', 'Outlook', 'Teams'])
    surfs = ''.join(f'<label><input type="checkbox" value="{s}"> {s}</label>' for s in ['Copilot Chat', 'Word', 'PowerPoint', 'Excel', 'Outlook', 'Teams'])
    tabs_nav = '<nav class="tabs"><a href="#tracks">Tracks</a><a href="#plan">Plan</a><a href="#build">Build + check</a></nav>'
    body = topbar('Capstone · <b>Your Workflow</b>').replace('</div></div>', tabs_nav + '</div></div>', 1) + f'''
<div class="wrap narrow">
  <div class="hero-c">
    <span class="eyebrow">Day 3 · Capstone</span>
    <h1>Create a workflow.</h1>
    <p class="intro">Chain <b>two or more</b> Copilot surfaces to solve <b>one real, repeating task</b> from your job. Pick a track, adapt the starter scenario, and build it. No submission, no showcase — it goes home with you.</p>
    <div class="how">
      <div><b>1 · Track</b>Pick the track closest to your job.</div>
      <div><b>2 · Task</b>Your real task — or the starter.</div>
      <div><b>3 · Chain</b>Each step's output feeds the next.</div>
      <div><b>4 · Check</b>Three boxes. No grade.</div>
    </div>
    <div class="audit" id="audit"></div>
  </div>

  <div class="sec-label anchor" id="tracks">The four tracks</div>
  <div class="tabs2">{tabs}</div>
  <div class="track" id="track"></div>

  <div class="sec-label anchor" id="plan">Plan your workflow · E3.4</div>
  <div class="card planner">
    <div><label for="pTask">My real task (repeating, from my job)</label><input class="in" id="pTask" placeholder="e.g. Every Sunday I turn the weekly sales export into a summary email for my manager"></div>
    <div><label for="pTrack">Closest track</label><select class="in" id="pTrack">{track_opts}</select></div>
    <div><label>Copilot surfaces in my chain</label><div class="surfs">{surfs}</div><div class="count" id="surfN" style="font-family:var(--mono);font-size:12px;color:var(--ink-faint);margin-top:6px"></div></div>
    <div><label>The chain — which surface does what</label>
      <div class="row3"><select class="in" id="pS1s">{surf_opts}</select><input class="in" id="pS1" placeholder="Step 1 — e.g. extract the key numbers from the export"></div>
      <div class="row3" style="margin-top:8px"><select class="in" id="pS2s">{surf_opts}</select><input class="in" id="pS2" placeholder="Step 2 — e.g. draft the summary in Word"></div>
      <div class="row3" style="margin-top:8px"><select class="in" id="pS3s">{surf_opts}</select><input class="in" id="pS3" placeholder="Step 3 (optional) — e.g. email it from Outlook"></div>
    </div>
    <div><label for="pPrompt">My first prompt (CTFT)</label><textarea class="in" id="pPrompt" rows="4" placeholder="Context · Task · Format · Tone — and a Source if you have one"></textarea></div>
    <div class="bar2"><button class="btn" id="pSave">＋ Save prompt to Prompt Bank</button><button class="btn" id="pCopy">Copy my plan</button><button class="btn primary" id="pDl">Download my plan (.txt)</button></div>
  </div>

  <div class="sec-label anchor" id="build">Build + self-check · E3.5</div>
  <p class="p">Build the chain step by step. Check every output before it feeds the next step. Tick each box when it's true.</p>
  <div class="rub">
    <label><input type="checkbox" value="chain"><span><b>Chains 2 or more Copilot surfaces</b><small>The output of one step is the input of the next.</small></span></label>
    <label><input type="checkbox" value="ctft"><span><b>Uses CTFT — or Goal · Context · Source · Expectations</b><small>Every prompt has the ingredients it needs.</small></span></label>
    <label><input type="checkbox" value="real"><span><b>Solves a real, repeating task from your job</b><small>Something you will run again next week.</small></span></label>
  </div>
  <div class="card" style="margin-top:16px">
    <label style="display:block;font-size:12.5px;font-weight:700;color:var(--ink-dim)">How long does this task take?</label>
    <div class="times"><input class="in" id="tHand" placeholder="By hand — e.g. 3 hours"><input class="in" id="tAi" placeholder="With your chain — e.g. 40 minutes"></div>
  </div>
  <p class="note"><b>Take it home:</b> download your plan, and export your <a href="prompt-bank.html" style="color:var(--amber);text-decoration:underline">Prompt Bank</a>. On Sunday, run the chain on the real task.</p>
</div>
<script>window.TRACKS = {_json.dumps(TRACKS)};</script>
''' + footer_row()
    return page('Capstone — ' + TITLE + ' · CODED', body, css=CSS, js=JS, desc='The capstone: build a Copilot workflow that chains two or more surfaces for a real task.')
