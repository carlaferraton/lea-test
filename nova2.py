import streamlit as st

# ── Data ──────────────────────────────────────────────────────────────────────

SEGMENTS = {
    "Healthcare Professionals (HCPs)": [
        "Cardiologists", "Dermatologists", "Oncologists",
        "Neurologists", "General Practitioners",
    ],
    "Pharmacists": ["Hospital Pharmacists", "Retail Pharmacists"],
    "Payers & Institutions": ["Insurers / Payers", "Hospital Procurement"],
    "Key Opinion Leaders (KOLs)": ["KOL Network"],
    "Patient Associations": ["Patient Associations"],
}

PROFILS = {
    "Cardiologists": [
        {"avatar": "👨‍⚕️", "name": "Dr. F. Müller",    "institution": "Zurich University Hospital", "preference": "Email"},
        {"avatar": "👩‍⚕️", "name": "Dr. L. Schmidt",   "institution": "Private practice, Basel",    "preference": "Phone call"},
        {"avatar": "👩‍⚕️", "name": "Dr. A. Chavez",    "institution": "CHUV, Lausanne",             "preference": "In-person"},
        {"avatar": "👨‍⚕️", "name": "Dr. R. Patel",     "institution": "HUG, Geneva",                "preference": "Video call"},
    ],
    "Dermatologists": [
        {"avatar": "👩‍⚕️", "name": "Dr. M. Bernard",   "institution": "Derma Clinic Bern",          "preference": "Email"},
        {"avatar": "👨‍⚕️", "name": "Dr. K. Nakamura",  "institution": "Zurich University Hospital", "preference": "Phone call"},
        {"avatar": "👩‍⚕️", "name": "Dr. T. Ait-Kaci",  "institution": "Private practice, Geneva",   "preference": "Email"},
    ],
    "Oncologists": [
        {"avatar": "👩‍⚕️", "name": "Dr. S. Roche",     "institution": "HUG — Oncology dept.",       "preference": "Phone call"},
        {"avatar": "👨‍⚕️", "name": "Prof. B. Liang",   "institution": "Swiss Cancer Center",        "preference": "In-person"},
    ],
    "Neurologists": [
        {"avatar": "👩‍⚕️", "name": "Dr. E. Villanueva","institution": "CHUV — Neurology",           "preference": "Video call"},
        {"avatar": "👨‍⚕️", "name": "Dr. J. Perret",    "institution": "Private practice",           "preference": "Email"},
    ],
    "General Practitioners": [
        {"avatar": "👩‍⚕️", "name": "Dr. M. Dufour",    "institution": "Medical practice, Nyon",     "preference": "Email"},
        {"avatar": "👨‍⚕️", "name": "Dr. H. Weber",     "institution": "Group practice, Aarau",      "preference": "Phone call"},
        {"avatar": "👩‍⚕️", "name": "Dr. L. Keller",    "institution": "Olten Health Center",        "preference": "In-person"},
        {"avatar": "👨‍⚕️", "name": "Dr. N. Amghar",    "institution": "Geneva South district",      "preference": "Video call"},
    ],
    "Hospital Pharmacists": [
        {"avatar": "👩‍⚕️", "name": "P. Girardin", "institution": "CHUV Pharmacy",    "preference": "Email"},
        {"avatar": "👨‍⚕️", "name": "O. Klose",     "institution": "Inselspital Bern", "preference": "Phone call"},
    ],
    "Retail Pharmacists": [
        {"avatar": "👩‍⚕️", "name": "C. Costas", "institution": "Amavita Lausanne",      "preference": "Email"},
        {"avatar": "👨‍⚕️", "name": "D. Russo",   "institution": "Coop Vitality Zurich", "preference": "Phone call"},
    ],
    "Insurers / Payers": [
        {"avatar": "👨‍💼", "name": "M. Hofer",  "institution": "Groupe Mutuel", "preference": "Email"},
        {"avatar": "👩‍💼", "name": "T. Nguyen", "institution": "CSS Insurance", "preference": "Phone call"},
    ],
    "Hospital Procurement": [
        {"avatar": "👨‍💼", "name": "A. Rey", "institution": "HUG — Procurement", "preference": "In-person"},
    ],
    "KOL Network": [
        {"avatar": "👨‍🏫", "name": "Prof. P. Burnier", "institution": "EPFL / Cardiology",    "preference": "Email"},
        {"avatar": "👩‍🏫", "name": "Prof. M. Studer",  "institution": "University of Zurich", "preference": "In-person"},
    ],
    "Patient Associations": [
        {"avatar": "🤝", "name": "H. Favre",   "institution": "SwissHeart Foundation", "preference": "Email"},
        {"avatar": "🤝", "name": "G. Lombard", "institution": "Psoriasis Switzerland", "preference": "Phone call"},
    ],
}

