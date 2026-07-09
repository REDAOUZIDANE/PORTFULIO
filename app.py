import os
import streamlit as st

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Ouzidane Reda | Portfolio",
    page_icon="R",
    layout="wide",
    initial_sidebar_state="expanded",
)

IMG_DIR = "images"
UPLOAD_DIR = os.path.join(IMG_DIR, "uploads")
CV_PATH = os.path.join("documents", "CV_Ouzidane_Reda.pdf")


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
                <span>Ajouter <code>images/{filename}</code></span>
            </div>
            """,
            unsafe_allow_html=True,
        )


def get_admin_password() -> str:
    try:
        return st.secrets["ADMIN_PASSWORD"]
    except Exception:
        return os.environ.get("ADMIN_PASSWORD", "changeme123")


def cv_download_button(key: str):
    if os.path.exists(CV_PATH):
        with open(CV_PATH, "rb") as f:
            st.download_button(
                "Télécharger le CV (PDF)",
                f,
                file_name="CV_Ouzidane_Reda.pdf",
                mime="application/pdf",
                use_container_width=True,
                key=key,
            )


# ---------------------------------------------------------------------------
# Styling
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400;600;700&family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] { font-family: 'Inter', sans-serif; }

    .stApp {
        background: #10131a;
        color: #e6e9ee;
    }

    section[data-testid="stSidebar"] {
        background: #0c0e13;
        border-right: 1px solid #232833;
    }

    h1, h2, h3, h4 {
        font-family: 'Source Serif 4', Georgia, serif !important;
        color: #f2f3f5 !important;
        font-weight: 600 !important;
        letter-spacing: -0.01em;
    }

    .hero-card {
        background: #151920;
        border: 1px solid #262c38;
        border-left: 3px solid #6f93b8;
        border-radius: 6px;
        padding: 2.2rem 2.4rem;
    }

    .status-dot {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #4caf7d;
        margin-right: 0.5rem;
    }

    .badge {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        margin: 0.2rem 0.35rem 0.2rem 0;
        border-radius: 4px;
        background: #1a1f28;
        border: 1px solid #2a3038;
        color: #b7c1cc;
        font-size: 0.8rem;
        font-weight: 500;
        letter-spacing: 0.01em;
    }

    .card {
        background: #151920;
        border: 1px solid #232833;
        border-radius: 6px;
        padding: 1.5rem 1.7rem;
        margin-bottom: 1.2rem;
    }
    .card:hover { border-color: #3a4250; }

    .card h4 { margin-bottom: 0.2rem !important; font-size: 1.15rem !important; }
    .card .meta { color: #838d99; font-size: 0.85rem; margin-bottom: 0.5rem; }
    .card .eyebrow {
        text-transform: uppercase;
        letter-spacing: 0.08em;
        font-size: 0.72rem;
        color: #6f93b8;
        font-weight: 600;
        margin-bottom: 0.3rem;
    }
    .card .result {
        color: #c9a15a;
        font-weight: 600;
        font-size: 0.88rem;
        margin-top: 0.4rem;
    }

    .cert-chip {
        background: #151920;
        border: 1px solid #232833;
        border-radius: 6px;
        padding: 0.75rem 1rem;
        margin-bottom: 0.6rem;
        font-size: 0.87rem;
    }
    .cert-chip b { color: #e6e9ee; }
    .cert-chip span { color: #838d99; font-size: 0.78rem; }

    .img-placeholder {
        display: flex;
        align-items: center;
        justify-content: center;
        height: 170px;
        border: 1px dashed #2a3038;
        border-radius: 6px;
        color: #5c6672;
        font-size: 0.82rem;
        background: #12151b;
        text-align: center;
        padding: 1rem;
    }

    .stat-box {
        text-align: center;
        padding: 1rem 0.5rem;
        border-radius: 6px;
        background: #151920;
        border: 1px solid #232833;
    }
    .stat-box .num {
        font-family: 'Source Serif 4', serif;
        font-size: 1.7rem;
        font-weight: 700;
        color: #eef1f4;
    }
    .stat-box .lbl {
        font-size: 0.74rem;
        color: #838d99;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-top: 0.2rem;
    }

    a { color: #8fb2d6 !important; text-decoration: none !important; }
    a:hover { text-decoration: underline !important; }

    hr { border-color: #232833; }

    table td { border-bottom: 1px solid #1e232c; }
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

PROJECTS = [
    {
        "title": "SecureProd — AI-Assisted Intrusion Detection for SCADA/ICS",
        "category": "Cybersécurité / Industrie 4.0",
        "meta": "Équipe Secure Prod (avec Kaouthar Belkebir) · Teal Technology Services · Jul. 2025",
        "result": "1st Place",
        "prize": "30 000 DHS",
        "abstract": "Les réseaux SCADA/ICS ont vu une hausse documentée de 54% des attaques ciblées, tout en "
        "reposant sur des protocoles historiques (Modbus TCP, DNP3) sans authentification ni chiffrement natifs. "
        "SecureProd combine un parsing conscient des protocoles avec un modèle de détection d'anomalies "
        "supervisé pour signaler en temps réel les comportements OT anormaux, et restitue le risque sous forme "
        "de carte de menace 3D pour les opérateurs d'usine. Conçu et livré en 36 heures de hackathon.",
        "specs": [
            ("Protocoles sécurisés", "Modbus TCP, DNP3"),
            ("Méthode de détection", "Modèle supervisé de détection d'anomalies"),
            ("Mode de déploiement", "Tap réseau passif (non-intrusif)"),
            ("Visualisation", "Carte de menace 3D en temps réel"),
            ("Reporting", "Export automatisé prêt pour audit de conformité"),
            ("Fenêtre de développement", "36 heures (format hackathon)"),
        ],
        "images": ["secureprod_logo.png", "secureprod_photo.png"],
    },
    {
        "title": "NEURO FIT — Gamified EMG Biofeedback for Muscular Rehabilitation",
        "category": "Santé Digitale / Gamification",
        "meta": "Équipe ESITH — Reda et al. · Game4Health, ISMAGI Rabat × SmartTech Lab · 4 avr. 2026",
        "result": "2nd Place",
        "prize": "6 000 DHS",
        "abstract": "L'adhérence aux protocoles de rééducation musculaire est limitée par le manque de retour "
        "immédiat des exercices classiques de physiothérapie. NEURO FIT capte le signal EMG de surface (sEMG) "
        "via électrodes à l'avant-bras et transforme l'activation musculaire en gameplay temps réel autour de "
        "trois objectifs — Follow, Avoid, Maintain. Lors d'une démonstration live, le système a atteint une "
        "précision de 93% avec un taux de fatigue détecté de 0% et un rapport de session généré automatiquement "
        "pour le suivi clinique à distance.",
        "specs": [
            ("Source du signal", "EMG de surface, électrodes 2 canaux à l'avant-bras"),
            ("Métriques live", "Score de précision, fatigue musculaire, charge du modèle ML"),
            ("Sortie observée (démo)", "Amplitude temps réel 354 μV, précision 93%, fatigue 0%"),
            ("Modes de jeu", "Follow, Avoid, Maintain"),
            ("Reporting", "Rapport de session automatisé pour suivi clinicien"),
        ],
        "images": ["neurofit_dashboard.png", "neurofit_electrodes.png", "neurofit_presenting.png", "neurofit_award.png"],
    },
    {
        "title": "Vamosway — Full-Stack Mobility & Travel Web Application",
        "category": "Web Application / Mobilité",
        "meta": "Équipe Vamosway · ACCEDE Internationale · Track Sciences et Technologie",
        "result": "1st Place",
        "prize": "10 000 DHS",
        "abstract": "Application web full-stack conçue et livrée dans la fenêtre fixe d'un hackathon pour "
        "répondre à un enjeu de mobilité du track « Sciences et Technologie ». Priorité donnée à un parcours "
        "utilisateur cohérent et fonctionnel plutôt qu'à une exhaustivité des fonctionnalités — cadrage du "
        "problème, conception de l'interface, implémentation et pitch live devant le jury.",
        "specs": [
            ("Livrable", "Application web full-stack"),
            ("Format d'équipe", "Équipe pluridisciplinaire étudiante"),
            ("Critères d'évaluation", "Innovation, utilisabilité, exécution technique"),
            ("Fenêtre de développement", "Format hackathon (budget temps fixe)"),
        ],
        "images": [],
    },
    {
        "title": "AI for Social Impact — Applied Machine Learning Prototype",
        "category": "Intelligence Artificielle Appliquée",
        "meta": "Équipe ESITH — Reda Ouzidane · Hackathon ESITH Casablanca · Track AI for Social Impact",
        "result": "2nd Place",
        "prize": None,
        "abstract": "Prototype IA fonctionnel développé pour répondre à un besoin social réel plutôt qu'à une "
        "simple preuve de concept sur données synthétiques, dans le cadre du track « AI for Social Impact » "
        "de l'ESITH Casablanca. Évalué sur la pertinence par rapport au besoin social, la faisabilité "
        "technique et la qualité d'exécution.",
        "specs": [
            ("Livrable", "Prototype IA fonctionnel"),
            ("Critères d'évaluation", "Pertinence, faisabilité, exécution technique"),
            ("Institution hôte", "ESITH Casablanca"),
        ],
        "images": [],
    },
    {
        "title": "Le Phare de l'Entrepreneuriat — Social-Impact Venture Award",
        "category": "Entrepreneuriat Social",
        "meta": "Reda Ouzidane · KEDGE Business School · 15 mai 2025",
        "result": "Prix Impact Positif & Social",
        "prize": "10 000 DHS",
        "abstract": "Compétition d'entrepreneuriat de KEDGE Business School évaluant les ventures candidates sur "
        "deux axes combinés : viabilité entrepreneuriale et impact social positif démontrable. La venture a été "
        "reconnue pour sa capacité à combiner innovation et création de valeur sociale mesurable, avec un pitch "
        "live à Casablanca.",
        "specs": [
            ("Prix", "Prix Impact Positif & Social"),
            ("Institution hôte", "KEDGE Business School"),
            ("Lieu", "Casablanca, Maroc"),
        ],
        "images": ["le_phare_photo.png"],
    },
    {
        "title": "Industry 4.0, AI & Cybersecurity for Smart Manufacturing",
        "category": "Industrie 4.0 / Smart Manufacturing",
        "meta": "Ouzidane R., Baroudi M., Fahsi Y. · ESITH, Maroc · IEEE ICCITX.0 2026, Paris",
        "result": "Top 10 Finalist",
        "prize": "77 projets · 5 pays",
        "abstract": "Projet de recherche et d'innovation à l'intersection de l'Industrie 4.0, de l'IA, de la "
        "cybersécurité et du smart manufacturing, soumis au concours d'innovation CITx.C 2026. Sélectionné "
        "Top 10 Finaliste parmi 77 projets évalués sur 3 phases, annoncé lors de la session de clôture de la "
        "conférence internationale IEEE ICCITX.0 2026 à Paris, cérémonie de remise des prix le 16 juin 2026.",
        "specs": [
            ("Soumissions évaluées", "77 projets, 5 pays"),
            ("Résultat", "Top 10 Finalist"),
            ("Domaine", "Industrie 4.0, IA, cybersécurité, smart manufacturing"),
            ("Conférence", "IEEE ICCITX.0 2026, Paris, France"),
            ("Organisations partenaires", "Fondation UTT, Chaire Connected Innovation"),
        ],
        "images": ["ieee_finalist_screenshot.png"],
    },
    {
        "title": "Red Team Practitioner — Offensive Security Track",
        "category": "Sécurité Offensive",
        "meta": "TryHackMe · Profil : tryhackme.com/p/OUZIDANEREDA",
        "result": "Top 5%",
        "prize": None,
        "abstract": "Parcours pratique de sécurité offensive développé via des labs hands-on couvrant l'ensemble "
        "du cycle de vie d'un adversaire — de la reconnaissance initiale au reporting post-exploitation. "
        "Classement dans le top 5% des utilisateurs de la plateforme, avec compétences démontrées en "
        "simulation d'adversaire, développement d'exploits, analyse réseau et reporting technique.",
        "specs": [
            ("Adversary simulation", "Reproduction de techniques d'attaquants réels"),
            ("Penetration testing", "Identification et exploitation de vulnérabilités"),
            ("Exploit development", "Développement d'outils de compromission"),
            ("Network analysis", "Étude du trafic pour identifier des enjeux de sécurité"),
            ("Risk & reporting", "Évaluation des risques et documentation claire"),
        ],
        "images": [],
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
    "email": "redaouzidan@gmail.com",
    "phone": "",
    "location": "Casablanca-Settat, Maroc",
    "tagline": "Ingénieur passionné par la cybersécurité offensive et l'optimisation des systèmes industriels.",
}

# ---------------------------------------------------------------------------
# Sidebar navigation
# ---------------------------------------------------------------------------
with st.sidebar:
    safe_image("profile_photo.jpg", use_container_width=True)
    st.markdown("### Ouzidane Reda")
    st.caption("Ingénieur d'État en Génie Industriel")
    st.markdown(
        '<span class="status-dot"></span><span style="color:#9aa3af; font-size:0.85rem;">'
        "Ouvert aux opportunités</span>",
        unsafe_allow_html=True,
    )
    st.markdown("---")
    section = st.radio(
        "Navigation",
        ["Accueil", "Expérience", "Hackathons & Projets", "Formation", "Certifications", "Contact", "Espace privé"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    cv_download_button(key="cv_sidebar")
    st.markdown(f"[Profil LinkedIn]({CONTACT['linkedin']})")
    st.caption(CONTACT["location"])

# ---------------------------------------------------------------------------
# Hero (always visible at top)
# ---------------------------------------------------------------------------
st.markdown(
    f"""
    <div class="hero-card">
        <h1>Ouzidane Reda</h1>
        <p style="font-size:1.1rem; color:#b7c1cc; margin-top:-0.6rem;">
            Ingénieur d'État en Génie Industriel · Cybersécurité & Industrie 4.0
        </p>
        <p style="color:#9aa3af; margin-top:0.8rem; max-width:56rem;">{CONTACT['tagline']}</p>
        <div style="margin-top:1rem;">
            <span class="badge">Génie Industriel</span>
            <span class="badge">Cybersécurité</span>
            <span class="badge">IA Appliquée</span>
            <span class="badge">Supply Chain</span>
            <span class="badge">Industrie 4.0</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")

