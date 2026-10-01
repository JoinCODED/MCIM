/* ===== Prompt Bank → Word (.docx), built in the browser — no library, no upload =====
   window.bankDocx(prompts, opts) returns a Blob.  prompts: [{title,text,day,app,role}]  opts: {roles:{key:label}, course, dateText} */
(function(){
  /* ---- tiny zip writer (stored, no compression) ---- */
  var CRC = (function(){ var t = [], c; for (var n = 0; n < 256; n++) { c = n; for (var k = 0; k < 8; k++) c = c & 1 ? 0xEDB88320 ^ (c >>> 1) : c >>> 1; t[n] = c >>> 0; } return t; })();
  function crc32(b){ var c = 0xFFFFFFFF; for (var i = 0; i < b.length; i++) c = CRC[(c ^ b[i]) & 0xFF] ^ (c >>> 8); return (c ^ 0xFFFFFFFF) >>> 0; }
  function u16(v){ return [v & 255, (v >>> 8) & 255]; }
  function u32(v){ return [v & 255, (v >>> 8) & 255, (v >>> 16) & 255, (v >>> 24) & 255]; }
  function zip(files){
    var enc = new TextEncoder(), parts = [], central = [], off = 0;
    var now = new Date(), dt = (now.getHours() << 11) | (now.getMinutes() << 5) | (now.getSeconds() >> 1),
        dd = ((now.getFullYear() - 1980) << 9) | ((now.getMonth() + 1) << 5) | now.getDate();
    files.forEach(function(f){
      var name = enc.encode(f.name), data = enc.encode(f.data), crc = crc32(data);
      var head = [].concat([0x50,0x4B,0x03,0x04], u16(20), u16(0x0800), u16(0), u16(dt), u16(dd), u32(crc), u32(data.length), u32(data.length), u16(name.length), u16(0));
      parts.push(new Uint8Array(head), name, data);
      central.push(new Uint8Array([].concat([0x50,0x4B,0x01,0x02], u16(20), u16(20), u16(0x0800), u16(0), u16(dt), u16(dd), u32(crc), u32(data.length), u32(data.length), u16(name.length), u16(0), u16(0), u16(0), u16(0), u32(0), u32(off))), name);
      off += head.length + name.length + data.length;
    });
    var csize = central.reduce(function(a, p){ return a + p.length; }, 0);
    var end = new Uint8Array([].concat([0x50,0x4B,0x05,0x06], u16(0), u16(0), u16(files.length), u16(files.length), u32(csize), u32(off), u16(0)));
    return new Blob(parts.concat(central, [end]), { type: 'application/vnd.openxmlformats-officedocument.wordprocessingml.document' });
  }

  /* ---- WordprocessingML ---- */
  function x(s){ return String(s == null ? '' : s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;'); }
  function runs(text, rpr){
    return String(text).split('\n').map(function(line, i){ return (i ? '<w:r><w:br/></w:r>' : '') + '<w:r>' + (rpr || '') + '<w:t xml:space="preserve">' + x(line) + '</w:t></w:r>'; }).join('');
  }
  function p(text, style, rpr){ return '<w:p>' + (style ? '<w:pPr><w:pStyle w:val="' + style + '"/></w:pPr>' : '') + runs(text, rpr) + '</w:p>'; }
  function lead(b, rest){ return '<w:p><w:r><w:rPr><w:b/></w:rPr><w:t xml:space="preserve">' + x(b) + '</w:t></w:r>' + runs(rest) + '</w:p>'; }

  var STYLES = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
  '<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">' +
  '<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri" w:eastAsia="Calibri"/><w:sz w:val="22"/><w:szCs w:val="22"/><w:lang w:val="en-GB"/></w:rPr></w:rPrDefault>' +
  '<w:pPrDefault><w:pPr><w:spacing w:after="120" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>' +
  '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>' +
  '<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:after="60"/></w:pPr><w:rPr><w:b/><w:color w:val="0B1F3A"/><w:sz w:val="48"/><w:szCs w:val="48"/></w:rPr></w:style>' +
  '<w:style w:type="paragraph" w:styleId="Subtitle"><w:name w:val="Subtitle"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:after="240"/></w:pPr><w:rPr><w:color w:val="595959"/><w:sz w:val="20"/></w:rPr></w:style>' +
  '<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="360" w:after="120"/><w:outlineLvl w:val="0"/></w:pPr><w:rPr><w:b/><w:color w:val="004AA3"/><w:sz w:val="32"/><w:szCs w:val="32"/></w:rPr></w:style>' +
  '<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="240" w:after="40"/><w:outlineLvl w:val="1"/></w:pPr><w:rPr><w:b/><w:color w:val="0B1F3A"/><w:sz w:val="26"/><w:szCs w:val="26"/></w:rPr></w:style>' +
  '<w:style w:type="paragraph" w:customStyle="1" w:styleId="PromptMeta"><w:name w:val="Prompt meta"/><w:basedOn w:val="Normal"/><w:pPr><w:keepNext/><w:spacing w:after="60"/></w:pPr><w:rPr><w:color w:val="6B7280"/><w:sz w:val="18"/></w:rPr></w:style>' +
  '<w:style w:type="paragraph" w:customStyle="1" w:styleId="PromptText"><w:name w:val="Prompt text"/><w:basedOn w:val="Normal"/><w:pPr><w:pBdr><w:left w:val="single" w:sz="18" w:space="8" w:color="2F74D6"/></w:pBdr><w:shd w:val="clear" w:color="auto" w:fill="EEF3FB"/><w:spacing w:before="60" w:after="200"/><w:ind w:left="200" w:right="120"/></w:pPr></w:style>' +
  '</w:styles>';

  window.bankDocx = function(prompts, opts){
    opts = opts || {};
    var roles = opts.roles || {}, b = '';
    b += p('My Copilot Prompt Bank', 'Title');
    b += p((opts.course || 'Mastering Copilot in Microsoft 365 · CODED') + ' · saved ' + (opts.dateText || new Date().toDateString()), 'Subtitle');
    b += p('How to use this document', 'Heading1');
    b += lead('1. Save it to your OneDrive. ', 'Then it is yours after the workshop — on any device.');
    b += lead('2. Use it in Copilot. ', 'Type / in Copilot and pick this file. For example: “Use the prompt called Weekly sales update from /my-copilot-prompt-bank, on the file I attached.”');
    b += lead('3. Keep adding. ', 'When a prompt works, paste it under the right heading. Note what you changed and why.');
    b += lead('4. Keep it safe. ', 'Prompts only — no customer names, Civil IDs, salaries, passwords or keys.');

    var groups = [], seen = {};
    (prompts || []).forEach(function(q){ var g = q.day || 'Added by hand'; if (!seen[g]) { seen[g] = []; groups.push(g); } seen[g].push(q); });
    groups.sort(function(a, c){ var o = function(s){ var m = /Day (\d)/.exec(s); return m ? +m[1] : 9; }; return o(a) - o(c); });
    if (!groups.length) {
      b += p('My prompts', 'Heading1');
      b += p('Example · Weekly update for my manager', 'Heading2');
      b += p('Example · Copilot Chat', 'PromptMeta');
      b += p('I lead the wholesale team at a food company in Kuwait. Summarise my emails since Sunday and list the actions I must take. A table: action, who asked, deadline — urgent first. Short and plain.', 'PromptText');
    }
    groups.forEach(function(g){
      b += p(g, 'Heading1');
      seen[g].forEach(function(q){
        b += p(q.title || 'My prompt', 'Heading2');
        var meta = [q.app, q.role ? (roles[q.role] || q.role) : ''].filter(Boolean).join(' · ');
        if (meta) b += p(meta, 'PromptMeta');
        b += p(q.text || '', 'PromptText');
      });
    });
    b += p('New prompt — copy this block', 'Heading1');
    b += p('Title:', 'Heading2');
    b += p('Context: who I am, the situation, the audience\nTask: exactly what Copilot should produce\nFormat: length, structure, layout\nTone: the voice, plus any limits\nSource (optional): which file — type / in Copilot', 'PromptText');

    var doc = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>' +
      '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main" xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"><w:body>' + b +
      '<w:sectPr><w:pgSz w:w="11906" w:h="16838"/><w:pgMar w:top="1134" w:right="1134" w:bottom="1134" w:left="1134" w:header="567" w:footer="567" w:gutter="0"/></w:sectPr></w:body></w:document>';
    return zip([
      { name: '[Content_Types].xml', data: '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types"><Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/><Default Extension="xml" ContentType="application/xml"/><Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/><Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/></Types>' },
      { name: '_rels/.rels', data: '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/></Relationships>' },
      { name: 'word/_rels/document.xml.rels', data: '<?xml version="1.0" encoding="UTF-8" standalone="yes"?><Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"><Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/></Relationships>' },
      { name: 'word/document.xml', data: doc },
      { name: 'word/styles.xml', data: STYLES }
    ]);
  };
})();