SUGGESTIONS = [
    {"priority": "🔴 High priority", "text": "Dr. Müller (cardiology) hasn't been contacted in 6 weeks — new clinical data now available."},
    {"priority": "🟡 Follow-up",     "text": "PharmaPlus Zurich submitted 3 questions via the NOVA app — a call today could be valuable."},
    {"priority": "🟢 Opportunity",   "text": "A Groupe Mutuel representative is active on product pages — good moment to reach out."},
]

PRODUCTS = [
    {"tag": "Cardiology",  "name": "Entresto", "desc": "Sacubitril/valsartan for chronic heart failure. 20% relative risk reduction in cardiovascular death vs enalapril (PARADIGM-HF)."},
    {"tag": "Cardiology",  "name": "Leqvio",   "desc": "Inclisiran — twice-yearly injection reducing LDL-C by ~50%. RNA interference mechanism targeting PCSK9."},
    {"tag": "Oncology",    "name": "Kisqali",  "desc": "Ribociclib for HR+/HER2- breast cancer in combination with an aromatase inhibitor."},
    {"tag": "Dermatology", "name": "Cosentyx", "desc": "Secukinumab for moderate-to-severe plaque psoriasis, psoriatic arthritis, and ankylosing spondylitis."},
]

FAQ = [
    {"question": "What is the dosing schedule for Leqvio?",       "count": 87, "answer": "Leqvio is administered as a 284 mg subcutaneous injection: first dose, again at 3 months, then every 6 months thereafter."},
    {"question": "Does Entresto require dose titration?",          "count": 64, "answer": "Yes. Start at 49/51 mg twice daily, titrate up to 97/103 mg twice daily as tolerated. Allow a 36-hour washout when switching from an ACE inhibitor."},
    {"question": "Are there patient support programs available?",  "count": 51, "answer": "Yes, Novartis offers patient support programs including financial assistance, monitoring tools, and dedicated helplines."},
    {"question": "What are the contraindications for Kisqali?",    "count": 39, "answer": "Contraindicated in patients with QT interval prolongation, severe hepatic impairment, or hypersensitivity to ribociclib. ECG monitoring is recommended."},
]


def nova_employee_reply(question, segment):
    q = question.lower()
    if "müller" in q or "muller" in q:
        return "Dr. Müller prefers emails and typically responds on Tuesday mornings. He has shown strong interest in the latest Entresto clinical data vs DAPA-HF. I'd recommend a targeted email this week."
    if "prefer" in q or "contact" in q:
        return "In this segment: 42% prefer email, 29% phone calls, 17% in-person visits, 12% video calls. Would you like me to filter contacts by preference?"
    if "leqvio" in q:
        return "Dr. Schmidt and Dr. Patel have shown particular interest in Leqvio's twice-yearly convenience. This could be a strong talking point for your next outreach."
    if "entresto" in q:
        return "3 contacts in this segment haven't yet been briefed on the latest ESC guidelines mentioning Entresto. A good conversation starter."
    if "priorit" in q:
        return "I'd recommend prioritising: 1) Dr. Müller (no contact in 6 weeks), 2) Dr. Patel (visited Leqvio page 3 times this week), 3) Dr. Chavez (protocol renewal coming up)."
    return f"For the **{segment}** segment: I know every contact's profile, preferences, and interaction history. Ask me anything specific!"


