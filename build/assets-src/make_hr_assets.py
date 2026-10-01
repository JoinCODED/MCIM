"""Day 3 Agent Builder (E3.2) knowledge files: four Tamra HR and employee policy documents.
Uses the helpers from make_assets.py so the look matches the other Tamra files.
Planted test: the 2024 handbook allows 15 carry-over leave days; the 2026 leave policy (newer, and says it
replaces that section) allows 10. A good agent uses the newer file and says so.
Run:  python3 make_hr_assets.py"""
import make_assets as A

HR_MAIL = 'hr@' + A.DOMAIN


def build_handbook():
    d = A.new_doc("Tamra Foods Co. — Employee Handbook",
                  "Version 3 · Published January 2024 · Owner: Human Resources")
    A.h1(d, "1. Welcome")
    A.para(d, "Welcome to Tamra. This handbook explains how we work together. It applies to all employees: head office, cafés, "
              "warehouse and delivery. If a newer policy covers the same topic, the newer policy applies.")
    A.h1(d, "2. Working hours")
    A.table(d, ["Team", "Normal hours", "Days"], [
        ["Head office (Shuwaikh)", "8:00 am – 4:00 pm, with a one-hour break", "Sunday – Thursday"],
        ["Cafés", "8-hour shifts on a weekly rota", "Rota published every Thursday for the next week"],
        ["Warehouse", "6:00 am – 2:00 pm", "Sunday – Thursday"],
        ["Delivery drivers", "8-hour shifts on a weekly rota", "Seven days, by rota"],
    ])
    A.para(d, "During Ramadan, head office works 9:30 am – 2:30 pm. Café and warehouse managers publish Ramadan rotas two weeks before Ramadan starts.")
    A.h1(d, "3. Probation")
    A.para(d, "New employees have a probation period of 100 working days. Your manager meets you at day 50 and at day 100 to review your progress.")
    A.h1(d, "4. Dress code and uniform")
    A.bullets(d, [
        ("Cafés and warehouse: ", "wear the Tamra uniform and closed shoes. Hair covered in food areas."),
        ("Head office: ", "smart business dress, Sunday to Wednesday. Smart casual on Thursday."),
    ])
    A.h1(d, "5. Annual leave")
    A.para(d, "You get 30 working days of paid annual leave each year. You can carry over up to 15 unused days to the next year. "
              "Ask your manager at least two weeks before your leave starts.")
    A.h1(d, "6. Staff benefits")
    A.bullets(d, [
        ("Staff discount: ", "30% off in all Tamra Cafés and the Tamra app, up to KWD 20 of discount a month."),
        ("Health insurance: ", "for you, your spouse and up to three children, from your first day."),
        ("Training: ", "up to KWD 300 a year for approved courses. Ask your manager first."),
    ])
    A.h1(d, "7. Conduct and discipline")
    A.para(d, "We expect every employee to be honest, polite and on time. If there is a problem, we follow these steps:")
    A.table(d, ["Step", "What happens", "Who decides"], [
        ["1. Verbal warning", "A private talk with your manager, written in your HR file", "Line manager"],
        ["2. Written warning", "A letter that explains the problem and what must change", "Line manager with HR"],
        ["3. Final written warning", "A last chance, valid for 12 months", "Department head with HR"],
        ["4. Dismissal", "The contract ends, in line with Kuwait labour law", "Department head and HR Director"],
    ])
    A.para(d, "Lateness: three late arrivals in one month lead to a verbal warning. "
              "Serious misconduct (for example theft, violence, or sharing customer data) can lead to dismissal without earlier warnings. "
              "HR is always part of a decision to dismiss someone.")
    A.h1(d, "8. Confidentiality and AI tools")
    A.para(d, "Never put customer data, staff data or company secrets into personal accounts, personal devices or public AI tools. "
              "Use only the tools the company approves, on your work account.")
    A.h1(d, "9. Who to contact")
    A.bullets(d, [
        ("HR team: ", HR_MAIL + " · extension 2200 · Sunday to Thursday, 8:00 am – 4:00 pm."),
        ("TamraHub: ", "the HR portal for leave, expenses, payslips and your personal details."),
    ])
    d.save(A.out("tamra-employee-handbook.docx"))


