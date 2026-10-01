# My Prompt Bank — the participant's saved prompts (localStorage, shared with every lab)
CSS = SUB_CSS + '''
  .pb-bar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:26px 0 18px}
  .pb-bar .grow{flex:1}
  .filters{display:flex;flex-wrap:wrap;gap:6px}
  .flt{padding:7px 12px;border-radius:999px;font-size:12.5px;font-weight:700;cursor:pointer;border:1px solid var(--w1);background:var(--w06);color:var(--ink-dim);font-family:var(--f)}
  .flt.on{border-color:rgba(47,116,214,.55);color:#fff;background:rgba(47,116,214,.22)}
  .pcard{background:linear-gradient(180deg,var(--surf2),var(--surf));border:1px solid var(--w1);border-left:3px solid var(--crimson);border-radius:14px;padding:16px 18px;margin-bottom:12px}
  .pc-top{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-bottom:8px}
  .pc-title{font-size:15px;font-weight:800;color:var(--ink);margin-right:auto}
  .pc-text{font-family:var(--mono);font-size:13px;line-height:1.6;color:var(--ink);white-space:pre-wrap;background:rgba(0,0,0,.25);border:1px solid var(--w1);border-radius:9px;padding:12px 14px;cursor:pointer}
  .pc-text:hover{border-color:rgba(47,116,214,.4)}
  .pc-act{display:flex;gap:8px;margin-top:10px;flex-wrap:wrap}
  .pc-act button{font-size:12px;padding:6px 11px}
  .empty{border:1px dashed var(--w2);border-radius:14px;padding:30px 24px;text-align:center;color:var(--ink-dim);font-size:14.5px;line-height:1.6}
  .add{margin-top:30px}
  .add .row{display:grid;grid-template-columns:1fr;gap:10px}
  .count{font-family:var(--mono);font-size:12px;color:var(--ink-faint)}
'''

JS = r'''
(function(){
  var list = document.getElementById('list'), flt = 'all';
  function esc(s){ return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
  function draw(){
    var a = PB.all();
    document.getElementById('cnt').textContent = a.length + (a.length === 1 ? ' prompt' : ' prompts');
    var shown = a.filter(function(p){ return flt === 'all' || p.day === flt || p.role === flt; });
    if (!a.length) { list.innerHTML = '<div class="empty"><b>Your Prompt Bank is empty in this browser.</b><br>In any lab, tap <b>＋ Save to Prompt Bank</b> under a prompt — or add one below.<br>New laptop? <b>Download as Word</b> still gives you the template to fill in.</div>'; return; }
    if (!shown.length) { list.innerHTML = '<div class="empty">No prompts match this filter.</div>'; return; }
    list.innerHTML = shown.map(function(p){
      var tags = [p.day, p.app, p.role ? (window.ROLES[p.role] || p.role) : ''].filter(Boolean).map(function(t){ return '<span class="pill-tag">' + esc(t) + '</span>'; }).join('');
      return '<div class="pcard" data-id="' + p.id + '"><div class="pc-top"><span class="pc-title">' + esc(p.title || 'My prompt') + '</span>' + tags + '</div>' +
        '<div class="pc-text" title="Tap to copy">' + esc(p.text) + '</div>' +
        '<div class="pc-act"><button class="btn primary" data-a="copy">Copy</button><button class="btn" data-a="edit">Edit</button><button class="btn danger" data-a="del">Delete</button></div></div>';
    }).join('');
  }
  list.addEventListener('click', function(e){
    var card = e.target.closest('.pcard'); if (!card) return;
    var id = card.getAttribute('data-id'), p = PB.all().filter(function(x){ return x.id === id; })[0]; if (!p) return;
    var a = e.target.getAttribute('data-a') || (e.target.classList.contains('pc-text') ? 'copy' : '');
    if (a === 'copy') copyText(p.text).then(function(){ toast('Copied ✓'); });
    if (a === 'del' && confirm('Delete this prompt?')) { PB.remove(id); draw(); }
    if (a === 'edit') {
      var t = prompt('Edit the prompt text:', p.text); if (t === null) return;
      var ti = prompt('Title (optional):', p.title || ''); PB.update(id, { text: t.trim() || p.text, title: ti === null ? p.title : ti.trim() }); draw();
    }
  });
  document.querySelectorAll('.flt').forEach(function(b){ b.onclick = function(){ flt = b.getAttribute('data-f'); document.querySelectorAll('.flt').forEach(function(x){ x.classList.toggle('on', x === b); }); draw(); }; });
  function asText(){ return PB.all().map(function(p, i){ return (i + 1) + '. ' + (p.title || 'My prompt') + (p.day ? ' (' + p.day + (p.app ? ' · ' + p.app : '') + ')' : '') + '\n' + p.text; }).join('\n\n'); }
  document.getElementById('copyAll').onclick = function(){ var t = asText(); if (!t) return toast('Nothing to copy yet'); copyText(t).then(function(){ toast('All prompts copied ✓'); }); };
  document.getElementById('dlWord').onclick = function(){
    var a = document.createElement('a'); a.href = URL.createObjectURL(window.bankDocx(PB.all(), { roles: window.ROLES, dateText: new Date().toLocaleDateString('en-GB', { day: 'numeric', month: 'long', year: 'numeric' }) }));
    a.download = 'my-copilot-prompt-bank.docx'; document.body.appendChild(a); a.click(); a.remove();
    toast(PB.all().length ? 'Word file downloaded ✓ Save it to your OneDrive' : 'Empty template downloaded ✓');
  };
  document.getElementById('dl').onclick = function(){
    var t = asText(); if (!t) return toast('Nothing to export yet');
    var blob = new Blob(['My Copilot Prompt Bank — Mastering Copilot in Microsoft 365 (CODED)\n\n' + t + '\n'], { type: 'text/plain' });
    var a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'my-copilot-prompt-bank.txt'; document.body.appendChild(a); a.click(); a.remove();
  };
  document.getElementById('addBtn').onclick = function(){
    var t = document.getElementById('newText').value, ti = document.getElementById('newTitle').value;
    var r = pbAdd(t, { title: ti.trim() || 'My prompt', app: 'Added by hand' }); if (r === 'ok') { document.getElementById('newText').value = ''; document.getElementById('newTitle').value = ''; draw(); }
  };
  document.getElementById('clearAll').onclick = function(){ if (PB.all().length && confirm('Delete ALL prompts in your Prompt Bank? Download as Word first if you want to keep them.')) { PB.save([]); draw(); } };
  window.addEventListener('storage', draw);
  draw();
})();
'''


