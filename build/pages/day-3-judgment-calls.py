# Day 3 · Exercise E3.4 — Judgment calls (would you let this through?). Written for a cross-industry room.
# State: localStorage key coded_copilot_judgment_calls  → {i:{share,redact,esc,rationale}}. Suggested answer per scenario unlocks after you answer.
CSS = SUB_CSS + '''
  .top-in,.wrap{max-width:940px}
  .warn{margin-top:16px;display:inline-flex;align-items:center;gap:10px;padding:11px 18px;border-radius:12px;
    background:rgba(240,165,68,.08);border:1px solid rgba(240,165,68,.32);color:var(--amber);font-size:13.5px;font-weight:600}

  .prog{margin-top:24px;display:flex;align-items:center;gap:8px;flex-wrap:wrap}
  .dot-nav{display:flex;gap:7px}
  .pdot{width:11px;height:11px;border-radius:50%;background:var(--w1);cursor:pointer;transition:.15s;border:none;padding:0}
  .pdot.on{background:var(--rose-lt)}.pdot.done{background:var(--green-lt)}
  .pcount{font-family:var(--mono);font-size:12px;color:var(--ink-faint);margin-left:6px}

  .card{margin-top:20px;background:var(--card);border:1px solid var(--line-2);border-radius:18px;padding:26px 28px}
  @media(max-width:620px){.card{padding:20px 16px}}
  .sc-tag{display:inline-flex;align-items:center;gap:10px;margin-bottom:16px;flex-wrap:wrap}
  .sc-tag .num{font-family:var(--mono);font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--w);
    background:linear-gradient(135deg,var(--crimson),var(--maroon));border-radius:999px;padding:5px 12px}
  .sc-tag h2{font-size:20px;font-weight:800;letter-spacing:-.2px}
  .quote{border-left:3px solid var(--rose);background:var(--surf);border-radius:0 12px 12px 0;padding:16px 20px;
    font-size:15.5px;font-style:italic;color:var(--ink);line-height:1.6}
  .hint{margin-top:16px;background:rgba(240,165,68,.08);border:1px solid rgba(240,165,68,.28);border-radius:12px;padding:14px 18px}
  .hint .hk{font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--amber);margin-bottom:6px}
  .hint p{font-size:14px;color:var(--ink);line-height:1.55}

  .q{margin-top:24px}
  .q-l{font-family:var(--mono);font-size:11px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-dim);margin-bottom:10px}
  textarea.a,input.a{width:100%;background:var(--surf);border:1px solid var(--w1);border-radius:10px;padding:13px 15px;color:var(--ink);
    font-family:var(--f);font-size:14.5px;line-height:1.55}
  textarea.a{min-height:74px;resize:vertical}
  textarea.a:focus,input.a:focus{outline:none;border-color:rgba(47,116,214,.5)}
  textarea.a.filled,input.a.filled{border-color:var(--green-bd)}

  .esc{display:grid;grid-template-columns:1fr 1fr 1fr;gap:10px}
  @media(max-width:620px){.esc{grid-template-columns:1fr}}
  .escbtn{display:flex;align-items:center;gap:10px;padding:13px 16px;border-radius:10px;border:1px solid var(--w1);text-align:left;
    background:var(--w06);color:var(--ink);font-family:var(--f);font-weight:700;font-size:14px;cursor:pointer;transition:.14s}
  .escbtn .rd{width:16px;height:16px;border-radius:50%;border:2px solid var(--w4);flex:none}
  .escbtn:hover{border-color:var(--w4)}
  .escbtn.sel{border-width:2px}
  .escbtn.sel[data-v="no"]{border-color:var(--green);background:rgba(90,208,160,.1)}.escbtn.sel[data-v="no"] .rd{border-color:var(--green);background:var(--green)}
  .escbtn.sel[data-v="maybe"]{border-color:var(--amber);background:rgba(240,165,68,.1)}.escbtn.sel[data-v="maybe"] .rd{border-color:var(--amber);background:var(--amber)}
  .escbtn.sel[data-v="yes"]{border-color:var(--danger);background:rgba(255,107,107,.1)}.escbtn.sel[data-v="yes"] .rd{border-color:var(--danger);background:var(--danger)}

  .nav{display:flex;justify-content:space-between;margin-top:26px;gap:12px}
  .nbtn{padding:12px 20px;border-radius:10px;border:1px solid var(--w1);background:var(--w06);color:var(--ink);font-family:var(--f);font-weight:700;font-size:14px;cursor:pointer}
  .nbtn:hover{border-color:rgba(47,116,214,.45)}
  .nbtn.next{background:linear-gradient(135deg,var(--crimson),var(--maroon));border:none;color:var(--w)}
  .nbtn:disabled{opacity:.4;cursor:not-allowed}
  .tiers{display:flex;flex-wrap:wrap;gap:9px}
  .tb{padding:10px 15px;border-radius:999px;border:1px solid var(--w1);background:var(--w06);color:var(--ink);font-family:var(--f);font-weight:700;font-size:13.5px;cursor:pointer}
  .tb.sel{border:2px solid var(--rose-lt);padding:9px 14px;background:rgba(47,116,214,.16)}
  .legend{margin-top:10px;font-size:12.8px;color:var(--ink-faint);line-height:1.6}
  .legend b{color:var(--ink-dim)}
  .sugg{margin-top:26px}
  .sugg summary{cursor:pointer;font-weight:800;font-size:14.5px;color:var(--green-lt);padding:12px 16px;border:1px solid rgba(90,208,160,.35);border-radius:12px;background:rgba(90,208,160,.06);list-style:none}
  .sugg summary::-webkit-details-marker{display:none}
  .sugg.locked summary{color:var(--ink-faint);border-color:var(--w1);background:var(--w06);cursor:not-allowed}
  .sg-body{margin-top:10px;border:1px solid rgba(90,208,160,.3);border-radius:12px;padding:16px 18px;background:rgba(90,208,160,.05)}
  .sg-row{display:grid;grid-template-columns:150px 1fr;gap:10px;padding:7px 0;border-bottom:1px solid var(--w1);font-size:14px;line-height:1.55;color:var(--ink)}
  .sg-row:last-child{border-bottom:none}
  .sg-row .k{font-family:var(--mono);font-size:10.5px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--green-lt);padding-top:3px}
  @media(max-width:620px){.sg-row{grid-template-columns:1fr;gap:2px}}
  .sg-note{margin-top:10px;font-size:12.8px;color:var(--ink-faint)}
  .clearbar{margin-top:18px;text-align:right}
  .clearbar button{font-family:var(--mono);font-size:12px;color:var(--rose-lt);background:none;border:none;cursor:pointer;font-weight:700}
'''