stat_cols = st.columns(5)
stats = [
    ("7", "Projets & hackathons"),
    ("18", "Certifications"),
    ("2 968", "Abonnés LinkedIn"),
    ("500+", "Relations"),
    ("5", "Pays au concours IEEE"),
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
    c1, c2, c3 = st.columns(3)
    with c1:
        safe_image("secureprod_photo.png", caption="SecureProd — 1st Place, Teal Technology Services")
    with c2:
        safe_image("ieee_finalist_screenshot.png", caption="Top 10 Finalist — IEEE ICCITX.0 2026, Paris")
    with c3:
        safe_image("le_phare_photo.png", caption="Prix Impact Positif & Social — KEDGE")
    c4, c5, c6 = st.columns(3)
    with c4:
        safe_image("neurofit_presenting.png", caption="NEURO FIT — Game4Health, ISMAGI Rabat")
    with c5:
        safe_image("hackathon_collage.png", caption="Hackathons & compétitions")
    with c6:
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
                            {f'<div class="result">{exp["impact"]}</div>' if exp['impact'] else ''}
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
                        {f'<div class="result">{exp["impact"]}</div>' if exp['impact'] else ''}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

elif section == "Hackathons & Projets":
    st.header("Hackathons & Projets")
    st.caption("Fiches techniques de projets — cybersécurité, IA appliquée, santé digitale & entrepreneuriat social")
    for p in PROJECTS:
        prize_html = f" · <b>{p['prize']}</b>" if p["prize"] else ""
        specs_rows = "".join(
            f"<tr><td style='padding:0.3rem 0.8rem 0.3rem 0; color:#838d99; white-space:nowrap;'>{k}</td>"
            f"<td style='padding:0.3rem 0; color:#d5dae0;'>{v}</td></tr>"
            for k, v in p["specs"]
        )
        st.markdown(
            f"""
            <div class="card">
                <div class="eyebrow">{p['category']}</div>
                <h4>{p['title']}</h4>
                <div class="meta">{p['meta']}</div>
                <div class="result">{p['result']}{prize_html}</div>
                <p style="margin-top:0.7rem;">{p['abstract']}</p>
                <table style="width:100%; border-collapse:collapse; margin-top:0.6rem; font-size:0.85rem;">
                    {specs_rows}
                </table>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if p["images"]:
            img_cols = st.columns(len(p["images"]))
            for col, img in zip(img_cols, p["images"]):
                with col:
                    safe_image(img)
        st.write("")

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

    uploaded_files = sorted(os.listdir(UPLOAD_DIR)) if os.path.isdir(UPLOAD_DIR) else []
    image_files = [f for f in uploaded_files if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    if image_files:
        st.subheader("Diplômes & certificats (scans)")
        gcols = st.columns(4)
        for i, fname in enumerate(image_files):
            with gcols[i % 4]:
                st.image(os.path.join(UPLOAD_DIR, fname), caption=fname, use_container_width=True)

elif section == "Contact":
    st.header("Contact")
    st.write(
        "Ouvert aux opportunités en tant qu'Ingénieur Industriel, Ingénieur IA, Software Engineer ou "
        "Ingénieur Transformation Digitale."
    )
    st.markdown(f"**LinkedIn** : [{CONTACT['linkedin']}]({CONTACT['linkedin']})")
    st.markdown(f"**Email** : {CONTACT['email']}")
    if CONTACT["phone"]:
        st.markdown(f"**Téléphone** : {CONTACT['phone']}")
    st.markdown(f"**Localisation** : {CONTACT['location']}")
    st.markdown("**Formation** : ESITH Casablanca")
    st.write("")
    cv_download_button(key="cv_contact")

elif section == "Espace privé":
    st.header("Espace privé")
    st.caption("Zone réservée — ajout de certificats, diplômes et photos supplémentaires.")

    if "admin_ok" not in st.session_state:
        st.session_state.admin_ok = False

    if not st.session_state.admin_ok:
        pwd = st.text_input("Mot de passe", type="password")
        if st.button("Se connecter"):
            if pwd and pwd == get_admin_password():
                st.session_state.admin_ok = True
                st.rerun()
            else:
                st.error("Mot de passe incorrect.")
    else:
        st.success("Accès autorisé.")
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        uploaded = st.file_uploader(
            "Ajouter des fichiers (certificats, diplômes, photos)",
            type=["png", "jpg", "jpeg", "pdf"],
            accept_multiple_files=True,
        )
        if uploaded:
            for f in uploaded:
                dest = os.path.join(UPLOAD_DIR, f.name)
                with open(dest, "wb") as out:
                    out.write(f.getbuffer())
            st.success(f"{len(uploaded)} fichier(s) ajouté(s).")
            st.rerun()

        existing = sorted(os.listdir(UPLOAD_DIR)) if os.path.isdir(UPLOAD_DIR) else []
        if existing:
            st.subheader("Fichiers enregistrés")
            gcols = st.columns(4)
            for i, fname in enumerate(existing):
                fpath = os.path.join(UPLOAD_DIR, fname)
                with gcols[i % 4]:
                    if fname.lower().endswith((".png", ".jpg", ".jpeg")):
                        st.image(fpath, caption=fname, use_container_width=True)
                    else:
                        st.markdown(f"**{fname}**")
                    if st.button("Supprimer", key=f"del_{fname}"):
                        os.remove(fpath)
                        st.rerun()
        else:
            st.info("Aucun fichier pour le moment.")

        st.write("")
        if st.button("Se déconnecter"):
            st.session_state.admin_ok = False
            st.rerun()

st.markdown("---")
st.caption("Portfolio — Ouzidane Reda")
