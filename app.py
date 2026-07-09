import os
import streamlit as st

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Ouzidane Reda | Portfolio",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

IMG_DIR = "images"


def img_path(filename: str) -> str | None:
    path = os.path.join(IMG_DIR, filename)
    return path if os.path.exists(path) else None


def safe_image(filename: str, caption: str = "", use_container_width: bool = True):
    """Render an image if present, otherwise a placeholder box explaining what's missing."""
    path = img_path(filename)
    if path:
        st.image(path, caption=caption, use_container_width=use_container_width)
    else:
        st.markdown(
            f"""
            <div class="img-placeholder">
                <span>📷 Ajouter <code>images/{filename}</code></span>
            </div>
            """,
            unsafe_allow_html=True,
        )


# ---------------------------------------------------------------------------
# Styling
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .stApp {
        background: radial-gradient(circle at 15% 0%, #12222b 0%, #0b1418 45%, #090f12 100%);
        color: #e6edf0;
    }

    section[data-testid="stSidebar"] {
        background: #0d1a20;
        border-right: 1px solid rgba(45, 212, 191, 0.15);
    }

    h1, h2, h3, h4 { color: #f2f7f6 !important; font-weight: 700 !important; }

    .accent { color: #2dd4bf; }

    .hero-card {
        background: linear-gradient(135deg, rgba(45,212,191,0.08), rgba(56,189,248,0.04));
        border: 1px solid rgba(45,212,191,0.25);
        border-radius: 18px;
        padding: 2rem 2.2rem;
    }

    .badge {
        display: inline-block;
        padding: 0.28rem 0.75rem;
        margin: 0.18rem 0.3rem 0.18rem 0;
        border-radius: 999px;
        background: rgba(45,212,191,0.12);
        border: 1px solid rgba(45,212,191,0.35);
        color: #7ee8d8;
        font-size: 0.82rem;
        font-weight: 500;
    }

    .badge-open {
        background: rgba(34,197,94,0.15);
        border: 1px solid rgba(34,197,94,0.45);
        color: #86efac;
    }

    .card {
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 1.4rem 1.5rem;
        margin-bottom: 1.1rem;
        transition: border-color 0.2s ease, transform 0.2s ease;
    }
    .card:hover {
        border-color: rgba(45,212,191,0.4);
        transform: translateY(-2px);
    }

    .card h4 { margin-bottom: 0.15rem !important; }
    .card .meta { color: #8fa3a8; font-size: 0.88rem; margin-bottom: 0.6rem; }
    .card .impact {
        color: #2dd4bf;
        font-weight: 600;
        font-size: 0.85rem;
        margin-top: 0.5rem;
    }

    .cert-chip {
        background: rgba(56,189,248,0.06);
        border: 1px solid rgba(56,189,248,0.25);
        border-radius: 12px;
        padding: 0.7rem 0.9rem;
        margin-bottom: 0.6rem;
        font-size: 0.88rem;
    }
    .cert-chip b { color: #e6edf0; }
    .cert-chip span { color: #7fb8d6; font-size: 0.78rem; }

    .img-placeholder {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 180px;
        border: 1.5px dashed rgba(255,255,255,0.18);
        border-radius: 14px;
        color: #6b7d82;
        font-size: 0.85rem;
        background: rgba(255,255,255,0.02);
        text-align: center;
        padding: 1rem;
    }

    .stat-box {
        text-align: center;
        padding: 0.9rem 0.5rem;
        border-radius: 14px;
        background: rgba(255,255,255,0.03);
        border: 1px solid rgba(255,255,255,0.08);
    }
    .stat-box .num { font-size: 1.6rem; font-weight: 800; color: #2dd4bf; }
    .stat-box .lbl { font-size: 0.78rem; color: #9db0b5; text-transform: uppercase; letter-spacing: 0.04em; }

    a { color: #5eead4 !important; }

    hr { border-color: rgba(255,255,255,0.08); }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Data
# ---------------------------------------------------------------------------
EXPERIENCE = [
    {
        "role": "PFE Intern – Industry 4.0 & Digitalization Consultant",
        "org": "DOUNITEX Confection SA",
        "period": "Mars 2026 – Juin 2026 · 4 mois",
        "desc": "Conception et déploiement d'un Warehouse Management System (WMS) pour optimiser la gestion "
        "des stocks et fluidifier les flux logistiques. Analyse des processus existants, identification des "
        "goulots d'étranglement (suivi manuel, incohérences de données, retards d'information) et déploiement "
        "d'une solution digitale centralisée.",
        "impact": "Gain d'efficacité opérationnelle estimé à +30% · Impact 240 000 MAD/an",
        "image": "pfe_defense.jpg",
    },
    {
        "role": "Stagiaire (PFA) – Full Stack Web Developer @ CAPN",
        "org": "ESITH Digital Center",
        "period": "Juillet 2025 · 1 mois",
        "desc": "Développement d'outils web pour la digitalisation des processus internes. Conception d'APIs "
        "RESTful robustes avec la stack MERN (MongoDB, Express.js, React.js, Node.js).",
        "impact": None,
        "image": None,
    },
    {
        "role": "Bug Bounty Hunter",
        "org": "HackerOne · Temps partiel · À distance",
        "period": "Décembre 2024 – Juillet 2025 · 8 mois",
        "desc": "Recherche active de vulnérabilités de sécurité sur des applications web, APIs et infrastructures "
        "pour aider les organisations à sécuriser leurs actifs numériques.",
        "impact": None,
        "image": None,
    },
    {
        "role": "Internship Trainee",
        "org": "Stellantis · Kénitra, Maroc",
        "period": "Juin 2024 · 1 mois",
        "desc": "Optimisation des processus de contrôle des pièces pour le département EUP. Analyse des causes "
        "racines (Ishikawa, 5 Whys), conception de workflows Lean Manufacturing et proposition de KPIs/dashboards.",
        "impact": None,
        "image": None,
    },
]

EDUCATION = [
    {
        "school": "ESITH Casablanca",
        "degree": "Ingénieur d'État en Génie Industriel",
        "period": "2023 – 2026",
        "desc": "Spécialisation Production Management & Optimization · Lean, Six Sigma, technologies digitales, "
        "modèles d'optimisation, simulation et IA appliqués à l'Industrie 4.0.",
        "image": "esith_logo.png",
    },
    {
        "school": "CPGE – Classes préparatoires aux grandes écoles",
        "degree": "Physique, Math et Sciences de l'Ingénieur (PCSI / PSI)",
        "period": "Déc. 2021 – Févr. 2023",
        "desc": "Lycée Prince Héritier Moulay El Hassan, Ouarzazate.",
        "image": None,
    },
]

HACKATHONS = [
    {
        "title": "CITx.C 2026 Innovation Competition — IEEE ICCITX.0",
        "result": "🏆 Winner · 5 000 MAD",
        "desc": "SecureProd sélectionné Top 10 parmi 77 projets de 5 pays. Solution de cybersécurité "
        "industrielle IA pour l'Industrie 4.0 et le Smart Manufacturing.",
        "image": "hackathon_collage.png",
    },
    {
        "title": "AI for Industry Hackathon — Teal Technology Services",
        "result": "🥇 1st Place · 30 000 MAD",
        "desc": "SecureProd : surveillance proactive, détection d'anomalies par IA et communications "
        "sécurisées pour environnements SCADA/ICS. Avec Kaouthar Belkebir.",
        "image": None,
    },
    {
        "title": "Hackathon — ACCEDE Internationale",
        "result": "🥇 1st Place · 10 000 MAD",
        "desc": "Développement de Vamosway, une application web, en équipe.",
        "image": None,
    },
    {
        "title": "Game4Health Hackathon — ISMAGI Rabat",
        "result": "🥈 2nd Place · 6 000 MAD",
        "desc": "NEURO FIT : plateforme de rééducation par IA utilisant des signaux EMG de surface en temps réel "
        "pour gamifier la kinésithérapie. Précision de 93%, suivi de la fatigue et rapports cliniques automatisés.",
        "image": None,
    },
    {
        "title": "AI for Social Impact Hackathon — ESITH Casablanca",
        "result": "🥈 2nd Place",
        "desc": "Solution IA multidisciplinaire répondant à un enjeu social réel.",
        "image": None,
    },
]

CERTIFICATIONS = [
    ("Six Sigma Green Belt", "Coursera"),
    ("Google Data Analytics", "Google"),
    ("Data Science", "DataCamp"),
    ("Google Project Management", "Google"),
    ("Data Science", "IBM"),
    ("API Penetration Testing", "APIsec University"),
    ("CS50x", "Harvard University"),
    ("Windows Privilege Escalation", "Hack The Box"),
    ("Attacking Common Applications", "Hack The Box"),
    ("AD Enumeration & Attacks", "Hack The Box"),
    ("Web-Attacks", "Hack The Box"),
    ("Fortinet Certified Associate Cybersecurity", "Fortinet"),
    ("Ethical Hacking Essentials (EHE)", "EC-Council"),
    ("Jr Penetration Tester", "TryHackMe"),
    ("Offensive Pentesting", "TryHackMe"),
    ("Red-Team (Top 5%)", "TryHackMe"),
    ("Junior Cybersecurity Analyst Career Path", "Cisco"),
    ("Ethical Hacker", "Cisco"),
]

SKILLS = [
    "Penetration Testing", "Red Teaming", "Web Exploitation (XSS, SQLi, IDOR, SSRF)",
    "JWT / Auth Attacks", "Active Directory Attacks", "Reverse Engineering",
    "Warehouse Management Systems (WMS)", "Lean Six Sigma", "Industry 4.0",
    "Data Analytics", "Machine Learning", "MERN Stack (MongoDB, Express, React, Node)",
    "Process Optimization", "Supply Chain & Logistique",
]

CONTACT = {
    "linkedin": "https://www.linkedin.com/in/ouzidane-reda-a9b010295",
    "location": "Casablanca-Settat, Maroc",
    "tagline": "$ whoami → \"An engineer who understands hacking and systems deeply.\"",
}

# ---------------------------------------------------------------------------
# Sidebar navigation
# ---------------------------------------------------------------------------
with st.sidebar:
    safe_image("profile_photo.jpg", use_container_width=True)
    st.markdown("### Ouzidane Reda")
    st.caption("Ingénieur d'État en Génie Industriel")
    st.markdown(
        '<span class="badge badge-open">🟢 Open to work</span>',
        unsafe_allow_html=True,
    )
    st.markdown("---")
    section = st.radio(
        "Navigation",
        ["Accueil", "Expérience", "Hackathons & Projets", "Formation", "Certifications", "Contact"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown(f"[🔗 Profil LinkedIn]({CONTACT['linkedin']})")
    st.caption(f"📍 {CONTACT['location']}")

# ---------------------------------------------------------------------------
# Hero (always visible at top)
# ---------------------------------------------------------------------------
st.markdown(
    f"""
    <div class="hero-card">
        <h1>Ouzidane Reda</h1>
        <p style="font-size:1.15rem; color:#b7c6ca; margin-top:-0.6rem;">
            Ingénieur d'État en Génie Industriel · Passionné de Cybersécurité & Industrie 4.0
        </p>
        <p style="font-family: monospace; color:#5eead4; margin-top:0.8rem;">{CONTACT['tagline']}</p>
        <div style="margin-top:0.8rem;">
            <span class="badge">🏭 Génie Industriel</span>
            <span class="badge">🔐 Cybersécurité</span>
            <span class="badge">🤖 IA Appliquée</span>
            <span class="badge">📦 Supply Chain</span>
            <span class="badge">⚙️ Industrie 4.0</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

stat_cols = st.columns(5)
stats = [
    ("6+", "Hackathons gagnés"),
    ("18", "Certifications"),
    ("2 968", "Abonnés LinkedIn"),
    ("500+", "Relations"),
    ("3", "Pays représentés (IEEE)"),
]
for col, (num, lbl) in zip(stat_cols, stats):
    with col:
        st.markdown(
            f'<div class="stat-box"><div class="num">{num}</div><div class="lbl">{lbl}</div></div>',
            unsafe_allow_html=True,
        )

st.write("")

# ---------------------------------------------------------------------------
# Sections
# ---------------------------------------------------------------------------
if section == "Accueil":
    st.header("À propos")
    st.write(
        "Ingénieur d'État en Génie Industriel fraîchement diplômé de l'ESITH Casablanca (2023–2026), "
        "combinant une expertise en optimisation des processus industriels (Lean, Six Sigma, Industrie 4.0) "
        "avec une passion approfondie pour la cybersécurité offensive. Lauréat de plusieurs hackathons nationaux "
        "et finaliste d'une compétition internationale IEEE, j'aime construire des solutions concrètes — d'un "
        "Warehouse Management System industriel à une plateforme de cybersécurité SCADA/ICS pilotée par l'IA."
    )

    st.subheader("Compétences")
    st.markdown(
        "".join(f'<span class="badge">{s}</span>' for s in SKILLS),
        unsafe_allow_html=True,
    )

    st.subheader("Aperçu du parcours")
    c1, c2 = st.columns(2)
    with c1:
        safe_image("hackathon_collage.png", caption="Hackathons & compétitions")
    with c2:
        safe_image("pfe_defense.jpg", caption="Soutenance PFE — WMS chez DOUNITEX")

elif section == "Expérience":
    st.header("Expérience professionnelle")
    for exp in EXPERIENCE:
        with st.container():
            if exp["image"]:
                c1, c2 = st.columns([1, 2.4])
                with c1:
                    safe_image(exp["image"])
                with c2:
                    st.markdown(
                        f"""
                        <div class="card">
                            <h4>{exp['role']}</h4>
                            <div class="meta">{exp['org']} · {exp['period']}</div>
                            <p>{exp['desc']}</p>
                            {f'<div class="impact">📈 {exp["impact"]}</div>' if exp['impact'] else ''}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
            else:
                st.markdown(
                    f"""
                    <div class="card">
                        <h4>{exp['role']}</h4>
                        <div class="meta">{exp['org']} · {exp['period']}</div>
                        <p>{exp['desc']}</p>
                        {f'<div class="impact">📈 {exp["impact"]}</div>' if exp['impact'] else ''}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

elif section == "Hackathons & Projets":
    st.header("Hackathons & Projets")
    cols = st.columns(2)
    for i, h in enumerate(HACKATHONS):
        with cols[i % 2]:
            safe_image(h["image"] or "hackathon_placeholder.png")
            st.markdown(
                f"""
                <div class="card">
                    <h4>{h['title']}</h4>
                    <div class="meta">{h['result']}</div>
                    <p>{h['desc']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

elif section == "Formation":
    st.header("Formation")
    for edu in EDUCATION:
        c1, c2 = st.columns([1, 2.4])
        with c1:
            safe_image(edu["image"] or "school_placeholder.png")
        with c2:
            st.markdown(
                f"""
                <div class="card">
                    <h4>{edu['school']}</h4>
                    <div class="meta">{edu['degree']} · {edu['period']}</div>
                    <p>{edu['desc']}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

elif section == "Certifications":
    st.header("Certifications (18)")
    st.caption("Cybersécurité, Data & Management")
    cols = st.columns(3)
    for i, (name, issuer) in enumerate(CERTIFICATIONS):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="cert-chip">
                    <b>{name}</b><br/><span>{issuer}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

elif section == "Contact":
    st.header("Contact")
    st.write(
        "Ouvert aux opportunités en tant qu'Ingénieur Industriel, Ingénieur IA, Software Engineer ou "
        "Ingénieur Transformation Digitale."
    )
    st.markdown(f"🔗 **LinkedIn** : [{CONTACT['linkedin']}]({CONTACT['linkedin']})")
    st.markdown(f"📍 **Localisation** : {CONTACT['location']}")
    st.markdown("🏢 **Entreprise actuelle** : DOUNITEX Confection SA")
    st.markdown("🎓 **Formation** : ESITH Casablanca")

st.markdown("---")
st.caption("Portfolio généré avec Streamlit · Données issues du profil LinkedIn de Ouzidane Reda")
