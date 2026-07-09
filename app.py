import json
import os
import re

import pandas as pd
import streamlit as st

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Ouzidane Reda | Portfolio",
    page_icon="R",
    layout="wide",
    initial_sidebar_state="auto",
)

IMG_DIR = "images"
UPLOAD_DIR = os.path.join(IMG_DIR, "uploads")
CV_PATH = os.path.join("documents", "CV_Ouzidane_Reda.pdf")
CONTENT_PATH = "content.json"

# ---------------------------------------------------------------------------
# Default content (seeds content.json on first run)
# ---------------------------------------------------------------------------
DEFAULT_CONTENT = {
    "tagline": "Ingénieur passionné par la cybersécurité offensive et l'optimisation des systèmes industriels.",
    "skills": [
        "Penetration Testing", "Red Teaming", "Web Exploitation (XSS, SQLi, IDOR, SSRF)",
        "JWT / Auth Attacks", "Active Directory Attacks", "Reverse Engineering",
        "Warehouse Management Systems (WMS)", "Lean Six Sigma", "Industry 4.0",
        "Data Analytics", "Machine Learning", "MERN Stack (MongoDB, Express, React, Node)",
        "Process Optimization", "Supply Chain & Logistique",
    ],
    "badges": ["Génie Industriel", "Cybersécurité", "IA Appliquée", "Supply Chain", "Industrie 4.0"],
    "contact": {
        "linkedin": "https://www.linkedin.com/in/ouzidane-reda-a9b010295",
        "email": "redaouzidan@gmail.com",
        "phone": "",
        "location": "Casablanca-Settat, Maroc",
    },
    "stats": [
        {"num": "8", "label": "Projets & hackathons"},
        {"num": "19", "label": "Certifications"},
        {"num": "2 968", "label": "Abonnés LinkedIn"},
        {"num": "500+", "label": "Relations"},
        {"num": "5", "label": "Pays au concours IEEE"},
    ],
    "experience": [
        {
            "role": "PFE Intern – Industry 4.0 & Digitalization Consultant",
            "org": "DOUNITEX Confection SA",
            "period": "Mars 2026 – Juin 2026 · 4 mois",
            "desc": "Conception et déploiement de WMS DOUNITEX, un Warehouse Management System sur mesure piloté "
            "par l'IA (React.js, Flask/Python, PostgreSQL) pour digitaliser la gestion des stocks, fiabiliser "
            "les données et anticiper les ruptures. Tableau de bord stratégique temps réel, prévision de la "
            "demande par IA et conception d'entrepôt 2D/3D.",
            "impact": "+33% de gain de temps moyen · Temps de recherche ÷4 · 100% de traçabilité des flux · "
            "75% de précision des prévisions IA · 1 688 min économisées sur 150 opérations · 0 coût de licence "
            "(open-source)",
            "image": "pfe_defense.jpg",
        },
        {
            "role": "Stagiaire (PFA) – Full Stack Web Developer @ CAPN",
            "org": "ESITH Digital Center",
            "period": "Juillet 2025 · 1 mois",
            "desc": "Développement d'outils web pour la digitalisation des processus internes. Conception d'APIs "
            "RESTful robustes avec la stack MERN (MongoDB, Express.js, React.js, Node.js).",
            "impact": "",
            "image": "",
        },
        {
            "role": "Bug Bounty Hunter",
            "org": "HackerOne · Temps partiel · À distance",
            "period": "Décembre 2024 – Juillet 2025 · 8 mois",
            "desc": "Recherche active de vulnérabilités de sécurité sur des applications web, APIs et "
            "infrastructures pour aider les organisations à sécuriser leurs actifs numériques.",
            "impact": "",
            "image": "",
        },
        {
            "role": "Internship Trainee",
            "org": "Stellantis · Kénitra, Maroc",
            "period": "Juin 2024 · 1 mois",
            "desc": "Optimisation des processus de contrôle des pièces pour le département EUP. Analyse des "
            "causes racines (Ishikawa, 5 Whys), conception de workflows Lean Manufacturing et proposition de "
            "KPIs/dashboards.",
            "impact": "",
            "image": "",
        },
    ],
    "education": [
        {
            "school": "ESITH Casablanca",
            "degree": "Ingénieur d'État en Génie Industriel",
            "period": "2023 – 2026",
            "desc": "Spécialisation Production Management & Optimization · Lean, Six Sigma, technologies "
            "digitales, modèles d'optimisation, simulation et IA appliqués à l'Industrie 4.0.",
            "image": "esith_logo.png",
        },
        {
            "school": "CPGE – Classes préparatoires aux grandes écoles",
            "degree": "Physique, Math et Sciences de l'Ingénieur (PCSI / PSI)",
            "period": "Déc. 2021 – Févr. 2023",
            "desc": "Lycée Prince Héritier Moulay El Hassan, Ouarzazate.",
            "image": "",
        },
    ],
    "projects": [
        {
            "title": "WMS DOUNITEX — Warehouse Management System piloté par l'IA",
            "category": "Supply Chain / Industrie 4.0",
            "meta": "PFE — DOUNITEX Confection SA × ESITH Smart Factory · 2026",
            "result": "Déployé en production",
            "prize": "",
            "abstract": "Solution WMS sur mesure conçue pour digitaliser la gestion des stocks d'une PME "
            "industrielle et textile, fiabiliser les données et anticiper les ruptures grâce à l'IA. La "
            "plateforme centralise la gestion des articles et de l'inventaire, la réception/sortie des flux, "
            "le contrôle qualité, les demandes d'achat automatisées et un tableau de bord stratégique en temps "
            "réel, avec une conception d'entrepôt en 2D/3D.",
            "specs_text": "Gain de temps moyen: +33%\n"
            "Temps de recherche: ÷4\n"
            "Traçabilité des flux: 100%\n"
            "Précision des prévisions IA: 75%\n"
            "Minutes économisées: 1 688 min sur 150 opérations mesurées\n"
            "Coût de licence: 0 (solution open-source)\n"
            "Stack technique: React.js (SPA) · Flask/Python (API REST) · PostgreSQL · ORM SQLAlchemy · "
            "déploiement LAN\n"
            "Méthodologie: Cadrage → Conception → Conduite → Clôture (4C)",
            "images": "pfe_defense.jpg",
        },
        {
            "title": "SecureProd — AI-Assisted Intrusion Detection for SCADA/ICS",
            "category": "Cybersécurité / Industrie 4.0",
            "meta": "Équipe Secure Prod (avec Kaouthar Belkebir) · Teal Technology Services · Jul. 2025",
            "result": "1st Place",
            "prize": "30 000 DHS",
            "abstract": "Les réseaux SCADA/ICS ont vu une hausse documentée de 54% des attaques ciblées, tout en "
            "reposant sur des protocoles historiques (Modbus TCP, DNP3) sans authentification ni chiffrement "
            "natifs. SecureProd combine un parsing conscient des protocoles avec un modèle de détection "
            "d'anomalies supervisé pour signaler en temps réel les comportements OT anormaux, et restitue le "
            "risque sous forme de carte de menace 3D pour les opérateurs d'usine. Conçu et livré en 36 heures "
            "de hackathon.",
            "specs_text": "Protocoles sécurisés: Modbus TCP, DNP3\n"
            "Méthode de détection: Modèle supervisé de détection d'anomalies\n"
            "Mode de déploiement: Tap réseau passif (non-intrusif)\n"
            "Visualisation: Carte de menace 3D en temps réel\n"
            "Reporting: Export automatisé prêt pour audit de conformité\n"
            "Fenêtre de développement: 36 heures (format hackathon)",
            "images": "secureprod_logo.png, secureprod_photo.png",
        },
        {
            "title": "NEURO FIT — Gamified EMG Biofeedback for Muscular Rehabilitation",
            "category": "Santé Digitale / Gamification",
            "meta": "Équipe ESITH — Reda et al. · Game4Health, ISMAGI Rabat × SmartTech Lab · 4 avr. 2026",
            "result": "2nd Place",
            "prize": "6 000 DHS",
            "abstract": "L'adhérence aux protocoles de rééducation musculaire est limitée par le manque de retour "
            "immédiat des exercices classiques de physiothérapie. NEURO FIT capte le signal EMG de surface "
            "(sEMG) via électrodes à l'avant-bras et transforme l'activation musculaire en gameplay temps réel "
            "autour de trois objectifs — Follow, Avoid, Maintain. Lors d'une démonstration live, le système a "
            "atteint une précision de 93% avec un taux de fatigue détecté de 0% et un rapport de session "
            "généré automatiquement pour le suivi clinique à distance.",
            "specs_text": "Source du signal: EMG de surface, électrodes 2 canaux à l'avant-bras\n"
            "Métriques live: Score de précision, fatigue musculaire, charge du modèle ML\n"
            "Sortie observée (démo): Amplitude temps réel 354 μV, précision 93%, fatigue 0%\n"
            "Modes de jeu: Follow, Avoid, Maintain\n"
            "Reporting: Rapport de session automatisé pour suivi clinicien",
            "images": "neurofit_dashboard.png, neurofit_electrodes.png, neurofit_presenting.png, neurofit_award.png",
        },
        {
            "title": "Vamosway — Full-Stack Mobility & Travel Web Application",
            "category": "Web Application / Mobilité",
            "meta": "Équipe Vamosway · ACCEDE Internationale · Track Sciences et Technologie",
            "result": "1st Place",
            "prize": "10 000 DHS",
            "abstract": "Application web full-stack conçue et livrée dans la fenêtre fixe d'un hackathon pour "
            "répondre à un enjeu de mobilité du track « Sciences et Technologie ». Priorité donnée à un "
            "parcours utilisateur cohérent et fonctionnel plutôt qu'à une exhaustivité des fonctionnalités — "
            "cadrage du problème, conception de l'interface, implémentation et pitch live devant le jury.",
            "specs_text": "Livrable: Application web full-stack\n"
            "Format d'équipe: Équipe pluridisciplinaire étudiante\n"
            "Critères d'évaluation: Innovation, utilisabilité, exécution technique\n"
            "Fenêtre de développement: Format hackathon (budget temps fixe)",
            "images": "",
        },
        {
            "title": "AI for Social Impact — Applied Machine Learning Prototype",
            "category": "Intelligence Artificielle Appliquée",
            "meta": "Équipe ESITH — Reda Ouzidane · Hackathon ESITH Casablanca · Track AI for Social Impact",
            "result": "2nd Place",
            "prize": "",
            "abstract": "Prototype IA fonctionnel développé pour répondre à un besoin social réel plutôt qu'à une "
            "simple preuve de concept sur données synthétiques, dans le cadre du track « AI for Social Impact » "
            "de l'ESITH Casablanca. Évalué sur la pertinence par rapport au besoin social, la faisabilité "
            "technique et la qualité d'exécution.",
            "specs_text": "Livrable: Prototype IA fonctionnel\n"
            "Critères d'évaluation: Pertinence, faisabilité, exécution technique\n"
            "Institution hôte: ESITH Casablanca",
            "images": "",
        },
        {
            "title": "Le Phare de l'Entrepreneuriat — Social-Impact Venture Award",
            "category": "Entrepreneuriat Social",
            "meta": "Reda Ouzidane · KEDGE Business School · 15 mai 2025",
            "result": "Prix Impact Positif & Social",
            "prize": "10 000 DHS",
            "abstract": "Compétition d'entrepreneuriat de KEDGE Business School évaluant les ventures candidates "
            "sur deux axes combinés : viabilité entrepreneuriale et impact social positif démontrable. La "
            "venture a été reconnue pour sa capacité à combiner innovation et création de valeur sociale "
            "mesurable, avec un pitch live à Casablanca.",
            "specs_text": "Prix: Prix Impact Positif & Social\n"
            "Institution hôte: KEDGE Business School\n"
            "Lieu: Casablanca, Maroc",
            "images": "le_phare_photo.png",
        },
        {
            "title": "Industry 4.0, AI & Cybersecurity for Smart Manufacturing",
            "category": "Industrie 4.0 / Smart Manufacturing",
            "meta": "Ouzidane R., Baroudi M., Fahsi Y. · ESITH, Maroc · IEEE ICCITX.0 2026, Paris",
            "result": "Top 10 Finalist",
            "prize": "77 projets · 5 pays",
            "abstract": "Projet de recherche et d'innovation à l'intersection de l'Industrie 4.0, de l'IA, de la "
            "cybersécurité et du smart manufacturing, soumis au concours d'innovation CITx.C 2026. Sélectionné "
            "Top 10 Finaliste parmi 77 projets évalués sur 3 phases, annoncé lors de la session de clôture de "
            "la conférence internationale IEEE ICCITX.0 2026 à Paris, cérémonie de remise des prix le 16 juin "
            "2026.",
            "specs_text": "Soumissions évaluées: 77 projets, 5 pays\n"
            "Résultat: Top 10 Finalist\n"
            "Domaine: Industrie 4.0, IA, cybersécurité, smart manufacturing\n"
            "Conférence: IEEE ICCITX.0 2026, Paris, France\n"
            "Organisations partenaires: Fondation UTT, Chaire Connected Innovation",
            "images": "ieee_finalist_screenshot.png",
        },
        {
            "title": "Red Team Practitioner — Offensive Security Track",
            "category": "Sécurité Offensive",
            "meta": "TryHackMe · Profil : tryhackme.com/p/OUZIDANEREDA",
            "result": "Top 5%",
            "prize": "",
            "abstract": "Parcours pratique de sécurité offensive développé via des labs hands-on couvrant "
            "l'ensemble du cycle de vie d'un adversaire — de la reconnaissance initiale au reporting "
            "post-exploitation. Classement dans le top 5% des utilisateurs de la plateforme, avec compétences "
            "démontrées en simulation d'adversaire, développement d'exploits, analyse réseau et reporting "
            "technique.",
            "specs_text": "Adversary simulation: Reproduction de techniques d'attaquants réels\n"
            "Penetration testing: Identification et exploitation de vulnérabilités\n"
            "Exploit development: Développement d'outils de compromission\n"
            "Network analysis: Étude du trafic pour identifier des enjeux de sécurité\n"
            "Risk & reporting: Évaluation des risques et documentation claire",
            "images": "",
        },
    ],
    "certifications": [
        {"name": "Six Sigma Green Belt", "issuer": "Coursera"},
        {"name": "Google Data Analytics", "issuer": "Google"},
        {"name": "Data Science", "issuer": "DataCamp"},
        {"name": "Google Project Management", "issuer": "Google"},
        {"name": "Data Science", "issuer": "IBM"},
        {"name": "Machine Learning", "issuer": "IBM"},
        {"name": "API Penetration Testing", "issuer": "APIsec University"},
        {"name": "CS50x", "issuer": "Harvard University"},
        {"name": "Windows Privilege Escalation", "issuer": "Hack The Box"},
        {"name": "Attacking Common Applications", "issuer": "Hack The Box"},
        {"name": "AD Enumeration & Attacks", "issuer": "Hack The Box"},
        {"name": "Web-Attacks", "issuer": "Hack The Box"},
        {"name": "Fortinet Certified Associate Cybersecurity", "issuer": "Fortinet"},
        {"name": "Ethical Hacking Essentials (EHE)", "issuer": "EC-Council"},
        {"name": "Jr Penetration Tester", "issuer": "TryHackMe"},
        {"name": "Offensive Pentesting", "issuer": "TryHackMe"},
        {"name": "Red-Team (Top 5%)", "issuer": "TryHackMe"},
        {"name": "Junior Cybersecurity Analyst Career Path", "issuer": "Cisco"},
        {"name": "Ethical Hacker", "issuer": "Cisco"},
    ],
}


