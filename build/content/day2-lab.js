(function(){
var WORD_STEPS = [
  'Copy your notes (tap the box below). In Word, open a <b>new blank document</b> and select <b>Copilot</b> (or <b>Draft with Copilot</b>).',
  '<b>Draft:</b> write your prompt for goal 1 and paste your notes after it. Read the result once. Don\'t fix anything by hand yet.',
  '<b>Rewrite:</b> write your prompt for goal 2. Steer it — don\'t retype.',
  '<b>Ground:</b> save your grounding file (below) to your OneDrive. Write your prompt for goal 3 and pick the file after you type <kbd>/</kbd>. No file option? Upload or paste the file\'s text instead.',
  '<b>Check:</b> compare the final version with your notes. Anything missing? Anything invented? Fix it by hand — then save your best prompt.'
];
var WORD_FALLBACK = 'Open Copilot Chat. Paste your notes and write your prompts for the same goals. For goal 3, upload the grounding file with <b>+</b> → <b>Upload</b>. Copy the final text into Word.';
var PPT_STEPS = [
  'Download your source file (below) and save it to your <b>OneDrive</b>.',
  'In PowerPoint, open a <b>blank presentation</b>. Select <b>Copilot</b> → <b>Create a presentation from a file</b> — or type <kbd>/</kbd> in the Copilot box and pick your file. Write your prompt for goal 1.',
  '<b>Generate:</b> write your prompt for goal 2 to add one new slide.',
  '<b>Check:</b> open two slides. Check every number against the source file. Then fix one slide by hand — feel where Copilot stops and you start.'
];
var PPT_FALLBACK = 'Upload the file to Copilot Chat and run: <i>“Turn this document into a slide-by-slide outline: a title, three bullets and speaker notes for each slide.”</i> Build the slides in PowerPoint from the outline.';
var XL_STEPS = [
  'Download your workbook. Open it in Excel (desktop or web) and click anywhere inside the table.',
  '<b>Check the data first:</b> one header row, no merged cells, no blank rows or columns. Not a table yet? Click inside the data and press <kbd>Ctrl</kbd>+<kbd>T</kbd> (Format as Table).',
  'Open <b>Copilot</b>. For each step below, write your own CTFT prompt to reach the goal. Stuck? Reveal the suggested prompt.',
  'Check each answer against the sheet before you write it down. Copilot greyed out? Save the file to OneDrive and turn on AutoSave.'
];
var XL_FALLBACK = 'Upload the workbook to Copilot Chat and ask the same questions. Ask it to show the numbers behind every answer — then check them yourself in Excel with a filter or a PivotTable.';
var OL_STEPS = [
  'Copy the thread (tap the box below). Write a new email <b>to yourself</b>, paste it, use the subject line shown, and send. (Or paste it straight into Copilot Chat.)',
  'Open the email. Select <b>Summary by Copilot</b> at the top — or write your prompt for goal 1 in the Copilot pane.',
  'Write your prompt for goal 2 to draft the reply. Then steer the tone twice: <i>“shorter”</i>, <i>“a little warmer”</i>. Don\'t retype.',
  'Before you send: write your prompt for goal 3, or use <b>Coaching by Copilot</b>, to check tone and clarity. Would you send it?'
];
var OL_FALLBACK = 'No Summary by Copilot button? Paste the thread into the Copilot pane in Outlook — or into Copilot Chat — and work through the same goals.';

window.LAB = {
  day: 'Day 2',
  key: 'coded_copilot_day2',
  tasks: [
    /* ======================================================= WORD */
    {
      id: 'E2.1', app: 'Word', title: 'Notes in — a document out', minutes: '25 min', block: 'Block 1 · Word', writeOwn: true,
      scenario: '', steps: WORD_STEPS, fallback: WORD_FALLBACK,
      roles: {
        executive: {
          scenario: 'Last week\'s operations review ran for two hours. Your notes are below. The CEO wants <b>one page</b> before Sunday\'s leadership meeting: what happened, what matters, and what she must decide.',
          briefs: [{ label: 'Your notes · operations review', text:
'MONTHLY OPERATIONS REVIEW — notes (Tamra Foods Co., sample data)\nThursday 24 Sep 2026 · Chair: Yousef (COO)\n\n- Cafés: August revenue up about 2% again. Satisfaction still the highest of the three units (about 4.6 out of 5).\n- Salmiya café: lunch wait time too long — average 11 min, target 6 min. Two staff short since July.\n- Wholesale: July dropped about 21% vs June. August recovered part of it. Two big hotel clients paused orders in July (summer).\n- Top 5 hotel clients = about 31% of wholesale revenue. Risk if one leaves.\n- Delivery app: revenue up about 60% since January, BUT operating costs up faster (driver pay + platform fees). August operating margin slightly negative (about -3%).\n- Faisal (CFO) wants a new delivery fee model by Q4. Options: minimum order value, distance fee, or a monthly subscription.\n- POS terminals: repeated faults at Fahaheel after the firmware 4.2 update in August (13 tickets). IT proposes a KWD 120k upgrade for all 6 cafés.\n- Cold brew launch 18 Oct. Marketing asks for KWD 18k. CFO says 12k.\n- Decisions needed from the CEO: (1) delivery fee model direction, (2) approve the POS upgrade, (3) cold brew budget.\n- Next review: Thursday 29 Oct.' }],
          files: [{ label: 'tamra-h1-2026-business-review.docx', href: 'tamra-h1-2026-business-review.docx', note: '<b>Grounding file</b> — the board\'s H1 review. Your summary should use its unit names and style.' }],
          prompts: [
            { label: '1 · Draft', goal: 'Turn your notes into a one-page summary for the CEO: what happened, what matters, and the decisions she must make.', text: 'Using these notes, draft a one-page executive summary for our CEO. Three sections: What happened, What matters, Decisions needed. Under 300 words. [paste the notes]' },
            { label: '2 · Rewrite', goal: 'Make the draft shorter. Put the three decisions first, with the options for each.', text: 'Make it 20% shorter. Put the three decisions first, as a numbered list, with one line on the options for each.' },
            { label: '3 · Ground', goal: 'Make the summary match the board’s H1 review — same unit names, same style — without changing any of your numbers. Type <kbd>/</kbd> to point Copilot to the file.', text: 'Use the same business-unit names and headline style as /tamra-h1-2026-business-review. Keep every number exactly as it is in my notes.' }
          ],
          expect: 'One page, decisions first — and every number matches your notes: +60%, about −3%, −21%, 31%, KWD 120k, 18k vs 12k.',
          stretch: 'The <b>summarise</b> move: open <a href="tamra-supplier-notice.docx" download>tamra-supplier-notice.docx</a> in Word and ask: <i>“Summarise this notice into five key points for a busy manager.”</i> Check it: does the new cut-off say 2:00 pm (new) or 5:00 pm (old)?',
          boss: 'Ask Copilot: <i>“What is missing from these notes that a CEO will ask about?”</i> Add the two best questions to your summary under “Open questions”.'
        },
        sales: {
          scenario: 'You met a new co-op yesterday. They want Tamra dates and date syrup on the shelves of their new branch. Turn your call notes into a <b>proposal letter</b> they can take to their board.',
          briefs: [{ label: 'Your notes · call with Al-Ward Co-op', text:
'CALL NOTES — Al-Ward Co-op (fictional, sample data)\nTuesday 29 Sep 2026 · Met: Abdullah (Purchasing Manager) and Reem (Branch Manager)\n\n- New branch opens in Farwaniya on 15 Nov. They want a "local premium" shelf near the entrance.\n- Interested in: premium dates (1 kg boxes), stuffed dates (gift boxes), date syrup (500 ml).\n- Expected volume: about 300 boxes a month to start. Could double in busy seasons.\n- Current supplier: late twice last month. Nobody answers the phone after 3 pm.\n- They care about: on-time delivery, help with the shelf display, easy returns for damaged boxes.\n- Payment: from 1 Nov, co-ops pay within 45 days. They asked about the 2% early-payment discount.\n- Our offer: next-day delivery if they order by 2:00 pm; a free display stand for the first 3 months; a tasting day at the opening.\n- Price: Tier 2 (standard co-op price). Tier 1 possible if they sign for 12 months.\n- Next step: they need a short proposal letter by Sunday for their board meeting on Tuesday 6 Oct.' }],
          files: [{ label: 'tamra-house-style-letter.docx', href: 'tamra-house-style-letter.docx', note: '<b>Grounding file</b> — Tamra\'s house voice: warm, clear, short sentences.' }],
          prompts: [
            { label: '1 · Draft', goal: 'Turn your call notes into a proposal letter for Al-Ward’s board: their needs, our offer, delivery and payment terms, and the next step.', text: 'Using these call notes, draft a proposal letter from Tamra Foods to Al-Ward Co-op. Include their needs, our offer, delivery and payment terms, and the next step. Under 350 words. [paste the notes]' },
            { label: '2 · Rewrite', goal: 'Make the letter warmer and more confident. Our three strongest points should be easy to see near the top.', text: 'Make it warmer and more confident. Put our three strongest points in a short bulleted list near the top.' },
            { label: '3 · Ground', goal: 'Make the letter sound like Tamra’s house voice. Type <kbd>/</kbd> to point Copilot to the house-style letter.', text: 'Rewrite it in the voice of /tamra-house-style-letter: warm, clear, short sentences, and a direct contact line at the end.' }
          ],
          expect: 'A letter you would send, with the right terms: 2:00 pm order cut-off, 45-day payment, 2% early-payment discount, three months of free display stand, and their board date (6 Oct).',
          stretch: 'Check your terms against the source: open <a href="tamra-supplier-notice.docx" download>tamra-supplier-notice.docx</a> and ask Copilot <i>“Which payment terms in this notice apply to co-ops?”</i> Does your letter match?',
          boss: 'Ask Copilot for the three hardest questions Al-Ward\'s board might ask. Add a short answer to each at the end of your letter.'
        },
        marketing: {
          scenario: 'Tamra Cold Brew launches on 18 October. Turn the product facts into a <b>launch article</b> for the Tamra website — then a LinkedIn post.',
          briefs: [{ label: 'Your notes · product facts', text:
'PRODUCT FACTS — Tamra Cold Brew (sample data)\n\n- What: cold brew coffee, steeped slowly, sweetened with Tamra date syrup.\n- Size and price: 250 ml bottle, KWD 1.750.\n- Where: all 6 Tamra Cafés, the Tamra app, and selected co-ops — from Sunday 18 Oct 2026.\n- Taste: smooth, low bitterness, a naturally sweet finish.\n- Made in Kuwait: from our Shuwaikh kitchen.\n- Launch offer (first two weeks, app only): a bundle of two bottles and a date bar at a launch price.\n- Audience: young professionals, 22–35, busy mornings, like things that feel local and modern.\n- Brand rules: local and warm. English and Arabic. NO health claims — never "healthy", "sugar-free" or "good for you".\n- Quote from Sara Al-Hajri, Head of Marketing: "We wanted a coffee that tastes like Kuwait: dates, and a little patience."' }],
          files: [{ label: 'tamra-campaign-brief-cold-brew.docx', href: 'tamra-campaign-brief-cold-brew.docx', note: '<b>Grounding file</b> — the campaign brief, with the brand rules.' }],
          prompts: [
            { label: '1 · Draft', goal: 'Turn the product facts into a short launch article for the Tamra website, with a headline, the launch offer and Sara’s quote.', text: 'Using these product facts, write a 300-word launch article for the Tamra website. Include a headline, the launch offer and Sara\'s quote. [paste the facts]' },
            { label: '2 · Rewrite', goal: 'Turn the article into a short LinkedIn post that ends with a call to action.', text: 'Turn it into a LinkedIn post: under 120 words, three short paragraphs, one call to action and three hashtags.' },
            { label: '3 · Ground', goal: 'Check the post against the brand rules in the campaign brief (type <kbd>/</kbd>), and fix anything that breaks a rule.', text: 'Check the post against the brand rules in /tamra-campaign-brief-cold-brew. List anything that breaks a rule, then fix it.' }
          ],
          expect: 'An article and a LinkedIn post with the right facts — 18 Oct, 250 ml, KWD 1.750, the app-only bundle — and not one health claim.',
          stretch: 'Ask for an Arabic version of the LinkedIn post. If you read Arabic, check it sounds natural — not translated word for word.',
          boss: 'Copilot likes words like “healthy” and “guilt-free”. Ask it for five more headlines, then catch every one that breaks the no-health-claims rule.'
        },
        technical: {
          scenario: 'Café staff call IT every time a POS terminal freezes. Turn your rough notes into a <b>how-to guide</b> a new cashier can follow on a busy shift.',
          briefs: [{ label: 'Your notes · POS terminal freeze', text:
'ROUGH NOTES — POS terminal freeze (sample data)\n\n- happens mostly at lunch rush. screen stops, card reader light stays orange\n- first: DON\'T unplug. a sale in progress can be lost\n- hold power button 10 sec until screen goes black. wait 30 sec. press power again\n- restart takes ~2 min. log in with cashier PIN\n- check last sale in "Recent sales". not there → ring the sale again\n- card reader still orange after restart → unplug reader cable, wait 10 sec, plug back in\n- frozen again within 1 hour → move to the backup terminal + call the IT help desk (ext. 4400)\n- Fahaheel: happens more since the firmware 4.2 update in Aug. IT is on it (upgrade project).\n- log every freeze in the IT form: time, terminal number, what you were doing' }],
          files: [{ label: 'tamra-pos-upgrade-project-plan.docx', href: 'tamra-pos-upgrade-project-plan.docx', note: '<b>Grounding file</b> — the POS upgrade plan, with the support plan and the help-desk promise.' }],
          prompts: [
            { label: '1 · Draft', goal: 'Turn your rough notes into a step-by-step guide a new cashier can follow when a POS terminal freezes. Plain English, numbered steps.', text: 'Using these notes, write a step-by-step guide for café cashiers: "What to do when a POS terminal freezes". Numbered steps, plain English, under 250 words. [paste the notes]' },
            { label: '2 · Rewrite', goal: 'Make the guide safer and faster to scan: what never to do comes first, and it ends with a quick reference — problem, what to do, who to call.', text: 'Add a short "Never do this" box at the top, and a table at the end with three columns: Problem · What to do · Who to call.' },
            { label: '3 · Ground', goal: 'Check the guide against the support plan in the POS project plan (type <kbd>/</kbd>). Names and contacts must match.', text: 'Check the guide against the support plan in /tamra-pos-upgrade-project-plan. Use the same names for the help desk and the café POS champion, and fix anything that doesn\'t match.' }
          ],
          expect: 'A guide a new cashier could follow at lunch rush: “don\'t unplug” first, clear numbered steps, the table, and the right help-desk contact.',
          stretch: 'Ask: <i>“Rewrite this for a laminated card next to the till — six steps at most, 60 words.”</i>',
          boss: 'Ask Copilot: <i>“What could go wrong if a cashier follows this guide exactly? List three risks.”</i> Change your guide so each risk is covered.'
        }
      }
    },

    /* ======================================================= POWERPOINT */
    {
      id: 'E2.2', app: 'PowerPoint', title: 'A document becomes a deck', minutes: '25 min', block: 'Block 2 · PowerPoint', writeOwn: true,
      scenario: '', steps: PPT_STEPS, fallback: PPT_FALLBACK,
      findings: [ { label: 'A number you checked — and where it is in the source', hint: 'e.g. KWD 120,000 · Budget table' }, { label: 'Anything wrong, vague or missing?', hint: 'what you fixed by hand' } ],
      roles: {
        executive: {
          scenario: 'The board meets next week. Turn the H1 business review into a <b>6-slide board deck</b> — then check that every number survived the trip.',
          files: [{ label: 'tamra-h1-2026-business-review.docx', href: 'tamra-h1-2026-business-review.docx', note: 'Your source: the H1 2026 business review.' }],
          prompts: [
            { label: '1 · Create', goal: 'Build a 6-slide board deck from the H1 review: results, what drives them, the outlook, risks and the decisions needed. Add speaker notes. Every number must come from the source.', text: 'Create a 6-slide board presentation from /tamra-h1-2026-business-review: headline results, results by business unit, what is driving the numbers, outlook for H2, risks, and the three decisions we need. Keep every figure traceable to the source. Add speaker notes.' },
            { label: '2 · Generate', goal: 'Add one slide that compares the three business units side by side: revenue, margin and customer satisfaction.', text: 'Add one slide that compares the three business units in a simple table: H1 revenue, operating margin and customer satisfaction.' }
          ],
          reveal: '<ul><li>H1 revenue: <b>KWD 5,026,200</b> — Cafés 1,954,200 · Wholesale 2,418,100 · Delivery app 653,900.</li><li>Operating profit KWD 1,011,400 — a <b>20.1%</b> margin.</li><li>Delivery margin fell from 18.2% (Jan) to 8.1% (Jun). Top 5 hotel clients ≈ 31% of wholesale.</li><li>Decisions: POS upgrade <b>KWD 120,000</b> · a new delivery fee model · cold-brew budget <b>KWD 18,000</b>.</li></ul>',
          expect: 'A 6-slide deck from the report, one new comparison slide, and two slides checked number by number.',
          stretch: 'Ask Copilot to rewrite the deck for café managers instead of the board. What changes — the words, the numbers, the “so what”?',
          boss: 'Ask: <i>“Which slide would a board member challenge first, and why?”</i> Add one speaker-note line that answers it.'
        },
        sales: {
          scenario: 'Darwaza Hotels decides on a supplier by 30 November. Turn the account brief into a <b>client-facing pitch deck</b>.',
          files: [{ label: 'tamra-account-brief-darwaza-hotels.docx', href: 'tamra-account-brief-darwaza-hotels.docx', note: 'Your source: the internal account brief. Careful — parts of it are for our eyes only.' }],
          prompts: [
            { label: '1 · Create', goal: 'Build a 7-slide pitch deck for Darwaza Hotels from the account brief, with speaker notes. It goes to the client — nothing internal on any slide.', text: 'Create a 7-slide pitch deck for Darwaza Hotels from /tamra-account-brief-darwaza-hotels: their needs, the problems with their current supplier, our offer, our three price tiers, our delivery promise, proof points, and next steps. It goes to the client — leave out internal notes. Add speaker notes.' },
            { label: '2 · Generate', goal: 'Add one slide that shows Darwaza their first 90 days with Tamra, from contract to full delivery.', text: 'Add one slide: "Your first 90 days with Tamra" — a simple timeline from contract to full delivery.' }
          ],
          reveal: '<ul><li>Budget about <b>KWD 70,000</b> a year · proposal due <b>15 Oct</b> · decision by <b>30 Nov 2026</b> · first delivery Sunday 3 Jan 2027.</li><li>Delivery promise: next-day, <b>98% on-time</b> over 12 months, one account manager.</li><li><b>Watch out:</b> the brief has an internal “Risks and objections” table. Did any of it land on a client slide? Delete it.</li></ul>',
          expect: 'A client-ready 7-slide deck, a 90-day timeline slide — and no internal notes on any slide.',
          stretch: 'Ask Copilot to make a 3-slide version for the group\'s general manager, who has five minutes.',
          boss: 'Ask: <i>“Which objection is Darwaza most likely to raise in the tasting session?”</i> Write the answer into the speaker notes of the right slide.'
        },
        marketing: {
          scenario: 'Management wants to see the cold-brew launch plan on Sunday. Turn the campaign brief into a <b>6-slide launch deck</b>.',
          files: [{ label: 'tamra-campaign-brief-cold-brew.docx', href: 'tamra-campaign-brief-cold-brew.docx', note: 'Your source: the cold-brew campaign brief.' }],
          prompts: [
            { label: '1 · Create', goal: 'Build a 6-slide launch plan for management from the campaign brief: objective, audience, messages, channels and budget, timeline, and how we measure success. Add speaker notes.', text: 'Create a 6-slide launch plan for our management team from /tamra-campaign-brief-cold-brew: the objective, the audience, key messages, channels and budget, timeline, and how we will measure success. Add speaker notes.' },
            { label: '2 · Generate', goal: 'Add one slide with three example posts for launch week — Instagram, TikTok and Snapchat — that follow the brand rules.', text: 'Add one slide with three example social posts for launch week — one each for Instagram, TikTok and Snapchat. Follow the brand rules in the brief.' }
          ],
          reveal: '<ul><li>Launch <b>18 Oct 2026</b>, six weeks to 28 Nov · budget <b>KWD 18,000</b>.</li><li>Targets: 25,000 bottles · 4,000 new app users · 15% of café coffee orders · 2 million impressions.</li><li>Brand rules: bilingual, <b>no health claims</b>. Check your three example posts for “healthy” or “sugar-free”.</li></ul>',
          expect: 'A 6-slide plan with the right targets and budget, plus a posts slide that follows the brand rules.',
          stretch: 'Ask Copilot to add an Arabic version of the key-messages slide.',
          boss: 'The CFO wants KWD 12,000, not 18,000. Ask Copilot to add a slide: what we cut, and what we lose, at 12k.'
        },
        technical: {
          scenario: 'The steering committee meets on Thursday. Turn the POS upgrade project plan into a <b>6-slide decision deck</b>.',
          files: [{ label: 'tamra-pos-upgrade-project-plan.docx', href: 'tamra-pos-upgrade-project-plan.docx', note: 'Your source: the POS upgrade project plan.' }],
          prompts: [
            { label: '1 · Create', goal: 'Build a 6-slide decision deck for the steering committee from the POS project plan: why, scope, timeline, budget, risks, and support and training. Add speaker notes.', text: 'Create a 6-slide steering-committee presentation from /tamra-pos-upgrade-project-plan: why we need it, scope, phases and timeline, budget, risks and mitigations, and support and training. Add speaker notes.' },
            { label: '2 · Generate', goal: 'Add one slide for café managers: what changes for their team, and when. No technical words.', text: 'Add one slide for café managers: "What changes for your team, and when" — plain language, no technical terms.' }
          ],
          reveal: '<ul><li>Budget <b>KWD 120,000</b> · all six cafés · kitchen screens · app orders go straight to the POS.</li><li>Why now: <b>13 POS tickets at Fahaheel in August</b>, many after the firmware 4.2 update · vendor support ends in 2027.</li><li>Installs at night · Fahaheel first in wave 1 · P1 POS tickets answered within 30 minutes.</li></ul>',
          expect: 'A 6-slide decision deck with the right budget and reasons, plus a jargon-free slide for café managers.',
          stretch: 'Ask Copilot to turn the risks slide into a table: Risk · Impact · Mitigation · Owner.',
          boss: 'Ask: <i>“What would the CFO ask about this budget?”</i> Add the answers to the speaker notes on the budget slide.'
        }
      }
    },
    {
      id: 'E2.3', app: 'PowerPoint', title: 'Fix a messy deck', minutes: 'stretch · 10 min', block: 'Block 2 · PowerPoint', optional: true,
      scenario: 'Someone hands you a deck that grew over time: text walls, slides out of order, a near-duplicate, and a junk slide nobody deleted. Make Copilot fix it — <b>without losing a real point</b>.',
      files: [{ label: 'tamra-messy-deck.pptx', href: 'tamra-messy-deck.pptx', note: '“Café Operations Review — Q3 2026”, 9 slides. Open it in PowerPoint.' }],
      steps: [
        'Open the deck and skim it. Spot the wrong order, the duplicate and the junk slide <b>yourself</b> first.',
        'Write your own CTFT prompt to reach the goal, run it in Copilot, and compare its new order with yours.',
        'Make the final call by hand: you decide what stays. Copilot does the heavy lifting.'
      ],
      goal: 'Get Copilot to reorder the deck (title → agenda → findings → recommendations → next steps → summary), merge the duplicate, remove the junk slide, cut each text wall to 3–4 bullets, and list exactly what it changed.',
      prompt: 'This presentation is disorganised. Reorganise it into a logical flow: title, agenda, findings, recommendations, next steps, and the summary at the end. Merge the two wait-time slides, delete the placeholder slide, and cut each text wall to 3–4 clear bullets. Then list exactly what you changed, and confirm you didn\'t drop any real point.',
      hidePrompt: true,
      findings: [ { label: 'Slides you merged or cut', hint: 'which ones + why' }, { label: 'New running order (one line)', hint: 'Title → Agenda → …' }, { label: 'A real point at risk of being lost', hint: 'the one to protect' } ],
      reveal: '<ul><li>Faults: Summary at the start · Agenda on slide 4 · text walls on 3, 5, 6, 8 · slides 5 and 6 are near-duplicates · slide 7 is a placeholder.</li><li>Target: <b>7 slides</b> — Title → Agenda → Customer complaints → Findings: wait times (merged — keep v2\'s extra Fahaheel point) → Recommendations → Next steps → Summary.</li></ul>',
      expect: 'A tighter, ordered deck and a change list — and proof that no real point was lost. Reordering is easy; keeping the signal is the skill.',
      stretch: 'Ask Copilot to cut the whole deck to three slides for a busy executive. What survives is the real message.'
    },

    /* ======================================================= EXCEL */
    {
      id: 'E2.4', app: 'Excel', title: 'Find the story in your numbers', minutes: '30 min', block: 'Block 3 · Excel',
      scenario: '', steps: XL_STEPS, fallback: XL_FALLBACK, ctftNote: true,
      roles: {
        executive: {
          scenario: 'The monthly KPI pack lands on your desk: three business units, eight months. Find the story before the leadership meeting — and be ready to defend every number.',
          dataset: { label: 'tamra-monthly-kpis.xlsx', href: 'tamra-monthly-kpis.xlsx', note: 'Monthly KPIs by business unit · Jan–Aug 2026 · 24 rows. Fictional.',
            head: ['Month', 'Business unit', 'Revenue (KWD)', 'Cost of sales (KWD)', 'Operating costs (KWD)', 'Orders', 'Customer satisfaction (1-5)'],
            rows: [['Jan 2026', 'Cafés', '309,300', '124,600', '117,700', '90,480', '4.5'], ['Jan 2026', 'Wholesale', '398,600', '232,300', '88,700', '1,275', '4.3'], ['Jan 2026', 'Delivery app', '92,000', '41,600', '33,700', '12,606', '4.2'], ['Feb 2026', 'Cafés', '316,200', '126,800', '118,900', '92,312', '4.6']],
            more: '… + 20 more rows in the workbook' },
          promptSteps: [
            { label: 'Step 1 · Find the trends', goal: 'Get Copilot to name the top 3 trends by month and business unit — with the numbers behind each one.', prompt: 'Analyse this table. What are the top 3 trends by month and by business unit? For each trend, show the numbers so I can check them.', findings: [{ label: 'Trend 1', hint: 'unit + number' }, { label: 'Trend 2', hint: 'unit + number' }, { label: 'Trend 3', hint: 'unit + number' }] },
            { label: 'Step 2 · Add a formula column', goal: 'Add an <b>Operating margin</b> column — (Revenue − Cost of sales − Operating costs) ÷ Revenue — and find the weakest unit and month.', prompt: 'Add a column called Operating margin: (Revenue − Cost of sales − Operating costs) ÷ Revenue, as a percentage. Which business unit and month has the lowest margin? Show me the formula.', findings: [{ label: 'Lowest margin — unit + month', hint: 'and the %' }, { label: 'Can you explain the formula?', hint: 'yes / no — what does it compute?' }] },
            { label: 'Step 3 · Chart + CEO email', goal: 'One chart of revenue by unit by month, a one-line caption, then a 5-bullet email for the CEO — every bullet backed by a number.', prompt: 'Create a line chart of revenue by business unit by month. Then write a 5-bullet email to our CEO: the biggest win, the biggest worry and one action — each with a number from the table.', findings: [{ label: 'Chart caption (one line)', hint: 'what the chart shows' }, { label: 'Biggest worry + number', hint: 'for the email' }] }
          ],
          reveal: '<ul><li><b>Delivery app:</b> revenue +61% (KWD 92,000 → 148,000, Jan → Aug) — but operating costs +155%. Operating margin falls from 18.2% to <b>−3.1% in August</b>, its first loss.</li><li><b>Wholesale:</b> July drops 21% vs June (KWD 408,500 → 321,900), then partly recovers in August (371,900). The reason is <b>not</b> in the table.</li><li><b>Cafés:</b> steady growth of about 2% a month, and the highest satisfaction (4.6 of 5).</li></ul>',
          expect: 'Three findings with numbers, an operating-margin column you can explain, and a chart with a one-line caption. If a bullet has no number behind it, it doesn\'t go in the email.',
          stretch: 'Ask: <i>“What is driving the wholesale dip in July?”</i> Copilot can find the dip — but can it know why? Say in your email what the data can\'t tell you.',
          boss: 'Add a column for average order value (Revenue ÷ Orders). Which unit\'s value changes most over the eight months — and is that good or bad news?'
        },
        sales: {
          scenario: 'Your Head of Sales wants a pipeline review before Sunday: what\'s stuck, where you win, and why you lose. The pipeline export is below.',
          dataset: { label: 'tamra-sales-pipeline.xlsx', href: 'tamra-sales-pipeline.xlsx', note: 'B2B pipeline · 120 deals · created Jan–Sep 2026 · data as of 24 Sep. Fictional.',
            head: ['Deal ID', 'Client', 'Segment', 'Account manager', 'Region', 'Stage', 'Deal value (KWD)', 'Created', 'Expected close', 'Days in stage', 'Loss reason'],
            rows: [['D-1001', 'Al-Ghadeer Co-op', 'Co-op', 'Fatima', 'Mubarak Al-Kabeer', 'Won', '16,350', '11 Jan 2026', '25 Feb 2026', '211', ''], ['D-1002', 'Oasis Court Hotel', 'Hotel', 'Noura', 'Mubarak Al-Kabeer', 'Won', '18,600', '11 Jan 2026', '22 Feb 2026', '214', ''], ['D-1003', 'Al-Nakheel Co-op', 'Co-op', 'Fatima', 'Ahmadi', 'Lost', '19,350', '18 Jan 2026', '19 Mar 2026', '189', 'Chose competitor']],
            more: '… + 117 more rows in the workbook' },
          promptSteps: [
            { label: 'Step 1 · What\'s stuck?', goal: 'Find deals stuck in <b>Negotiation</b> for more than 60 days, and their total value.', prompt: 'Show me all deals in the Negotiation stage for more than 60 days. List client, account manager, value and days in stage, and give the total value.', findings: [{ label: 'How many deals?', hint: 'and which clients' }, { label: 'Total value (KWD)', hint: '' }] },
            { label: 'Step 2 · Where do we win?', goal: 'Win rate by segment — Won ÷ (Won + Lost) — and which segment to focus on.', prompt: 'Calculate the win rate for each segment: Won deals ÷ (Won + Lost deals). Show it as a small table and tell me which segment we win most often.', findings: [{ label: 'Best segment + %', hint: '' }, { label: 'Worst segment + %', hint: '' }] },
            { label: 'Step 3 · Why do we lose? + note', goal: 'Who loses the most deals, and why? Chart it, then write a short note to the Head of Sales.', prompt: 'Count lost deals by account manager and by loss reason, and make a chart. Then write a 5-bullet note to our Head of Sales with one recommended action.', findings: [{ label: 'Most losses — who + how many', hint: '' }, { label: 'Main reason', hint: '' }] }
          ],
          reveal: '<ul><li><b>Stuck:</b> 3 deals over 60 days in Negotiation — Sidra Heights Hotel (KWD 32,400, 88 days), Gulf Horizon Holding (29,100, 74 days), Blue Dhow Hotel (24,500, 67 days) = <b>KWD 86,000</b>.</li><li><b>Win rate:</b> Hotels 56.7% · Co-ops 43.5% · Corporate offices 25.0%.</li><li><b>Losses:</b> Khalid has the most (13) — 9 of them on <b>Price</b>.</li></ul>',
          expect: 'Three findings with numbers, a win-rate table you can explain, and a chart with a one-line caption — ready for your Head of Sales.',
          stretch: 'Ask: <i>“What is our Q3 won value?”</i> Then check how Copilot defined Q3 — by the date the deal was created, or the date it closed? Different definitions, different answers. (By close date: KWD 320,000 from 17 deals.)',
          boss: 'Darwaza Hotels (D-1107) is in Proposal at KWD 70,000. Ask Copilot what our hotel win rate suggests about this deal — then write one line on why that is only a rough guide.'
        },
        marketing: {
          scenario: 'Summer campaigns are over. Before you spend the cold-brew budget, find out what worked: which channels paid back, which lost money, and one strange week.',
          dataset: { label: 'tamra-campaign-results.xlsx', href: 'tamra-campaign-results.xlsx', note: 'Weekly campaign results · 13 weeks from Sun 7 Jun 2026 · 173 rows. Fictional.',
            head: ['Week starting', 'Campaign', 'Channel', 'Spend (KWD)', 'Impressions', 'Clicks', 'Orders', 'Revenue (KWD)'],
            rows: [['7 Jun 2026', 'Summer Iced Coffee', 'Instagram', '321', '465,350', '5,493', '233', '751'], ['7 Jun 2026', 'Summer Iced Coffee', 'TikTok', '208', '513,210', '7,850', '255', '816'], ['7 Jun 2026', 'Summer Iced Coffee', 'Snapchat', '209', '528,740', '4,998', '156', '452']],
            more: '… + 170 more rows in the workbook' },
          promptSteps: [
            { label: 'Step 1 · What paid back?', goal: 'Add <b>Cost per order</b> (Spend ÷ Orders) and <b>Return</b> (Revenue ÷ Spend) columns. Which channel gives the best return overall?', prompt: 'Add two columns: Cost per order = Spend ÷ Orders, and Return = Revenue ÷ Spend. Then summarise Return by channel for all campaigns. Which channel is best, and which is worst?', findings: [{ label: 'Best channel + return', hint: '' }, { label: 'Worst channel + return', hint: '' }] },
            { label: 'Step 2 · What lost money?', goal: 'Find any campaign-and-channel pair that loses money (Return below 1).', prompt: 'Which campaign and channel pairs have a Return below 1 — we spent more than we earned? Show spend, revenue and return for each.', findings: [{ label: 'Campaign + channel', hint: '' }, { label: 'Spend vs revenue', hint: '' }] },
            { label: 'Step 3 · The strange week + chart', goal: 'Chart weekly orders by channel, find the unusual week, and ask what caused it.', prompt: 'Create a chart of weekly orders by channel. Which week has an unusual spike? What could explain it?', findings: [{ label: 'Spike — week + channel', hint: '' }, { label: 'Did Copilot know the real reason?', hint: 'yes / no — how can you tell?' }] }
          ],
          reveal: '<ul><li><b>Best return:</b> Email, 4.93 (worst overall: Google Ads, 1.75).</li><li><b>Loses money:</b> Back to Office × Google Ads — spend KWD 4,700, revenue 3,803, return <b>0.81</b>. It is also the biggest spend of any pair.</li><li><b>Cheapest orders:</b> TikTok on Summer Iced Coffee, KWD 0.839 per order.</li><li><b>Spike:</b> Snapchat, week of 2 Aug — 1,239 orders vs about 300 normally (4×). The cause (an influencer post) is <b>not in the data</b>. Copilot can only guess.</li></ul>',
          expect: 'Two new columns you can explain, the money-losing pair found, and a chart with an honest caption about the spike.',
          stretch: 'Write a 5-bullet results summary for your manager: what worked, what didn\'t, and where to move budget — each with a number.',
          boss: 'Ask Copilot to suggest a budget split for the cold-brew launch (KWD 18,000) from this data. Then list two reasons past campaigns may <b>not</b> predict the new one.'
        },
        technical: {
          scenario: 'The Head of IT wants to know where the pain is. You have three months of help-desk tickets. Find the hot spots, the slow fixes, and one pattern nobody has noticed.',
          dataset: { label: 'tamra-it-tickets.xlsx', href: 'tamra-it-tickets.xlsx', note: 'IT tickets · 1 Jul – 24 Sep 2026 · 320 rows. Fictional.',
            head: ['Ticket ID', 'Opened', 'Day', 'Site', 'Category', 'Priority', 'Status', 'Hours to resolve', 'Reopened', 'Assigned to', 'Notes'],
            rows: [['T-24001', '1 Jul 2026', 'Wednesday', 'HQ', 'Delivery app', 'P2', 'Resolved', '4.2', 'No', 'Mariam', ''], ['T-24002', '1 Jul 2026', 'Wednesday', 'HQ', 'Laptop / hardware', 'P4', 'Resolved', '16.3', 'No', 'Omar', ''], ['T-24003', '1 Jul 2026', 'Wednesday', 'Salmiya', 'POS terminal', 'P2', 'Resolved', '2.7', 'No', 'Lulwa', '']],
            more: '… + 317 more rows in the workbook' },
          promptSteps: [
            { label: 'Step 1 · Hot spots', goal: 'Find where and when tickets spike — by site, category and month. Check the Notes column for clues.', prompt: 'Analyse these tickets. Which site and category had an unusual spike, and in which month? Show the counts. Check the Notes column for clues.', findings: [{ label: 'Site + category + month', hint: '' }, { label: 'The clue in Notes', hint: '' }] },
            { label: 'Step 2 · Speed and quality', goal: 'Average <b>hours to resolve</b> by category, and the <b>reopen rate</b> by category.', prompt: 'Calculate the average Hours to resolve for each category, and the reopen rate (Reopened = Yes ÷ all tickets) for each category. Show both in one table, sorted worst to best.', findings: [{ label: 'Slowest category + hours', hint: '' }, { label: 'Highest reopen rate', hint: '' }] },
            { label: 'Step 3 · The pattern + update', goal: 'Find the day-of-week pattern for <b>P1 Delivery app</b> tickets, chart it, and write a short update for the Head of IT.', prompt: 'For P1 tickets in the Delivery app category, count tickets by day of the week and chart it. Then write a 5-bullet update for our Head of IT with one recommended action.', findings: [{ label: 'Busiest day for P1s', hint: '' }, { label: 'Your recommended action', hint: '' }] }
          ],
          reveal: '<ul><li><b>Hot spot:</b> POS terminal tickets at Fahaheel — Jul 2 → <b>Aug 13</b> → Sep 3. Seven notes say “after firmware 4.2 update”.</li><li><b>Slowest:</b> Wi-Fi / network, 18.8 hours on average. <b>Most reopened:</b> Printer, 31% (next is POS at 7%).</li><li><b>Pattern:</b> 8 of the 12 P1 Delivery app tickets were on <b>Thursdays</b> — the busy evening before the weekend.</li></ul>',
          expect: 'Three findings with numbers, a speed-and-quality table you can explain, and a chart with a one-line caption for the Head of IT.',
          stretch: 'Ask Copilot to add a column that flags tickets over 24 hours. How many are there, and which category owns most of them?',
          boss: 'Ask: <i>“Did the firmware 4.2 update cause the Fahaheel spike?”</i> What does the data <b>prove</b>, and what does it only <b>suggest</b>? Write the difference in one sentence.'
        }
      }
    },

    /* ======================================================= OUTLOOK */
    {
      id: 'E2.5', app: 'Outlook', title: 'Tame the thread — then reply', minutes: '20 min', block: 'Block 4 · Outlook', writeOwn: true,
      scenario: '', steps: OL_STEPS, fallback: OL_FALLBACK,
      roles: {
        executive: {
          scenario: 'You\'re back from three days of leave. The board-pack thread has six emails, three opinions and one deadline. Get the picture, then answer the CEO\'s office.',
          briefs: [{ label: 'Thread · Board pack — Q3 numbers (need your call)', text:
'SUBJECT: Board pack — Q3 numbers (need your call)   [sample data]\n\n[1] From: Faisal Al-Rashed (CFO) — Sun 27 Sep, 9:12\nAll, the board pack is due to the CEO\'s office on Wednesday 30 Sep. I\'ll show the delivery app figures as they are: August operating margin is -3.1%. I think the fee-model options paper must go with it.\n\n[2] From: Sara Al-Hajri (Head of Marketing) — Sun 27 Sep, 10:40\nCan we lead with growth? Delivery revenue is up 61% since January. If we open with "loss", the board will cut the cold brew budget.\n\n[3] From: Yousef Al-Shammari (COO) — Sun 27 Sep, 13:05\nBoth are true. My view: show growth AND margin on the same slide. The POS upgrade (KWD 120k) must be in the pack too — Fahaheel had 13 terminal faults in August.\n\n[4] From: Faisal Al-Rashed (CFO) — Mon 28 Sep, 8:30\nFine with one slide. But the fee-model paper is not ready — two options still need costing. Can it go to the November board instead?\n\n[5] From: Noura Al-Ajmi (Head of Sales) — Mon 28 Sep, 11:15\nSmall point: please don\'t show client names in the wholesale section. Darwaza Hotels is still in negotiation.\n\n[6] From: Mariam (CEO\'s office) — Tue 29 Sep, 9:00\n@you — welcome back. Dana asks you to confirm by Wednesday noon: (a) one slide or two for delivery, (b) fee-model paper now or in November, (c) POS upgrade in or out.' }],
          prompts: [
            { label: '1 · Summarise', goal: 'Get the picture fast: what is already agreed, what is still open, and who wants what.', text: 'Summarise this thread for me — I have been on leave. List the decisions already agreed, the questions still open, and who wants what.' },
            { label: '2 · Draft the reply', goal: 'Draft your reply to Mariam. Answer (a), (b) and (c), with a short reason for each. Your calls: one delivery slide with growth and margin together; the fee-model paper goes to the November board; the POS upgrade is in.', text: 'Draft my reply to Mariam in the CEO\'s office. Answer (a), (b) and (c) with a one-line reason each: one slide for delivery showing growth and margin together; the fee-model paper goes to the November board; the POS upgrade is in. Under 150 words. Direct and polite.' },
            { label: '3 · Check before sending', goal: 'Before you send: is the reply clear, is the tone right for the CEO’s office, and does it answer all three questions?', text: 'Check my reply: is it clear, is the tone right for the CEO\'s office, and did I answer all three questions?' }
          ],
          expect: 'A summary that separates what\'s <b>agreed</b> (growth and margin on one slide; no client names) from what\'s <b>still open</b> (a, b, c) — and a reply that answers all three.',
          stretch: 'Ask: <i>“Draft a two-line note to Faisal and Sara explaining my decision on (a).”</i> Same facts, a softer tone.',
          boss: 'Ask Copilot: <i>“What is missing from this thread that the board will ask about?”</i> Add one line to your reply if it matters.'
        },
        sales: {
          scenario: 'Darwaza Hotels is testing Tamra before choosing a supplier. Their trial order arrived damaged — twice. Six emails later, your manager asks you to reply this morning.',
          briefs: [{ label: 'Thread · Darwaza Hotels — damaged trial order', text:
'SUBJECT: Darwaza Hotels — damaged trial order   [sample data]\n\n[1] From: Hessa Al-Qattan (Procurement Manager, Darwaza Hotels) — Sun 27 Sep, 10:05\nHello, our trial order arrived this morning. Three boxes of stuffed dates were crushed — the second time this month. We use them for VIP welcome trays, so this matters. We choose our supplier by 30 November.\n\n[2] From: Bader (Warehouse, Tamra) — Sun 27 Sep, 12:30\nRe: damaged boxes. We can send replacements on Thursday 1 Oct, morning slot. The packaging team is checking the carton type for hotel orders.\n\n[3] From: Khalid (Sales, Tamra) — Sun 27 Sep, 14:10\nFW: can someone own this today? They are comparing us with two other suppliers.\n\n[4] From: Finance (Tamra) — Mon 28 Sep, 9:20\nIs a credit note approved for the three boxes (KWD 37.500)? I need a manager\'s OK before I issue it.\n\n[5] From: Hessa Al-Qattan (Darwaza Hotels) — Mon 28 Sep, 16:45\nWe still have no answer. Also, can you send the Tier 1 prices you mentioned? Our review meeting is on Thursday.\n\n[6] From: Noura Al-Ajmi (Head of Sales) — Tue 29 Sep, 8:15\n@you — please reply to Hessa this morning. The credit note is approved. Tier 1 prices: send the approved price sheet only — no new discounts.' }],
          prompts: [
            { label: '1 · Summarise', goal: 'Find out what went wrong, what has been promised and by whom, and what is still open.', text: 'Summarise this thread: the issue, what has been promised and by whom, and what is still open.' },
            { label: '2 · Draft the reply', goal: 'Draft your reply to Hessa: one apology, the replacement date, the credit note and the Tier 1 price sheet. No new discounts. Warm and short.', text: 'Draft my reply to Hessa. Apologise once, confirm the replacement boxes on Thursday 1 Oct (morning), confirm the credit note, and say the Tier 1 price sheet is attached. No new discounts. Under 130 words. Warm and confident.' },
            { label: '3 · Check before sending', goal: 'Before you send: do you promise anything that is not in the thread? Is the tone right for a client who is comparing suppliers?', text: 'Check my reply: did I promise anything that is not in the thread? Is the tone right for a client who is comparing suppliers?' }
          ],
          expect: 'A summary that separates <b>promised</b> (replacement Thu 1 Oct, credit note approved) from <b>still open</b> (the price sheet) — and a reply that promises nothing new.',
          stretch: 'Ask Copilot to draft the internal follow-up to Bader and Finance: who does what, by when.',
          boss: 'Hessa replies: <i>“Can you match the other supplier\'s 10% discount?”</i> Draft an answer that holds the line, stays warm, and keeps the deal alive.'
        },
        marketing: {
          scenario: 'The launch shoot with your agency moved, the budget grew, and three captions need approval by Thursday. One problem is hiding in the thread. Find it before you reply.',
          briefs: [{ label: 'Thread · Cold brew launch — influencer shoot', text:
'SUBJECT: Cold brew launch — influencer shoot   [sample data]\n\n[1] From: Lamia (Account Director, Bayt Creative — our agency) — Sun 27 Sep, 11:00\nHi team! The rooftop café in Shuwaikh is confirmed for the shoot. We need to move it from Sun 4 Oct to Thu 8 Oct. The location fee is an extra KWD 1,200.\n\n[2] From: Sara Al-Hajri (Head of Marketing) — Sun 27 Sep, 15:20\n8 Oct is tight — launch is 18 Oct. Can we still get edited videos by 13 Oct? The extra 1,200 needs Faisal\'s approval.\n\n[3] From: Lamia (Bayt Creative) — Mon 28 Sep, 10:10\nYes — edited videos by 13 Oct if we get caption approval by Thursday 1 Oct. Draft captions:\n1) "Tamra Cold Brew — the healthy way to wake up."\n2) "Dates + coffee = Kuwait in a bottle."\n3) "Sugar-free energy for busy mornings."\n\n[4] From: Faisal Al-Rashed (CFO) — Mon 28 Sep, 17:30\nApproved: the extra KWD 1,200, one time only. Keep the total launch budget within KWD 18,000.\n\n[5] From: Sara Al-Hajri — Tue 29 Sep, 9:05\n@you — please reply to Lamia today: confirm 8 Oct, the 13 Oct video deadline, and the captions. Remember our brand rules.' }],
          prompts: [
            { label: '1 · Summarise', goal: 'Find what is agreed, what is still open, and every deadline with its date.', text: 'Summarise this thread: what is agreed, what is still open, and every deadline with its date.' },
            { label: '2 · Draft the reply', goal: 'Draft your reply to Lamia: confirm the dates, approve only the captions that follow the brand rules, and ask for new options — in English and Arabic — to replace the rest.', text: 'Draft my reply to Lamia: confirm the shoot on Thursday 8 Oct and edited videos by 13 Oct. Approve caption 2. Politely reject captions 1 and 3 — they break our no-health-claims rule — and ask for two new options in English and Arabic by Thursday 1 Oct. Under 150 words. Friendly and clear.' },
            { label: '3 · Check before sending', goal: 'Before you send: check the reply against the brand rules (bilingual, no health claims, local and warm). Could the agency misread anything?', text: 'Check my reply against our brand rules: bilingual, no health claims, local and warm. Is anything unclear for the agency?' }
          ],
          expect: 'A summary that catches the two caption problems (“healthy”, “sugar-free”) — and a reply that confirms the dates and keeps the brand rules.',
          stretch: 'Write the two replacement captions yourself with Copilot — English and Arabic. Check: no “healthy”, no “sugar-free”, no “good for you”.',
          boss: 'Ask Copilot: <i>“With the extra KWD 1,200, what is left of the 18,000 budget if the shoot and influencers cost what the brief says?”</i> Check its maths against the brief\'s budget table.'
        },
        technical: {
          scenario: 'Last Thursday the delivery app failed at checkout for 95 minutes. The thread is a mix of fixes, questions and worried managers. The Head of IT wants a clear update today.',
          briefs: [{ label: 'Thread · P1 — delivery app orders failing', text:
'SUBJECT: P1 — delivery app orders failing (Thu 24 Sep)   [sample data]\n\n[1] From: Ahmad (IT Support) — Thu 24 Sep, 19:52\nP1 opened. Delivery app orders failing at checkout since about 19:40. Customers see "payment error". Investigating.\n\n[2] From: Mariam (IT Support) — Thu 24 Sep, 20:25\nThe payment gateway certificate expired at 19:38. Renewing now. Workaround: cafés are taking phone orders.\n\n[3] From: Yousef Al-Shammari (COO) — Thu 24 Sep, 20:40\nHow many orders are affected? Thursday night is our busiest evening. I need an update for Dana tonight.\n\n[4] From: Mariam (IT Support) — Thu 24 Sep, 21:20\nFixed at 21:15. About 180 orders failed. No customer was charged twice — failed payments were not taken.\n\n[5] From: Sara Al-Hajri (Head of Marketing) — Fri 25 Sep, 10:10\nCustomers are asking on Instagram. Should we send an apology message and a code?\n\n[6] From: Omar Al-Enezi (Head of IT) — Sun 27 Sep, 8:30\n@you — please write the stakeholder update today: what happened, the impact, the fix, and how we stop it happening again. Also a short customer message Sara can use. No promo code until Faisal agrees.' }],
          prompts: [
            { label: '1 · Summarise', goal: 'Turn the thread into a timeline: when each thing happened, and who acted.', text: 'Summarise this incident thread as a timeline: time, what happened, who acted.' },
            { label: '2 · Draft the update', goal: 'Draft the update the Head of IT asked for: what happened, the impact, the fix, the root cause, and how we stop it happening again. A non-technical reader should get it in one minute.', text: 'Draft a stakeholder update from IT: what happened, the impact, the fix, the root cause, and three actions to stop it happening again. Under 200 words. Clear, calm, no jargon.' },
            { label: '3 · Customer message + check', goal: 'Write a short customer message Sara can use: sorry, no promo code, no technical words. Then have Copilot check both messages for tone and clarity.', text: 'Now write a two-sentence customer message for Sara: apologetic, no promo code, no technical words. Then check both messages for tone and clarity.' }
          ],
          expect: 'A timeline that matches the thread (expired 19:38 → fixed 21:15, about 180 orders, no double charges) and an update a non-technical COO can read in one minute.',
          stretch: 'Ask Copilot to turn the three actions into a checklist with an owner and a due date for each.',
          boss: 'Ask: <i>“What information is missing from this thread that I need before I send the update?”</i> (Hint: when does the next certificate expire — and who is watching it?)'
        }
      }
    },

    /* ======================================================= TEAMS */
    {
      id: 'E2.6', app: 'Teams', title: 'Recap the meeting', minutes: '10 min', block: 'Block 4 · Outlook + Teams', writeOwn: true,
      scenario: 'Sunday\'s leadership meeting ran almost two hours. The Teams transcript is below. Turn it into <b>who does what, by when</b> — then write the follow-up for your area.',
      files: [ { label: 'tamra-leadership-meeting-transcript.docx', href: 'tamra-leadership-meeting-transcript.docx', note: 'A Teams transcript (downloaded as a Word file). Same meeting as the Day 3 Executive capstone.' } ],
      fallback: 'At work, open the meeting in Teams → <b>Recap</b> → Copilot, and ask the same questions. It needs transcription or recording switched on. Here, everyone uploads the transcript to Copilot Chat.',
      steps: [
        'Download the transcript. In Copilot Chat, select <b>+</b> → <b>Upload</b> and attach it.',
        '<b>Recap:</b> write your prompt for goal 1. Check one decision against the transcript.',
        '<b>Follow up:</b> write your prompt for goal 2 — the follow-up for your area.',
        '<b>Check:</b> write your prompt for goal 3. Every action should point to a time in the transcript. Vague dates like “next week”? Turn them into real dates.'
      ],
      roles: {
        executive: { prompts: [
          { label: '1 · Recap', goal: 'Pull out the decisions, the actions (owner and due date) and the open questions — in a form you can scan in seconds.', text: 'Recap this meeting transcript: the decisions made, the action items with owner and due date, and the questions still open. Use three short tables.' },
          { label: '2 · Follow up', goal: 'Draft Dana’s follow-up email to the leadership team: the decisions, every action with owner and date, and the open questions for next Sunday.', text: 'Draft a follow-up email from Dana to the leadership team: the three decisions, every action with owner and date, and the open questions for next Sunday. Under 200 words. Clear and direct.' },
          { label: '3 · Check', goal: 'Make Copilot prove it: where in the transcript was each action agreed?', text: 'For each action item, give the time in the transcript where it was agreed.' } ] },
        sales: { prompts: [
          { label: '1 · Recap', goal: 'Pull out the decisions, the actions (owner and due date) and the open questions — in a form you can scan in seconds.', text: 'Recap this meeting transcript: the decisions made, the action items with owner and due date, and the questions still open. Use three short tables.' },
          { label: '2 · Follow up', goal: 'Write a short note to Noura’s sales team: what the meeting decided on Darwaza Hotels, Noura’s action and deadline, and what the team must prepare this week.', text: 'I work in Noura\'s sales team. Draft a short note to the team: what the meeting decided about Darwaza Hotels, Noura\'s action and deadline, and what we must prepare this week. Under 100 words.' },
          { label: '3 · Check', goal: 'Check your note against the source: find the exact lines on Darwaza Hotels and on discount rules, with the times.', text: 'Quote the exact lines from the transcript about Darwaza Hotels and about discount rules. Give the times.' } ] },
        marketing: { prompts: [
          { label: '1 · Recap', goal: 'Pull out the decisions, the actions (owner and due date) and the open questions — in a form you can scan in seconds.', text: 'Recap this meeting transcript: the decisions made, the action items with owner and due date, and the questions still open. Use three short tables.' },
          { label: '2 · Follow up', goal: 'Write Sara a neutral note on the cold-brew budget: both positions and the reasons given, and what she must bring to the board, by when.', text: 'Draft a note to Sara about the cold-brew budget: both positions (18,000 vs 12,000) and the reasons given, what she must bring to the board, and when. Neutral — show both sides fairly. Under 120 words.' },
          { label: '3 · Check', goal: 'Check that it is fair: find what Faisal and Sara each said about the budget, with the times, and compare it with your note.', text: 'Quote what Faisal and Sara each said about the budget, with the times. Did your note describe both fairly?' } ] },
        technical: { prompts: [
          { label: '1 · Recap', goal: 'Pull out the decisions, the actions (owner and due date) and the open questions — in a form you can scan in seconds.', text: 'Recap this meeting transcript: the decisions made, the action items with owner and due date, and the questions still open. Use three short tables.' },
          { label: '2 · Follow up', goal: 'Write a plain-English note to the IT team: the POS pilot decision and dates, the new firmware rule, the budget, and what IT must deliver next week.', text: 'Draft a note to the IT team: the POS pilot decision and dates, the new rule on firmware updates, the budget, and what IT must deliver next week. Under 120 words. Plain English.' },
          { label: '3 · Check', goal: 'Check your note against the source: find the exact lines on the POS budget and the firmware rule, with the times.', text: 'Quote the lines about the POS budget and the firmware rule, with the times.' } ] }
      },
      reveal: '<ul><li><b>3 decisions:</b> POS pilot at Salmiya from Sunday 25 Oct · new delivery promo codes paused until the fee model is agreed · Noura leads Darwaza with the three price tiers.</li><li><b>5 actions:</b> Faisal (fee options, Thu 1 Oct) · Omar (pilot plan + contract, “next week”) · Noura (Darwaza draft, 15 Oct) · Sara (two budget options, before the board) · Yousef (July dip + calls, end of month).</li><li><b>Open:</b> who leads the partner negotiation · cold-brew budget · Jahra late hours · is the July dip a one-off.</li><li>The POS budget is <b>KWD 120,000</b> in the transcript. Keep that number — you will need it on Day 3.</li></ul>',
      expect: 'A recap in three tables — decisions, actions with owners and dates, open questions — and a follow-up for your area that you would send.',
      stretch: 'Turn the recap into three slides in PowerPoint: decisions, actions, open questions. That is the Teams → Word → PowerPoint → Outlook chain you will build on Day 3.'
    },

    /* ======================================================= CLOSE */
    {
      id: 'E2.7', app: 'Reflection', title: 'Which app saves you the most time?', minutes: '5 min', block: 'Close',
      scenario: 'Two minutes of thinking now pays back on Thursday, when you build your capstone. Name the app that saves you the most time, the task it takes off your desk, and your best prompt from today.',
      steps: [
        'In the box below, write one line: <b>your role · the app · the task · hours saved per week</b> (your honest guess).',
        'Open <a href="prompt-bank.html" target="_blank" rel="noopener">My Prompt Bank</a>. Check that today\'s best prompt is there. If not, save it now.',
        'Your capstone chains <b>two or more</b> Copilot surfaces. Which second app would help with the same task? Add it to your line.'
      ],
      expect: 'One line — role, app, task, hours, second app — and today\'s best prompt saved in your Prompt Bank.'
    }
  ]
};
})();
