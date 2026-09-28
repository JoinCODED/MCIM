"""Extra Day 3 capstone input (Sales track): a lead brief that reopens a deal lost in June.
Uses the helpers from make_assets.py so the look matches the other Tamra files.
Consistent with tamra-sales-pipeline.xlsx: D-1047 Mersal Tech Park, Corporate office, Khalid, Lost 28 Jun 2026 on Price."""
import make_assets as A

def build_lead_brief():
    d = A.new_doc("Lead Brief: Mersal Tech Park (second chance)",
                  "Tamra Foods Co. — Wholesale team. Prepared for the account manager. Updated Wednesday 30 September 2026.")
    A.h1(d, "Why this lead is back")
    A.para(d, "In June 2026 Mersal Tech Park chose another supplier for office coffee and snacks. The reason was price (pipeline deal D-1047, KWD 10,800). "
              "On Tuesday 29 September their new Facilities Manager called us. The other supplier is often late, and staff complain about quality.")
    A.h1(d, "About the client")
    A.bullets(d, [
        "A business campus in Shuwaikh with 6 office buildings and about 2,000 staff.",
        "Tenants: tech companies, a training institute and two banks' back offices.",
        "Pantries on every floor (48 in total) and one staff café on the ground floor.",
        "Events: a monthly tenants' breakfast (about 300 people) and two big events a year.",
    ])
    A.h1(d, "What they need")
    A.bullets(d, [
        ("Weekly pantry supply: ", "specialty coffee, premium dates and date snacks for 48 pantries."),
        ("Monthly tenants' breakfast: ", "date platters, date paste, coffee for about 300 people."),
        ("Reliability: ", "delivery on a fixed day and time, before 8:00 am."),
        ("One invoice: ", "one monthly invoice for the whole campus, not one per building."),
    ])
    A.h1(d, "The people")
    A.table(d, ["Name", "Role", "What they care about"], [
        ["Eng. Bader Al-Mutairi", "Facilities Manager (new, joined in August)", "Reliability; fewer complaints from tenants"],
        ["Haya Al-Rashidi", "Procurement Officer", "Price per pantry; clear contract terms"],
        ["Tenants' committee", "Six tenant representatives", "Quality and variety; local products"],
    ])
    A.h1(d, "Budget and timeline")
    A.bullets(d, [
        "Budget: about KWD 1,100 a month for pantries (about KWD 13,200 a year) plus events.",
        "They want a proposal and a 20-minute meeting before Thursday 15 October 2026.",
        "Trial month: November 2026. Contract start: 1 January 2027 if the trial goes well.",
        "Their current contract allows them to leave with 30 days' notice.",
    ])
    A.h1(d, "What we can offer")
    A.bullets(d, [
        "Weekly delivery every Sunday before 8:00 am (our 98% on-time record).",
        "Office pantry packs in three sizes; price per pack falls as volume grows.",
        "Monthly breakfast package at a fixed price per person.",
        "One monthly invoice. Corporate office payment terms stay at 30 days.",
        "Free tasting for the tenants' committee in the staff café.",
    ])
    A.h1(d, "Watch-outs")
    A.bullets(d, [
        "Price lost us this deal in June. Lead with reliability and total value, not a discount.",
        "Do not criticise the other supplier by name.",
        "Discounts above 5% need approval from Noura Al-Ajmi, Head of Sales.",
    ])
    A.para(d, "Account manager: Khalid (sales@tamrafoods.example). Head of Sales: Noura Al-Ajmi.")
    p = A.out("tamra-lead-brief-mersal-tech-park.docx")
    d.save(p)
    return p

if __name__ == "__main__":
    print(build_lead_brief())