def build():
    roles = ''.join(f'<button class="flt" data-f="{k}">{v}</button>' for k, v in M['roles'].items())
    body = topbar('My Prompt <b>Bank</b>') + f'''
<div class="wrap narrow">
  <span class="eyebrow">Your Prompts · Kept</span>
  <h1>My Prompt Bank.</h1>
  <p class="intro">Every prompt you save in the labs lands here. Reuse them at work, improve them, and build your Day 3 capstone from them. They are saved <b>in this browser only</b> — so keep them in a <b>Word document</b>: tap <b>Download as Word</b>, then save the file to your OneDrive.</p>
  <div class="card" style="margin-top:18px;border-left:3px solid var(--rose)"><b>Your Prompt Bank lives in Word.</b> The Word file groups your prompts by day, with a heading for each one and a blank CTFT template at the end. In OneDrive it is yours after the workshop, on any device — and Copilot can use it: type <b>/</b> and pick the file, then say which prompt to run. Download it again whenever you save new prompts here.</div>

  <div class="pb-bar">
    <div class="filters"><button class="flt on" data-f="all">All</button><button class="flt" data-f="Day 1">Day 1</button><button class="flt" data-f="Day 2">Day 2</button><button class="flt" data-f="Day 3">Day 3</button>{roles}</div>
    <span class="grow"></span><span class="count" id="cnt">0 prompts</span>
  </div>
  <div class="pb-bar" style="margin-top:0">
    <button class="btn primary" id="dlWord">Download as Word (.docx)</button>
    <button class="btn" id="copyAll">Copy all</button>
    <button class="btn" id="dl">Plain text (.txt)</button>
    <span class="grow"></span>
    <button class="btn danger" id="clearAll">Delete all</button>
  </div>

  <div id="list"></div>

  <div class="card add">
    <div class="sc-k" style="font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:.18em;text-transform:uppercase;color:var(--rose-lt);margin-bottom:12px">Add a prompt by hand</div>
    <div class="row">
      <input class="in" id="newTitle" placeholder="Title — e.g. Weekly sales update">
      <textarea class="in" id="newText" rows="4" placeholder="Paste or write the prompt. Tip: Context · Task · Format · Tone."></textarea>
      <div><button class="btn primary" id="addBtn">＋ Add to my Prompt Bank</button></div>
    </div>
  </div>

  <p class="note"><b>Keep it after the workshop:</b> tap <b>Download as Word</b> and save the file to your OneDrive. Add new prompts straight into the Word file from now on. In Copilot itself, you can also save prompts to <b>Your prompts</b> in the Prompt Gallery (Day 3).</p>
</div>
''' + footer_row()
    return page('My Prompt Bank — ' + TITLE + ' · CODED', body, css=CSS, js=rd('static/docx-bank.js') + '\n' + JS, desc='Your saved Copilot prompts from the workshop labs.')
