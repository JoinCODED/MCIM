# Day 3 · Exercise E3.1 — Classify + Redact (six items, four tiers). Written for a cross-industry room.
# State: localStorage key coded_copilot_classify_redact  → {i:{tier,text}}
CSS = SUB_CSS + '''
  .top-in,.wrap{max-width:960px}

  /* toolbar */
  .bar{position:sticky;top:59px;z-index:20;margin-top:24px;display:flex;align-items:center;gap:14px;flex-wrap:wrap;
    background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:14px 18px}
  .bar .count{font-size:15px;font-weight:800;color:var(--ink)}
  .bar .count b{color:var(--rose-lt)}
  .bar .spacer{flex:1}
  .btn{padding:10px 16px;border-radius:9px;font-weight:700;font-size:13.5px;cursor:pointer;border:1px solid var(--w1);background:var(--w06);color:var(--ink);transition:.15s}
  .btn:hover{border-color:rgba(47,116,214,.45)}
  .btn.key{background:linear-gradient(135deg,var(--crimson),var(--maroon));border:none;color:var(--w)}
  .btn.key:disabled{opacity:.4;cursor:not-allowed;background:var(--w06);color:var(--ink-faint)}
  .btn.clear{color:var(--rose-lt);border-color:rgba(47,116,214,.3)}

  .how{margin-top:16px;border-left:3px solid var(--rose);background:rgba(47,116,214,.06);border-radius:0 12px 12px 0;
    padding:14px 18px;font-size:14px;color:var(--ink-dim);line-height:1.6}
  .how b{color:var(--ink)}

  /* item (resets the cheat-sheet .item from SUB_CSS) */
  .item{margin-top:26px;background:var(--card);border:1px solid var(--line-2);border-radius:16px;overflow:hidden;padding:0}
  .it-head{display:flex;align-items:center;gap:12px;padding:18px 22px;border-bottom:1px solid var(--line);flex-wrap:wrap}
  .it-tag{font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:var(--rose-lt);
    background:rgba(47,116,214,.12);border:1px solid rgba(47,116,214,.3);border-radius:6px;padding:4px 9px}
  .it-head h2{font-size:16.5px;font-weight:800;letter-spacing:-.2px;flex:1;min-width:180px}
  .it-status{font-family:var(--mono);font-size:11px;font-weight:700;color:var(--ink-faint)}
  .it-status.on{color:var(--green-lt)}
  .it-body{padding:20px 22px}
  .raw{font-family:var(--mono);font-size:13px;color:var(--ink);background:var(--surf);border:1px solid var(--w1);
    border-radius:10px;padding:16px 18px;line-height:1.6;white-space:pre-wrap;overflow-wrap:anywhere;overflow-x:auto}

  .lbl{font-family:var(--mono);font-size:10.5px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-faint);margin:20px 0 10px}
  .tiers{display:flex;flex-wrap:wrap;gap:9px}
  .tier{display:inline-flex;align-items:center;gap:8px;padding:9px 15px;border-radius:999px;border:1px solid var(--w1);
    background:var(--w06);color:var(--ink);font-family:var(--f);font-weight:700;font-size:13.5px;cursor:pointer;transition:.14s}
  .tier .d{width:11px;height:11px;border-radius:50%;flex:none}
  .tier:hover{border-color:var(--w4)}
  .tier.sel{border-width:2px;padding:8px 14px}
  .tier[data-t="public"] .d{background:var(--green)}.tier[data-t="public"].sel{border-color:var(--green);background:rgba(90,208,160,.12)}
  .tier[data-t="internal"] .d{background:var(--rose)}.tier[data-t="internal"].sel{border-color:var(--rose);background:rgba(111,156,232,.16)}
  .tier[data-t="confidential"] .d{background:var(--amber)}.tier[data-t="confidential"].sel{border-color:var(--amber);background:rgba(240,165,68,.12)}
  .tier[data-t="restricted"] .d{background:var(--danger)}.tier[data-t="restricted"].sel{border-color:var(--danger);background:rgba(255,107,107,.12)}
  .tier[data-t="never"] .d{background:var(--red-deep);box-shadow:0 0 0 2px var(--w)}.tier[data-t="never"].sel{border-color:var(--red-deep);background:rgba(194,48,48,.28)}

  .palette{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
  .palette .pl-lbl{font-size:12.5px;color:var(--ink-faint);margin-right:4px}
  .chipbtn{font-family:var(--mono);font-size:12px;font-weight:700;color:var(--rose-lt);background:rgba(47,116,214,.1);
    border:1px solid rgba(47,116,214,.28);border-radius:7px;padding:6px 10px;cursor:pointer;transition:.14s}
  .chipbtn:hover{background:rgba(47,116,214,.2)}
  textarea.redact{width:100%;min-height:150px;margin-top:10px;background:var(--surf);border:1px solid var(--w1);border-radius:10px;
    padding:14px 16px;color:var(--ink);font-family:var(--mono);font-size:13px;line-height:1.6;resize:vertical}
  textarea.redact:focus{outline:none;border-color:rgba(47,116,214,.5)}
  textarea.redact:disabled{opacity:.45}
  .neverbox{margin-top:10px;background:rgba(248,75,75,.08);border:1px solid rgba(255,107,107,.35);border-radius:10px;padding:14px 16px;
    font-size:13.5px;color:var(--ink);line-height:1.6;display:none}
  .neverbox.on{display:block}
  .it-body .foot-row{display:flex;justify-content:space-between;align-items:center;margin-top:12px;flex-wrap:wrap;gap:8px}
  .reset{font-family:var(--f);font-size:12.5px;color:var(--rose-lt);cursor:pointer;background:none;border:none;font-weight:700}
  .hint{font-size:12px;color:var(--ink-faint)}

  /* answer key */
  .akey{display:none;margin-top:16px;border-radius:12px;padding:16px 18px;border:1px solid rgba(90,208,160,.3);background:rgba(90,208,160,.06)}
  .akey.on{display:block}
  .akey .ak-k{font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:.16em;text-transform:uppercase;color:var(--green-lt);margin-bottom:10px}
  .akey .verdict{display:inline-flex;align-items:center;gap:8px;font-weight:800;font-size:14px;margin-bottom:10px}
  .akey .verdict.ok{color:var(--green-lt)}.akey .verdict.no{color:var(--danger)}
  .akey .ak-tier{font-weight:800}
  .akey p{font-size:13.5px;color:var(--ink);line-height:1.6;margin-top:6px}
  .akey .model{font-family:var(--mono);font-size:12.5px;color:var(--ink);background:var(--surf);border:1px solid var(--w1);
    border-radius:9px;padding:12px 14px;margin-top:10px;white-space:pre-wrap;overflow-wrap:anywhere;line-height:1.55}
  .warn{margin-top:18px;display:inline-flex;align-items:center;gap:10px;padding:11px 18px;border-radius:12px;
    background:rgba(240,165,68,.08);border:1px solid rgba(240,165,68,.32);color:var(--amber);font-size:13.5px;font-weight:600}
  @media(max-width:620px){.it-head,.it-body{padding-left:16px;padding-right:16px}.raw{padding:14px}}
'''