# ---------------------------------------------------------------------------
# Day 2 (Teams) + Day 3 (Executive capstone): the leadership meeting as a Teams transcript.
# Same meeting as tamra-leadership-meeting-notes.docx. The transcript is RIGHT about the
# POS budget (KWD 120,000); the typed notes wrongly say 102k — a cross-check trap.
TRANSCRIPT = [
 ("0:00:04", "Dana Al-Kandari", "Good morning, everyone. Let's start. Hind is taking notes. Omar is on his way — he'll join in a few minutes. First item: the numbers to August."),
 ("0:00:31", "Faisal Al-Rashed", "Thank you, Dana. The good news first. The delivery app keeps growing. Revenue went from ninety-two thousand in January to one hundred and forty-eight thousand in August."),
 ("0:00:52", "Faisal Al-Rashed", "The bad news: operating costs have grown faster since May. Driver pay went up, and the platform raised its fees. In August the app's operating margin was about minus three percent. That's our first negative month."),
 ("0:01:20", "Dana Al-Kandari", "So we grow — and we lose money on every order? We need to fix that before Q4."),
 ("0:01:34", "Yousef Al-Shammari", "On wholesale: July dropped about twenty-one percent compared with June. Hotels are quiet in summer, and two hotels paused orders for renovation. August came back partly."),
 ("0:02:02", "Noura Al-Ajmi", "Also, our top five hotel clients are about thirty-one percent of wholesale. If one of them leaves, we feel it."),
 ("0:02:15", "Dana Al-Kandari", "Agreed. I want a plan for that. Cafés?"),
 ("0:02:21", "Yousef Al-Shammari", "Cafés are fine. Growing about two percent a month. Satisfaction around four point six."),
 ("0:14:40", "Omar Al-Enezi", "Sorry I'm late. On the POS terminals: Fahaheel had a spike in tickets in August, after the firmware 4.2 update. Terminals froze and card payments failed. We rolled back some terminals, but we still have issues."),
 ("0:15:12", "Omar Al-Enezi", "I'm asking for a full upgrade in all six cafés, connected to the delivery app. The budget is one hundred and twenty thousand, as in the board pack."),
 ("0:15:40", "Yousef Al-Shammari", "I support it. Pilot at Salmiya first. But not during the cold brew launch week — that's the eighteenth of October."),
 ("0:16:05", "Dana Al-Kandari", "Then it's decided: we go ahead with the pilot at Salmiya, starting Sunday the twenty-fifth of October. The full rollout in November and December, if the board approves."),
 ("0:16:30", "Yousef Al-Shammari", "One more thing: no more automatic firmware updates until IT tests them in one café first."),
 ("0:16:41", "Omar Al-Enezi", "Fine by me."),
 ("0:23:10", "Faisal Al-Rashed", "Delivery fees. Two options. Option A: a customer delivery fee of five hundred fils on orders under five dinars. Option B: renegotiate the partner's commission from twenty-two percent down to seventeen. Probably we need both."),
 ("0:23:48", "Sara Al-Hajri", "I'm worried about option A. A fee will hurt app growth and new users."),
 ("0:24:10", "Dana Al-Kandari", "Decision for now: we pause all new delivery promo codes until the fee model is agreed. The promos that are already running can continue to the end of October."),
 ("0:24:35", "Yousef Al-Shammari", "Who leads the negotiation with the delivery partner — Faisal or me?"),
 ("0:24:44", "Dana Al-Kandari", "Let's leave that open for now. Next item."),
 ("0:31:02", "Sara Al-Hajri", "The cold brew launch is on the eighteenth of October. I'm asking for eighteen thousand dinars: Instagram four and a half, TikTok four, influencers three, Snapchat two and a half, in-café two and a half, email five hundred, and one thousand contingency."),
 ("0:31:40", "Faisal Al-Rashed", "That's too much while delivery is losing money. I'd say twelve thousand. Drop the influencers and cut TikTok. We can do in-café and Instagram only."),
 ("0:32:05", "Sara Al-Hajri", "I disagree. TikTok and the creators are how we reach people aged twenty-two to thirty-five. Without them, twenty-five thousand bottles is not realistic."),
 ("0:32:30", "Dana Al-Kandari", "I'm not deciding this today. You both bring options to the board."),
 ("0:40:15", "Noura Al-Ajmi", "Darwaza Hotels: four hotels, about seventy thousand a year. They decide by the thirtieth of November and start in January. Their current supplier delivers late."),
 ("0:40:48", "Dana Al-Kandari", "Noura, you lead the Darwaza proposal. The three price tiers — Classic, Premium and Signature — are approved. Send me the draft by the fifteenth of October."),
 ("0:41:10", "Noura Al-Ajmi", "Will do. Separately, Khalid lost a lot of deals on price this year. I want to look at our discount rules."),
 ("0:52:30", "Faisal Al-Rashed", "Any other business: the one hundred and twenty thousand for POS is already in the Q4 capital budget, so cash is fine."),
 ("0:52:50", "Yousef Al-Shammari", "Jahra café: do we keep the late opening on Thursday and Friday nights? We don't have data yet."),
 ("0:53:05", "Dana Al-Kandari", "And the July wholesale dip — one-off or a trend? Yousef thinks it's the summer. I want proof."),
 ("0:53:30", "Dana Al-Kandari", "Actions. Faisal: the fee model options with numbers for the board pack, by Thursday the first of October. Omar: the Salmiya pilot plan and the vendor contract, next week. Noura: the Darwaza draft by the fifteenth. Sara: two budget options, eighteen and twelve, with the impact on targets, before the board. Yousef: the July dip analysis and calls to the top five hotel clients, by the end of the month."),
 ("0:54:40", "Dana Al-Kandari", "Next meeting: Sunday the fourth of October, same time. The board date is not fixed yet — probably mid-October. Thank you, everyone."),
]

