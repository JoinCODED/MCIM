# Copilot cheat sheet — three-of-a-kind cards (analogy + one line + the tell)
SECTIONS = [
 ('The prompt recipe', [
  ('rose', 'CTFT', 'context · task · format · tone', 'Like a recipe card — four ingredients, one dish.',
   'Context (the situation, any role for Copilot) · Task (what to do) · Format (length, structure) · Tone (the voice). You rarely need all four.',
   'Regular customer, catering 45 min late, our mistake → apology email → under 120 words + a number to call → warm, no refund promised.',
   'The tell: a weak answer = a missing ingredient. Find it, add it, run it again.'),
  ('cyan', 'Iterate', 'the first answer is a first draft', 'Like a tailor\'s first fitting — pins, not the final suit.',
   'Talk back to the draft instead of rewriting it by hand: shorter, warmer, as a table, for your manager, in Arabic.',
   '“Make it 20% shorter and a little more formal.”',
   'The tell: you steer with follow-ups — you don\'t start again.'),
  ('amber', 'Source', 'the “which” — type /', 'Like handing the intern the right folder.',
   'Point Copilot at a file, email or meeting (type /), or upload a file. Microsoft\'s four parts: Goal · Context · Source · Expectations.',
   '“Summarise /Tamra supplier notice in five points for the sales team.”',
   'The tell: a grounded answer quotes your file, not the internet.'),
 ], 'Context · Task · Format · Tone — plus a Source when you have one. A wrong result tells you which ingredient is missing.'),
 ('Write and reply', [
  ('rose', 'Copilot Chat', 'ask · draft · summarise', 'Like a sharp new colleague on call.',
   'The chat app at copilot.cloud.microsoft. It answers from the web, your files, emails and meetings.',
   '“Using only the attached file, list the three biggest risks.”',
   'The tell: say where the answer should come from — web, a file, or your work.'),
  ('cyan', 'Word', 'draft · rewrite · ground', 'Like a sous-chef — it chops, you plate.',
   'Draft from notes, rewrite the tone or length, summarise a long document — and refer to a file so the draft follows real content.',
   '“Draft a proposal letter from these notes…” → “Rewrite it in the voice of /house-style-letter.”',
   'The tell: iterate, don\'t hand-edit — then check every fact against your notes.'),
  ('amber', 'Outlook & Teams', 'summarise · draft · recap', 'Like the colleague who takes perfect minutes.',
   'Summarise the messy thread and draft the reply in your tone. In Teams, recap a meeting into decisions, actions and owners (transcript on).',
   '“Summarise this thread — what\'s promised, what\'s still open? Draft a warm reply under 120 words.”',
   'The tell: separate promised from still open before you reply.'),
 ], 'Chat asks, Word drafts, Outlook replies — one recipe steering all three.'),
 ('Show and analyse', [
  ('rose', 'PowerPoint', 'create · generate · restructure', 'Like a designer who already read the report.',
   'Create a deck from a Word file (PDF with Premium), add slides from a prompt, and reorder, merge and trim a messy deck.',
   '“Create a 6-slide board summary from /H1 review. Keep every figure traceable. Add speaker notes.”',
   'The tell: polish is not proof — check two slides against the source.'),
  ('cyan', 'Excel', 'analyse · add · visualise', 'Like an analyst who shows the working.',
   'Clean data first: one header row, no merged cells, Format as Table (Ctrl+T). Then ask questions, add formula columns, build charts.',
   '“Add an Operating margin column: (Revenue − Cost of sales − Operating costs) ÷ Revenue. Show me the formula.”',
   'The tell: open the formula. If you can\'t read the working, you can\'t trust the answer.'),
  ('amber', 'Prompt Gallery', 'find · adapt · save', 'Like a recipe book — you still season to taste.',
   'Ready-made prompts in Copilot (the … menu) or at adoption.microsoft.com/copilot/prompt-gallery. Save to Your prompts; share with a team.',
   'Gallery prompt + your context, format and tone = your prompt.',
   'The tell: never copy as-is — adapt with CTFT.'),
 ], 'PowerPoint presents, Excel answers, the Gallery gives you a head start — and you check all three.'),
 ('Safe, always', [
  ('rose', 'Strip before you paste', 'nothing sensitive in a prompt', 'Like talking in a lift — assume others can hear.',
   'No raw personal data (Civil ID, phone, card), no passwords or keys, no HR or medical records. Use placeholders: Customer A.',
   '“Analyse Customer A\'s last 10 orders” — not their name and Civil ID.',
   'The tell: pause before paste.'),
  ('cyan', 'The boundary', 'work account · your permissions', 'Like an intern with a badge — only the doors you can open.',
   'On a work account, prompts get enterprise data protection and don\'t train the models. Copilot sees only what you can see. Web search sends a short query to Bing.',
   'Work data → work account. Never a personal chatbot.',
   'The tell: same kind of engine as public AI — very different walls.'),
  ('amber', 'You\'re accountable', 'fluent ≠ correct', 'Like a maker-checker — nothing goes out unchecked.',
   'Copilot drafts; people decide. Check numbers and facts, watch for bias, and say when AI helped. Microsoft\'s six principles: fairness, reliability & safety, privacy & security, inclusiveness, transparency, accountability.',
   '“Show me the exact sentence in the file where this number comes from.”',
   'The tell: you sign it, you own it.'),
 ], 'Strip it, keep it inside the walls, check it — that\'s responsible use.'),
]


def build():
    parts = []
    for title, items, summary in SECTIONS:
        cards = ''.join(f'''<div class="item {c}"><div class="nm">{esc(nm)}</div><div class="st">{esc(st)}</div><div class="an">{esc(an)}</div>
<div class="df">{esc(df)}</div><div class="ex">{esc(ex)}</div><div class="tl">{esc(tl)}</div></div>''' for c, nm, st, an, df, ex, tl in items)
        parts.append(f'<div class="sec-label">{esc(title)}</div><div class="grid3">{cards}</div><p class="summary">{esc(summary)}</p>')
    body = topbar('Copilot <b>Cheat Sheet</b>') + f'''
<div class="wrap">
  <span class="eyebrow">Quick Reference</span>
  <h1>Microsoft Copilot — the moves that matter.</h1>
  <p class="intro">Everything from the three days, on one page. Each card: what it is, the everyday thing it's like, and the one tell that makes it click. Keep it open while you work.</p>
  {''.join(parts)}
</div>
''' + footer_row()
    return page('Cheat Sheet — ' + TITLE + ' · CODED', body, css=SUB_CSS, desc='Copilot cheat sheet: CTFT, the apps, the Prompt Gallery and safe use — one page.')
