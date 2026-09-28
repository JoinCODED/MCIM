/* ===== CODED Copilot workshop — shared runtime (inlined into every page) =====
   config text + links + QR · clipboard · toast · role · Prompt Bank · profile */
(function(){
  var S = window.SITE || {};
  function get(path){ return String(path).split('.').reduce(function(o,k){ return o == null ? o : o[k]; }, S); }
  window.cfgGet = get;

  function applyConfig(root){
    root = root || document;
    root.querySelectorAll('[data-cfg]').forEach(function(el){
      var v = get(el.getAttribute('data-cfg')); if (v) el.textContent = v;
    });
    root.querySelectorAll('[data-link]').forEach(function(el){
      var v = get('links.' + el.getAttribute('data-link'));
      var lab = el.querySelector('[data-pending]');
      if (v) {
        el.setAttribute('href', v); el.setAttribute('target', '_blank'); el.setAttribute('rel', 'noopener');
        el.classList.remove('pending'); el.removeAttribute('aria-disabled');
      } else {
        el.classList.add('pending'); el.removeAttribute('href');
        el.setAttribute('aria-disabled', 'true'); el.setAttribute('title', 'Link coming soon');
        if (lab) lab.textContent = lab.getAttribute('data-pending');
      }
    });
    root.querySelectorAll('[data-linktext]').forEach(function(el){
      var v = get('links.' + el.getAttribute('data-linktext'));
      el.textContent = v ? v.replace(/^https?:\/\/(www\.)?/, '').replace(/\/$/, '') : 'Link coming soon';
    });
    root.querySelectorAll('[data-qr]').forEach(function(el){
      var v = get('links.' + el.getAttribute('data-qr'));
      if (v && window.qrcode) {
        try { var q = qrcode(0, 'M'); q.addData(v); q.make();
          el.innerHTML = q.createSvgTag({ cellSize: 4, margin: 2, scalable: true });
          el.classList.add('ready'); el.setAttribute('data-url', v);
        } catch (e) { el.innerHTML = '<span class="qr-soon">QR code<br>unavailable</span>'; }
      } else {
        el.classList.remove('ready');
        el.innerHTML = '<span class="qr-soon">QR code<br>coming soon</span>';
      }
    });
  }
  window.applyConfig = applyConfig;
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function(){ applyConfig(); });
  else applyConfig();

  /* ---- safe storage ---- */
  var store = {
    get: function(k, d){ try { var v = localStorage.getItem(k); return v == null ? d : JSON.parse(v); } catch (e) { return d; } },
    set: function(k, v){ try { localStorage.setItem(k, JSON.stringify(v)); return true; } catch (e) { return false; } }
  };
  window.store = store;

  /* ---- clipboard with fallback ---- */
  window.copyText = function(text){
    text = String(text || '');
    function fallback(){
      return new Promise(function(res, rej){
        try { var ta = document.createElement('textarea'); ta.value = text; ta.setAttribute('readonly', '');
          ta.style.position = 'fixed'; ta.style.opacity = '0'; document.body.appendChild(ta); ta.select();
          var ok = document.execCommand('copy'); document.body.removeChild(ta); ok ? res() : rej(); }
        catch (e) { rej(e); }
      });
    }
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(text).catch(fallback);
    return fallback();
  };

  /* ---- toast ---- */
  window.toast = function(msg){
    var t = document.getElementById('toast');
    if (!t) { t = document.createElement('div'); t.id = 'toast'; t.className = 'toast'; t.setAttribute('role', 'status'); document.body.appendChild(t); }
    t.textContent = msg; t.classList.add('on');
    clearTimeout(t._h); t._h = setTimeout(function(){ t.classList.remove('on'); }, 2200);
  };

  /* ---- role (the participant's track, remembered across all three days) ---- */
  var ROLES = { executive: 'Executive', sales: 'Sales', marketing: 'Marketing', technical: 'Technical' };
  window.ROLES = ROLES;
  window.ROLE = {
    get: function(){ var r = store.get('coded_copilot_role', ''); return ROLES[r] ? r : ''; },
    set: function(r){ if (ROLES[r]) store.set('coded_copilot_role', r); }
  };

  /* ---- Prompt Bank (one list, shared by every lab and the Prompt Bank page) ---- */
  var PBK = 'coded_copilot_prompt_bank';
  window.PB = {
    all: function(){ var a = store.get(PBK, []); return Array.isArray(a) ? a : []; },
    save: function(a){ return store.set(PBK, a); },
    add: function(text, meta){
      text = String(text || '').trim(); meta = meta || {};
      if (!text) return 'empty';
      var a = this.all();
      if (a.some(function(x){ return x.text === text; })) return 'dup';
      a.unshift({ id: Date.now().toString(36) + Math.random().toString(36).slice(2, 6), text: text,
        title: meta.title || '', app: meta.app || '', day: meta.day || '', role: meta.role || (window.ROLE ? ROLE.get() : ''),
        ts: new Date().toISOString() });
      return this.save(a) ? 'ok' : 'fail';
    },
    remove: function(id){ this.save(this.all().filter(function(x){ return x.id !== id; })); },
    update: function(id, patch){ this.save(this.all().map(function(x){ return x.id === id ? Object.assign({}, x, patch) : x; })); }
  };
  window.pbAdd = function(text, meta){
    var r = PB.add(text, meta);
    toast(r === 'ok' ? 'Saved to your Prompt Bank ✓' : r === 'dup' ? 'Already in your Prompt Bank' :
          r === 'empty' ? 'Nothing to save yet' : 'Could not save — your browser blocked storage');
    return r;
  };

  /* ---- profile (Day 1 time audit → Day 3 capstone) ---- */
  window.PROFILE = {
    get: function(){ return store.get('coded_copilot_profile', { tasks: [] }); },
    set: function(p){ return store.set('coded_copilot_profile', p); }
  };
})();
