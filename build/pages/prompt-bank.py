# Your Prompt Bank in Word — a guide. Trainees create and keep their own Word document; the site stores no prompts.
# The only thing the page reads: prompts an older version of the site saved in this browser (Days 1–2), so they can copy them into Word once.
CSS = SUB_CSS + '''
  .steps{counter-reset:s;list-style:none;margin:26px 0 0;padding:0;display:flex;flex-direction:column;gap:12px}
  .steps li{counter-increment:s;position:relative;background:linear-gradient(180deg,var(--surf2),var(--surf));border:1px solid var(--w1);border-radius:14px;padding:16px 18px 16px 62px}
  .steps li::before{content:counter(s);position:absolute;left:18px;top:16px;width:30px;height:30px;border-radius:50%;display:grid;place-items:center;
    background:rgba(47,116,214,.2);border:1px solid rgba(47,116,214,.5);color:#fff;font-weight:800;font-size:14px}
  .steps h3{font-size:16px;font-weight:800;margin:3px 0 6px;color:var(--ink)}
  .steps p{font-size:14px;line-height:1.6;color:var(--ink-dim)}
  .steps p b{color:var(--ink)}
  .sample{margin-top:12px;background:#fff;color:#1f2937;border-radius:10px;padding:18px 22px;font-family:Calibri,Arial,sans-serif;line-height:1.45;max-width:640px}
  .sample .t{font-size:22px;font-weight:700;color:#0b1f3a}
  .sample .h1{font-size:16px;font-weight:700;color:#004aa3;margin-top:12px}
  .sample .h2{font-size:14px;font-weight:700;color:#0b1f3a;margin-top:8px}
  .sample .pr{font-size:13.5px;border-left:3px solid #2f74d6;background:#eef3fb;padding:6px 10px;margin-top:4px}
  .sample .nt{font-size:12px;color:#6b7280;margin-top:3px}
  .try{font-family:var(--mono);font-size:13px;color:var(--ink);background:rgba(0,0,0,.25);border:1px solid var(--w1);border-radius:9px;padding:10px 12px;margin-top:8px;cursor:pointer}
  .old{display:none;margin-top:28px;border:1px dashed rgba(240,165,68,.5);background:rgba(240,165,68,.06);border-radius:14px;padding:16px 18px}
  .old.on{display:block}
  .old p{font-size:14px;line-height:1.6;color:var(--ink)}
  .old .row{display:flex;gap:10px;flex-wrap:wrap;margin-top:12px}
'''

JS = r'''
(function(){
  document.querySelectorAll('.try').forEach(function(el){ el.onclick = function(){ copyText(el.textContent).then(function(){ toast('Copied ✓'); }); }; });
  // one-time move: prompts an earlier version of this site saved in this browser
  var old = (window.PB && PB.all()) || [];
  if (old.length) {
    document.getElementById('oldN').textContent = old.length;
    document.getElementById('old').classList.add('on');
    var text = old.map(function(p){ return (p.title || 'My prompt') + (p.day ? ' (' + p.day + (p.app ? ' · ' + p.app : '') + ')' : '') + '\n' + p.text; }).join('\n\n');
    document.getElementById('oldCopy').onclick = function(){ copyText(text).then(function(){ toast('Copied ✓ Paste into your Word Prompt Bank'); }); };
    document.getElementById('oldClear').onclick = function(){ if (confirm('Remove the old prompts from this browser? Paste them into Word first.')) { PB.save([]); document.getElementById('old').classList.remove('on'); } };
  }
})();
'''


def build():
    body = topbar('Your Prompt <b>Bank</b>') + '''
<div class="wrap narrow">
  <span class="eyebrow">Your Prompts · Kept In Word</span>
  <h1>Your Prompt Bank — in Word.</h1>
  <p class="intro">Your Prompt Bank is a <b>Word document you create yourself</b> and keep in your OneDrive. Every time a prompt works, paste it in.
  It goes home with you, it works on any device — and Copilot can read it.</p>

  <ol class="steps">
    <li><h3>Create it</h3><p>Open Word. Start a <b>new blank document</b>. Name it <b>My Prompt Bank</b> and save it to your <b>OneDrive</b>.</p></li>
    <li><h3>Give it a shape</h3><p>Use <b>Heading 1</b> for each day or app (Day 1 · Copilot Chat, Word, Excel…). Use <b>Heading 2</b> for each prompt's name.
      Paste the prompt under it. Add one line: when you use it, and what you changed. Headings let you jump around with the Navigation pane.</p>
      <div class="sample">
        <div class="t">My Prompt Bank</div>
        <div class="h1">Day 2 · Outlook</div>
        <div class="h2">Reply to a messy thread</div>
        <div class="pr">Summarise this thread: what was promised, what is still open. Then draft a warm reply under 120 words that answers both open points.</div>
        <div class="nt">Use: any thread longer than 5 emails. Changed: added “under 120 words”.</div>
        <div class="h1">Day 3 · Agent Builder</div>
        <div class="h2">Tamra HR Helper — instructions</div>
        <div class="pr">You answer staff questions about HR policy. Use only the four policy files. If two files disagree, use the newest and say so…</div>
      </div></li>
    <li><h3>Fill it as you go</h3><p>In the labs, tap a prompt to copy it. In Copilot, copy the prompt you improved. Paste it into Word under the right heading.
      Only keep prompts you will <b>use again</b>.</p></li>
    <li><h3>Use it in Copilot</h3><p>In Copilot, type <b>/</b> and pick your <b>My Prompt Bank</b> file. Then ask, for example:</p>
      <div class="try" title="Tap to copy">Use the prompt called “Reply to a messy thread” from my Prompt Bank on the email I pasted below.</div></li>
    <li><h3>Keep it safe</h3><p>Prompts only. <b>No</b> customer names, Civil IDs, salaries, passwords or keys — use placeholders like [CUSTOMER].
      Keep it on your work OneDrive, not a personal drive.</p></li>
  </ol>

  <div class="old" id="old">
    <p><b>You saved <span id="oldN">0</span> prompts in this browser on Days 1–2.</b> Copy them all, paste them into your Word Prompt Bank, then tidy them under headings.</p>
    <div class="row"><button class="btn primary" id="oldCopy">Copy all my old prompts</button><button class="btn danger" id="oldClear">Remove them from this browser</button></div>
  </div>

  <p class="note">Also in Copilot: save your favourite prompts to <b>Your prompts</b> in the Prompt Gallery (Day 3). Your Word Prompt Bank holds the full set — with your notes.</p>
</div>
''' + footer_row()
    return page('Your Prompt Bank in Word — ' + TITLE + ' · CODED', body, css=CSS, js=JS, desc='How to build your own Copilot Prompt Bank in Word, keep it in OneDrive and use it in Copilot.')
