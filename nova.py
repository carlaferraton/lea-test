import streamlit as st

SEGMENTS = {
    " Healthcare Professionals (HCPs)": [
        "Cardiologists", "Dermatologists", "Oncologists",
        "Neurologists", "General Practitioners",
    ],
    " Pharmacists": [
        "Hospital Pharmacists", "Retail Pharmacists",
    ],
    " Payers & Institutions": [
        "Insurers / Payers", "Hospital Procurement",
    ],
    " Key Opinion Leaders (KOLs)": ["KOL Network"],
    " Patient Associations": ["Patient Associations"],
}

PROFILS = {
    "Cardiologists": [
        {"avatar": "👨‍⚕️", "name": "Dr. F. Müller",    "institution": "Zurich University Hospital",  "preference": "Email"},
        {"avatar": "👩‍⚕️", "name": "Dr. L. Schmidt",   "institution": "Private practice, Basel",      "preference": "Phone call"},
        {"avatar": "👩‍⚕️", "name": "Dr. A. Chavez",    "institution": "CHUV, Lausanne",               "preference": "In-person"},
        {"avatar": "👨‍⚕️", "name": "Dr. R. Patel",     "institution": "HUG, Geneva",                  "preference": "Video call"},
    ],
    "Dermatologists": [
        {"avatar": "👩‍⚕️", "name": "Dr. M. Bernard",   "institution": "Derma Clinic Bern",            "preference": "Email"},
        {"avatar": "👨‍⚕️", "name": "Dr. K. Nakamura",  "institution": "Zurich University Hospital",   "preference": "Phone call"},
        {"avatar": "👩‍⚕️", "name": "Dr. T. Ait-Kaci",  "institution": "Private practice, Geneva",     "preference": "Email"},
    ],
    "Oncologists": [
        {"avatar": "👩‍⚕️", "name": "Dr. S. Roche",     "institution": "HUG — Oncology dept.",         "preference": "Phone call"},
        {"avatar": "👨‍⚕️", "name": "Prof. B. Liang",   "institution": "Swiss Cancer Center",           "preference": "In-person"},
    ],
    "Neurologists": [
        {"avatar": "👩‍⚕️", "name": "Dr. E. Villanueva","institution": "CHUV — Neurology",              "preference": "Video call"},
        {"avatar": "👨‍⚕️", "name": "Dr. J. Perret",    "institution": "Private practice",              "preference": "Email"},
    ],
    "General Practitioners": [
        {"avatar": "👩‍⚕️", "name": "Dr. M. Dufour",    "institution": "Medical practice, Nyon",        "preference": "Email"},
        {"avatar": "👨‍⚕️", "name": "Dr. H. Weber",     "institution": "Group practice, Aarau",         "preference": "Phone call"},
        {"avatar": "👩‍⚕️", "name": "Dr. L. Keller",    "institution": "Olten Health Center",           "preference": "In-person"},
        {"avatar": "👨‍⚕️", "name": "Dr. N. Amghar",    "institution": "Geneva South district",         "preference": "Video call"},
    ],
    "Hospital Pharmacists": [
        {"avatar": "👩‍⚕️", "name": "P. Girardin",      "institution": "CHUV Pharmacy",                "preference": "Email"},
        {"avatar": "👨‍⚕️", "name": "O. Klose",         "institution": "Inselspital Bern",             "preference": "Phone call"},
    ],
    "Retail Pharmacists": [
        {"avatar": "👩‍⚕️", "name": "C. Costas",        "institution": "Amavita Lausanne",             "preference": "Email"},
        {"avatar": "👨‍⚕️", "name": "D. Russo",         "institution": "Coop Vitality Zurich",         "preference": "Phone call"},
    ],
    "Insurers / Payers": [
        {"avatar": "👨‍💼", "name": "M. Hofer",          "institution": "Groupe Mutuel",                "preference": "Email"},
        {"avatar": "👩‍💼", "name": "T. Nguyen",         "institution": "CSS Insurance",                "preference": "Phone call"},
    ],
    "Hospital Procurement": [
        {"avatar": "👨‍💼", "name": "A. Rey",            "institution": "HUG — Procurement",           "preference": "In-person"},
    ],
    "KOL Network": [
        {"avatar": "👨‍🏫", "name": "Prof. P. Burnier",  "institution": "EPFL / Cardiology",            "preference": "Email"},
        {"avatar": "👩‍🏫", "name": "Prof. M. Studer",   "institution": "University of Zurich",         "preference": "In-person"},
    ],
    "Patient Associations": [
        {"avatar": "🤝", "name": "H. Favre",            "institution": "SwissHeart Foundation",        "preference": "Email"},
        {"avatar": "🤝", "name": "G. Lombard",          "institution": "Psoriasis Switzerland",        "preference": "Phone call"},
    ],
}