def nova_customer_reply(question):
    q = question.lower()
    if "entresto" in q:
        return "**Entresto**: Start at 49/51 mg twice daily, titrate to 97/103 mg twice daily. Allow a 36-hour washout if switching from an ACE inhibitor. Demonstrated a 20% reduction in cardiovascular death vs enalapril (PARADIGM-HF)."
    if "leqvio" in q or "inclisiran" in q:
        return "**Leqvio**: 284 mg subcutaneous injection at Day 0, Month 3, then every 6 months. Reduces LDL-C by approximately 50% through RNA interference targeting PCSK9."
    if "kisqali" in q:
        return "**Kisqali**: 600 mg/day for 21 days followed by 7 days off. Indicated for HR+/HER2- breast cancer. ECG monitoring recommended due to QT prolongation risk."
    if "cosentyx" in q:
        return "**Cosentyx**: Subcutaneous injection for plaque psoriasis, psoriatic arthritis, and ankylosing spondylitis. Monthly induction then maintenance every 4 weeks."
    if "program" in q or "patient" in q or "support" in q:
        return "Novartis offers patient support programs including financial assistance, monitoring tools, and dedicated helplines. Contact your local Novartis representative for regional details."
    return "I can answer questions about any Novartis product — Entresto, Leqvio, Kisqali, Cosentyx, and more. What would you like to know?"


# ── Config & CSS ──────────────────────────────────────────────────────────────