JS = r'''
(function(){
  const SCEN = [
    {
      title:'The complaint reply',
      role:'Sales · Customer service',
      quote:`"A customer, Hessa Al-Enezi, is very angry about a late and wrong delivery. I have her full email and her order history. The history shows her Civil ID, 2870xxxxxxxx, because she registered for the loyalty card. Can I paste all of it into Copilot to draft a reply? It will be faster."`,
      sugg:{tier:'restricted',share:'The problem only: the order was late and wrong, what she asked for, and what you can offer (a refund or credit, a new delivery).',redact:'Her name, email, Civil ID, loyalty and order history. Copilot does not need any of it to write a polite reply.',esc:'no',escw:'No — handle it in the team. Nothing has gone wrong yet.',line:'“Give Copilot the problem, not the person — then add her name yourself in Outlook before you send.”'},
      hint:`A good reply is the right goal. Pasting all of her personal data is the wrong method. What is the smallest amount of data Copilot needs to draft a polite, useful reply?`
    },
    {
      title:'The whole customer list',
      role:'Marketing',
      quote:`"I want to know which loyalty customers will stop buying from us. I'll export the full customer list from the loyalty app — 18,000 names, phone numbers and total spend — and upload it to a free AI website. It is better with data than our tools."`,
      sugg:{tier:'restricted',share:'Nothing from the list, and nothing on a free AI website. Instead: totals and trends (e.g. spend by month, by customer group) with no names or phones — in Copilot in Excel on your work account.',redact:"Refuse the upload. 18,000 customers' names, phones and spend is personal data, and a free public tool is outside the company's control.",esc:'maybe',escw:'Maybe — get approval first. A real churn analysis needs the data owner (and the data protection lead) to agree how.',line:"“Not on a free AI site — let's ask the data owner, and work on totals with no names in Copilot at work.”"},
      hint:`There are two problems here: the data (every customer's personal details) and the channel (a free public tool that your company does not control). Which problem stops this first? What could you do instead, with your work account and less data?`
    },
    {
      title:'Rank the candidates',
      role:'Executive · HR',
      quote:`"We have 40 CVs for the new branch manager role. Can Copilot score them and give me the top 5 to interview? It will save me a full day."`,
      sugg:{tier:'restricted',share:'Help with the wording of the job criteria, or a summary of each CV against those criteria — on your work account.',redact:'Refuse the ranking. Copilot must not decide who gets an interview. Leave out photos, age, nationality and marital status.',esc:'maybe',escw:'Maybe — check with HR first. Many companies have rules on AI in hiring, and a person must make and own the decision.',line:'“Copilot can summarise each CV against the criteria — you choose the five, and you can explain why.”'},
      hint:`Copilot can help you read and summarise CVs. Should it decide who gets an interview? Think about bias and fairness. If a strong candidate is rejected, who is accountable — Copilot or you?`
    },
    {
      title:'Debug with the real keys',
      role:'Technical',
      quote:`"The delivery app is down and orders are failing. I'll paste our production API keys and the app architecture into my personal ChatGPT account to find the bug. It's just for a minute."`,
      sugg:{tier:'restricted',share:'The error message and the steps that cause it — with [SECRET] in place of every key — in Copilot on your work account.',redact:'Refuse the keys and the architecture, and refuse the personal account. Secrets never go into any prompt.',esc:'yes',escw:'Yes — escalate now. The outage goes to the on-call or IT lead. If any key was already pasted anywhere, IT security must replace (rotate) it today.',line:"“Stop — no keys in any AI tool. Send me the error message, and I'll call the IT lead about the outage.”"},
      hint:`This is not customer data. Is it any safer? Think about secrets, a personal account that the company cannot see or control, and what you cannot undo after one minute. What could you share instead?`
    },
    {
      title:'The "anonymised" extract',
      role:'Mixed · any role',
      quote:`"For my MBA project I want two years of 'anonymised' order data from the delivery app. I removed the names, but I kept the phone numbers so I can link each customer's orders. I'll save it on my personal Google Drive. It's anonymised, so it's fine, right?"`,
      sugg:{tier:'restricted',share:'Nothing from the real customer data. Ask for an approved, fully anonymous summary (totals only) — or use made-up sample data for the project.',redact:'Refuse the extract. A phone number points to one person, a personal Google Drive is outside the company, and an MBA project is not company work.',esc:'maybe',escw:'Maybe — get approval first. Only the data owner can approve company data for a personal project — usually as totals, never as records.',line:"“Removing names isn't anonymous — a phone number is a person. Ask the data owner, and keep it off your personal drive.”"},
      hint:`Anonymised is not the same as anonymous. A phone number points to one person. There are three issues here: the data, the channel (a personal cloud drive) and the purpose (a personal project, not company work). Which issue is the most serious?`
    },
    {
      title:'The job advert',
      role:'Executive · HR · any manager',
      quote:`"Copilot wrote our advert for a café shift supervisor in ten seconds. It says: 'We are looking for a young, energetic man who can handle long shifts and fits our fun team culture.' It sounds great. Can I post it today?"`,
      sugg:{tier:'public',share:'All of it — a job advert is Public once posted. The problem is not the data. It is bias in what Copilot wrote.',redact:'Remove “young”, “man” and “fits our fun team culture”. Describe the job instead: “a supervisor who can lead a busy shift of 6 people, open and close the café, and train new staff.”',esc:'no',escw:'No — fix it in the team, and ask HR to check it before it goes live.',line:'“Describe the job, not the person — then HR checks it before we post.”'},
      hint:`Nothing confidential here — the problem is bias in the output. Which words shut people out (age, gender, "culture fit")? What should the advert describe instead? Who is accountable if it goes out as it is?`
    }
  ];
  const TIERS = [['public','Public'],['internal','Internal'],['confidential','Confidential'],['restricted','Restricted']];
  const TL = {public:'Public',internal:'Internal',confidential:'Confidential',restricted:'Restricted'};
  const ESC = [
    {v:'no', ic:'✅', label:'No — handle it in the team'},
    {v:'maybe', ic:'🟡', label:'Maybe — get approval first'},
    {v:'yes', ic:'🛑', label:'Yes — escalate now'}
  ];

  const KEY='coded_copilot_judgment_calls';
  let state=store.get(KEY,{}); // {i:{share,redact,esc,rationale}}
  if(!state||typeof state!=='object'||Array.isArray(state)) state={};
  let cur=0;
  const card=document.getElementById('card');
  function save(){store.set(KEY,state)}
  function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
  function answered(i){const s=state[i]; return !!(s && (s.share||s.redact||s.esc||s.rationale||s.tier))}
  function complete(i){const s=state[i]; return !!(s && s.tier && s.esc && (s.rationale||'').trim())}

  function drawDots(){
    const d=document.getElementById('dots'); d.innerHTML='';
    SCEN.forEach((_,i)=>{
      const b=document.createElement('button');
      b.type='button';
      b.className='pdot'+(i===cur?' on':'')+(answered(i)?' done':'');
      b.setAttribute('aria-label','Scenario '+(i+1));
      b.onclick=()=>{cur=i;render()};
      d.appendChild(b);
    });
    document.getElementById('pcount').textContent=(cur+1)+' / '+SCEN.length;
  }

  function render(){
    const sc=SCEN[cur], s=state[cur]||{};
    card.innerHTML=`
      <div class="sc-tag"><span class="num">Scenario ${cur+1}</span><h2>${esc(sc.title)}</h2><span class="pill-tag">${esc(sc.role)}</span></div>
      <div class="quote">${esc(sc.quote)}</div>
      <div class="hint"><div class="hk">Discussion hint</div><p>${esc(sc.hint)}</p></div>

      <div class="q"><div class="q-l">1 — Which tier is the data in this request?</div>
        <div class="tiers" id="q-tier">${TIERS.map(t=>`<button type="button" class="tb${s.tier===t[0]?' sel':''}" data-v="${t[0]}">${t[1]}</button>`).join('')}</div>
        <div class="legend">Not sure? <a href="day-3-classify-redact.html" style="color:var(--rose-lt)">See the four tiers</a> at the top of E3.3.</div></div>

      <div class="q"><div class="q-l">2 — What can you share with AI safely here?</div>
        <textarea class="a${s.share?' filled':''}" id="q-share" placeholder="For example: the main points, the counts, a summary with no names — but not the original records.">${esc(s.share||'')}</textarea></div>

      <div class="q"><div class="q-l">3 — What must you redact (or refuse)?</div>
        <textarea class="a${s.redact?' filled':''}" id="q-redact" placeholder="For example: all names, Civil IDs, phone numbers, card digits — and the raw file itself.">${esc(s.redact||'')}</textarea></div>

      <div class="q"><div class="q-l">4 — Should you escalate?</div>
        <div class="esc" id="q-esc">${ESC.map(e=>`<button type="button" class="escbtn${s.esc===e.v?' sel':''}" data-v="${e.v}"><span class="rd"></span><span>${e.ic}</span> ${e.label}</button>`).join('')}</div>
        <div class="legend"><b>Handle it in the team:</b> you and the colleague fix it now. <b>Get approval first:</b> ask your manager or the data owner before anything happens. <b>Escalate now:</b> something may already be exposed or broken — tell IT security, HR or your manager today.</div></div>

      <div class="q"><div class="q-l">5 — One line you would say to your colleague</div>
        <input class="a${s.rationale?' filled':''}" id="q-rat" placeholder="The one sentence you would say to them, out loud." value="${esc(s.rationale||'').replace(/"/g,'&quot;')}"></div>

      <details class="sugg${complete(cur)?'':' locked'}" id="sugg">
        <summary>${complete(cur)?'✔ Compare with a suggested answer':'🔒 Pick a tier, an escalation and write your line — then compare with a suggested answer'}</summary>
        <div class="sg-body">
          <div class="sg-row"><span class="k">Tier</span><span>${TL[sc.sugg.tier]}${s.tier?(s.tier===sc.sugg.tier?' · ✓ same as yours':' · you chose '+TL[s.tier]):''}</span></div>
          <div class="sg-row"><span class="k">Safe to share</span><span>${esc(sc.sugg.share)}</span></div>
          <div class="sg-row"><span class="k">Redact / refuse</span><span>${esc(sc.sugg.redact)}</span></div>
          <div class="sg-row"><span class="k">Escalate?</span><span>${esc(sc.sugg.escw)}</span></div>
          <div class="sg-row"><span class="k">Say this</span><span>${esc(sc.sugg.line)}</span></div>
          <div class="sg-note">A suggested call, not the only right one. If your table decided differently, can you defend it with a rule?</div>
        </div>
      </details>

      <div class="nav">
        <button type="button" class="nbtn" id="prev" ${cur===0?'disabled':''}>← Previous</button>
        <button type="button" class="nbtn next" id="next" ${cur===SCEN.length-1?'disabled':''}>Next →</button>
      </div>`;

    function lockCheck(){const d=document.getElementById('sugg'), ok=complete(cur); d.classList.toggle('locked',!ok); if(!ok) d.open=false;
      d.querySelector('summary').textContent = ok ? '✔ Compare with a suggested answer' : '🔒 Pick a tier, an escalation and write your line — then compare with a suggested answer'; }
    function set(k,v){state[cur]=state[cur]||{};state[cur][k]=v;save();drawDots();lockCheck()}
    document.getElementById('sugg').querySelector('summary').addEventListener('click',e=>{ if(!complete(cur)) e.preventDefault(); });
    card.querySelectorAll('#q-tier .tb').forEach(b=>b.onclick=()=>{ set('tier',b.dataset.v); card.querySelectorAll('#q-tier .tb').forEach(x=>x.classList.toggle('sel',x===b)); });
    const sh=document.getElementById('q-share'), rd=document.getElementById('q-redact'), rt=document.getElementById('q-rat');
    sh.oninput=e=>{set('share',e.target.value);e.target.classList.toggle('filled',!!e.target.value)};
    rd.oninput=e=>{set('redact',e.target.value);e.target.classList.toggle('filled',!!e.target.value)};
    rt.oninput=e=>{set('rationale',e.target.value);e.target.classList.toggle('filled',!!e.target.value)};
    card.querySelectorAll('#q-esc .escbtn').forEach(b=>b.onclick=()=>{
      set('esc',b.dataset.v);
      card.querySelectorAll('#q-esc .escbtn').forEach(x=>x.classList.toggle('sel',x===b));
    });
    const p=document.getElementById('prev'), n=document.getElementById('next');
    if(p)p.onclick=()=>{if(cur>0){cur--;render()}};
    if(n)n.onclick=()=>{if(cur<SCEN.length-1){cur++;render()}};
    drawDots();
  }

  document.getElementById('clearBtn').onclick=()=>{
    if(!confirm('Clear all your judgment-call answers?')) return;
    state={};save();cur=0;render();
  };
  render();
})();
'''


