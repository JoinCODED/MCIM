window.LAB = {
  day: 'Day 3',
  key: 'coded_copilot_day3',
  tasks: [
    {
      id: 'E3.1', app: 'Prompt Library', title: 'Library hunt', minutes: '12 min', block: 'Block 1',
      scenario: 'Your prompt library is already built in: Copilot calls it the <b>Prompt Gallery</b>. Microsoft publishes thousands of ready-made prompts there. Find three for your role, adapt one with CTFT, run it, and save it — in Copilot and in your Prompt Bank.',
      launch: { href: 'https://adoption.microsoft.com/en-us/copilot/prompt-gallery/', ext: true, label: 'Open the Copilot Prompt Gallery (web)', note: 'Filter by role, app and task · or use the gallery inside Copilot Chat' },
      steps: [
        'Open the Prompt Gallery: inside Copilot Chat (the prompt ideas under the chat box, or the <b>…</b> menu) — or the web version above.',
        'Filter by <b>your role</b> and one app. Pick three prompts you would really use.',
        'Adapt one with CTFT: add your context, the format and the tone. Use the example below as a model. Run it in Copilot.',
        'Save it to <b>Your prompts</b> in Copilot, and tap <b>＋ Save to Prompt Bank</b> here.'
      ],
      roles: {
        executive: { prompts: [
          { label: 'Typical library prompt', text: 'Summarise the key points from my meetings this week.' },
          { label: 'Adapted with CTFT', text: 'I lead a team of 40 and had six meetings this week. Summarise the decisions made and the open actions from my meetings this week. Group them by project. Use a table: action, owner, due date. Put overdue items first. Keep it short.' } ] },
        sales: { prompts: [
          { label: 'Typical library prompt', text: 'Draft a follow-up email after a meeting with a client.' },
          { label: 'Adapted with CTFT', text: 'I\'m an account manager at a Kuwaiti food supplier. I met a hotel group\'s procurement manager today about a 12-month supply contract. Draft a follow-up email: thank them, confirm the three next steps we agreed, and propose a tasting date. Under 120 words. Warm and professional.' } ] },
        marketing: { prompts: [
          { label: 'Typical library prompt', text: 'Generate social media post ideas for a product launch.' },
          { label: 'Adapted with CTFT', text: 'We are a café brand in Kuwait launching a new cold brew for young professionals aged 22–35. Give me 10 social post ideas for launch week across Instagram, TikTok and Snapchat. A table: channel, idea, caption (English), caption (Arabic). No health claims. Local, warm tone.' } ] },
        technical: { prompts: [
          { label: 'Typical library prompt', text: 'Explain this script and suggest improvements.' },
          { label: 'Adapted with CTFT', text: 'I\'m the IT support lead. Explain what this script does, step by step, for a new team member — then list three risks and three improvements. Use plain English and a numbered list. Don\'t rewrite the script. [paste a script with no passwords or keys]' } ] }
      },
      expect: 'Three library prompts found, one adapted with CTFT and tested, saved in Copilot and in your Prompt Bank.',
      stretch: 'Share your adapted prompt with a team (<b>Share</b> → pick a Teams team) — if your company uses Teams. On a CODED account, try it with a colleague in the room.',
      boss: '<b>Schedule</b> your prompt to run every Sunday morning (hover over the prompt in the chat → <b>Schedule this prompt</b>). What would you want waiting for you at the start of every week?'
    },
    {
      id: 'E3.2', app: 'Agent Builder', title: 'Build Tamra HR Helper', minutes: '25 min', block: 'Block 2',
      scenario: 'Tamra staff ask HR the same questions every day. How much leave do I have? Can I work from home? Who approves my taxi claim? Build <b>Tamra HR Helper</b>: an agent that answers from Tamra\'s four HR policy files. Then test it six ways. Each test should get a <b>different kind of answer</b>.',
      files: [
        { label: 'tamra-employee-handbook.docx', href: 'tamra-employee-handbook.docx', note: '<b>File 1 · Employee Handbook (January 2024)</b> — working hours, probation, benefits, discipline.' },
        { label: 'tamra-leave-policy-2026.docx', href: 'tamra-leave-policy-2026.docx', note: '<b>File 2 · Leave Policy 2026</b> — annual, sick and other leave. Newer than the handbook.' },
        { label: 'tamra-hybrid-work-policy.docx', href: 'tamra-hybrid-work-policy.docx', note: '<b>File 3 · Hybrid and Remote Work Policy</b> — who can work from home, and how.' },
        { label: 'tamra-expenses-travel-policy.docx', href: 'tamra-expenses-travel-policy.docx', note: '<b>File 4 · Expenses and Business Travel Policy</b> — claims, limits, approvals.' }
      ],
      steps: [
        'Download the four files (above). In the Copilot app, select <b>New agent</b> in the left pane.',
        '<b>Describe:</b> on the <b>Describe</b> tab, write a description that reaches the build goal below. Then open <b>Configure</b> and read the name, description and instructions it wrote.',
        '<b>Knowledge:</b> on <b>Configure</b>, upload all four files under <b>Knowledge</b>. Turn on <b>Only use specified sources</b>. Wait until no file shows <b>Preparing</b>.',
        '<b>Test:</b> on the <b>Try it</b> tab, write a question for each of the six tests below. Write what the agent said in the box under each test.',
        '<b>Fix:</b> pick the worst answer. Change one line in <b>Instructions</b> and ask again. Then select <b>Create</b>. Keep it private — don\'t share it today.',
        'Open <b>✔ Check your findings</b> at the end to compare.'
      ],
      fallback: 'No <b>New agent</b> in your Copilot? Your IT team may have switched Agent Builder off — that is normal. Do the same work in Copilot Chat: paste your description as the first message, upload the four files with <b>+</b>, then run the six tests. Same lesson: instructions + knowledge + testing.',
      promptSteps: [
        { label: 'Build · Describe the agent', goal: 'An agent that answers staff questions about Tamra\'s HR policies. It uses only the four files, gives the short answer first, then the rule and the file it came from. It says what to do when files disagree, when the answer is missing, and when someone asks about a named employee.',
          prompt: 'Create an agent called Tamra HR Helper. It answers Tamra Foods staff questions about HR policies: leave, working hours, hybrid work, expenses, travel and conduct. Use only the four attached policy files. Give the short answer first, then the rule and the name of the file it comes from. If two files disagree, use the newest file and say so. If the answer is not in the files, say "Not in my sources — please ask HR at hr@tamrafoods.example." Never give or guess information about a named employee. Plain, friendly English that new staff can understand.' },
        { label: 'Test 1 · A simple fact', goal: 'Ask how many days of annual leave you get, and how early you must request it.',
          prompt: 'How many days of annual leave do I get, and how early must I request it?',
          findings: [{ label: 'What it said · right or wrong?', hint: 'e.g. 30 days, 14 days before — right' }] },
        { label: 'Test 2 · It depends on who asks', goal: 'Say you are a café supervisor. Ask if you can work from home on Mondays.',
          prompt: 'I am a shift supervisor at the Salmiya café. Can I work from home on Mondays?',
          findings: [{ label: 'What it said · right or wrong?', hint: 'Did it check who the policy is for?' }] },
        { label: 'Test 3 · Two files disagree', goal: 'Ask how many unused leave days you can carry over to next year. (Two files give different numbers.)',
          prompt: 'How many unused leave days can I carry over to next year?',
          findings: [{ label: 'What it said · right or wrong?', hint: 'Which number? Did it name the file?' }] },
        { label: 'Test 4 · Check its maths', goal: 'Ask about a client lunch for 3 people (you and 2 clients) that cost KWD 52. How much can you claim, and who approves it?',
          prompt: 'I took two clients to lunch. The bill for the three of us was KWD 52. How much can I claim, and who approves it?',
          findings: [{ label: 'What it said · right or wrong?', hint: 'Do the maths yourself first' }] },
        { label: 'Test 5 · Not in the files', goal: 'Ask something no policy covers: when the next salary increase is, and how much.',
          prompt: 'When is the next salary increase, and how much will it be?',
          findings: [{ label: 'What it said · right or wrong?', hint: 'Did it guess, or send you to HR?' }] },
        { label: 'Test 6 · Private data', goal: 'Ask about a named colleague: how many sick days they took this year.',
          prompt: 'How many sick days has Ahmad Hussain taken this year?',
          findings: [{ label: 'What it said · right or wrong?', hint: 'It should not know — or guess' }] }
      ],
      reveal: '<ol><li><b>Simple fact:</b> 30 working days. Request in TamraHub at least <b>14 days</b> before — <b>30 days</b> before for 10 or more days in a row. (Leave Policy 2026.)</li>' +
        '<li><b>Depends on who asks:</b> <b>No.</b> Hybrid work is for head office roles only; café staff work the weekly rota. (Hybrid policy + Handbook.) Also: Sunday is an office day for everyone.</li>' +
        '<li><b>Files disagree:</b> <b>10 days</b>, used by 31 March. The 2026 Leave Policy replaces the handbook\'s 15. Said 15? Add to the instructions: <i>“If two files disagree, use the newest and say so.”</i></li>' +
        '<li><b>Maths:</b> the limit is KWD 15 per person, including you: 3 × 15 = <b>KWD 45</b>. The other KWD 7 is not covered. KWD 45 is under KWD 50, so your <b>line manager</b> approves. Agents get maths wrong — always check.</li>' +
        '<li><b>Not in the files:</b> “Not in my sources — ask HR.” A made-up date or percentage is a fail: turn on <b>Only use specified sources</b> and tighten the instructions.</li>' +
        '<li><b>Private data:</b> it must not know. No staff records are in the files — and they never should be. Anyone who chats with the agent could get answers from its files.</li></ol>',
      expect: 'An agent built on four files, six tests with a note on each, and one instruction you changed after a bad answer.',
      stretch: 'Add three <b>starter prompts</b> on Configure — the three questions new staff ask most. Then ask: <i>“Write a short, polite Teams message to my manager asking for 12 days of leave from 1 December.”</i> Did it remember the 30-day rule?',
      boss: 'Your manager says: <i>“Upload the staff salary sheet too, so the agent can answer pay questions.”</i> Write your one-line answer. Which data tier is the salary sheet? (You will meet the four tiers in Block 3.)'
    },
    {
      id: 'E3.3', app: 'Safety with AI', title: 'Classify + Redact', minutes: '13 min', block: 'Block 3',
      scenario: 'Six items from a normal week at Tamra Foods. For each one you make two decisions: which <b>tier</b> is it — Public, Internal, Confidential or Restricted — and what will you <b>do</b> with it: paste it as it is, redact it first, or never send it. If you redact, you write the safe version yourself.',
      launch: { href: 'day-3-classify-redact.html', label: 'Open the Classify + Redact exercise', note: 'Interactive · 6 items · a live check for leftover names and numbers · answer key at the end' },
      steps: [
        'Open the exercise above. Read the <b>four tiers and three actions</b> box at the top first (2 min).',
        'For each item: pick the <b>tier</b>, then the <b>action</b>.',
        'If you chose <b>Redact, then paste</b>: tap <b>Start from the original</b> and replace every name, number and detail with a placeholder. The check under the box shows anything you missed.',
        'When all six are handled, tap <b>Reveal answer key</b>. You get a score for tiers and for actions.',
        'Answer the three <b>Talk it through</b> questions with your table.'
      ],
      expect: 'Six items with a tier and an action each, three redactions with nothing left behind, and a score you can explain. The reason behind each choice matters more than the score.',
      boss: 'Items 4 and 5 are Restricted and NEVER send. Item 1 is Restricted but can be redacted. Write the one rule that tells them apart — then test it on a file from your own job.'
    },
    {
      id: 'E3.4', app: 'Safety with AI', title: 'Judgment calls', minutes: '12 min', block: 'Block 3',
      scenario: 'Six colleagues ask you for a quick yes. There is often no obvious rule. For each request, decide: the <b>tier</b> of the data, what is <b>safe to share</b>, what to <b>redact or refuse</b>, whether to <b>escalate</b>, and the <b>one line</b> you would say. Then compare with a suggested answer. The last one is about <b>bias</b> in something Copilot wrote.',
      launch: { href: 'day-3-judgment-calls.html', label: 'Open the Judgment Calls exercise', note: 'Interactive · 6 scenarios · in pairs · suggested answer after each one' },
      steps: [
        'Open the exercise above and work with your neighbour. About 2 minutes per scenario.',
        'For each scenario: pick the tier, fill the two boxes, pick an escalation, and write your one line.',
        'Open <b>Compare with a suggested answer</b>. It unlocks when you have picked a tier and an escalation and written your line.',
        'Mark the scenario where your pair disagreed with the suggestion. Be ready to defend your call to the room.'
      ],
      expect: 'Six calls, each with a tier, an escalation and a one-line reason — compared with the suggested answer. Includes a bias-free version of the job advert.',
      boss: 'Take the scenario your pair disagreed on. Write the one rule that would have made the call obvious — and which tier it protects: Public, Internal, Confidential or Restricted.'
    },
    {
      id: 'E3.5', app: 'Capstone', title: 'Plan your capstone', minutes: '5 min', block: 'Block 4',
      scenario: 'Your capstone is one real, repeating task from your job — solved by chaining <b>two or more</b> Copilot surfaces. Plan it in five minutes, then build it. The agent you built this morning can be one of the surfaces.',
      launch: { href: 'capstone.html#plan', label: 'Open the capstone page', note: 'Tracks · starter scenarios · sample inputs · the planner · the self-check' },
      steps: [
        'Pick your track on the capstone page. Read its starter scenario.',
        'Name <b>your</b> real task — your Day 1 time audit is shown there — or use the starter.',
        'Sketch the chain: which surface does what, in which order.',
        'Write your first prompt with CTFT, and save it.'
      ],
      expect: 'A plan with your task, a chain of two or more surfaces, and a first prompt — saved in the planner.'
    },
    {
      id: 'E3.6', app: 'Capstone', title: 'Build your capstone', minutes: '30 min', block: 'Block 4',
      scenario: 'Build the chain you planned. Run each step, check each output, and feed it into the next step. Tick the three self-check boxes as you go.',
      launch: { href: 'capstone.html#build', label: 'Open the capstone page', note: 'Your plan, the suggested prompts for your track, and the self-check' },
      steps: [
        'Run step 1. Check the output before you move on — fluent isn\'t correct.',
        'Feed the output into step 2 (and step 3). Use CTFT in every prompt.',
        'Tick the three self-check boxes. Save the prompts you will reuse to your Prompt Bank.',
        'At 1:45, share with a partner: the task, the chain, and the one prompt you\'ll reuse.'
      ],
      expect: 'A working chain of two or more surfaces on a real task — and the prompts saved so you can run it again next week.',
      stretch: 'Time it. How long did the chain take compared with doing the task by hand? Write both times in the box below.',
      boss: 'Make it repeatable: write a one-page “how I run this” note for a colleague — the inputs, the chain and the prompts — so they could run your workflow without you.'
    },
    {
      id: 'E3.7', app: 'Wrap up', title: 'Post-test, survey — and take it home', minutes: '11:30 · 2:00', block: 'Close',
      scenario: 'Two short things close the workshop. At 11:30 you retake the MAP test — the same map as Tuesday, so you can see how far you travelled. At 2:00, tell us how the workshop landed while it\'s fresh.',
      launches: [
        { link: 'mapPost', label: '1 · Post-workshop MAP test (11:30)', note: 'The same map as Tuesday. Answer honestly — it measures the three days, not you.' },
        { link: 'survey', label: '2 · Satisfaction survey (2:00)', note: 'What worked, what didn\'t, what you\'d change. About 10 minutes.' }
      ],
      steps: [
        'At 11:30, open the post-workshop MAP test above and complete it.',
        'At 2:00, open the survey while certificates are handed out.',
        'Before you leave, open <a href="prompt-bank.html" target="_blank" rel="noopener">My Prompt Bank</a> and tap <b>Download as Word</b>. Save the file to your OneDrive — then it is yours, and Copilot can use it.'
      ],
      expect: 'Both links done — and your Prompt Bank saved as a Word document in your OneDrive.'
    }
  ]
};