st.set_page_config(page_title="NOVA by Novartis", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
/* Hide all Streamlit chrome */
#MainMenu, header[data-testid="stHeader"], footer,
[data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stStatusWidget"], [data-testid="stDeployButton"],
.stDeployButton, section[data-testid="stSidebar"] {
    display: none !important;
}

/* White background everywhere */
html, body,
.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
.main,
.block-container {
    background: #ffffff !important;
}

.block-container {
    max-width: 1140px !important;
    padding: 2.5rem 2rem 3rem !important;
}

/* Force all text dark */
p, div, span, label, h1, h2, h3, h4, h5, h6,
[data-testid="stMarkdownContainer"] * {
    color: #111111 !important;
}

/* ── BUTTONS: default style (secondary) ── */
div.stButton > button,
div[data-testid="stFormSubmitButton"] > button {
    background-color: #ffffff !important;
    color: #111111 !important;
    border: 1.5px solid #cccccc !important;
    border-radius: 8px !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    box-shadow: none !important;
}
div.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {
    background-color: #f5f5f5 !important;
    border-color: #999 !important;
}
div.stButton > button:focus,
div[data-testid="stFormSubmitButton"] > button:focus,
div.stButton > button:active,
div[data-testid="stFormSubmitButton"] > button:active {
    box-shadow: none !important;
    outline: none !important;
}
/* Primary buttons — BLUE */
div.stButton > button[kind="primary"] {
    background-color: #0067B1 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 0 0 8px 8px !important;
    font-weight: 700 !important;
    height: 50px !important;
}
div.stButton > button[kind="primary"]:hover {
    background-color: #005a98 !important;
}
div.stButton > button[kind="primary"] p,
div.stButton > button[kind="primary"] span {
    color: #ffffff !important;
}
/* Form submit — BLUE */
div[data-testid="stFormSubmitButton"] > button {
    background-color: #0067B1 !important;
    color: #ffffff !important;
    border: none !important;
    border-radius: 8px !important;
    font-weight: 700 !important;
    height: 50px !important;
    width: 100% !important;
}
div[data-testid="stFormSubmitButton"] > button p,
div[data-testid="stFormSubmitButton"] > button span {
    color: #ffffff !important;
}

/* ── INPUTS ── */
input, textarea {
    background: #ffffff !important;
    color: #111111 !important;
}
[data-baseweb="input"] > div,
[data-baseweb="textarea"],
[data-baseweb="select"] > div:first-child {
    background: #ffffff !important;
    border-color: #cccccc !important;
}
[data-baseweb="tag"] {
    background: #e8f0fb !important;
    border-radius: 6px !important;
    padding: 2px 10px !important;
    margin: 3px 4px !important;
}
[data-baseweb="tag"] span { color: #0067B1 !important; }
/* Fix multiselect clipping first character */
[data-baseweb="select"] > div {
    padding-left: 8px !important;
    flex-wrap: wrap !important;
    overflow: visible !important;
}
[data-baseweb="select"] > div > div {
    overflow: visible !important;
}

/* ── EXPANDERS ── */
details, summary,
[data-testid="stExpander"],
[data-testid="stExpanderDetails"] {
    background: #ffffff !important;
    border-color: #e5e5e5 !important;
}
[data-testid="stExpander"] > details {
    background: #ffffff !important;
}

/* ── CONTAINERS (st.container border=True) ── */
[data-testid="stVerticalBlockBorderWrapper"] {
    background: #ffffff !important;
    border-color: #e5e5e5 !important;
}
[data-testid="stVerticalBlockBorderWrapper"] > div {
    background: #ffffff !important;
}

/* Divider */
hr { border-color: #e5e5e5 !important; }
</style>
""", unsafe_allow_html=True)

# ── Session defaults ──────────────────────────────────────────────────────────

for k, v in {
    "page": "login",
    "emp_segment": "Cardiologists",
    "emp_chat": [],
    "portal_chat": [],
    "suggestions": list(SUGGESTIONS),
    "customer_profile": {},
    "new_customers": [],
}.items():
    if k not in st.session_state:
        st.session_state[k] = v


# ══════════════════════════════════════════════════════════════════════════════
#  LOGIN
# ══════════════════════════════════════════════════════════════════════════════

if st.session_state.page == "login":

    # Header row via columns (no raw HTML block)
    h1, h2, h3, h4, h5 = st.columns([3, 1, 1, 1, 1])
    with h1:
        st.markdown(
            "<span style='font-size:18px;font-weight:800;'>Novartis</span>"
            "&ensp;<span style='font-size:11px;letter-spacing:2px;color:#888;font-weight:700;'>NOVA</span>",
            unsafe_allow_html=True,
        )
    for col, label, color in zip(
        [h2, h3, h4, h5],
        ["Choose access", "Support", "Resources", "EN"],
        ["#0067B1", "#555", "#555", "#555"],
    ):
        with col:
            st.markdown(
                f"<div style='padding-top:2px;font-size:13px;font-weight:600;color:{color};'>{label}</div>",
                unsafe_allow_html=True,
            )

    st.divider()

    # Hero — all inline styles, no custom CSS classes
    st.markdown(
        "<p style='color:#999;font-size:11px;font-weight:700;letter-spacing:2px;"
        "text-transform:uppercase;margin:0 0 20px 0;'>NOVA PLATFORM</p>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<h1 style='font-size:78px;font-weight:800;letter-spacing:6px;"
        "line-height:1;margin:0 0 28px 0;color:#000;'>NOVA</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='font-size:18px;color:#555;line-height:1.65;max-width:720px;"
        "margin-bottom:48px;'>A focused workspace for Novartis associates and "
        "healthcare partners to access resources, engagement signals, and "
        "compliant product support.</p>",
        unsafe_allow_html=True,
    )

    # Cards
    col_hcp, col_emp = st.columns(2, gap="large")

    with col_hcp:
        st.markdown(
            "<div style='border:1px solid #e0e0e0;border-radius:10px 10px 0 0;"
            "background:#fff;min-height:240px;padding:30px;'>"
            "<div style='width:52px;height:4px;background:#ff4b19;border-radius:2px;margin-bottom:32px;'></div>"
            "<div style='font-size:22px;font-weight:800;color:#111;line-height:1.2;margin-bottom:14px;'>"
            "Healthcare professionals and partners</div>"
            "<div style='font-size:14px;color:#666;line-height:1.55;'>"
            "Access medical information, clinical data, product resources, and patient support tools.</div>"
            "</div>",
            unsafe_allow_html=True,
        )
        if st.button("Continue as HCP or partner", use_container_width=True, key="btn_hcp", type="primary"):
            st.session_state.page = "register"
            st.rerun()

    with col_emp:
        st.markdown(
            "<div style='border:1px solid #e0e0e0;border-radius:10px 10px 0 0;"
            "background:#fff;min-height:240px;padding:30px;'>"
            "<div style='width:52px;height:4px;background:#0067B1;border-radius:2px;margin-bottom:32px;'></div>"
            "<div style='font-size:22px;font-weight:800;color:#111;line-height:1.2;margin-bottom:14px;'>"
            "Novartis associates</div>"
            "<div style='font-size:14px;color:#666;line-height:1.55;'>"
            "Use internal resources, engagement intelligence, training, and support services.</div>"
            "</div>",
            unsafe_allow_html=True,
        )
        if st.button("Continue as associate", use_container_width=True, key="btn_emp", type="primary"):
            st.session_state.page = "employee"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # Feature strip
    fc1, fc2, fc3, fc4 = st.columns(4)
    for col, label in zip([fc1, fc2, fc3, fc4],
                          ["Secure access", "Clinical resources", "Engagement insights", "Patient support"]):
        with col:
            st.markdown(
                f"<div style='border-left:2px solid #ff4b19;padding-left:12px;"
                f"font-size:13px;color:#777;'>{label}</div>",
                unsafe_allow_html=True,
            )


# ══════════════════════════════════════════════════════════════════════════════
#  EMPLOYEE
# ══════════════════════════════════════════════════════════════════════════════

elif st.session_state.page == "employee":

    tb1, _, tb3, tb4 = st.columns([3, 5, 1, 1])
    with tb1:
        st.markdown("<h2 style='margin:0;padding-top:2px;'>Nova</h2>", unsafe_allow_html=True)
    with tb3:
        st.markdown("<div style='padding-top:8px;font-size:13px;font-weight:600;text-align:right;'>👤 Sophie C.</div>", unsafe_allow_html=True)
    with tb4:
        if st.button("Sign out", key="emp_logout"):
            st.session_state.page = "login"
            st.rerun()

    st.divider()

    # Suggestions banner
    st.markdown(
        "<span style='background:#fff;color:#C8102E;border:1.5px solid #C8102E;"
        "padding:3px 12px;border-radius:20px;font-size:11px;font-weight:700;"
        "letter-spacing:1px;'>NOVA AI</span>"
        "&nbsp;<span style='color:#555;font-size:14px;'>Today's suggestions — "
        "<em>you decide whether to act on them</em></span>",
        unsafe_allow_html=True,
    )
    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    if st.session_state.suggestions:
        scols = st.columns(len(st.session_state.suggestions))
        to_remove = None
        for i, (col, sug) in enumerate(zip(scols, st.session_state.suggestions)):
            with col:
                with st.container(border=True):
                    st.markdown(
                        f"<div style='color:#C8102E;font-weight:700;font-size:12px;"
                        f"margin-bottom:4px;'>{sug['priority']}</div>"
                        f"<div style='font-size:13px;color:#333;line-height:1.4;'>{sug['text']}</div>",
                        unsafe_allow_html=True,
                    )
                    if st.button("✕ Dismiss", key=f"dismiss_{i}"):
                        to_remove = i
        if to_remove is not None:
            st.session_state.suggestions.pop(to_remove)
            st.rerun()
    else:
        st.info("No suggestions at the moment.")

    st.divider()

    col_sidebar, col_main = st.columns([1, 3])

    with col_sidebar:
        st.markdown("#### Customer segments")
        for group_name, subsegments in SEGMENTS.items():
            st.markdown(
                f"<div style='font-size:11px;font-weight:700;color:#888;"
                f"text-transform:uppercase;letter-spacing:1px;margin:14px 0 6px;'>{group_name}</div>",
                unsafe_allow_html=True,
            )
            for seg_name in subsegments:
                if st.button(seg_name, key=f"seg_{seg_name}", use_container_width=True):
                    st.session_state.emp_segment = seg_name
                    st.session_state.emp_chat = []
                    st.rerun()

        if st.session_state.new_customers:
            st.divider()
            st.markdown("#### New sign-ups")
            for c in st.session_state.new_customers:
                st.success(f"**{c['name']}** — {c['sector']}")

    with col_main:
        seg = st.session_state.emp_segment
        st.markdown(f"## {seg}")
        st.caption("Active segment · Data last updated 2 hours ago")

        profils = PROFILS.get(seg, [])
        if profils:
            dcols = st.columns(min(len(profils), 4))
            for col, p in zip(dcols, profils):
                with col:
                    with st.container(border=True):
                        st.markdown(
                            f"<div style='text-align:center;padding:6px 0;'>"
                            f"<div style='font-size:2rem;'>{p['avatar']}</div>"
                            f"<div style='font-weight:700;font-size:14px;margin-top:6px;color:#111;'>{p['name']}</div>"
                            f"<div style='font-size:12px;color:#777;margin-top:2px;'>{p['institution']}</div>"
                            f"<div style='background:#fce8eb;color:#C8102E;border-radius:20px;"
                            f"padding:2px 10px;font-size:11px;font-weight:700;"
                            f"margin-top:8px;display:inline-block;'>{p['preference']}</div>"
                            f"</div>",
                            unsafe_allow_html=True,
                        )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("##### 💬 Ask NOVA")

        for msg in st.session_state.emp_chat:
            if msg["role"] == "user":
                st.markdown(
                    f"<div style='background:#f5f5f5;border:1px solid #e0e0e0;"
                    f"border-radius:18px 18px 4px 18px;padding:10px 14px;"
                    f"margin:6px 0;font-size:14px;color:#111;'>{msg['content']}</div>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"<div style='background:#ffffff;border:1px solid #ddd;"
                    f"border-radius:18px 18px 18px 4px;padding:10px 14px;"
                    f"margin:6px 0;font-size:14px;color:#111;'>"
                    f"🤖 <strong>NOVA</strong>: {msg['content']}</div>",
                    unsafe_allow_html=True,
                )

        with st.form(key="emp_chat_form", clear_on_submit=True):
            user_input = st.text_input(
                "q", placeholder="e.g. What is the best time to contact Dr. Müller?",
                label_visibility="collapsed",
            )
            if st.form_submit_button("Send ➤") and user_input.strip():
                st.session_state.emp_chat.append({"role": "user", "content": user_input})
                st.session_state.emp_chat.append({"role": "nova", "content": nova_employee_reply(user_input, seg)})
                st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
#  REGISTER
# ══════════════════════════════════════════════════════════════════════════════

elif st.session_state.page == "register":

    st.markdown(
        "<h1 style='text-align:center;font-size:40px;font-weight:800;margin-bottom:4px;color:#111;'>nova</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align:center;color:#888;font-size:12px;letter-spacing:3px;"
        "text-transform:uppercase;margin-bottom:32px;'>Create your account</p>",
        unsafe_allow_html=True,
    )

    _, col2, _ = st.columns([1, 2, 1])
    with col2:
        with st.form("register_form"):
            ca, cb = st.columns(2)
            with ca:
                prenom = st.text_input("First name", placeholder="Marie")
            with cb:
                nom_f = st.text_input("Last name", placeholder="Dupont")
            secteur = st.selectbox("Sector", [
                "Healthcare Professional (HCP)", "Hospital Pharmacist",
                "Retail Pharmacist", "Payer / Insurance",
                "Hospital Procurement", "Key Opinion Leader (KOL)",
                "Patient Association",
            ])
            specialite = None
            if "HCP" in secteur or "KOL" in secteur:
                specialite = st.selectbox(
                    "Speciality",
                    ["Cardiology", "Dermatology", "Oncology", "Neurology", "General Medicine"],
                )
            lieu = st.text_input("Place of work", placeholder="HUG – Geneva")
            contact_pref = st.multiselect(
                "Preferred contact method",
                ["Email", "Phone call", "Video call", "In-person visit"],
                default=["Email"],
            )
            submitted = st.form_submit_button("✅  Create my account", use_container_width=True)
            if submitted:
                st.session_state.customer_profile = {
                    "name": f"{prenom} {nom_f}",
                    "sector": secteur,
                    "specialite": specialite,
                    "lieu": lieu,
                    "preferences": contact_pref,
                }
                st.session_state.new_customers.append({"name": f"{prenom} {nom_f}", "sector": secteur})
                st.session_state.page = "portal"
                st.rerun()

        if st.button("← Back", key="reg_back"):
            st.session_state.page = "login"
            st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
#  PORTAL
# ══════════════════════════════════════════════════════════════════════════════

elif st.session_state.page == "portal":

    profil = st.session_state.customer_profile
    nom = profil.get("name", "User")

    tb1, _, tb3, tb4 = st.columns([3, 4, 1, 1])
    with tb1:
        st.markdown("<h2 style='margin:0;padding-top:2px;'>Nova</h2>", unsafe_allow_html=True)
    with tb3:
        st.markdown(
            f"<div style='padding-top:8px;font-size:13px;font-weight:600;text-align:right;'>👤 {nom}</div>",
            unsafe_allow_html=True,
        )
    with tb4:
        if st.button("Sign out", key="portal_logout"):
            st.session_state.page = "login"
            st.rerun()

    st.divider()

    col_products, col_chat = st.columns([2, 1])

    with col_products:
        st.markdown("#### Novartis Products")
        for i in range(0, len(PRODUCTS), 2):
            pcols = st.columns(2)
            for j, pcol in enumerate(pcols):
                if i + j < len(PRODUCTS):
                    p = PRODUCTS[i + j]
                    with pcol:
                        with st.container(border=True):
                            st.markdown(
                                f"<span style='background:#fce8eb;color:#C8102E;padding:2px 10px;"
                                f"border-radius:20px;font-size:11px;font-weight:700;'>{p['tag']}</span>",
                                unsafe_allow_html=True,
                            )
                            st.markdown(f"**{p['name']}**")
                            st.markdown(
                                f"<span style='font-size:13px;color:#555;'>{p['desc']}</span>",
                                unsafe_allow_html=True,
                            )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("#### ❓ Frequently asked questions")
        st.caption("These questions are also visible to the Novartis marketing team")
        for faq in FAQ:
            with st.expander(f"{faq['question']} — *asked {faq['count']} times*"):
                st.write(faq["answer"])

    with col_chat:
        st.markdown("#### 💬 Ask NOVA")

        if not st.session_state.portal_chat:
            st.markdown(
                f"<div style='background:#ffffff;border:1px solid #ddd;"
                f"border-radius:18px 18px 18px 4px;padding:10px 14px;"
                f"margin:6px 0;font-size:14px;color:#111;'>"
                f"🤖 <strong>NOVA</strong>: Hi {nom}! I can answer any questions about "
                f"Novartis products, clinical data, or patient support programs.</div>",
                unsafe_allow_html=True,
            )

        for msg in st.session_state.portal_chat:
            if msg["role"] == "user":
                st.markdown(
                    f"<div style='background:#f5f5f5;border:1px solid #e0e0e0;"
                    f"border-radius:18px 18px 4px 18px;padding:10px 14px;"
                    f"margin:6px 0;font-size:14px;color:#111;'>{msg['content']}</div>",
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f"<div style='background:#ffffff;border:1px solid #ddd;"
                    f"border-radius:18px 18px 18px 4px;padding:10px 14px;"
                    f"margin:6px 0;font-size:14px;color:#111;'>"
                    f"🤖 <strong>NOVA</strong>: {msg['content']}</div>",
                    unsafe_allow_html=True,
                )

        with st.form(key="portal_chat_form", clear_on_submit=True):
            user_input = st.text_input(
                "q", placeholder="e.g. What is the dosing for Entresto?",
                label_visibility="collapsed",
            )
            if st.form_submit_button("Send ➤") and user_input.strip():
                st.session_state.portal_chat.append({"role": "user", "content": user_input})
                st.session_state.portal_chat.append({"role": "nova", "content": nova_customer_reply(user_input)})
                st.rerun()