def build():
    body = topbar('Judgment <b>calls</b>', back='coded-copilot-day-3-lab.html#E3.4', back_label='← Day 3 lab') + '''
<div class="wrap">
  <span class="eyebrow">Exercise E3.4 · Safety with AI</span>
  <h1>Judgment calls — would you let this through?</h1>
  <p class="intro">Six colleagues ask you for a quick yes. These are real work situations where the right answer is not
  always clear. Work in pairs. For each one, decide five things: the <b>tier</b> of the data, what you can <b>share</b> with AI
  safely, what you must <b>redact or refuse</b>, whether to <b>escalate</b>, and the <b>one line</b> you would say. Then open the
  suggested answer and compare. Where you disagree, argue it out — the reason matters more than the answer.</p>
  <div class="warn">⚠ All fictional scenarios — no real customers, staff or figures.</div>

  <div class="prog">
    <div class="dot-nav" id="dots"></div>
    <span class="pcount" id="pcount"></span>
  </div>

  <div class="card" id="card"><!-- built by JS --></div>

  <div class="clearbar"><button type="button" id="clearBtn">Clear all my answers</button></div>
</div>
''' + footer_row()
    return page('Judgment Calls — Day 3 · ' + TITLE + ' · CODED', body, css=CSS, js=JS,
                desc='Exercise E3.4: six workplace scenarios. Decide what to share with AI, what to redact or refuse, and when to escalate.')
