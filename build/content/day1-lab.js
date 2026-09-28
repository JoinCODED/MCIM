window.LAB = {
  day: 'Day 1',
  key: 'coded_copilot_day1',
  tasks: [
    {
      id: 'E1.1', app: 'Copilot Chat', title: 'Feel the engine', minutes: '10 min', block: 'Block 1',
      scenario: 'Three quick experiments that show how a large language model behaves. You use Copilot Chat — you meet it properly in Block 2.',
      steps: [
        'Open Copilot Chat at <a href="https://copilot.cloud.microsoft/" target="_blank" rel="noopener">copilot.cloud.microsoft</a>. Sign in with your work account or the CODED account on your card.',
        '<b>Experiment A — same question, twice.</b> Run prompt A. Start a <b>New chat</b> and run it again. Compare the two answers.',
        '<b>Experiment B — the most likely words.</b> Run prompt B. Which endings feel predictable?',
        '<b>Experiment C — catch a confident guess.</b> Run prompt C. Open one of the sources it gives. Does the source really say that?'
      ],
      prompts: [
        { label: 'A · Same question, twice', text: 'Give me three tips for writing a clear email to a busy manager.' },
        { label: 'B · The most likely words', text: "Finish this sentence in five different ways: 'The meeting has been moved to…'" },
        { label: 'C · Catch a confident guess', text: 'Give me three statistics about how companies in Kuwait use AI at work. Add the source and the year for each one.' }
      ],
      expect: 'You noticed three things: the answer changes each time, it picks likely words, and it can sound sure without being right. Write your biggest surprise in the box below.',
      stretch: "Ask: <i>“How sure are you about each statistic? Which one should I check first?”</i> Does it admit what it doesn't know?",
      boss: 'Get Copilot to be confidently wrong about something you know very well — your company, your field, your part of Kuwait. Correct it. How does it respond?'
    },
    {
      id: 'E1.2', app: 'Your week', title: 'Your time audit', minutes: '8 min', block: 'Block 1',
      scenario: 'Where does your week go? List three tasks that drain your time. Tag each one with what AI does best — <b>Generate, Condense, Find or Transform</b> — and guess the hours. This list comes back on Thursday: <b>your capstone starts here.</b>',
      steps: [
        'Pick your track below: Executive, Sales, Marketing or Technical. The labs use it for all three days.',
        'Need ideas? Run the helper prompt in Copilot Chat. Replace the [brackets] first.',
        'Fill in three tasks from <b>your</b> real week. Add a tag and a rough number of hours per week.'
      ],
      prompt: 'I work as a [your job title] in [your industry] in Kuwait. List 10 tasks in a typical week where AI could save me time. Group them under four headings: Generate, Condense, Find, Transform. One line each.',
      widget: 'timeaudit',
      expect: 'Three real tasks, tagged, with hours. The biggest one is your capstone candidate for Thursday.',
      stretch: "Ask Copilot: <i>“Break this task into steps: [your biggest task]. Which steps could Copilot do, and which must I do myself?”</i>",
      boss: 'Multiply your three tasks’ hours by 46 working weeks. That is your yearly “drag”. What would you do with half of it back?'
    },
    {
      id: 'E1.3', app: 'Copilot Chat', title: 'First contact', minutes: '5 min', block: 'Block 2',
      scenario: 'Your first real win. Pick any starter that fits your work, tap to copy, replace the [brackets], and run it. The bar is simple: <b>would you use the result?</b>',
      steps: [
        'Open Copilot Chat and start a <b>New chat</b>.',
        'Pick <b>one</b> starter below and tap it to copy. Replace the [brackets] with your own details — nothing confidential.',
        'Read the result. Would you use it? If not, tell Copilot what to change — don\'t start again.'
      ],
      starters: [
        'Explain [a term from your industry] in two sentences, like I\'m new here.',
        'Draft a three-line message telling my team our 10 AM meeting moved to 11 AM.',
        "Give me five ways to say 'thank you for your patience' to a frustrated customer.",
        'Turn these rough notes into three clear bullet points: [paste your notes]',
        'Rewrite this to sound more professional and polite: [paste your sentence]',
        'Summarise what this email asks me to do, in one line: [paste an email with no confidential details]',
        'Suggest three subject lines for an email about [your topic].',
        'Give me a checklist for [a routine task you do], so I don\'t miss a step.'
      ],
      expect: 'A result you would actually use — your first win to share with the room.',
      stretch: "Steer it without rewriting your prompt: <i>“Make it shorter.”</i> → <i>“Make it warmer.”</i> → <i>“Now write it in Arabic.”</i>",
      boss: 'Ask for a version for a customer who has already complained twice. What changed in the tone — and did Copilot promise something you can\'t deliver?'
    },
    {
      id: 'E1.4', app: 'Copilot Chat', title: 'Web, a file, your work', minutes: '10 min', block: 'Block 2',
      scenario: 'Copilot\'s answers come from three places: the <b>web</b>, a <b>file</b> you give it, or — with a Premium licence — <b>your work</b> (emails, files, meetings). Try each one you have. Then decide which answer you can check.',
      files: [ { label: 'tamra-company-profile.docx', href: 'tamra-company-profile.docx', note: 'A profile of Tamra Foods Co. — a fictional Kuwaiti company used in all our exercises.' } ],
      steps: [
        '<b>Web.</b> Run prompt 1. Look for the links at the end of the answer — that is where it came from.',
        '<b>A file.</b> Download the Tamra profile above. In Copilot Chat, select <b>+</b> (Add) → <b>Upload</b>, choose the file, then run prompt 2. Check the answer against the file.',
        '<b>Your work (Premium only).</b> Turn on <b>Work IQ</b>. Type <kbd>/</kbd> and pick a file you know well, then run prompt 3. No Work IQ button? Skip this step.',
        '<b>Compare.</b> Which answer could you check fastest? Write one line in the box below.'
      ],
      prompts: [
        { label: '1 · Web', text: 'What is Microsoft Graph? Explain it in two sentences for someone who isn\'t technical.' },
        { label: '2 · A file', text: 'Using only the attached file: what does Tamra Foods sell, and which three customer groups matter most? Answer in three bullet points, and quote the sentence each point comes from.' },
        { label: '3 · Your work (Premium)', text: 'Summarise [type / and pick your file] in three bullet points. Then list any deadlines it mentions.' }
      ],
      expect: 'An answer from each source you can reach — and one line on which one you could check.',
      stretch: "Ask the file something it can't answer: <i>“Using only the attached file, what was Tamra's profit in 2025?”</i> Does Copilot say it isn't in the file — or does it guess?",
      boss: 'Ask the same question twice: once with the file attached and once without (or Work IQ on, then off). Write down exactly what changed.'
    },
    {
      id: 'E1.5', app: 'Copilot Chat', title: 'The one-page brief', minutes: '12 min', block: 'Block 2',
      scenario: 'Your manager forwards Tamra\'s 2025 annual report and asks: <i>“Give me one page before Sunday.”</i> Condense it, pull out the numbers that matter — and check them against the source before anything goes to your manager.',
      files: [ { label: 'tamra-annual-report-2025.docx', href: 'tamra-annual-report-2025.docx', note: 'A 3-page annual report from Tamra Foods Co. (fictional). Upload it to Copilot Chat — or open it in Word and use Copilot there.' } ],
      steps: [
        'Download the report. In Copilot Chat, select <b>+</b> → <b>Upload</b> and attach it. (Or open it in Word and open the Copilot pane.)',
        '<b>Brief:</b> run prompt 1. Read it once.',
        '<b>Extract:</b> run prompt 2. Every number should come with the section it came from.',
        '<b>Verify — don\'t skip:</b> run prompt 3. Then open the report and read the sentence yourself. Does Copilot\'s brief say the same?'
      ],
      prompts: [
        { label: '1 · Brief', text: 'Summarise the attached annual report into a one-page brief for a busy manager: headline performance, the five numbers that matter, the main risks and the outlook. For each point, say which section of the report it comes from.' },
        { label: '2 · Extract', text: 'List the five most important figures in this report. For each one, give the section and quote the exact sentence or table row it comes from.' },
        { label: '3 · Verify', text: 'How many active users does the Tamra app have? Quote the exact sentence from the report.' }
      ],
      reveal: '<ul><li><b>Active users vs downloads:</b> 38,000 active users; 52,000 downloads. A summary that says “52,000 users” mixed them up.</li><li><b>Two percentages:</b> 98% is wholesale on-time delivery; 94% is café guest satisfaction. Easy to swap.</li><li><b>Growth:</b> revenue KWD 8.9m → 9.6m (+7.9%); operating profit KWD 1.87m (19.5% margin).</li></ul>',
      expect: 'A one-page brief with a section next to every point — and at least one number you checked in the report yourself.',
      stretch: 'Research a topic on the web: <i>“What are three trends in food-delivery apps in the Gulf in 2026? Cite a source for each.”</i> Open one source. Does it really say that?',
      boss: 'Two sources: attach the annual report <b>and</b> <a href="tamra-h1-2026-business-review.docx" download>the H1 2026 business review</a>. Ask: <i>“What changed between 2025 and the first half of 2026? For each point, say which document it comes from.”</i> Premium? Try the <b>Researcher</b> agent for the same question.'
    },
    {
      id: 'E1.6', app: 'Copilot Chat', title: 'Feature hunt', minutes: 'early finishers', block: 'Block 2', optional: true,
      scenario: 'Finished early? Find these features in your Copilot. Some need the Premium licence — that is useful to know, too. Menus move often; if you can\'t find one, ask your neighbour.',
      widget: 'hunt',
      hunt: [
        { name: 'New chat', where: 'Top of the chat. Starts a clean conversation — Copilot forgets the old one.' },
        { name: 'Chat history', where: 'Your past chats, in the left panel.' },
        { name: 'Upload a file', where: 'The <b>+</b> button in the prompt box.' },
        { name: 'Prompt Gallery', where: 'Prompt ideas under the prompt box or in the … menu. We use it on Day 3.' },
        { name: 'Copilot Pages', where: 'Under an answer: <b>Edit in Pages</b> turns it into a page you can edit and share.' },
        { name: 'Model choice', where: 'Auto, Quick response or Think deeper — for fast or deeper answers.' },
        { name: 'Work IQ button', where: 'Top left of the chat. Premium only — switches your work data on or off.' },
        { name: 'Agents', where: 'Researcher and Analyst in the left panel. Premium only.' },
        { name: 'Type /', where: 'Refer to a file, person, email or meeting. Premium, with Work IQ on.' }
      ],
      expect: 'At least five features ticked — and you know which ones your licence doesn\'t include.'
    },
    {
      id: 'E1.7', app: 'Copilot Chat', title: 'From zero to hero', minutes: '15 min', block: 'Block 3',
      scenario: 'One weak prompt, four rounds. Each round adds one CTFT ingredient. Run it each time and rate the result. Rounds 0–1 with the room, rounds 2–4 on your own.',
      steps: [
        'Start a <b>New chat</b>. Run Round 0 on its own.',
        'For each round, copy the new line and add it to your prompt — or run the full Round 4 prompt at the end.',
        'Rate each result from 1 to 5. Which ingredient made the biggest jump?'
      ],
      widget: 'zth',
      rounds: [
        { label: 'The weak prompt', text: 'Write an email to a customer.' },
        { label: '+ Context', text: 'A customer who has ordered office catering from us every week for three years received today\'s order 45 minutes late. It was our scheduling mistake, and we have fixed the driver schedule.' },
        { label: '+ Task', text: 'Write them an email that apologises for the delay and reassures them it won\'t happen again.' },
        { label: '+ Format', text: 'Keep it under 120 words and give them a direct number to call.' },
        { label: '+ Tone & limits', text: 'Make it warm but professional. Don\'t promise a discount or refund. Sign off as the Customer Care Team.' }
      ],
      expect: 'Five results, five ratings — and one sentence on which ingredient made the biggest difference.',
      stretch: "Steer, don't rewrite: <i>“Make it 20% shorter.”</i> → <i>“Now a WhatsApp version.”</i> → <i>“Now in Arabic, same tone.”</i>",
      boss: 'The hard customer: they complained twice before, they are threatening to leave, and they were partly at fault (their office was closed when the driver arrived). Get an email that admits our part, holds the line on theirs, stays under 150 words, and promises nothing we can\'t deliver.'
    },
    {
      id: 'E1.8', app: 'Copilot Chat', title: 'Build your own prompt', minutes: '10 min', block: 'Block 3',
      scenario: 'Now build one for <b>your own job</b>. Role and Context set the scene. Task says what to do. Format and Tone shape it. Add a Source (a file) and an Example if you have them.',
      steps: [
        'Pick a real, repeating task — maybe one from your E1.2 time audit. Leave out confidential details.',
        'Fill the builder. Stuck? Tap <b>Load the example for my track</b>.',
        'Copy the prompt and run it in Copilot Chat. Did the role and context show up in the answer?',
        'Improve it once. Then tap <b>＋ Save to Prompt Bank</b>.'
      ],
      widget: 'builder',
      examples: {
        executive: { role: 'You are the chief of staff to the CEO of a mid-size Kuwaiti company.', ctx: 'Our board meets on Sunday. Q3 revenue grew 6%, but costs grew 11% — mainly delivery and staff costs.', task: 'Draft a one-page briefing for the CEO with the three decisions the board must make.', fmt: 'Three labelled sections: Situation, Options, Recommendation. Under 250 words.', tone: 'Direct and neutral. No jargon.' },
        sales: { role: 'You are an account manager at a Kuwaiti food supplier.', ctx: 'A hotel group that buys from us every month wants a 10% discount on a 12-month contract. Our margin can\'t take 10%.', task: 'Draft a reply that protects our margin and offers two alternatives.', fmt: 'Under 150 words, with the two alternatives as bullet points.', tone: 'Warm and confident — never pushy.' },
        marketing: { role: 'You are a social media specialist at a café chain in Kuwait.', ctx: 'We launch a new cold brew coffee next month. Our audience is young professionals aged 22–35.', task: 'Write three Instagram captions for the launch.', fmt: 'Each under 40 words, with one call to action and two hashtags.', tone: 'Playful and modern. No health claims.' },
        technical: { role: 'You are the IT support lead at a company with 400 staff.', ctx: 'The office Wi-Fi password changes every quarter, and staff keep calling the helpdesk to reconnect.', task: 'Write a short how-to message that explains how to reconnect on a laptop and on a phone.', fmt: 'Numbered steps, under 120 words, with a one-line “Still stuck?” contact at the end.', tone: 'Clear and friendly. No jargon.' }
      },
      expect: 'One prompt you will reuse — tested in Copilot and saved to your Prompt Bank.',
      stretch: 'Fill the Example field — paste a short sample you like — and run it again. One example changes the structure and voice. (This is called few-shot prompting.)',
      boss: 'One prompt, two readers: ask for two versions in one go — one for your manager, one for a client. Same facts, different tone.'
    }
  ]
};