JS = r'''
(function(){
  const PALETTE = ["[CUSTOMER]","[NAME]","[CIVIL ID]","[PHONE]","[ACCOUNT]","[AMOUNT]","[DATE]","[LOCATION]","[SECRET]"];
  const TIERS = [
    {id:"public",label:"Public"},{id:"internal",label:"Internal"},
    {id:"confidential",label:"Confidential"},{id:"restricted",label:"Restricted"},
    {id:"never",label:"NEVER send"}
  ];
  const TLABEL = {public:"Public",internal:"Internal",confidential:"Confidential",restricted:"Restricted",never:"NEVER send"};

  const ITEMS = [
    {
      title:"Customer complaint email (personal data)",
      raw:`From: dalal.alkandari@example.com
Subject: Charged twice for order TF-58213 — KWD 18.750

Hello, my name is Dalal Al-Kandari (Civil ID 2870xxxxxxxx, mobile +965 6xxx 2419).
I ordered from the Tamra app on 14 September. My card ending 4821 was charged KWD 18.750 two times.
The order came to my home in Salwa, Block 10. Only one payment should go through.
Please refund the second charge this week, or I will delete the app.`,
      answer:"restricted",
      why:"This is a customer's personal data: name, email, Civil ID, phone, card digits, home area and order number. Together they point to one real person. Restricted: you may put it into an AI tool only after you remove every identifier. The problem itself (a double charge of KWD 18.750) can stay. It does not identify anyone.",
      model:`From: [CUSTOMER]
Subject: Charged twice for order [ACCOUNT] — KWD 18.750

Hello, my name is [CUSTOMER] (Civil ID [CIVIL ID], mobile [PHONE]).
I ordered from the Tamra app on [DATE]. My card ending [ACCOUNT] was charged KWD 18.750 two times.
The order came to my home in [LOCATION]. Only one payment should go through.
Please refund the second charge this week, or I will delete the app.`
    },
    {
      title:"Café team retro (internal process notes)",
      raw:`Café Operations — Sprint 18 retro (6 branches)
Went well: the new breakfast menu launched on time in all 6 branches. Average wait time fell from 9 to 6 minutes.
Did not go well: the Salmiya branch ran out of oat milk twice. The stock app and the shelf count did not match.
Actions: Mariam owns the weekly stock check. Khaled updates the reorder levels in the stock app.
Each branch sends a photo of the shelf every Sunday.`,
      answer:"internal",
      why:"These are internal working notes about how the team works. There is no customer data, no secret and no sensitive figure. Internal: you can summarise them with Copilot on your work account. Good habit: replace colleague names with [NAME] before you paste.",
      model:`Café Operations — Sprint 18 retro (6 branches)
Went well: the new breakfast menu launched on time in all 6 branches. Average wait time fell from 9 to 6 minutes.
Did not go well: the Salmiya branch ran out of oat milk twice. The stock app and the shelf count did not match.
Actions: [NAME] owns the weekly stock check. [NAME] updates the reorder levels in the stock app.
Each branch sends a photo of the shelf every Sunday.`
    },
    {
      title:"Published menu and price list (public)",
      raw:`Tamra Café — Menu and prices (public: tamrafoods.example and the Tamra app)
Arabic coffee (pot for 2): KWD 1.500   |  Spanish latte: KWD 1.750
Date cake (slice): KWD 1.250           |  Halloumi sandwich: KWD 2.250
Delivery in Kuwait City: KWD 0.500. Free delivery on orders over KWD 10.000.
Prices may change. See the app for current prices.`,
      answer:"public",
      why:"The company already publishes this on its website and in its app. Anyone can see it. Public: you can paste it as it is. There is nothing to redact.",
      model:`No redaction needed. This is already public. Paste it as it is.`
    },
    {
      title:"HR salary and performance extract",
      raw:`HR_Review_2026.xlsx (extract — Café Operations)
Emp 1042 | Noura Al-Mutairi  | Branch manager   | Salary KWD 1,450 | Score 2/5 | On improvement plan
Emp 1057 | Ahmad Hussain     | Barista lead     | Salary KWD 620   | Score 4/5 | Bonus proposed
Emp 1063 | Reem Al-Shammari  | Shift supervisor | Salary KWD 780   | Score 3/5 | Medical leave 12 days (surgery)
Manager note: send to the Operations Director before the bonus meeting.`,
      answer:"never",
      why:"Salary, performance and medical data about named staff. This is some of the most sensitive data a company holds. Removing the names is not enough: a job title, a branch and a salary together can point to one person. NEVER send it to a general AI tool, even with redaction. Use only the approved HR system, and share it only with people who are allowed to see it.",
      model:`NEVER send. Do not paste staff salary, performance or medical data into any AI prompt. Redaction does not make it safe.
Keep it in the approved HR system.
If you need help with the wording of a letter or a policy, write your request with no real staff data in it.`
    },
    {
      title:"Live credentials (payment gateway + database)",
      raw:`# delivery-app/config/prod.env   (a colleague pasted this into the team chat)
PAYMENT_GATEWAY_API_KEY=gw_live_4c9e71b2d0a84f6e_tamra
DB_HOST=orders-db.tamrafoods.example
DB_PASSWORD=Tamra#Orders_2026!
# "Can someone ask AI why checkout keeps failing?"`,
      answer:"never",
      why:"These are live production secrets. Pasting them anywhere outside the approved password vault is a security incident on its own. NEVER send. A leaked key must be rotated (replaced with a new one). Redaction does not fix a leak.",
      model:`NEVER send. Live keys and passwords never go into an AI prompt.
These are now exposed in a chat, so:
1. Ask the owner to rotate (replace) the key and the password today.
2. Report it to IT security.
3. Delete the chat message.
For help with the checkout error, share the error message only, with [SECRET] in place of any key.`
    },
    {
      title:"Draft Q3 board pack (before the announcement)",
      raw:`DRAFT — Q3 2026 Board Pack (not for circulation before the results announcement on 20 October)
Revenue: KWD 4.82M (+11% vs Q3 2025)  |  Gross margin: 38.4%  |  Delivery app orders: 212,000
Plan: raise café prices by 8% from 1 January 2027.
Risk: dispute with our dairy supplier, Al-Waha Dairy Co., over KWD 146,000 in late-delivery penalties.
Please improve the wording of the summary before Sunday.`,
      answer:"confidential",
      why:"Unreleased results, a planned price rise and a named supplier dispute. If this leaks before the announcement, it can harm the company, its staff and its partners. Confidential: keep it in approved tools (for example Copilot on your work account), and share it only with the people who need it. If you need help with the wording, remove the figures and names first.",
      model:`DRAFT — Q3 Board Pack (not for circulation before the results announcement on [DATE])
Revenue: [AMOUNT] ([AMOUNT] vs last year)  |  Gross margin: [AMOUNT]  |  Delivery app orders: [AMOUNT]
Plan: raise café prices by [AMOUNT] from [DATE].
Risk: dispute with our dairy supplier, [NAME], over [AMOUNT] in late-delivery penalties.
Please improve the wording of the summary before Sunday.`
    }
  ];

  const KEY='coded_copilot_classify_redact';
  let state=store.get(KEY,{}); // {i:{tier,text}}
  if(!state||typeof state!=='object'||Array.isArray(state)) state={};
  let revealed=false;
  const wrap=document.getElementById('items');

  function h(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;').replace(/"/g,'&quot;')}
  function handled(i){
    const s=state[i]; if(!s||!s.tier) return false;
    if(s.tier==='never') return true;
    const ta=document.getElementById('ta'+i);
    const v = ta ? ta.value : (s.text || '');
    return v.trim().length>0; // a redaction (or NEVER) is needed to count as handled
  }
  function doneCount(){return ITEMS.map((_,i)=>i).filter(handled).length}
  function save(){store.set(KEY,state)}

  function updateBar(){
    const n=doneCount();
    document.getElementById('cDone').textContent=n;
    document.getElementById('revealBtn').disabled = n<ITEMS.length || revealed;
  }

  function insertPlaceholder(ta,ph){
    const start=ta.selectionStart, end=ta.selectionEnd, v=ta.value;
    ta.value = v.slice(0,start) + ph + v.slice(end);
    ta.selectionStart = ta.selectionEnd = start + ph.length;
    ta.focus();
  }

  function build(){
    wrap.innerHTML='';
    ITEMS.forEach((it,i)=>{
      const s=state[i]||{};
      const card=document.createElement('div');
      card.className='item';
      card.innerHTML=`
        <div class="it-head"><span class="it-tag">Item ${i+1}</span><h2>${h(it.title)}</h2>
          <span class="it-status${handled(i)?' on':''}" id="st${i}">${handled(i)?'✓ handled':'not handled'}</span></div>
        <div class="it-body">
          <pre class="raw">${h(it.raw)}</pre>

          <div class="lbl">1 — Pick the tier</div>
          <div class="tiers" id="tiers${i}">
            ${TIERS.map(t=>`<button type="button" class="tier${s.tier===t.id?' sel':''}" data-t="${t.id}"><span class="d"></span>${t.label}</button>`).join('')}
          </div>

          <div class="lbl">2 — Write your own redacted version</div>
          <div class="palette">
            <span class="pl-lbl">Insert placeholder:</span>
            ${PALETTE.map(p=>`<button type="button" class="chipbtn" data-ph="${p}">${p}</button>`).join('')}
          </div>
          <textarea class="redact" id="ta${i}" ${s.tier==='never'?'disabled':''} placeholder="Write a version that is safe to paste. Read the original above and remove every identifier yourself, or click a placeholder to insert it. Or mark it NEVER send.">${s.text!==undefined?h(s.text):''}</textarea>
          <div class="neverbox${s.tier==='never'?' on':''}" id="nb${i}">Marked <b>NEVER send</b>. Do not paste any part of this item into a general AI tool, even with redaction.</div>
          <div class="foot-row">
            <button type="button" class="reset" data-reset="${i}">↺ Clear</button>
            <span class="hint">Tip: type your redacted version, or place the cursor and click a placeholder.</span>
          </div>

          <div class="akey" id="ak${i}">
            <div class="ak-k">Answer key</div>
            <div class="verdict" id="vd${i}"></div>
            <p><span class="ak-tier">Correct tier: ${TLABEL[it.answer]}.</span> ${h(it.why)}</p>
            <div class="model">${h(it.model)}</div>
          </div>
        </div>`;
      wrap.appendChild(card);

      // tiers
      card.querySelectorAll(`#tiers${i} .tier`).forEach(btn=>btn.onclick=()=>{
        state[i]=state[i]||{}; state[i].tier=btn.dataset.t;
        card.querySelectorAll(`#tiers${i} .tier`).forEach(b=>b.classList.toggle('sel',b===btn));
        const ta=document.getElementById('ta'+i), nb=document.getElementById('nb'+i);
        const isNever=btn.dataset.t==='never';
        ta.disabled=isNever; nb.classList.toggle('on',isNever);
        save(); refreshStatus(i); updateBar();
      });
      // palette
      const ta=card.querySelector('#ta'+i);
      card.querySelectorAll('.chipbtn').forEach(b=>b.onclick=()=>{
        if(ta.disabled) return;
        insertPlaceholder(ta,b.dataset.ph);
        state[i]=state[i]||{}; state[i].text=ta.value; save(); refreshStatus(i); updateBar();
      });
      ta.oninput=()=>{state[i]=state[i]||{}; state[i].text=ta.value; save(); refreshStatus(i); updateBar();};
      card.querySelector(`[data-reset="${i}"]`).onclick=()=>{
        ta.value=''; state[i]=state[i]||{}; state[i].text=''; save(); refreshStatus(i); updateBar();
      };
    });
  }

  function refreshStatus(i){
    const el=document.getElementById('st'+i);
    const ok=handled(i);
    el.textContent=ok?'✓ handled':'not handled'; el.classList.toggle('on',ok);
  }

  function reveal(){
    revealed=true;
    ITEMS.forEach((it,i)=>{
      const ak=document.getElementById('ak'+i); ak.classList.add('on');
      const vd=document.getElementById('vd'+i);
      const picked=(state[i]||{}).tier;
      const ok=picked===it.answer;
      vd.className='verdict '+(ok?'ok':'no');
      vd.textContent=ok?('✓ You chose '+TLABEL[it.answer]+'. Correct.')
                       :('✕ You chose '+(picked?TLABEL[picked]:'nothing')+'. The answer is '+TLABEL[it.answer]+'.');
    });
    document.getElementById('revealBtn').disabled=true;
    const first=document.getElementById('ak0');
    if(first && first.scrollIntoView) first.scrollIntoView({behavior:'smooth',block:'center'});
  }

  document.getElementById('revealBtn').onclick=reveal;
  document.getElementById('clearBtn').onclick=()=>{
    if(!confirm('Clear all your tiers and redactions?')) return;
    state={}; revealed=false; save(); build(); updateBar();
  };

  build(); updateBar();
})();
'''