SUGGESTIONS = [
    {"priority": "🔴 High priority", "text": "Dr. Müller (cardiology) hasn't been contacted in 6 weeks — new clinical data now available."},
    {"priority": "🟡 Follow-up",     "text": "PharmaPlus Zurich submitted 3 questions via the NOVA app — a call today could be valuable."},
    {"priority": "🟢 Opportunity",   "text": "A Groupe Mutuel representative is active on product pages — good moment to reach out."},
]

PRODUCTS = [
    {"tag": "Cardiology",    "name": "Entresto",  "desc": "Sacubitril/valsartan for chronic heart failure. 20% relative risk reduction in cardiovascular death vs enalapril (PARADIGM-HF)."},
    {"tag": "Cardiology",    "name": "Leqvio",    "desc": "Inclisiran — twice-yearly injection reducing LDL-C by ~50%. RNA interference mechanism targeting PCSK9."},
    {"tag": "Oncology",      "name": "Kisqali",   "desc": "Ribociclib for HR+/HER2- breast cancer in combination with an aromatase inhibitor."},
    {"tag": "Dermatology",   "name": "Cosentyx",  "desc": "Secukinumab for moderate-to-severe plaque psoriasis, psoriatic arthritis, and ankylosing spondylitis."},
]

FAQ = [
    {"question": "What is the dosing schedule for Leqvio?",          "count": 87, "answer": "Leqvio is administered as a 284 mg subcutaneous injection: first dose, again at 3 months, then every 6 months thereafter."},
    {"question": "Does Entresto require dose titration?",             "count": 64, "answer": "Yes. Start at 49/51 mg twice daily, titrate up to 97/103 mg twice daily as tolerated. Allow a 36-hour washout when switching from an ACE inhibitor."},
    {"question": "Are there patient support programs available?",     "count": 51, "answer": "Yes, Novartis offers patient support programs including financial assistance, monitoring tools, and dedicated helplines. Contact your local Novartis representative for details."},
    {"question": "What are the contraindications for Kisqali?",      "count": 39, "answer": "Contraindicated in patients with QT interval prolongation, severe hepatic impairment, or hypersensitivity to ribociclib. ECG monitoring is recommended at treatment initiation."},
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
        return "**Entresto (sacubitril/valsartan)**: Start at 49/51 mg twice daily, titrate to 97/103 mg twice daily. Allow a 36-hour washout if switching from an ACE inhibitor. Demonstrated a 20% reduction in cardiovascular death vs enalapril (PARADIGM-HF)."
    if "leqvio" in q or "inclisiran" in q:
        return "**Leqvio (inclisiran)**: 284 mg subcutaneous injection at Day 0, Month 3, then every 6 months. Reduces LDL-C by approximately 50% through RNA interference targeting PCSK9."
    if "kisqali" in q:
        return "**Kisqali (ribociclib)**: 600 mg/day for 21 days followed by 7 days off. Indicated for HR+/HER2- breast cancer. ECG monitoring is recommended due to QT prolongation risk."
    if "cosentyx" in q:
        return "**Cosentyx (secukinumab)**: Subcutaneous injection. Indicated for plaque psoriasis, psoriatic arthritis, and ankylosing spondylitis. Monthly induction then maintenance every 4 weeks."
    if "program" in q or "patient" in q or "support" in q:
        return "Novartis offers patient support programs including financial assistance, monitoring tools, and dedicated helplines. Contact your local Novartis representative for regional details."
    return "I can answer questions about any Novartis product — Entresto, Leqvio, Kisqali, Cosentyx, and more. What would you like to know?"

st.set_page_config(page_title="NOVA by Novartis", layout="wide")

st.markdown("""
<style>
    .nova-title { color: #C8102E; font-size: 2.5rem; font-weight: 700; text-align: center; }
    .nova-subtitle { text-align: center; color: #888; font-size: 0.85rem; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 2rem; }
    .chat-user { background-color: #C8102E; color: white; padding: 10px 14px; border-radius: 18px 18px 4px 18px; margin: 6px 0; max-width: 80%; margin-left: auto; font-size: 0.9rem; }
    .chat-nova { background-color: #f0f0f0; color: #222; padding: 10px 14px; border-radius: 18px 18px 18px 4px; margin: 6px 0; max-width: 80%; font-size: 0.9rem; }
    .nova-badge { background-color: #C8102E; color: white; padding: 2px 10px; border-radius: 20px; font-size: 0.75rem; font-weight: 600; }
    .product-tag { background-color: #fce8eb; color: #C8102E; padding: 2px 10px; border-radius: 20px; font-size: 0.75rem; display: inline-block; margin-bottom: 6px; }
</style>
""", unsafe_allow_html=True)

defaults = {
    "page": "login",
    "emp_segment": "Cardiologists",
    "emp_chat": [],
    "portal_chat": [],
    "suggestions": list(SUGGESTIONS),
    "customer_profile": {},
    "new_customers": [],
}
for k, v in defaults.items():
    if k not in st.session_state:
        st.session_state[k] = v

if st.session_state.page == "login":
    st.markdown('<p class="nova-title">nova</p>', unsafe_allow_html=True)
    st.markdown('<p class="nova-subtitle">by Novartis</p>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1.2, 1])
    with col2:
        st.subheader("Welcome")
        role = st.radio("I am a:", ["Novartis Employee", "Healthcare Professional / Customer"])
        if st.button(" Sign in", use_container_width=True, type="primary"):
            st.session_state.page = "employee" if role == "Novartis Employee" else "register"
            st.rerun()

elif st.session_state.page == "employee":
    col_logo, _, col_user = st.columns([2, 6, 2])
    with col_logo:
        st.markdown("# **Nova**")
    with col_user:
        st.markdown("👤 Sophie C.")
        if st.button("Sign out", key="emp_logout"):
            st.session_state.page = "login"
            st.rerun()
    st.divider()
    st.markdown('<span class="nova-badge">NOVA AI</span> &nbsp; Today\'s suggestions — *you decide whether to act on them*', unsafe_allow_html=True)
    if st.session_state.suggestions:
        cols = st.columns(len(st.session_state.suggestions))
        to_remove = None
        for i, (col, sug) in enumerate(zip(cols, st.session_state.suggestions)):
            with col:
                st.markdown(f"""<div style="border:1px solid #eee; border-radius:10px; padding:12px; background:white;">
                    <div style="color:#C8102E; font-weight:600; font-size:0.8rem;">{sug['priority']}</div>
                    <div style="font-size:0.85rem; margin-top:4px;">{sug['text']}</div></div>""", unsafe_allow_html=True)
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
            st.markdown(f"**{group_name}**")
            for seg_name in subsegments:
                if st.button(seg_name, key=f"seg_{seg_name}", use_container_width=True):
                    st.session_state.emp_segment = seg_name
                    st.session_state.emp_chat = []
                    st.rerun()
            st.markdown("")
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
            cols = st.columns(min(len(profils), 4))
            for col, p in zip(cols, profils):
                with col:
                    st.markdown(f"""<div style="border:1px solid #eee; border-radius:10px; padding:12px; background:white; text-align:center;">
                        <div style="font-size:1.8rem;">{p['avatar']}</div>
                        <div style="font-weight:600; font-size:0.9rem;">{p['name']}</div>
                        <div style="color:#888; font-size:0.78rem;">{p['institution']}</div>
                        <div style="background:#fce8eb; color:#C8102E; border-radius:20px; padding:2px 8px; font-size:0.72rem; margin-top:6px; display:inline-block;">{p['preference']}</div>
                    </div>""", unsafe_allow_html=True)
        st.markdown("")
        st.markdown("##### 💬 Ask NOVA")
        for msg in st.session_state.emp_chat:
            if msg["role"] == "user":
                st.markdown(f'<div class="chat-user">{msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-nova">🤖 <b>NOVA</b>: {msg["content"]}</div>', unsafe_allow_html=True)
        with st.form(key="emp_chat_form", clear_on_submit=True):
            user_input = st.text_input("Question", placeholder="e.g. What is the best time to contact Dr. Müller?", label_visibility="collapsed")
            if st.form_submit_button("Send ➤") and user_input.strip():
                st.session_state.emp_chat.append({"role": "user", "content": user_input})
                st.session_state.emp_chat.append({"role": "nova", "content": nova_employee_reply(user_input, seg)})
                st.rerun()

elif st.session_state.page == "register":
    st.markdown('<p class="nova-title">nova</p>', unsafe_allow_html=True)
    st.markdown('<p class="nova-subtitle">Create your account</p>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        with st.form("register_form"):
            col_a, col_b = st.columns(2)
            with col_a:
                prenom = st.text_input("First name", placeholder="Marie")
            with col_b:
                nom = st.text_input("Last name", placeholder="Dupont")
            secteur = st.selectbox("Sector", [
                "Healthcare Professional (HCP)", "Hospital Pharmacist",
                "Retail Pharmacist", "Payer / Insurance",
                "Hospital Procurement", "Key Opinion Leader (KOL)",
                "Patient Association",
            ])
            specialite = None
            if "HCP" in secteur or "KOL" in secteur:
                specialite = st.selectbox("Speciality", ["Cardiology", "Dermatology", "Oncology", "Neurology", "General Medicine"])
            lieu = st.text_input("Place of work", placeholder="HUG – Geneva")
            contact_pref = st.multiselect("Preferred contact method", ["Email", "Phone call", "Video call", "In-person visit"], default=["Email"])
            if st.form_submit_button("✅ Create my account", use_container_width=True, type="primary"):
                st.session_state.customer_profile = {"name": f"{prenom} {nom}", "sector": secteur, "specialite": specialite, "lieu": lieu, "preferences": contact_pref}
                st.session_state.new_customers.append({"name": f"{prenom} {nom}", "sector": secteur})
                st.session_state.page = "portal"
                st.rerun()
        if st.button("← Back"):
            st.session_state.page = "login"
            st.rerun()

elif st.session_state.page == "portal":
    profil = st.session_state.customer_profile
    nom = profil.get("name", "User")
    col_logo, _, col_user = st.columns([2, 5, 3])
    with col_logo:
        st.markdown("# **Nova**")
    with col_user:
        st.markdown(f"👤 **{nom}**")
        if st.button("Sign out", key="portal_logout"):
            st.session_state.page = "login"
            st.rerun()
    st.divider()
    col_products, col_chat = st.columns([2, 1])
    with col_products:
        st.markdown("#### Novartis Products")
        for i in range(0, len(PRODUCTS), 2):
            cols = st.columns(2)
            for j, col in enumerate(cols):
                if i + j < len(PRODUCTS):
                    p = PRODUCTS[i + j]
                    with col:
                        st.markdown(f"""<div style="border:1px solid #eee; border-radius:10px; padding:14px; background:white; margin-bottom:10px;">
                            <span class="product-tag">{p['tag']}</span>
                            <div style="font-weight:700; font-size:1rem;">{p['name']}</div>
                            <div style="color:#666; font-size:0.83rem; margin-top:4px;">{p['desc']}</div>
                        </div>""", unsafe_allow_html=True)
        st.markdown("#### ❓ Frequently asked questions")
        st.caption("These questions are also visible to the Novartis marketing team")
        for faq in FAQ:
            with st.expander(f"{faq['question']} — *asked {faq['count']} times*"):
                st.write(faq["answer"])
    with col_chat:
        st.markdown("#### 💬 Ask NOVA")
        if not st.session_state.portal_chat:
            st.markdown(f'<div class="chat-nova">🤖 <b>NOVA</b>: Hi {nom}! I can answer any questions about Novartis products, clinical data, or patient support programs.</div>', unsafe_allow_html=True)
        for msg in st.session_state.portal_chat:
            if msg["role"] == "user":
                st.markdown(f'<div class="chat-user">{msg["content"]}</div>', unsafe_allow_html=True)
            else:
                st.markdown(f'<div class="chat-nova">🤖 <b>NOVA</b>: {msg["content"]}</div>', unsafe_allow_html=True)
        with st.form(key="portal_chat_form", clear_on_submit=True):
            user_input = st.text_input("Question", placeholder="e.g. What is the dosing for Entresto?", label_visibility="collapsed")
            if st.form_submit_button("Send ➤") and user_input.strip():
                st.session_state.portal_chat.append({"role": "user", "content": user_input})
                st.session_state.portal_chat.append({"role": "nova", "content": nova_customer_reply(user_input)})
                st.rerun()
