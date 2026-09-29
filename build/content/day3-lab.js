window.LAB = {
  day: 'Day 3',
  key: 'coded_copilot_day3',
  tasks: [
    {
      id: 'E3.1', app: 'Responsible AI', title: 'Classify + Redact', minutes: '12 min', block: 'Block 1',
      scenario: 'Six items from a normal week at Tamra Foods cross all four data tiers — plus the ones that must <b>never</b> go into an AI tool. Pick the tier for each, then write a version you would be safe to paste, from a blank box. Reveal the answer key when all six are handled.',
      launch: { href: 'day-3-classify-redact.html', label: 'Open the Classify + Redact exercise', note: 'Interactive · 6 items · saves in your browser · answer key at the end' },
      steps: [
        'Open the exercise above. The six items are inside it.',
        'For each item: pick the tier, then write your redacted version by hand — or mark <b>NEVER send</b>. Use the placeholder buttons to go faster.',
        'Handle all six, tap <b>Reveal answer key</b>, and talk through the ones you got “wrong” with your neighbour.'
      ],
      expect: 'Six items tiered and handled, with redactions you wrote yourself. The score matters less than the reason behind each tier.',
      boss: 'For every item you marked Restricted or NEVER, name the one rule that makes it so: personal data, secrets, HR/medical, or market-sensitive. If you can\'t name the rule, you don\'t own the decision yet.'
    },
    {
      id: 'E3.2', app: 'Responsible AI', title: 'Judgment calls', minutes: '10 min', block: 'Block 1',
      scenario: 'Six grey-zone requests from colleagues — the calls you make when there is no obvious rule. The last one is about <b>bias</b> in something Copilot wrote. For each one: what can be shared safely, what must be removed or refused, whether to escalate, and the one line you would actually say. No answer key — argue the close ones.',
      launch: { href: 'day-3-judgment-calls.html', label: 'Open the Judgment Calls exercise', note: 'Interactive · 6 scenarios · work in pairs · saves in your browser' },
      steps: [
        'Open the exercise above. Work through the six scenarios with your neighbour.',
        'For each one, fill the four boxes: safe to share · remove or refuse · escalate? · your one-line reason.',
        'Pick the scenario you disagreed on most. Be ready to share it with the room.'
      ],
      expect: 'Six scenarios with a clear escalate / don\'t escalate call and a one-line reason each — including a fixed, bias-free version of the job advert.',
      boss: 'Take the scenario your pair split on. Write the one rule that would have made the call obvious — and which data class it belongs to: Public, Internal, Confidential or Restricted.'
    },
    {
      id: 'E3.3', app: 'Prompt Gallery', title: 'Gallery hunt', minutes: '12 min', block: 'Block 2',
      scenario: 'Microsoft publishes thousands of ready-made prompts. Find three for your role, adapt one with CTFT, run it, and save it — in Copilot and in your Prompt Bank.',
      launch: { href: 'https://adoption.microsoft.com/en-us/copilot/prompt-gallery/', ext: true, label: 'Open the Copilot Prompt Gallery (web)', note: 'Filter by role, app and task · or use the gallery inside Copilot Chat' },
      steps: [
        'Open the gallery: inside Copilot Chat (the prompt ideas under the chat box, or the <b>…</b> menu) — or the web version above.',
        'Filter by <b>your role</b> and one app. Pick three prompts you would really use.',
        'Adapt one with CTFT: add your context, the format and the tone. Use the example below as a model. Run it in Copilot.',
        'Save it to <b>Your prompts</b> in Copilot, and tap <b>＋ Save to Prompt Bank</b> here.'
      ],
      roles: {
        executive: { prompts: [
          { label: 'Typical gallery prompt', text: 'Summarise the key points from my meetings this week.' },
          { label: 'Adapted with CTFT', text: 'I lead a team of 40 and had six meetings this week. Summarise the decisions made and the open actions from my meetings this week. Group them by project. Use a table: action, owner, due date. Put overdue items first. Keep it short.' } ] },
        sales: { prompts: [
          { label: 'Typical gallery prompt', text: 'Draft a follow-up email after a meeting with a client.' },
          { label: 'Adapted with CTFT', text: 'I\'m an account manager at a Kuwaiti food supplier. I met a hotel group\'s procurement manager today about a 12-month supply contract. Draft a follow-up email: thank them, confirm the three next steps we agreed, and propose a tasting date. Under 120 words. Warm and professional.' } ] },
        marketing: { prompts: [
          { label: 'Typical gallery prompt', text: 'Generate social media post ideas for a product launch.' },
          { label: 'Adapted with CTFT', text: 'We are a café brand in Kuwait launching a new cold brew for young professionals aged 22–35. Give me 10 social post ideas for launch week across Instagram, TikTok and Snapchat. A table: channel, idea, caption (English), caption (Arabic). No health claims. Local, warm tone.' } ] },
        technical: { prompts: [
          { label: 'Typical gallery prompt', text: 'Explain this script and suggest improvements.' },
          { label: 'Adapted with CTFT', text: 'I\'m the IT support lead. Explain what this script does, step by step, for a new team member — then list three risks and three improvements. Use plain English and a numbered list. Don\'t rewrite the script. [paste a script with no passwords or keys]' } ] }
      },
      expect: 'Three gallery prompts found, one adapted with CTFT and tested, saved in Copilot and in your Prompt Bank.',
      stretch: 'Share your adapted prompt with a team (<b>Share</b> → pick a Teams team) — if your company uses Teams. On a CODED account, try it with a colleague in the room.',
      boss: '<b>Schedule</b> your prompt to run every Sunday morning (hover over the prompt in the chat → <b>Schedule this prompt</b>). What would you want waiting for you at the start of every week?'
    },
    {
      id: 'E3.4', app: 'Capstone', title: 'Plan your capstone', minutes: '10 min', block: 'Block 2',
      scenario: 'Your capstone is one real, repeating task from your job — solved by chaining <b>two or more</b> Copilot surfaces. Plan it now; build it after lunch.',
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
      id: 'E3.5', app: 'Capstone', title: 'Build your capstone', minutes: '40 min', block: 'Block 3',
      scenario: 'Build the chain you planned. Run each step, check each output, and feed it into the next step. Tick the three self-check boxes as you go.',
      launch: { href: 'capstone.html#build', label: 'Open the capstone page', note: 'Your plan, the suggested prompts for your track, and the self-check' },
      steps: [
        'Run step 1. Check the output before you move on — fluent isn\'t correct.',
        'Feed the output into step 2 (and step 3). Use CTFT in every prompt.',
        'Tick the three self-check boxes. Save the prompts you will reuse to your Prompt Bank.',
        'At 1:40, share with a partner: the task, the chain, and the one prompt you\'ll reuse.'
      ],
      expect: 'A working chain of two or more surfaces on a real task — and the prompts saved so you can run it again next week.',
      stretch: 'Time it. How long did the chain take compared with doing the task by hand? Write both times in the box below.',
      boss: 'Make it repeatable: write a one-page “how I run this” note for a colleague — the inputs, the chain and the prompts — so they could run your workflow without you.'
    },
    {
      id: 'E3.6', app: 'Wrap up', title: 'Post-test, survey — and take it home', minutes: '11:10 · 2:00', block: 'Close',
      scenario: 'Two short things close the workshop. At 11:10 you retake the MAP test — the same map as Tuesday, so you can see how far you travelled. At 2:00, tell us how the workshop landed while it\'s fresh.',
      launches: [
        { link: 'mapPost', label: '1 · Post-workshop MAP test (11:10)', note: 'The same map as Tuesday. Answer honestly — it measures the three days, not you.' },
        { link: 'survey', label: '2 · Satisfaction survey (2:00)', note: 'What worked, what didn\'t, what you\'d change. About 10 minutes.' }
      ],
      steps: [
        'At 11:10, open the post-workshop MAP test above and complete it.',
        'At 2:00, open the survey while certificates are handed out.',
        'Before you leave, open <a href="prompt-bank.html" target="_blank" rel="noopener">My Prompt Bank</a> and tap <b>Export</b>. It lives only in this browser.'
      ],
      expect: 'Both links done — and your Prompt Bank exported to a file you can keep.'
    }
  ]
};