def build_leave_policy():
    d = A.new_doc("Leave Policy 2026",
                  "Tamra Foods Co. — Human Resources · Effective Sunday 1 September 2026 · "
                  "This policy replaces section 5 (Annual leave) of the Employee Handbook (January 2024).")
    A.h1(d, "1. Annual leave")
    A.bullets(d, [
        "You get 30 working days of paid annual leave each year.",
        "You can start using annual leave after you finish probation.",
        "Request leave in TamraHub at least 14 days before it starts. For 10 or more days in a row, request it at least 30 days before.",
        "Your line manager approves or rejects the request within 3 working days.",
    ])
    A.h1(d, "2. Carry-over")
    A.para(d, "You can carry over up to 10 unused days to the next year. You must use carried-over days by 31 March. "
              "Days you do not use by 31 March are lost. This replaces the 15-day carry-over in the 2024 handbook.")
    A.h1(d, "3. Busy periods in cafés")
    A.para(d, "Café staff cannot take annual leave in the last 10 days of Ramadan or during Eid holidays, "
              "unless the area manager approves it in writing.")
    A.h1(d, "4. Sick leave")
    A.bullets(d, [
        "Tell your manager before your shift or working day starts — by phone or Teams, not by email.",
        "Send a medical certificate (from the Sahel app or your clinic) for every sick day, through TamraHub, within 2 working days.",
    ])
    A.table(d, ["Sick days in one year", "Pay"], [
        ["Days 1 – 15", "Full pay"],
        ["Days 16 – 25", "75% of pay"],
        ["Days 26 – 35", "50% of pay"],
        ["Days 36 – 45", "25% of pay"],
        ["After day 45", "Unpaid — HR will contact you"],
    ])
    A.h1(d, "5. Other paid leave")
    A.table(d, ["Leave", "How long", "Notes"], [
        ["Maternity leave", "70 days, full pay", "You can add up to 4 months of unpaid leave after it."],
        ["Paternity leave", "3 working days, full pay", "Take it within one month of the birth."],
        ["Bereavement leave", "3 working days, full pay", "For a parent, spouse, child, brother or sister."],
        ["Marriage leave", "3 working days, full pay", "Once during your employment."],
        ["Hajj leave", "21 days, full pay", "Once during your employment, after 2 years of service."],
    ])
    A.h1(d, "6. Unpaid leave")
    A.para(d, "You can ask for up to 30 days of unpaid leave a year. Your department head must approve it.")
    A.h1(d, "7. Questions")
    A.para(d, "Contact HR at " + HR_MAIL + " or extension 2200.")
    d.save(A.out("tamra-leave-policy-2026.docx"))


def build_hybrid_policy():
    d = A.new_doc("Hybrid and Remote Work Policy",
                  "Tamra Foods Co. — Human Resources and IT · Version 1.2 · June 2026")
    A.h1(d, "1. Who this policy is for")
    A.para(d, "This policy is for head office roles only. It does not apply to café, warehouse or delivery roles, "
              "because that work must be done on site.")
    A.h1(d, "2. How hybrid work works")
    A.bullets(d, [
        "You can work from home up to 2 days a week.",
        "Sunday is an office day for everyone. Team meetings happen on Sunday.",
        "Agree your home days with your manager in TamraHub by Thursday of the week before.",
        "Be online on Teams during core hours: 9:00 am – 1:00 pm.",
        "New employees work from the office for their whole probation period.",
    ])
    A.h1(d, "3. Working from outside Kuwait")
    A.para(d, "Normally you must work from Kuwait. You can work from another country for up to 10 working days a year. "
              "Your department head and the IT team must both approve it first, because of data and security rules.")
    A.h1(d, "4. Equipment and security")
    A.bullets(d, [
        "Use your company laptop only. Do not work on personal computers or personal email.",
        "Connect through the company VPN.",
        "Do not print customer or staff data at home.",
        "Lock your screen when you leave it, even at home.",
    ])
    A.h1(d, "5. Allowance")
    A.para(d, "Hybrid employees get an internet allowance of KWD 10 a month, paid with the salary.")
    A.h1(d, "6. Questions")
    A.para(d, "HR: " + HR_MAIL + ". IT help desk: extension 2300.")
    d.save(A.out("tamra-hybrid-work-policy.docx"))


def build_expenses_policy():
    d = A.new_doc("Expenses and Business Travel Policy",
                  "Tamra Foods Co. — Finance · Version 2.0 · March 2026 · Owner: Faisal Al-Rashed, CFO")
    A.h1(d, "1. How to claim")
    A.bullets(d, [
        "Claim in TamraHub within 30 days of spending the money.",
        "Add a photo of the receipt for every item. No receipt, no payment.",
        "Approved claims are paid with your next salary.",
    ])
    A.h1(d, "2. Who approves")
    A.table(d, ["Total of the claim", "Who approves"], [
        ["Up to KWD 50", "Your line manager"],
        ["KWD 50.001 – KWD 500", "Your department head"],
        ["Over KWD 500", "The CFO"],
    ])
    A.h1(d, "3. In Kuwait")
    A.table(d, ["Expense", "Rule"], [
        ["Taxi to a client or supplier", "Yes — claim the receipt"],
        ["Your daily trip to work", "No — not claimable"],
        ["Personal car for work trips", "KWD 0.050 per km — write the start and end point in the claim"],
        ["Client meal", "Up to KWD 15 per person, including you. Write the client's company name in the claim."],
        ["Parking at a client site", "Yes — claim the receipt"],
    ])
    A.h1(d, "4. Business travel abroad")
    A.bullets(d, [
        "Book flights and hotels through the HR travel desk, at least 14 days before you travel.",
        "Economy class. Business class only for department heads and above, on flights longer than 6 hours.",
        "Hotel: up to KWD 60 a night in GCC countries; up to KWD 80 a night in other countries.",
    ])
    A.table(d, ["Daily allowance (meals and local transport)", "KWD per day"], [
        ["GCC countries", "30"],
        ["Other countries", "45"],
    ])
    A.h1(d, "5. Not claimable")
    A.bullets(d, ["Traffic fines and parking fines.", "Hotel minibar and room movies.",
                  "Gifts for colleagues.", "Upgrades you choose yourself (seat, room or car)."])
    A.h1(d, "6. Questions")
    A.para(d, "Finance team: finance@" + A.DOMAIN + ". HR travel desk: " + HR_MAIL + ".")
    d.save(A.out("tamra-expenses-travel-policy.docx"))


if __name__ == "__main__":
    build_handbook()
    build_leave_policy()
    build_hybrid_policy()
    build_expenses_policy()
    print("written:", ", ".join(A.WRITTEN))