def build_transcript():
    d = A.new_doc("Leadership meeting — transcript",
                  "Microsoft Teams · Sunday 27 September 2026, 9:05–10:50 · Board room, Shuwaikh (in person + Teams). "
                  "Downloaded transcript (.docx). Attendees: Dana Al-Kandari (CEO, chair), Faisal Al-Rashed (CFO), Noura Al-Ajmi (Head of Sales), "
                  "Sara Al-Hajri (Head of Marketing), Omar Al-Enezi (Head of IT, joined late), Yousef Al-Shammari (COO). Some routine discussion is not shown.")
    for ts, who, text in TRANSCRIPT:
        p = d.add_paragraph()
        r = p.add_run(ts + "  " + who); r.bold = True
        d.add_paragraph(text)
    p = A.out("tamra-leadership-meeting-transcript.docx"); d.save(p); return p


# ---------------------------------------------------------------------------
# Day 1 (E1.5 The one-page brief): a long source to condense and verify.
# Traps for the verify habit: 52,000 downloads vs 38,000 active users; 98% on-time vs 94% satisfaction;
# revenue +7.9% (8.9m -> 9.6m); operating profit 1.87m.
def build_annual_report():
    d = A.new_doc("Tamra Foods Co. — Annual Report 2025",
                  "For shareholders, staff and partners. Published March 2026. All figures in Kuwaiti dinars (KWD).")
    A.h1(d, "1. Letter from the Chair")
    A.para(d, "2025 was a year of steady growth for Tamra. Revenue rose by almost 8%, to KWD 9.6 million. We opened our sixth café, in Jahra, "
              "and our delivery app finished its first full year. The app has now passed 52,000 downloads, and customers tell us it is easy to use.")
    A.para(d, "Growth brought new pressure. Coffee bean prices rose, driver costs went up, and hotel orders were quieter in summer. Our teams kept costs "
              "under control and protected our quality. I thank every one of our 420 colleagues for their hard work.")
    A.para(d, "In 2026 the Board will focus on three things: making the delivery app profitable, reducing our dependence on a few large hotel clients, "
              "and modernising the cafés' point-of-sale systems.")
    A.para(d, "— Chair of the Board")
    A.h1(d, "2. Our year in numbers")
    A.table(d, ["Measure", "2024", "2025", "Change"], [
        ["Revenue (KWD)", "8,900,000", "9,600,000", "+7.9%"],
        ["Operating profit (KWD)", "1,690,000", "1,870,000", "+10.7%"],
        ["Operating margin", "19.0%", "19.5%", "+0.5 pts"],
        ["Cafés", "5", "6", "+1 (Jahra)"],
        ["Employees", "385", "420", "+35"],
        ["Delivery app — active users (Dec)", "21,000", "38,000", "+81%"],
        ["Wholesale on-time delivery", "96%", "98%", "+2 pts"],
    ], right_cols=(1, 2, 3))
    A.h1(d, "3. Revenue by business unit")
    A.table(d, ["Business unit", "Revenue 2025 (KWD)", "Share"], [
        ["Wholesale", "4,800,000", "50%"], ["Cafés", "3,744,000", "39%"], ["Delivery app", "1,056,000", "11%"], ["Total", "9,600,000", "100%"],
    ], right_cols=(1, 2))
    A.h1(d, "4. Wholesale")
    A.para(d, "Wholesale is our largest business. We supply more than 40 hotels, 25 co-operative societies (co-ops) and 60 corporate offices. "
              "We delivered 98% of orders on time — our best result so far. Hotels bought more for events and welcome amenities, and co-ops "
              "grew our shelf space for premium dates and date syrup.")
    A.para(d, "The main risk is concentration. Our five largest hotel clients brought about one third of wholesale revenue. "
              "In 2026 we will grow co-ops and corporate offices to balance this.")
    A.h1(d, "5. Cafés")
    A.para(d, "Our six Tamra Cafés — Sharq, Salmiya, Hawally, Jabriya, Fahaheel and Jahra — served more than 1.1 million orders. "
              "Guest satisfaction was 94% (\"good\" or \"very good\" in our in-café survey). The new breakfast menu and date desserts sold well. "
              "The Jahra café, opened in March, reached its sales target in its fifth month.")
    A.para(d, "Our point-of-sale terminals are more than six years old. They cannot connect to the delivery app, so staff type app orders by hand. "
              "We plan to replace them in 2026.")
    A.h1(d, "6. Delivery app")
    A.para(d, "The Tamra app completed its first full year. By December it had 38,000 active users — people who ordered at least once in the last "
              "90 days. Downloads passed 52,000. App revenue reached KWD 1,056,000.")
    A.para(d, "Costs grew with volume. Delivery-partner fees and driver pay are the two largest costs. The app was profitable in 2025, "
              "but its margin became thinner in the second half of the year. Making every order profitable is a priority for 2026.")
    A.h1(d, "7. Our people")
    A.para(d, "We ended the year with 420 employees, 35 more than in 2024. Every café team received customer-service training. "
              "We introduced a new safety programme at the Shuwaikh warehouse, with zero lost-time injuries in the second half.")
    A.h1(d, "8. Sustainability")
    A.para(d, "We moved 70% of café packaging to recyclable materials and started buying dates directly from four Kuwaiti farms. "
              "Our goal for 2026 is 90% recyclable packaging.")
    A.h1(d, "9. Risks")
    A.bullets(d, [
        ("Delivery costs: ", "if partner fees and driver pay keep rising, the app may lose money."),
        ("Client concentration: ", "a few large hotel clients bring a large share of wholesale revenue."),
        ("Ageing systems: ", "old POS terminals fail more often and slow down service."),
        ("Coffee prices: ", "bean prices may rise again in 2026."),
    ])
    A.h1(d, "10. Outlook for 2026")
    A.para(d, "We expect revenue to pass KWD 10 million in 2026. Our plans: launch Tamra Cold Brew in October, upgrade the café POS systems, "
              "agree a new delivery fee model, and win at least two new hotel groups.")
    A.para(d, "Contact: investors@tamrafoods.example")
    p = A.out("tamra-annual-report-2025.docx"); d.save(p); return p


if __name__ == "__main__":
    print(build_transcript())
    print(build_annual_report())