def load_content() -> dict:
    if os.path.exists(CONTENT_PATH):
        try:
            with open(CONTENT_PATH, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    save_content(DEFAULT_CONTENT)
    return json.loads(json.dumps(DEFAULT_CONTENT))


def save_content(data: dict):
    with open(CONTENT_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def parse_specs(specs_text: str):
    rows = []
    for line in (specs_text or "").splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            if k.strip():
                rows.append((k.strip(), v.strip()))
    return rows


def parse_images(images_text: str):
    return [x.strip() for x in (images_text or "").split(",") if x.strip()]


content = load_content()

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def img_path(filename: str) -> str | None:
    for base in (IMG_DIR, UPLOAD_DIR):
        path = os.path.join(base, filename)
        if os.path.exists(path):
            return path
    return None


def safe_image(filename: str, caption: str = "", use_container_width: bool = True):
    path = img_path(filename) if filename else None
    if path:
        st.image(path, caption=caption, width="stretch" if use_container_width else "content")
    else:
        st.markdown(
            f"""
            <div class="img-placeholder">
                <span>Ajouter <code>images/{filename or '...'}</code></span>
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
                width="stretch",
                key=key,
            )


# ---------------------------------------------------------------------------
# Styling — professional theme with subtle motion
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

    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(14px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulseDot {
        0% { box-shadow: 0 0 0 0 rgba(76,175,125,0.55); }
        70% { box-shadow: 0 0 0 7px rgba(76,175,125,0); }
        100% { box-shadow: 0 0 0 0 rgba(76,175,125,0); }
    }
    @keyframes shimmer {
        0% { background-position: -400px 0; }
        100% { background-position: 400px 0; }
    }
    @keyframes borderCycle {
        0%, 100% { border-left-color: #6f93b8; }
        50% { border-left-color: #c9a15a; }
    }
    @keyframes blinkCursor {
        50% { border-right-color: transparent; }
    }
    @keyframes floatY {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-6px); }
    }
    @keyframes resultGlow {
        0%, 100% { text-shadow: 0 0 0 rgba(201,161,90,0); }
        50% { text-shadow: 0 0 10px rgba(201,161,90,0.55); }
    }

    .hero-card {
        background: #151920;
        border: 1px solid #262c38;
        border-left: 3px solid #6f93b8;
        border-radius: 6px;
        padding: 2.2rem 2.4rem;
        animation: fadeInUp 0.55s ease both, borderCycle 6s ease-in-out infinite;
    }

    .typewriter {
        display: inline-block;
        border-right: 2px solid #6f93b8;
        max-width: 100%;
    }
    .typewriter.blink { animation: blinkCursor 0.8s step-end infinite; }

    .status-dot {
        display: inline-block;
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: #4caf7d;
        margin-right: 0.5rem;
        animation: pulseDot 2.2s infinite;
    }

    div[data-testid="stSidebar"] div[data-testid="stImage"] img {
        animation: floatY 4s ease-in-out infinite;
        border-radius: 8px;
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
        opacity: 0;
        animation: fadeInUp 0.4s ease both;
        transition: transform 0.2s ease, border-color 0.2s ease, color 0.2s ease, box-shadow 0.2s ease;
    }
    .badge:hover {
        transform: translateY(-2px);
        border-color: #6f93b8;
        color: #eef1f4;
        box-shadow: 0 4px 14px rgba(111,147,184,0.25);
    }

    .card {
        background: #151920;
        border: 1px solid #232833;
        border-radius: 6px;
        padding: 1.5rem 1.7rem;
        margin-bottom: 1.2rem;
        animation: fadeInUp 0.5s ease both;
        transition: border-color 0.25s ease, transform 0.25s ease, box-shadow 0.25s ease;
    }
    .card:hover {
        border-color: #3a4250;
        transform: translateY(-3px);
        box-shadow: 0 10px 24px rgba(0,0,0,0.28);
    }

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
        animation: resultGlow 3s ease-in-out infinite;
    }

    .cert-chip {
        background: #151920;
        border: 1px solid #232833;
        border-radius: 6px;
        padding: 0.75rem 1rem;
        margin-bottom: 0.6rem;
        font-size: 0.87rem;
        animation: fadeInUp 0.5s ease both;
        transition: border-color 0.2s ease, transform 0.2s ease;
    }
    .cert-chip:hover {
        border-color: #6f93b8;
        transform: translateX(3px);
        box-shadow: 0 4px 16px rgba(111,147,184,0.2);
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
        animation: fadeInUp 0.6s ease both;
        transition: transform 0.25s ease, border-color 0.25s ease;
    }
    .stat-box:hover { transform: translateY(-3px); border-color: #6f93b8; }
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

    a { color: #8fb2d6 !important; text-decoration: none !important; transition: color 0.2s ease; }
    a:hover { text-decoration: underline !important; color: #c9a15a !important; }

    hr { border-color: #232833; }

    table td { border-bottom: 1px solid #1e232c; }

    .stButton > button {
        transition: transform 0.15s ease, border-color 0.15s ease;
    }
    .stButton > button:hover { transform: translateY(-1px); }

    img { transition: transform 0.3s ease, filter 0.3s ease; }
    div[data-testid="stImage"]:hover img { transform: scale(1.015); }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Sidebar navigation
# ---------------------------------------------------------------------------
with st.sidebar:
    safe_image("profile_photo.jpg")
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
    st.markdown(f"[Profil LinkedIn]({content['contact']['linkedin']})")
    st.caption(content["contact"]["location"])

# ---------------------------------------------------------------------------
# Hero (always visible at top)
# ---------------------------------------------------------------------------
SUBTITLE = "Ingénieur d'État en Génie Industriel · Cybersécurité & Industrie 4.0"
badges_html = "".join(
    f'<span class="badge" style="animation-delay:{0.05 * i:.2f}s">{b}</span>'
    for i, b in enumerate(content["badges"])
)
st.markdown(
    f"""
    <div class="hero-card">
        <h1>Ouzidane Reda</h1>
        <p class="typewriter type-target" data-full-text="{SUBTITLE}" style="font-size:1.1rem; color:#b7c1cc; margin-top:-0.6rem; min-height:1.4em;">{SUBTITLE}</p>
        <p style="color:#9aa3af; margin-top:0.8rem; max-width:56rem;">{content['tagline']}</p>
        <div style="margin-top:1rem;">{badges_html}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")


def split_stat_num(num_str: str):
    match = re.match(r"^([\d\s]+)(.*)$", num_str.strip())
    if match and match.group(1).replace(" ", "").isdigit():
        return match.group(1).replace(" ", ""), match.group(2)
    return None, num_str


stat_cols = st.columns(len(content["stats"]))
for i, (col, s) in enumerate(zip(stat_cols, content["stats"])):
    with col:
        target, suffix = split_stat_num(s["num"])
        if target:
            num_html = f'<div class="num count-num" data-target="{target}" data-suffix="{suffix}">0</div>'
        else:
            num_html = f'<div class="num">{s["num"]}</div>'
        st.markdown(
            f'<div class="stat-box" style="animation-delay:{0.08 * i:.2f}s">{num_html}'
            f'<div class="lbl">{s["label"]}</div></div>',
            unsafe_allow_html=True,
        )

st.iframe(
    """
    <script>
    (function animateCounts() {
        const doc = window.parent.document;
        const counters = doc.querySelectorAll('.count-num:not([data-done])');
        counters.forEach(el => {
            el.setAttribute('data-done', '1');
            const target = parseInt(el.getAttribute('data-target'), 10) || 0;
            const suffix = el.getAttribute('data-suffix') || '';
            const duration = 1100;
            const startTime = performance.now();
            function step(now) {
                const progress = Math.min((now - startTime) / duration, 1);
                const eased = 1 - Math.pow(1 - progress, 3);
                const value = Math.floor(eased * target);
                el.textContent = value.toLocaleString('fr-FR') + suffix;
                if (progress < 1) { requestAnimationFrame(step); }
                else { el.textContent = target.toLocaleString('fr-FR') + suffix; }
            }
            requestAnimationFrame(step);
        });
    })();
    (function typeText() {
        const doc = window.parent.document;
        const targets = doc.querySelectorAll('.type-target:not([data-typed])');
        targets.forEach(el => {
            el.setAttribute('data-typed', '1');
            const full = el.getAttribute('data-full-text') || '';
            el.textContent = '';
            let i = 0;
            const speed = 28;
            function typeStep() {
                i += 1;
                el.textContent = full.slice(0, i);
                if (i < full.length) {
                    setTimeout(typeStep, speed);
                } else {
                    el.classList.add('blink');
                }
            }
            setTimeout(typeStep, speed);
        });
    })();
    </script>
    """,
    height=1,
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
        "".join(f'<span class="badge">{s}</span>' for s in content["skills"]),
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
    for exp in content["experience"]:
        with st.container():
            if exp.get("image"):
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
                            {f'<div class="result">{exp["impact"]}</div>' if exp.get('impact') else ''}
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
                        {f'<div class="result">{exp["impact"]}</div>' if exp.get('impact') else ''}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

elif section == "Hackathons & Projets":
    st.header("Hackathons & Projets")
    st.caption("Fiches techniques de projets — cybersécurité, IA appliquée, santé digitale & entrepreneuriat social")
    for p in content["projects"]:
        prize_html = f" · <b>{p['prize']}</b>" if p.get("prize") else ""
        specs_rows = "".join(
            f"<tr><td style='padding:0.3rem 0.8rem 0.3rem 0; color:#838d99; white-space:nowrap;'>{k}</td>"
            f"<td style='padding:0.3rem 0; color:#d5dae0;'>{v}</td></tr>"
            for k, v in parse_specs(p.get("specs_text", ""))
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
        proj_images = parse_images(p.get("images", ""))
        if proj_images:
            img_cols = st.columns(len(proj_images))
            for col, img in zip(img_cols, proj_images):
                with col:
                    safe_image(img)
        st.write("")

elif section == "Formation":
    st.header("Formation")
    for edu in content["education"]:
        c1, c2 = st.columns([1, 2.4])
        with c1:
            safe_image(edu.get("image") or "school_placeholder.png")
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
    st.header(f"Certifications ({len(content['certifications'])})")
    st.caption("Cybersécurité, Data & Management")
    cols = st.columns(3)
    for i, c in enumerate(content["certifications"]):
        with cols[i % 3]:
            st.markdown(
                f"""
                <div class="cert-chip">
                    <b>{c['name']}</b><br/><span>{c['issuer']}</span>
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
                st.image(os.path.join(UPLOAD_DIR, fname), caption=fname, width="stretch")

elif section == "Contact":
    st.header("Contact")
    st.write(
        "Ouvert aux opportunités en tant qu'Ingénieur Industriel, Ingénieur IA, Software Engineer ou "
        "Ingénieur Transformation Digitale."
    )
    st.markdown(f"**LinkedIn** : [{content['contact']['linkedin']}]({content['contact']['linkedin']})")
    st.markdown(f"**Email** : {content['contact']['email']}")
    if content["contact"].get("phone"):
        st.markdown(f"**Téléphone** : {content['contact']['phone']}")
    st.markdown(f"**Localisation** : {content['contact']['location']}")
    st.markdown("**Formation** : ESITH Casablanca")
    st.write("")
    cv_download_button(key="cv_contact")

elif section == "Espace privé":
    st.header("Espace privé")
    st.caption("Zone réservée — modification du contenu du site et ajout de fichiers.")

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
        tabs = st.tabs(["Général", "Expérience", "Formation", "Projets", "Certifications", "Fichiers"])

        # ---- Général --------------------------------------------------
        with tabs[0]:
            st.subheader("En-tête & contact")
            tagline = st.text_area("Phrase d'accroche", value=content["tagline"], height=80)
            skills_text = st.text_area(
                "Compétences (une par ligne)", value="\n".join(content["skills"]), height=180
            )
            badges_text = st.text_area(
                "Badges du header (un par ligne)", value="\n".join(content["badges"]), height=100
            )
            st.markdown("---")
            linkedin = st.text_input("LinkedIn", value=content["contact"]["linkedin"])
            email = st.text_input("Email", value=content["contact"]["email"])
            phone = st.text_input("Téléphone", value=content["contact"].get("phone", ""))
            location = st.text_input("Localisation", value=content["contact"]["location"])
            if st.button("Enregistrer — Général", type="primary"):
                content["tagline"] = tagline
                content["skills"] = [s.strip() for s in skills_text.splitlines() if s.strip()]
                content["badges"] = [b.strip() for b in badges_text.splitlines() if b.strip()]
                content["contact"] = {
                    "linkedin": linkedin, "email": email, "phone": phone, "location": location,
                }
                save_content(content)
                st.success("Enregistré.")
                st.rerun()

        # ---- Expérience -------------------------------------------------
        with tabs[1]:
            st.subheader("Expérience professionnelle")
            exp_df = pd.DataFrame(content["experience"])
            edited_exp = st.data_editor(
                exp_df,
                num_rows="dynamic",
                width="stretch",
                key="editor_experience",
                column_config={
                    "desc": st.column_config.TextColumn("desc", width="large"),
                    "image": st.column_config.TextColumn("image", help="nom de fichier dans images/"),
                },
            )
            if st.button("Enregistrer — Expérience", type="primary"):
                content["experience"] = edited_exp.fillna("").to_dict(orient="records")
                save_content(content)
                st.success("Enregistré.")
                st.rerun()

        # ---- Formation ----------------------------------------------------
        with tabs[2]:
            st.subheader("Formation")
            edu_df = pd.DataFrame(content["education"])
            edited_edu = st.data_editor(
                edu_df,
                num_rows="dynamic",
                width="stretch",
                key="editor_education",
            )
            if st.button("Enregistrer — Formation", type="primary"):
                content["education"] = edited_edu.fillna("").to_dict(orient="records")
                save_content(content)
                st.success("Enregistré.")
                st.rerun()

        # ---- Projets --------------------------------------------------
        with tabs[3]:
            st.subheader("Hackathons & Projets")
            projects = content["projects"]
            for i, p in enumerate(projects):
                with st.expander(p.get("title") or f"Projet {i+1}"):
                    p["title"] = st.text_input("Titre", value=p.get("title", ""), key=f"pt_{i}")
                    p["category"] = st.text_input("Catégorie", value=p.get("category", ""), key=f"pc_{i}")
                    p["meta"] = st.text_input("Équipe / Événement / Date", value=p.get("meta", ""), key=f"pm_{i}")
                    col_r, col_pr = st.columns(2)
                    with col_r:
                        p["result"] = st.text_input("Résultat", value=p.get("result", ""), key=f"pr_{i}")
                    with col_pr:
                        p["prize"] = st.text_input("Prix", value=p.get("prize", ""), key=f"pp_{i}")
                    p["abstract"] = st.text_area("Résumé", value=p.get("abstract", ""), height=140, key=f"pa_{i}")
                    p["specs_text"] = st.text_area(
                        "Spécifications techniques (une ligne \"Clé: Valeur\" par ligne)",
                        value=p.get("specs_text", ""), height=120, key=f"ps_{i}",
                    )
                    p["images"] = st.text_input(
                        "Images (noms de fichiers séparés par des virgules)",
                        value=p.get("images", ""), key=f"pi_{i}",
                    )
                    if st.button("Supprimer ce projet", key=f"pdel_{i}"):
                        projects.pop(i)
                        content["projects"] = projects
                        save_content(content)
                        st.rerun()
            if st.button("Ajouter un projet"):
                projects.append({
                    "title": "Nouveau projet", "category": "", "meta": "", "result": "", "prize": "",
                    "abstract": "", "specs_text": "", "images": "",
                })
                content["projects"] = projects
                save_content(content)
                st.rerun()
            if st.button("Enregistrer — Projets", type="primary"):
                content["projects"] = projects
                save_content(content)
                st.success("Enregistré.")
                st.rerun()

        # ---- Certifications ------------------------------------------
        with tabs[4]:
            st.subheader("Certifications")
            cert_df = pd.DataFrame(content["certifications"])
            edited_cert = st.data_editor(
                cert_df,
                num_rows="dynamic",
                width="stretch",
                key="editor_certifications",
            )
            if st.button("Enregistrer — Certifications", type="primary"):
                content["certifications"] = edited_cert.fillna("").to_dict(orient="records")
                save_content(content)
                st.success("Enregistré.")
                st.rerun()

        # ---- Fichiers ---------------------------------------------------
        with tabs[5]:
            st.subheader("Fichiers (certificats, diplômes, photos)")
            os.makedirs(UPLOAD_DIR, exist_ok=True)
            uploaded = st.file_uploader(
                "Ajouter des fichiers",
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
                st.markdown("**Fichiers enregistrés** — utilisez le nom exact dans les champs image ci-dessus.")
                gcols = st.columns(4)
                for i, fname in enumerate(existing):
                    fpath = os.path.join(UPLOAD_DIR, fname)
                    with gcols[i % 4]:
                        if fname.lower().endswith((".png", ".jpg", ".jpeg")):
                            st.image(fpath, caption=fname, width="stretch")
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