def build():
    body = topbar('Classify <b>+ Redact</b>', back='coded-copilot-day-3-lab.html#E3.1', back_label='← Day 3 lab') + '''
<div class="wrap">
  <span class="eyebrow">Exercise E3.1 · Responsible AI</span>
  <h1>Classify + Redact — six items, four tiers.</h1>
  <p class="intro">Here are six sample items from Tamra Foods Co. Together they cover every data tier. Pick a tier for each item.
  Then write a version that is safe to paste into an AI tool — or mark it <b>NEVER send</b>. The placeholder buttons make
  redaction faster. When you finish all six, reveal the answer key and discuss any differences with your table.</p>
  <div class="warn">⚠ All fictional sample data — no real customers, staff, keys or figures.</div>

  <div class="bar">
    <span class="count"><b id="cDone">0</b> / 6 items classified + handled</span>
    <span class="spacer"></span>
    <button type="button" class="btn key" id="revealBtn" disabled>Reveal answer key</button>
    <button type="button" class="btn clear" id="clearBtn">Clear</button>
  </div>
  <div class="how"><b>How to do this exercise:</b> For each of the 6 items, (1) pick its tier. (2) Write a redacted version
  that is safe to paste into an AI tool — or mark it <i>NEVER send</i>. Place the cursor in the box and click a placeholder
  to insert it. When all 6 are handled, click <b>Reveal answer key</b>. Then compare your choices with your table.</div>

  <div id="items"><!-- built by JS --></div>
</div>
''' + footer_row()
    return page('Classify + Redact — Day 3 · ' + TITLE + ' · CODED', body, css=CSS, js=JS,
                desc='Exercise E3.1: tier six sample items from Tamra Foods Co. and write safe, redacted versions for AI tools.')
