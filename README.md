# Mastering Copilot in Microsoft 365 — workshop site (CODED)

A 3-day, open-enrollment workshop site: landing page, three day pages, three slide decks, three hands-on labs,
a Prompt Bank, the capstone, a cheat sheet, resources and fictional sample files (Tamra Foods Co.).

## Deploy
The deployable site is the flat `site/` folder — plain HTML, no build step. `vercel.json` tells Vercel to serve it as-is.

## Change dates or links (no rebuild needed)
Edit `site/site-config.js` — MAP test (pre/post), satisfaction survey, questions board, and the dates.
Every page reads it in the browser. Commit and push; Vercel redeploys.

## Change content
Edit the sources in `build/`, then run `python3 build/build.py` (Python 3.9+, no extra packages) and commit `site/`.
- `build/content/dayN-deck.html` — slides · `build/content/dayN-lab.js` — lab tasks · `build/content/days.py` — day pages
- `build/pages/*.py` — Before you start, Prompt Bank, Capstone, Cheat sheet, Resources, Sample files, Day 3 exercises
- `build/css/`, `build/static/` — design system (CODED SPECIMEN) and the deck/lab engines
- `build/assets-src/` — generators for the sample Word/Excel/PowerPoint files (needs openpyxl, python-docx, python-pptx)

`build.py` never overwrites `site/site-config.js` (pass `--reset-config` to replace it).

All company names, people and numbers in the exercises are fictional.
