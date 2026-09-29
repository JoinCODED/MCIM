/* ===== LAB ENGINE — task-based Copilot lab =====
   window.LAB = { day, key, back, tasks:[...] }  ·  deep link #E1.3  ·  progress in localStorage
   task fields: id app title minutes scenario steps prompt prompts starters promptSteps goal findings
                reveal dataset files briefs widget launch launches expect stretch boss fallback roles(variants) */
(function(){
  var L = window.LAB, T = L.tasks, KEY = L.key;
  var state = store.get(KEY, {}); if (typeof state !== 'object' || !state) state = {};
  var cur = 0;
  var $ = function(id){ return document.getElementById(id); };
  function save(){ store.set(KEY, state); }
  function esc(s){ return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }
  function attr(s){ return esc(s).replace(/"/g, '&quot;'); }
  function st(i){ return state[T[i].id] || (state[T[i].id] = {}); }

  /* ---- role handling ---- */
  function role(){ return ROLE.get(); }
  function variantOf(t){
    if (!t.roles) return t;
    var r = role(); var keys = Object.keys(t.roles);
    var pick = t.roles[r] ? r : keys[0];
    var v = Object.assign({}, t, t.roles[pick]); v._role = pick; v._roles = keys; return v;
  }
  function drawRoleChip(){
    var sel = $('roleSel'); if (!sel) return;
    sel.value = role() || '';
  }

  /* ---- nav + progress ---- */
  function buildNav(){
    var nl = $('navList'); nl.innerHTML = '';
    T.forEach(function(t, i){
      var d = state[t.id] && state[t.id].done;
      var el = document.createElement('button'); el.type = 'button';
      el.className = 'nav-item' + (i === cur ? ' active' : '') + (d ? ' done' : '') + (t.optional ? ' opt' : '');
      el.innerHTML = '<span class="ni-n">' + (d ? '✓' : esc(t.id.replace(/^E/, ''))) + '</span><span class="ni-t">' + esc(t.title) + (t.optional ? ' <em>stretch</em>' : '') + '</span>';
      el.onclick = function(){ go(i); if (window.innerWidth < 820) $('rail').classList.remove('open'); };
      nl.appendChild(el);
    });
  }
  function updateProg(){
    var core = T.filter(function(t){ return !t.optional; });
    var done = core.filter(function(t){ return state[t.id] && state[t.id].done; }).length;
    $('progFill').style.width = (done / Math.max(1, core.length) * 100) + '%';
    $('progLabel').textContent = done + ' of ' + core.length + ' core tasks done';
    var n = PB.all().length, pc = $('pbCount'); if (pc) pc.textContent = n;
  }

  /* ---- blocks ---- */
  function promptBox(text, label, tag){
    return '<div class="prompt-wrap"><div class="prompt" data-copy="' + attr(text) + '"><span class="copy-tag">tap to copy</span>' + (label ? '<span class="p-lab">' + esc(label) + '</span>' : '') + esc(text) + '</div>' +
      '<button class="pb-save" type="button" data-save="' + attr(text) + '" data-title="' + attr(tag || label || '') + '">＋ Save to Prompt Bank</button></div>';
  }
  function datasetBlock(d){
    return '<div class="dataset"><div class="ds-k">Attached data</div><div class="ds-note">' + d.note + '</div>' +
      '<a class="dl" href="' + attr(d.href) + '" download><span class="ic">⬇</span><span>Download the workbook<small>' + esc(d.label) + '</small></span></a>' +
      (d.head ? '<div class="ds-table-wrap"><table class="ds-table"><thead><tr>' + d.head.map(function(h){ return '<th>' + esc(h) + '</th>'; }).join('') + '</tr></thead><tbody>' +
      d.rows.map(function(r){ return '<tr>' + r.map(function(c){ return '<td>' + esc(c) + '</td>'; }).join('') + '</tr>'; }).join('') + '</tbody></table>' +
      (d.more ? '<div class="ds-more">' + esc(d.more) + '</div>' : '') + '</div>' : '') + '</div>';
  }
  function filesBlock(files){
    return '<div class="dataset"><div class="ds-k">Attached file' + (files.length > 1 ? 's' : '') + '</div>' + files.map(function(f){
      return (f.note ? '<div class="ds-note">' + f.note + '</div>' : '') + '<a class="dl" href="' + attr(f.href) + '" download><span class="ic">⬇</span><span>Download<small>' + esc(f.label) + '</small></span></a>';
    }).join('<div style="height:10px"></div>') + '</div>';
  }
  function briefsBlock(briefs){
    var tabs = briefs.length > 1 ? '<div class="lw-tabs">' + briefs.map(function(b, i){ return '<button type="button" class="lw-tab' + (i ? '' : ' on') + '" data-bt="' + i + '">' + esc(b.label) + '</button>'; }).join('') + '</div>' : '';
    return '<div class="step-card"><div class="sc-k">' + (briefs.length > 1 ? 'Sample material — pick one, tap to copy' : esc(briefs[0].label) + ' — tap to copy') + '</div>' + tabs +
      '<div class="lw-briefs">' + briefs.map(function(b, i){ return '<pre class="lw-pre copyable" data-b="' + i + '"' + (i ? ' hidden' : '') + '>' + esc(b.text) + '</pre>'; }).join('') + '</div>' +
      '<div class="lw-hint2">Tap the box to copy the whole text.</div></div>';
  }
  function findVal(k){ var s = st(cur); return (s.findings && s.findings[k]) || ''; }
  function findingsBlock(findings, prefix){
    return '<div class="findings-k">✎ Record what you found</div><div class="findings">' + findings.map(function(f, i){
      var k = prefix + '_' + i, v = findVal(k);
      return '<label class="find"><span>' + esc(f.label) + '</span><input class="find-in' + (v ? ' filled' : '') + '" data-fk="' + k + '" placeholder="' + attr(f.hint || '') + '" value="' + attr(v) + '"></label>';
    }).join('') + '</div>';
  }
  function goalBlock(g){ return '<div class="goal"><div class="gk">Your goal — write a CTFT prompt for this</div>' + g + '</div>'; }
  function revealPrompt(p, label){
    return '<details class="reveal"><summary>🔓 Stuck? Reveal a suggested prompt</summary>' + promptBox(p, '', label) + '</details>';
  }
  function promptStepsBlock(steps, t){
    return steps.map(function(ps, si){
      return '<div class="pstep"><div class="pstep-h"><span class="pstep-n">' + (si + 1) + '</span>' + esc(ps.label) + '</div>' +
        (ps.goal ? goalBlock(ps.goal) : '') + (ps.prompt ? revealPrompt(ps.prompt, t.id + ' · ' + ps.label) : '') +
        (ps.findings ? findingsBlock(ps.findings, 's' + si) : '') + '</div>';
    }).join('');
  }
  function checkBlock(r){ return '<details class="check"><summary>✔ Check your findings</summary><div class="check-body">' + r + '</div></details>'; }

  /* ---- widgets ---- */
  var W = {};
  W.timeaudit = function(){
    var p = PROFILE.get(); var tasks = (p.tasks || []).slice(0, 3); while (tasks.length < 3) tasks.push({ text: '', tag: '', hours: '' });
    var tags = ['Generate', 'Condense', 'Find', 'Transform'];
    return '<div class="step-card"><div class="sc-k">Your time audit — saved in this browser</div>' +
      '<div class="ta-role"><span>Your track for the three days:</span>' + Object.keys(ROLES).map(function(k){ return '<button type="button" class="ta-r' + (role() === k ? ' on' : '') + '" data-r="' + k + '">' + ROLES[k] + '</button>'; }).join('') + '</div>' +
      tasks.map(function(x, i){
        return '<div class="ta-row"><span class="ta-n">' + (i + 1) + '</span><input class="ta-t" data-i="' + i + '" placeholder="A task that drains your week, e.g. writing the weekly sales update" value="' + attr(x.text) + '">' +
          '<select class="ta-tag" data-i="' + i + '"><option value="">What would AI do?</option>' + tags.map(function(g){ return '<option' + (x.tag === g ? ' selected' : '') + '>' + g + '</option>'; }).join('') + '</select>' +
          '<input class="ta-h" data-i="' + i + '" type="number" min="0" step="0.5" placeholder="hrs / wk" value="' + attr(x.hours) + '"></div>';
      }).join('') + '<div class="ta-sum" id="taSum"></div></div>';
  };
  W.builder = function(t){
    var F = [['role', 'Role (part of Context) — who should Copilot act as?'], ['ctx', 'Context — the situation, background, audience'], ['task', 'Task — what exactly should it produce?'],
      ['fmt', 'Format — length, structure, layout'], ['tone', 'Tone — the voice, plus any limits'], ['src', 'Source (optional) — which file? Type / in Copilot to add it'], ['ex', 'Example (optional) — a sample to imitate']];
    var s = st(cur).builder || {};
    return '<div class="step-card"><div class="sc-k">Prompt builder</div><div class="lw-fields">' +
      F.map(function(f){ return '<input class="bf" data-k="' + f[0] + '" placeholder="' + attr(f[1]) + '" value="' + attr(s[f[0]] || '') + '">'; }).join('') +
      '<div class="lw-row"><button type="button" class="lw-btn" id="bLoad">Load the example for my track</button><button type="button" class="lw-btn ghost" id="bCopy">Copy</button><button type="button" class="lw-btn ghost" id="bSave">＋ Save to Prompt Bank</button><span class="lw-hint" id="bHint"></span></div>' +
      '<div class="bprev" id="bPrev"><em>Your assembled prompt appears here as you type…</em></div>' +
      '<div class="blegend"><span><i style="background:var(--amber)"></i>Role</span><span><i style="background:var(--rose-lt)"></i>Context</span><span><i style="background:#fff"></i>Task</span><span><i style="background:var(--ac-cyan)"></i>Format</span><span><i style="background:var(--green-lt)"></i>Tone</span><span><i style="background:var(--blue)"></i>Source</span></div>' +
      '<a class="lw-test" href="https://copilot.cloud.microsoft/" target="_blank" rel="noopener">Test in Copilot Chat ↗</a></div></div>';
  };
  W.zth = function(t){
    var s = st(cur).zth || {};
    return '<div class="step-card"><div class="sc-k">Rate each round — 1 (mush) to 5 (sendable)</div>' +
      t.rounds.map(function(r, i){
        return '<div class="zr"><div class="zr-h"><span class="zr-n">R' + i + '</span><span class="zr-l">' + esc(r.label) + '</span>' +
          '<span class="zr-rate">' + [1, 2, 3, 4, 5].map(function(n){ return '<button type="button" class="zr-b' + (s[i] == n ? ' on' : '') + '" data-z="' + i + '" data-v="' + n + '">' + n + '</button>'; }).join('') + '</span></div>' +
          '<div class="prompt" data-copy="' + attr(r.text) + '"><span class="copy-tag">tap to copy</span>' + esc(r.text) + '</div></div>';
      }).join('') +
      '<div class="zr-all"><div class="sc-k" style="margin:4px 0 10px">The full Round 4 prompt, assembled</div>' + promptBox(t.rounds.slice(1).map(function(r){ return r.text; }).join(' '), '', t.id + ' · Catering apology (Round 4)') + '</div></div>';
  };
  W.hunt = function(t){
    var s = st(cur).hunt || {};
    return '<div class="step-card"><div class="sc-k">Tick each one you can find</div><div class="hunt">' + t.hunt.map(function(h, i){
      return '<label class="hunt-i' + (s[i] ? ' on' : '') + '"><input type="checkbox" data-h="' + i + '"' + (s[i] ? ' checked' : '') + '><span><b>' + esc(h.name) + '</b><small>' + h.where + '</small></span></label>';
    }).join('') + '</div></div>';
  };

  /* ---- render ---- */
  function render(){
    var t = variantOf(T[cur]); var s = st(cur);
    $('crumb').textContent = t.id + ' · ' + t.app;
    var roleTabs = t._roles ? '<div class="role-tabs"><span class="rt-k">Scenario for:</span>' + t._roles.map(function(k){ return '<button type="button" class="role-tab' + (k === t._role ? ' on' : '') + '" data-role="' + k + '">' + ROLES[k] + '</button>'; }).join('') +
      '<span class="rt-note">' + (role() ? 'Showing your track. Tap another to switch.' : 'Pick your track — the lab remembers it.') + '</span></div>' : '';
    var h = '';
    h += '<div class="task-tag"><span class="app">' + esc(t.app) + '</span> ' + esc(t.id) + (t.minutes ? ' · ' + esc(t.minutes) : '') + (t.optional ? ' · stretch' : '') + '</div>';
    h += '<h1 class="task-h">' + esc(t.title) + '</h1>' + roleTabs;
    h += '<p class="scn">' + t.scenario + '</p>';
    if (t.fallback) h += '<details class="fallback"><summary>No Copilot in this app?</summary><div>' + t.fallback + '</div></details>';
    if (t.dataset) h += datasetBlock(t.dataset);
    if (t.files) h += filesBlock(t.files);
    if (t.briefs) h += briefsBlock(t.briefs);
    if (t.launch) h += '<a class="launch-btn" href="' + attr(t.launch.href) + '"' + (t.launch.ext ? ' target="_blank" rel="noopener"' : '') + '><span><b>' + esc(t.launch.label) + '</b><span class="sub">' + (t.launch.note || '') + '</span></span><span class="ar">→</span></a>';
    if (t.launches) h += t.launches.map(function(l){ return '<a class="launch-btn" ' + (l.link ? 'data-link="' + l.link + '"' : 'href="' + attr(l.href) + '" target="_blank" rel="noopener"') + '><span><b>' + esc(l.label) + '</b><span class="sub"' + (l.link ? ' data-pending="Link coming soon — your trainer will share it in the room."' : '') + '>' + (l.note || '') + '</span></span><span class="ar">→</span></a>'; }).join('');
    if (t.ctftNote) h += '<div class="ctft-note"><b>Write the prompt yourself.</b> Use <b>CTFT — Context · Task · Format · Tone</b> for each goal below. Stuck? Tap “Reveal a suggested prompt”.</div>';
    if (t.steps) {
      h += '<div class="step-card"><div class="sc-k">Steps</div><ol>' + t.steps.map(function(x){ return '<li>' + x + '</li>'; }).join('') + '</ol>';
      if (t.goal) h += goalBlock(t.goal);
      if (t.prompt) h += (t.hidePrompt ? revealPrompt(t.prompt, t.id + ' · ' + t.title) : promptBox(t.prompt, '', t.id + ' · ' + t.title));
      if (t.prompts) h += t.prompts.map(function(p){ return promptBox(p.text, p.label, t.id + ' · ' + (p.label || t.title)); }).join('');
      if (t.findings) h += findingsBlock(t.findings, 'top');
      h += '</div>';
    }
    if (t.starters) h += '<div class="step-card"><div class="sc-k">Starter menu — tap any to copy</div><div class="lw-starters">' + t.starters.map(function(x){ return promptBox(x, '', t.id + ' · starter'); }).join('') + '</div></div>';
    if (t.promptSteps) h += promptStepsBlock(t.promptSteps, t);
    if (t.widget && W[t.widget]) h += W[t.widget](t);
    if (t.reveal) h += checkBlock(t.reveal);
    h += '<div class="expect"><div class="ex-k">Done looks like</div><p>' + t.expect + '</p></div>';
    if (t.stretch) h += '<div class="tier tier-2"><div class="sc-k">Tier 2 · Stretch — finished early?</div><p>' + t.stretch + '</p></div>';
    if (t.boss) h += '<div class="tier tier-3"><div class="sc-k">Tier 3 · Boss challenge</div><p>' + t.boss + '</p></div>';
    h += '<div class="capture"><label for="note">Paste your Copilot result — or a note on how it went</label>' +
      '<textarea id="note" placeholder="Optional. Saved in this browser so you can come back to it.">' + esc(s.note || '') + '</textarea>' +
      '<div class="cap-row"><button type="button" class="cap-btn" id="markDone">' + (s.done ? 'Done ✓' : 'Mark done') + '</button><span class="cap-done' + (s.done ? ' on' : '') + '" id="capDone">✓ Saved</span></div></div>';
    h += '<div class="task-foot"><button type="button" class="tf-btn" id="tfPrev"' + (cur === 0 ? ' disabled' : '') + '>‹ Previous</button><button type="button" class="tf-btn next" id="tfNext"' + (cur === T.length - 1 ? ' disabled' : '') + '>Next task ›</button></div>';
    var v = $('view'); v.innerHTML = h; v.scrollTop = 0; window.scrollTo(0, 0);
    if (window.applyConfig) applyConfig(v);
    wire(v, t);
    buildNav(); updateProg();
    if (history.replaceState) history.replaceState(null, '', '#' + T[cur].id);
  }

  function flash(el, cls, tagSel, txt){ el.classList.add(cls); var tg = tagSel ? el.querySelector(tagSel) : null, old = tg ? tg.textContent : '';
    if (tg) tg.textContent = txt; setTimeout(function(){ el.classList.remove(cls); if (tg) tg.textContent = old; }, 1500); }

  function wire(v, t){
    v.querySelectorAll('.prompt[data-copy]').forEach(function(p){ p.onclick = function(){ copyText(p.getAttribute('data-copy')).then(function(){ flash(p, 'copied', '.copy-tag', 'copied ✓'); }).catch(function(){}); }; });
    v.querySelectorAll('.pb-save').forEach(function(b){ b.onclick = function(){ var r = pbAdd(b.getAttribute('data-save'), { title: b.getAttribute('data-title'), app: t.app, day: L.day, role: role() }); if (r === 'ok' || r === 'dup') { b.textContent = '✓ In your Prompt Bank'; b.classList.add('saved'); } updateProg(); }; });
    v.querySelectorAll('.role-tab').forEach(function(b){ b.onclick = function(){ ROLE.set(b.getAttribute('data-role')); drawRoleChip(); render(); }; });
    // brief tabs + copy
    v.querySelectorAll('.lw-tab[data-bt]').forEach(function(tb){ tb.onclick = function(){ var i = tb.getAttribute('data-bt');
      v.querySelectorAll('.lw-tab[data-bt]').forEach(function(x){ x.classList.toggle('on', x === tb); });
      v.querySelectorAll('.lw-briefs [data-b]').forEach(function(el){ el.hidden = el.getAttribute('data-b') !== i; }); }; });
    v.querySelectorAll('.lw-pre.copyable').forEach(function(pre){ pre.onclick = function(){ copyText(pre.textContent).then(function(){ pre.classList.add('copied'); toast('Copied ✓'); setTimeout(function(){ pre.classList.remove('copied'); }, 1200); }).catch(function(){}); }; });
    // findings
    v.querySelectorAll('.find-in').forEach(function(inp){ inp.oninput = function(e){ var s = st(cur); s.findings = s.findings || {}; s.findings[e.target.getAttribute('data-fk')] = e.target.value; save(); e.target.classList.toggle('filled', !!e.target.value); }; });
    // time audit
    if (v.querySelector('.ta-row')) {
      var p = PROFILE.get(); p.tasks = p.tasks || [];
      var sync = function(){ var rows = []; v.querySelectorAll('.ta-row').forEach(function(r, i){ rows.push({ text: r.querySelector('.ta-t').value.trim(), tag: r.querySelector('.ta-tag').value, hours: r.querySelector('.ta-h').value }); });
        p.tasks = rows; p.role = role(); PROFILE.set(p);
        var hrs = rows.reduce(function(a, r){ return a + (parseFloat(r.hours) || 0); }, 0), filled = rows.filter(function(r){ return r.text; }).length;
        $('taSum').innerHTML = filled ? '<b>' + filled + '</b> task' + (filled > 1 ? 's' : '') + ' · about <b>' + hrs + ' hours</b> a week. Biggest one = your capstone candidate on Thursday.' : ''; };
      v.querySelectorAll('.ta-t,.ta-h').forEach(function(x){ x.oninput = sync; }); v.querySelectorAll('.ta-tag').forEach(function(x){ x.onchange = sync; });
      v.querySelectorAll('.ta-r').forEach(function(b){ b.onclick = function(){ ROLE.set(b.getAttribute('data-r')); v.querySelectorAll('.ta-r').forEach(function(x){ x.classList.toggle('on', x === b); }); drawRoleChip(); sync(); }; });
      sync();
    }
    // builder
    if (v.querySelector('.bf')) {
      var bPrev = $('bPrev'), cls = { role: 'sg-role', ctx: 'sg-ctx', task: 'sg-task', fmt: 'sg-fmt', tone: 'sg-tone', src: 'sg-src', ex: 'sg-ctx' };
      var vals = function(){ var o = {}; v.querySelectorAll('.bf').forEach(function(f){ o[f.getAttribute('data-k')] = f.value.trim(); }); return o; };
      var assembled = function(){ var o = vals(); return ['role', 'ctx', 'task', 'fmt', 'tone', 'src', 'ex'].filter(function(k){ return o[k]; }).map(function(k){ return k === 'ex' ? 'Match the structure and voice of this example: ' + o[k] : (k === 'src' ? 'Use ' + o[k] + ' as the source.' : o[k]); }).join(' '); };
      var draw = function(){ var o = vals(); var html = ['role', 'ctx', 'task', 'fmt', 'tone', 'src', 'ex'].filter(function(k){ return o[k]; }).map(function(k){ return '<span class="' + cls[k] + '">' + esc(k === 'ex' ? 'Match the structure and voice of this example: ' + o[k] : (k === 'src' ? 'Use ' + o[k] + ' as the source.' : o[k])) + '</span>'; }).join(' ');
        bPrev.innerHTML = html || '<em>Your assembled prompt appears here as you type…</em>'; var s = st(cur); s.builder = o; save(); };
      v.querySelectorAll('.bf').forEach(function(f){ f.oninput = draw; });
      $('bLoad').onclick = function(){ var ex = (t.examples || {})[role() || 'sales'] || (t.examples || {}).sales; if (!ex) return; v.querySelectorAll('.bf').forEach(function(f){ f.value = ex[f.getAttribute('data-k')] || ''; }); draw(); };
      $('bCopy').onclick = function(){ var a = assembled(); if (!a) return; copyText(a).then(function(){ $('bHint').textContent = 'copied ✓'; setTimeout(function(){ $('bHint').textContent = ''; }, 1500); }); };
      $('bSave').onclick = function(){ pbAdd(assembled(), { title: t.id + ' · My own prompt', app: 'Copilot Chat', day: L.day, role: role() }); updateProg(); };
      draw();
    }
    // zero to hero ratings
    v.querySelectorAll('.zr-b').forEach(function(b){ b.onclick = function(){ var s = st(cur); s.zth = s.zth || {}; s.zth[b.getAttribute('data-z')] = +b.getAttribute('data-v'); save();
      v.querySelectorAll('.zr-b[data-z="' + b.getAttribute('data-z') + '"]').forEach(function(x){ x.classList.toggle('on', x === b); }); }; });
    // feature hunt
    v.querySelectorAll('.hunt input').forEach(function(c){ c.onchange = function(){ var s = st(cur); s.hunt = s.hunt || {}; s.hunt[c.getAttribute('data-h')] = c.checked; save(); c.closest('.hunt-i').classList.toggle('on', c.checked); }; });
    // capture
    $('markDone').onclick = function(){ var s = st(cur); s.done = true; s.note = $('note').value; save(); $('capDone').classList.add('on'); $('markDone').textContent = 'Done ✓'; buildNav(); updateProg(); toast('Task marked done ✓'); };
    $('note').oninput = function(e){ var s = st(cur); s.note = e.target.value; save(); };
    var p1 = $('tfPrev'), n1 = $('tfNext');
    if (p1) p1.onclick = function(){ go(cur - 1); };
    if (n1) n1.onclick = function(){ go(cur + 1); };
  }

  function go(i){ if (i < 0 || i >= T.length) return; cur = i; render(); }
  window.labGo = go;
  $('mPrev').onclick = function(){ go(cur - 1); };
  $('mNext').onclick = function(){ go(cur + 1); };
  $('ham').onclick = function(){ $('rail').classList.toggle('open'); };
  $('resetBtn').onclick = function(){ if (confirm('Clear your notes and progress for this day? (Your Prompt Bank is kept.)')) { state = {}; save(); cur = 0; render(); } };
  var rs = $('roleSel'); if (rs) rs.onchange = function(){ if (rs.value) ROLE.set(rs.value); render(); };
  window.addEventListener('hashchange', function(){ var i = T.findIndex(function(t){ return '#' + t.id === location.hash; }); if (i >= 0 && i !== cur) go(i); });
  var start = T.findIndex(function(t){ return '#' + t.id === location.hash; });
  cur = start >= 0 ? start : 0;
  drawRoleChip(); render();
})();
