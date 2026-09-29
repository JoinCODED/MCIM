/* ===== DECK ENGINE — CODED SPECIMEN deck =====
   content shows on arrival · → ← / PageUp PageDown / Space · F fullscreen · #slide-id deep links
   ☕ break timer · countdown timers · all slide widgets are opt-in by markup */
(function(){
  var slides = [].slice.call(document.querySelectorAll('.slide'));
  if (!slides.length) return;
  var cur = 0;
  var $ = function(id){ return document.getElementById(id); };

  function reveal(s){ [].slice.call(s.querySelectorAll('.b')).forEach(function(el, i){ setTimeout(function(){ el.classList.add('in'); }, 60 * i); }); }
  function fx(s){
    [].slice.call(s.querySelectorAll('.g-fill')).forEach(function(g){ g.style.width = '0%'; var v = g.getAttribute('data-fill') || 0; setTimeout(function(){ g.style.width = v + '%'; }, 260); });
    [].slice.call(s.querySelectorAll('[data-n]')).forEach(function(c){
      var target = +c.getAttribute('data-n'), t0 = null;
      function step(ts){ if (!t0) t0 = ts; var p = Math.min(1, (ts - t0) / 900); c.textContent = Math.round(target * (.1 + .9 * p * p)); if (p < 1) requestAnimationFrame(step); else c.textContent = target; }
      requestAnimationFrame(step);
    });
    if (s.querySelector('#acStem')) acStart(acIdx);
    if (s.querySelector('#predLine')) predReset();
  }
  function show(n, fromHash){
    if (n < 0 || n >= slides.length) return;
    slides[cur].classList.remove('active');
    cur = n;
    var s = slides[cur]; s.classList.add('active'); s.scrollTop = 0;
    [].slice.call(s.querySelectorAll('.b')).forEach(function(el){ el.classList.remove('in'); });
    reveal(s); fx(s);
    $('prog').textContent = (cur + 1) + ' / ' + slides.length;
    $('ptFill').style.width = (cur / Math.max(1, slides.length - 1) * 100) + '%';
    if (!fromHash && s.id && history.replaceState) history.replaceState(null, '', '#' + s.id);
  }
  window.deckShow = show;
  $('nextBtn').onclick = function(){ show(cur + 1); };
  $('prevBtn').onclick = function(){ show(cur - 1); };
  document.addEventListener('keydown', function(e){
    var tag = (e.target.tagName || '').toLowerCase();
    if (tag === 'input' || tag === 'textarea' || e.target.isContentEditable) return;
    if (document.querySelector('.break-pick.on')) return;
    if (e.key === 'ArrowRight' || e.key === 'PageDown' || e.key === ' ') { e.preventDefault(); show(cur + 1); }
    else if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); show(cur - 1); }
    else if (e.key === 'Home') show(0);
    else if (e.key === 'End') show(slides.length - 1);
    else if (e.key.toLowerCase() === 'f') { if (!document.fullscreenElement) { if (document.documentElement.requestFullscreen) document.documentElement.requestFullscreen(); } else document.exitFullscreen(); }
  });
  // clickable road rows / any [data-goto]
  [].slice.call(document.querySelectorAll('[data-goto]')).forEach(function(r){
    r.addEventListener('click', function(){ var i = slides.findIndex(function(s){ return s.id === r.getAttribute('data-goto'); }); if (i >= 0) show(i); });
  });
  // tap-to-copy every prompt
  [].slice.call(document.querySelectorAll('.prompt')).forEach(function(p){
    p.addEventListener('click', function(){ copyText(p.textContent.trim()).then(function(){ p.classList.add('copied'); setTimeout(function(){ p.classList.remove('copied'); }, 1400); }).catch(function(){}); });
  });

  /* ---- poll (toggle) ---- */
  [].slice.call(document.querySelectorAll('.poll button')).forEach(function(b){ b.onclick = function(){ b.classList.toggle('sel'); }; });

  /* ---- vote grid (counts) ---- */
  [].slice.call(document.querySelectorAll('.vote-opt')).forEach(function(b){
    b.onclick = function(){ var c = b.querySelector('.vc'); c.textContent = (+c.textContent || 0) + 1; b.classList.add('hit'); setTimeout(function(){ b.classList.remove('hit'); }, 250); };
    b.oncontextmenu = function(e){ e.preventDefault(); var c = b.querySelector('.vc'); c.textContent = Math.max(0, (+c.textContent || 0) - 1); };
  });

  /* ---- task wall ---- */
  var wallEl = $('wall');
  if (wallEl) {
    var pinTask = function(){
      var inp = $('wallInput'); var v = inp.value.trim(); if (!v) return;
      var c = document.createElement('span'); c.className = 'wchip';
      c.style.setProperty('--tilt', ((Math.random() * 6) - 3).toFixed(1) + 'deg');
      c.textContent = v; c.title = 'tap to remove'; c.onclick = function(){ c.remove(); };
      wallEl.appendChild(c); inp.value = ''; inp.focus();
    };
    $('wallBtn').onclick = pinTask;
    $('wallInput').addEventListener('keydown', function(e){ if (e.key === 'Enter') pinTask(); });
  }

  /* ---- countdown timers: <div class="mini-timer" data-min="30"> ---- */
  function fmt(s){ s = Math.max(0, s); return String(Math.floor(s / 60)).padStart(2, '0') + ':' + String(s % 60).padStart(2, '0'); }
  function hhmm(d){ var h = d.getHours(), m = String(d.getMinutes()).padStart(2, '0'); return (h % 12 || 12) + ':' + m + (h < 12 ? ' AM' : ' PM'); }
  [].slice.call(document.querySelectorAll('.mini-timer[data-min]')).forEach(function(w){
    var total = (+w.getAttribute('data-min')) * 60, remain = total, h = null;
    var tEl = w.querySelector('.mt-time'), fEl = w.querySelector('.mt-fill'), start = w.querySelector('.mt-start'), back = w.querySelector('.mt-back');
    var label = start ? start.textContent : '', idle = back ? back.textContent : '';
    function draw(){
      tEl.textContent = fmt(remain); fEl.style.width = Math.max(0, Math.min(100, remain / total * 100)) + '%'; w.classList.toggle('done', remain <= 0);
      if (back) back.textContent = remain <= 0 ? 'Time\'s up — welcome back' : (h ? 'Back at ' + hhmm(new Date(Date.now() + remain * 1000)) : idle);
    }
    if (start) start.onclick = function(){
      if (h) { clearInterval(h); h = null; start.textContent = 'Resume'; draw(); return; }
      if (remain <= 0) return;
      start.textContent = 'Pause';
      h = setInterval(function(){ remain--; if (remain <= 0) { clearInterval(h); h = null; start.textContent = label; } draw(); }, 1000);
      draw();
    };
    // adjust buttons: [data-d]="-5" / "1" (minutes). Plain .mt-plus without data-d adds 2 minutes.
    [].slice.call(w.querySelectorAll('[data-d], .mt-plus')).forEach(function(b){
      b.onclick = function(){
        var d = b.hasAttribute('data-d') ? +b.getAttribute('data-d') : 2;
        remain = Math.max(0, remain + d * 60); if (remain > total) total = remain; draw();
      };
    });
    var rst = w.querySelector('.mt-reset'); if (rst) rst.onclick = function(){ clearInterval(h); h = null; total = (+w.getAttribute('data-min')) * 60; remain = total; if (start) start.textContent = label; draw(); };
    draw();
  });

  /* ---- human autocomplete ---- */
  var AC = window.DECK_AC || [], acIdx = 0, acT1 = null, acT2 = null;
  function acStart(i){
    clearInterval(acT1); clearTimeout(acT2);
    var stemEl = $('acStem'), sg = $('acSugg'); if (!stemEl || !AC.length) return;
    stemEl.textContent = ''; sg.innerHTML = '';
    var txt = AC[i].stem, p = 0;
    acT1 = setInterval(function(){
      stemEl.textContent = txt.slice(0, ++p);
      if (p >= txt.length) { clearInterval(acT1);
        acT2 = setTimeout(function(){ AC[i].sugg.forEach(function(s, k){
          var el = document.createElement('span'); el.innerHTML = '<b>' + s[0] + '</b><span class="pct">' + s[1] + '</span>';
          sg.appendChild(el); setTimeout(function(){ el.classList.add('show'); }, 140 * k);
        }); }, 350); }
    }, 26);
  }
  if ($('acNext')) $('acNext').onclick = function(){ acIdx = (acIdx + 1) % AC.length; acStart(acIdx); };

  /* ---- next-token predictor ---- */
  var PRED = window.DECK_PRED || [], predI = 0;
  var predLine = $('predLine'), predCands = $('predCands'), predBtn = $('predBtn');
  function predReset(){ predI = 0; if (predLine) { predLine.innerHTML = '<span style="color:var(--ink-faint)">▸ watch it build an answer…</span>'; predCands.innerHTML = ''; predBtn.textContent = 'Predict the next piece'; } }
  if (predBtn) predBtn.onclick = function(){
    if (predI >= PRED.length) { predReset(); return; }
    if (predI === 0) predLine.innerHTML = '';
    var st = PRED[predI]; predCands.innerHTML = '';
    st.c.forEach(function(cd, k){ var el = document.createElement('span'); if (k === 0) el.className = 'top'; el.textContent = cd[0] + ' · ' + cd[1]; el.style.animationDelay = (k * .08) + 's'; predCands.appendChild(el); });
    setTimeout(function(){
      var w = document.createElement('span'); w.className = 'pw'; w.textContent = st.pick; predLine.appendChild(w);
      predI++; if (predI >= PRED.length) { predBtn.textContent = 'Run it again ↺'; predCands.innerHTML = ''; }
    }, 650);
  };

  /* ---- QR expand (SVG holders filled by common.js) ---- */
  (function(){
    var ov = $('qrOv'); if (!ov) return; var box = ov.querySelector('.qr-big'), cap = ov.querySelector('.qr-ov-cap');
    [].slice.call(document.querySelectorAll('.qr')).forEach(function(q){
      q.addEventListener('click', function(e){ if (!q.classList.contains('ready')) return; e.stopPropagation(); box.innerHTML = q.innerHTML; cap.textContent = (q.getAttribute('data-url') || '').replace(/^https?:\/\//, '') + ' · tap anywhere to close'; ov.classList.add('on'); });
    });
    ov.addEventListener('click', function(){ ov.classList.remove('on'); });
    document.addEventListener('keydown', function(e){ if (e.key === 'Escape') ov.classList.remove('on'); });
  })();

  /* ---- generic reveal buttons: <button data-reveal="id"> toggles .draw/.open on target ---- */
  [].slice.call(document.querySelectorAll('[data-reveal]')).forEach(function(b){
    b.onclick = function(){ var t = $(b.getAttribute('data-reveal')); if (t) { t.classList.add('draw'); t.classList.add('open'); } };
  });

  /* ---- flip tiles ---- */
  [].slice.call(document.querySelectorAll('.flip')).forEach(function(f){ f.onclick = function(){ f.classList.toggle('flipped'); }; });

  /* ---- step-through diagrams: <div class="stepper"> with .st-step children + .st-next ---- */
  [].slice.call(document.querySelectorAll('.stepper')).forEach(function(w){
    var steps = [].slice.call(w.querySelectorAll('.st-step')), i = -1, btn = w.querySelector('.st-next'), note = w.querySelector('.st-note');
    function draw(){ steps.forEach(function(s, k){ s.classList.toggle('on', k === i); s.classList.toggle('past', k < i); });
      if (note) note.textContent = i >= 0 ? (steps[i].getAttribute('data-note') || '') : (note.getAttribute('data-idle') || '');
      if (btn) btn.textContent = i >= steps.length - 1 ? 'Run it again ↺' : (i < 0 ? 'Press Enter ▸' : 'Next step ▸'); }
    if (btn) btn.onclick = function(){ i = i >= steps.length - 1 ? -1 : i + 1; draw(); };
    steps.forEach(function(s, k){ s.onclick = function(){ i = k; draw(); }; });
    draw();
  });

  /* ---- word doc mock ---- */
  [].slice.call(document.querySelectorAll('.dm-btn')).forEach(function(b){
    b.onclick = function(){ [].slice.call(document.querySelectorAll('.dm-btn')).forEach(function(x){ x.classList.remove('on'); }); b.classList.add('on'); $('dmPage').setAttribute('data-st', b.getAttribute('data-st')); };
  });

  /* ---- inbox collapse ---- */
  if ($('inboxBtn')) { $('inboxBtn').onclick = function(){ $('inboxW').classList.add('collapsed'); }; $('inboxReset').onclick = function(){ $('inboxW').classList.remove('collapsed'); }; }

  /* ---- tone dial ---- */
  var TONES = window.DECK_TONES || {};
  [].slice.call(document.querySelectorAll('#toneDial button')).forEach(function(b){
    b.onclick = function(){
      [].slice.call(document.querySelectorAll('#toneDial button')).forEach(function(x){ x.classList.remove('on'); }); b.classList.add('on');
      var tc = $('toneText'); tc.classList.add('fade');
      setTimeout(function(){ tc.textContent = TONES[b.getAttribute('data-t')] || ''; tc.classList.remove('fade'); }, 240);
    };
  });

  /* ---- init ---- */
  var start = 0;
  if (location.hash) { var i = slides.findIndex(function(s){ return '#' + s.id === location.hash; }); if (i >= 0) start = i; }
  slides.forEach(function(s){ s.classList.remove('active'); });
  slides[start].classList.add('active'); cur = start;
  $('prog').textContent = (cur + 1) + ' / ' + slides.length;
  $('ptFill').style.width = (cur / Math.max(1, slides.length - 1) * 100) + '%';
  reveal(slides[cur]); fx(slides[cur]);

  /* ---- ☕ break timer ---- */
  var pick = $('breakPick'), ov = $('breakOv'), timer = null, remain = 0;
  function tick(){ remain--; $('brkTime').textContent = fmt(remain); if (remain <= 0) { clearInterval(timer); $('brkTime').textContent = '00:00'; ov.classList.add('over'); } }
  function startBreak(min){
    remain = min * 60; $('brkTime').textContent = fmt(remain); ov.classList.remove('over');
    var back = new Date(Date.now() + remain * 1000);
    $('brkBack').textContent = 'Back at ' + String(back.getHours()).padStart(2, '0') + ':' + String(back.getMinutes()).padStart(2, '0');
    pick.classList.remove('on'); ov.classList.add('on'); clearInterval(timer); timer = setInterval(tick, 1000);
  }
  $('brkBtn').onclick = function(){ pick.classList.add('on'); };
  $('bpClose').onclick = function(){ pick.classList.remove('on'); };
  [].slice.call(document.querySelectorAll('.bp-opt')).forEach(function(b){ b.onclick = function(){ startBreak(+b.getAttribute('data-min')); }; });
  $('brkPlus').onclick = function(){ remain += 300; $('brkTime').textContent = fmt(remain); ov.classList.remove('over');
    var back = new Date(Date.now() + remain * 1000); $('brkBack').textContent = 'Back at ' + String(back.getHours()).padStart(2, '0') + ':' + String(back.getMinutes()).padStart(2, '0'); };
  $('brkEnd').onclick = function(){ clearInterval(timer); ov.classList.remove('on'); };
})();
