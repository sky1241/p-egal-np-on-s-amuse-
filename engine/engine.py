"""
P=NP ON S'AMUSE — MOTEUR STRATES × SYMBOLES v2
=================================================
Sky × Claude — 17 Février 2026
Tous les symboles scientifiques et mathématiques connus,
placés sur leur strate de calculabilité.
Pas de liaisons — juste la carte pure.
Usage:
    python engine.py          → génère JSON + rapport
    python engine.py --html   → génère aussi le HTML autonome
"""
import json
import math
import sys
from collections import defaultdict
from pathlib import Path
# ============================================================================
# STRATES — 7 niveaux
# ============================================================================
STRATES = [
    {
        "id": 0, "name": "SOL · Δ⁰₀ · Décidable", "short": "Δ⁰₀ SOL",
        "formula": "R(x) — tout se calcule en temps fini",
        "desc": "Arithmétique, algèbre, analyse, physique, chimie — toute formule calculable.",
        "color": [74, 222, 128], "yr": -0.44, "opacity": 0.18,
    },
    {
        "id": 1, "name": "NUAGE 1 · Σ⁰₁ · Halting Problem", "short": "Σ⁰₁ HALTING",
        "formula": "∃y R(x, y) — il existe, mais on sait pas quand",
        "desc": "Semi-décidable. On peut dire oui, jamais non.",
        "color": [96, 165, 250], "yr": -0.26, "opacity": 0.16,
    },
    {
        "id": 2, "name": "NUAGE 2 · Σ⁰₂ · Limite", "short": "Σ⁰₂ LIMITE",
        "formula": "∃y ∀z R(x,y,z) — deviner, corriger, jamais sûr",
        "desc": "Ensembles limites. TOT, FIN, COF.",
        "color": [167, 139, 250], "yr": -0.10, "opacity": 0.14,
    },
    {
        "id": 3, "name": "NUAGE n · Σ⁰ₙ · Motif", "short": "Σ⁰ₙ MOTIF",
        "formula": "∃∀∃∀… n alternances",
        "desc": "Chaque alternance = un étage. Post 1944.",
        "color": [244, 114, 182], "yr": 0.06, "opacity": 0.13,
    },
    {
        "id": 4, "name": "CIEL · AH = ∪ₙ Σ⁰ₙ", "short": "AH CIEL",
        "formula": "Tout le ciel arithmétique",
        "desc": "L'union de tous les nuages. Tarski.",
        "color": [251, 191, 36], "yr": 0.20, "opacity": 0.13,
    },
    {
        "id": 5, "name": "HYPERARITHMÉTIQUE", "short": "HYP ω₁ᶜᵏ",
        "formula": "∅⁽α⁾ pour α < ω₁^CK",
        "desc": "Kleene, Church-Kleene. Le transfini.",
        "color": [251, 146, 60], "yr": 0.34, "opacity": 0.16,
    },
    {
        "id": 6, "name": "PLAFOND · Turing 1936", "short": "∞ PLAFOND",
        "formula": "∄ M décidant l'arrêt — Prouvé.",
        "desc": "Gödel · Church · Turing. BB(n). Le mur.",
        "color": [239, 68, 68], "yr": 0.46, "opacity": 0.24,
    },
]
# ============================================================================
# TOUS LES SYMBOLES SCIENTIFIQUES ET MATHÉMATIQUES CONNUS
# ============================================================================
SYMBOLES = [
    # ==================================================================
    # STRATE 0 — SOL · DÉCIDABLE · Tout ce qui se calcule
    # ==================================================================
    # --- ARITHMÉTIQUE FONDAMENTALE ---
    {"s": "+",    "strate": 0, "from": "Addition",                   "domain": "arithmétique"},
    {"s": "−",    "strate": 0, "from": "Soustraction",               "domain": "arithmétique"},
    {"s": "×",    "strate": 0, "from": "Multiplication",             "domain": "arithmétique"},
    {"s": "÷",    "strate": 0, "from": "Division",                   "domain": "arithmétique"},
    {"s": "=",    "strate": 0, "from": "Égalité (Recorde 1557)",     "domain": "arithmétique"},
    {"s": "≠",    "strate": 0, "from": "Inégalité",                  "domain": "arithmétique"},
    {"s": "<",    "strate": 0, "from": "Inférieur strict",           "domain": "arithmétique"},
    {"s": ">",    "strate": 0, "from": "Supérieur strict",           "domain": "arithmétique"},
    {"s": "≤",    "strate": 0, "from": "Inférieur ou égal",          "domain": "arithmétique"},
    {"s": "≥",    "strate": 0, "from": "Supérieur ou égal",          "domain": "arithmétique"},
    {"s": "≈",    "strate": 0, "from": "Approximativement égal",     "domain": "arithmétique"},
    {"s": "≡",    "strate": 0, "from": "Identique / congruence",     "domain": "arithmétique"},
    {"s": "∝",    "strate": 0, "from": "Proportionnel à",            "domain": "arithmétique"},
    {"s": "±",    "strate": 0, "from": "Plus ou moins",              "domain": "arithmétique"},
    {"s": "√",    "strate": 0, "from": "Racine carrée",              "domain": "arithmétique"},
    {"s": "∛",    "strate": 0, "from": "Racine cubique",             "domain": "arithmétique"},
    {"s": "!",    "strate": 0, "from": "Factorielle n!",             "domain": "combinatoire"},
    {"s": "ⁿ",    "strate": 0, "from": "Puissance / exposant",       "domain": "arithmétique"},
    {"s": "%",    "strate": 0, "from": "Pourcentage",                "domain": "arithmétique"},
    {"s": "mod",  "strate": 0, "from": "Modulo",                     "domain": "arithmétique"},
    {"s": "⌊x⌋",  "strate": 0, "from": "Partie entière inférieure",  "domain": "arithmétique"},
    {"s": "⌈x⌉",  "strate": 0, "from": "Partie entière supérieure",  "domain": "arithmétique"},
    {"s": "|x|",  "strate": 0, "from": "Valeur absolue",             "domain": "arithmétique"},
    {"s": "∞",    "strate": 0, "from": "Infini potentiel (Wallis)",   "domain": "analyse"},
    # --- ENSEMBLES DE NOMBRES ---
    {"s": "ℕ",    "strate": 0, "from": "Nombres naturels",           "domain": "nombres"},
    {"s": "ℤ",    "strate": 0, "from": "Entiers relatifs",           "domain": "nombres"},
    {"s": "ℚ",    "strate": 0, "from": "Rationnels",                 "domain": "nombres"},
    {"s": "ℝ",    "strate": 0, "from": "Réels",                      "domain": "nombres"},
    {"s": "ℂ",    "strate": 0, "from": "Complexes",                  "domain": "nombres"},
    {"s": "ℍ",    "strate": 0, "from": "Quaternions (Hamilton)",      "domain": "nombres"},
    {"s": "𝕆",    "strate": 0, "from": "Octonions",                  "domain": "nombres"},
    {"s": "ℙ",    "strate": 0, "from": "Nombres premiers",           "domain": "nombres"},
    {"s": "𝔽ₚ",   "strate": 0, "from": "Corps fini à p éléments",    "domain": "algèbre"},
    # --- CONSTANTES FONDAMENTALES ---
    {"s": "π",    "strate": 0, "from": "Pi ~3.14159 (Archimède)",     "domain": "géométrie"},
    {"s": "e",    "strate": 0, "from": "Euler ~2.71828",              "domain": "analyse"},
    {"s": "i",    "strate": 0, "from": "Unité imaginaire √(-1)",      "domain": "complexes"},
    {"s": "φ",    "strate": 0, "from": "Nombre d'or (1+√5)/2",       "domain": "nombres"},
    {"s": "γₑ",   "strate": 0, "from": "Constante Euler-Mascheroni",  "domain": "analyse"},
    {"s": "0",    "strate": 0, "from": "Zéro (Brahmagupta 628)",      "domain": "arithmétique"},
    {"s": "1",    "strate": 0, "from": "Unité",                       "domain": "arithmétique"},
    {"s": "2",    "strate": 0, "from": "Deux — seul premier pair",    "domain": "arithmétique"},
    {"s": "3",    "strate": 0, "from": "Trois — plus petit premier impair", "domain": "arithmétique"},
    {"s": "4",    "strate": 0, "from": "Quatre — premier carré >1",   "domain": "arithmétique"},
    {"s": "5",    "strate": 0, "from": "Cinq — base pentagonale",     "domain": "arithmétique"},
    {"s": "6",    "strate": 0, "from": "Six — premier nombre parfait (1+2+3)", "domain": "arithmétique"},
    {"s": "7",    "strate": 0, "from": "Sept — premier mersenne (2³-1)", "domain": "arithmétique"},
    {"s": "8",    "strate": 0, "from": "Huit — premier cube >1 (2³)", "domain": "arithmétique"},
    {"s": "9",    "strate": 0, "from": "Neuf — premier carré impair >1 (3²)", "domain": "arithmétique"},
    # --- CONSTANTES PHYSIQUES ---
    {"s": "c",    "strate": 0, "from": "Vitesse lumière 299792458 m/s","domain": "relativité"},
    {"s": "G",    "strate": 0, "from": "Constante gravitationnelle",   "domain": "gravitation"},
    {"s": "ℏ",    "strate": 0, "from": "Planck réduite h/2π",         "domain": "quantique"},
    {"s": "h",    "strate": 0, "from": "Constante de Planck",         "domain": "quantique"},
    {"s": "kB",   "strate": 0, "from": "Constante de Boltzmann",      "domain": "thermo"},
    {"s": "NA",   "strate": 0, "from": "Nombre d'Avogadro",           "domain": "chimie"},
    {"s": "R",    "strate": 0, "from": "Constante gaz parfaits",      "domain": "thermo"},
    {"s": "e⁻",   "strate": 0, "from": "Charge élémentaire",          "domain": "électromagn"},
    {"s": "μ₀",   "strate": 0, "from": "Perméabilité du vide",        "domain": "électromagn"},
    {"s": "ε₀",   "strate": 0, "from": "Permittivité du vide",        "domain": "électromagn"},
    {"s": "σ_SB", "strate": 0, "from": "Constante Stefan-Boltzmann",  "domain": "thermo"},
    {"s": "α_fs", "strate": 0, "from": "Constante structure fine ~1/137","domain": "quantique"},
    {"s": "mₑ",   "strate": 0, "from": "Masse électron",              "domain": "particules"},
    {"s": "mₚ",   "strate": 0, "from": "Masse proton",                "domain": "particules"},
    {"s": "mₙ",   "strate": 0, "from": "Masse neutron",               "domain": "particules"},
    {"s": "H₀",   "strate": 0, "from": "Constante de Hubble",         "domain": "cosmologie"},
    {"s": "T_CMB","strate": 0, "from": "Température CMB ~2.725K",      "domain": "cosmologie"},
    # --- THÉORIE DES ENSEMBLES ---
    {"s": "∈",    "strate": 0, "from": "Appartenance (Cantor)",       "domain": "ensembles"},
    {"s": "∉",    "strate": 0, "from": "Non-appartenance",            "domain": "ensembles"},
    {"s": "∅",    "strate": 0, "from": "Ensemble vide",               "domain": "ensembles"},
    {"s": "∪",    "strate": 0, "from": "Union",                       "domain": "ensembles"},
    {"s": "∩",    "strate": 0, "from": "Intersection",                "domain": "ensembles"},
    {"s": "⊂",    "strate": 0, "from": "Inclusion stricte",           "domain": "ensembles"},
    {"s": "⊆",    "strate": 0, "from": "Inclusion large",             "domain": "ensembles"},
    {"s": "⊃",    "strate": 0, "from": "Sur-ensemble strict",         "domain": "ensembles"},
    {"s": "⊇",    "strate": 0, "from": "Sur-ensemble large",          "domain": "ensembles"},
    {"s": "∖",    "strate": 0, "from": "Différence ensembliste",       "domain": "ensembles"},
    {"s": "△",    "strate": 0, "from": "Différence symétrique",        "domain": "ensembles"},
    {"s": "𝒫(A)", "strate": 0, "from": "Ensemble des parties",        "domain": "ensembles"},
    {"s": "A×B",  "strate": 0, "from": "Produit cartésien",           "domain": "ensembles"},
    {"s": "|A|",  "strate": 0, "from": "Cardinal d'un ensemble",      "domain": "ensembles"},
    {"s": "ℵ₀",   "strate": 0, "from": "Cardinal dénombrable (Cantor)","domain": "ensembles"},
    {"s": "ℵ₁",   "strate": 0, "from": "Premier indénombrable",        "domain": "ensembles"},
    {"s": "𝔠",    "strate": 0, "from": "Cardinal du continu",          "domain": "ensembles"},
    {"s": "ℶ",    "strate": 0, "from": "Nombre de Beth",               "domain": "ensembles"},
    {"s": "Aᶜ",   "strate": 0, "from": "Complément ensemble",          "domain": "ensembles"},
    {"s": "⊔",    "strate": 0, "from": "Union disjointe (coproduct)",   "domain": "ensembles"},
    {"s": "κ",    "strate": 0, "from": "Cardinal inaccessible (Hausdorff 1908)", "domain": "ensembles"},
    {"s": "cf",   "strate": 0, "from": "Cofinalité (König, théorie cardinaux)", "domain": "ensembles"},
    {"s": "Card", "strate": 0, "from": "Classe des cardinaux",          "domain": "ensembles"},
    # --- LOGIQUE PROPOSITIONNELLE & PRÉDICATS ---
    {"s": "∧",    "strate": 0, "from": "ET logique (conjonction)",     "domain": "logique"},
    {"s": "∨",    "strate": 0, "from": "OU logique (disjonction)",     "domain": "logique"},
    {"s": "¬",    "strate": 0, "from": "Négation",                     "domain": "logique"},
    {"s": "→",    "strate": 0, "from": "Implication",                  "domain": "logique"},
    {"s": "↔",    "strate": 0, "from": "Bi-implication",               "domain": "logique"},
    {"s": "⊤",    "strate": 0, "from": "Vrai (tautologie)",            "domain": "logique"},
    {"s": "⊥₀",   "strate": 0, "from": "Faux (contradiction)",         "domain": "logique"},
    {"s": "⊕",    "strate": 0, "from": "OU exclusif (XOR)",            "domain": "logique"},
    {"s": "⊨",    "strate": 0, "from": "Satisfaction / modèle",        "domain": "logique"},
    {"s": "⊩",    "strate": 0, "from": "Forcing (Cohen)",              "domain": "logique"},
    {"s": "∴",    "strate": 0, "from": "Donc / par conséquent",        "domain": "logique"},
    {"s": "∵",    "strate": 0, "from": "Parce que",                    "domain": "logique"},
    {"s": "⟹",   "strate": 0, "from": "Implique (méta)",              "domain": "logique"},
    {"s": "⟺",   "strate": 0, "from": "Ssi (si et seulement si)",     "domain": "logique"},
    {"s": "∄",    "strate": 0, "from": "N'existe pas (¬∃)",           "domain": "logique"},
    {"s": "∃!",   "strate": 0, "from": "Quantificateur existence unique", "domain": "logique"},
    {"s": "ZFC",  "strate": 0, "from": "Zermelo-Fraenkel + Choix (Zermelo 1908, Fraenkel 1922)", "domain": "logique"},
    {"s": "ZF",   "strate": 0, "from": "Zermelo-Fraenkel sans Choix",  "domain": "logique"},
    {"s": "CH",   "strate": 0, "from": "Hypothèse du Continu (Cantor 1878, indép. Cohen 1963)", "domain": "logique"},
    {"s": "GCH",  "strate": 0, "from": "Hypothèse Continu Généralisée", "domain": "logique"},
    {"s": "Con",  "strate": 0, "from": "Consistance Con(T) — Gödel 2ème incomplétude 1931", "domain": "logique"},
    {"s": "V=L",  "strate": 0, "from": "Axiome Constructibilité (Gödel 1938)", "domain": "logique"},
    {"s": "□",    "strate": 0, "from": "Nécessité (logique modale, Kripke 1963)", "domain": "logique"},
    {"s": "◇",    "strate": 0, "from": "Possibilité (logique modale, Kripke 1963)", "domain": "logique"},
    {"s": "⊩_forc","strate": 0, "from": "Forcing (Cohen 1963, indép. CH)", "domain": "logique"},
    # --- ANALYSE / CALCUL ---
    {"s": "∫",    "strate": 0, "from": "Intégrale (Leibniz 1675)",     "domain": "analyse"},
    {"s": "∬",    "strate": 0, "from": "Intégrale double",             "domain": "analyse"},
    {"s": "∭",    "strate": 0, "from": "Intégrale triple",             "domain": "analyse"},
    {"s": "∮",    "strate": 0, "from": "Intégrale de contour",         "domain": "analyse"},
    {"s": "∂",    "strate": 0, "from": "Dérivée partielle",            "domain": "analyse"},
    {"s": "d/dx", "strate": 0, "from": "Dérivée totale",               "domain": "analyse"},
    {"s": "dx",   "strate": 0, "from": "Différentielle (Leibniz)",     "domain": "analyse"},
    {"s": "f'",   "strate": 0, "from": "Dérivée notation Lagrange",    "domain": "analyse"},
    {"s": "ẋ",    "strate": 0, "from": "Dérivée temporelle Newton",    "domain": "analyse"},
    {"s": "∇",    "strate": 0, "from": "Nabla / gradient (Hamilton)",  "domain": "analyse"},
    {"s": "∇²",   "strate": 0, "from": "Laplacien",                    "domain": "analyse"},
    {"s": "∇×",   "strate": 0, "from": "Rotationnel (curl)",           "domain": "analyse"},
    {"s": "∇·",   "strate": 0, "from": "Divergence",                   "domain": "analyse"},
    {"s": "Δ",    "strate": 0, "from": "Laplacien / variation",        "domain": "analyse"},
    {"s": "δ",    "strate": 0, "from": "Dirac delta δ(x)",             "domain": "analyse"},
    {"s": "lim",  "strate": 0, "from": "Limite (Cauchy/Weierstrass)",  "domain": "analyse"},
    {"s": "sup",  "strate": 0, "from": "Supremum / borne supérieure",  "domain": "analyse"},
    {"s": "inf",  "strate": 0, "from": "Infimum / borne inférieure",   "domain": "analyse"},
    {"s": "max",  "strate": 0, "from": "Maximum",                      "domain": "analyse"},
    {"s": "min",  "strate": 0, "from": "Minimum",                      "domain": "analyse"},
    {"s": "Σ",    "strate": 0, "from": "Sommation finie",              "domain": "analyse"},
    {"s": "Π",    "strate": 0, "from": "Produit fini",                 "domain": "analyse"},
    {"s": "O(n)",  "strate": 0, "from": "Grand-O Landau complexité",   "domain": "analyse"},
    {"s": "o(n)",  "strate": 0, "from": "Petit-o Landau",              "domain": "analyse"},
    {"s": "Θ(n)",  "strate": 0, "from": "Theta Landau",                "domain": "analyse"},
    {"s": "ε",    "strate": 0, "from": "Epsilon voisinage",            "domain": "analyse"},
    # --- FONCTIONS SPÉCIALES ---
    {"s": "sin",  "strate": 0, "from": "Sinus",                       "domain": "trigonométrie"},
    {"s": "cos",  "strate": 0, "from": "Cosinus",                     "domain": "trigonométrie"},
    {"s": "tan",  "strate": 0, "from": "Tangente",                    "domain": "trigonométrie"},
    {"s": "cot",  "strate": 0, "from": "Cotangente",                  "domain": "trigonométrie"},
    {"s": "sec",  "strate": 0, "from": "Sécante",                     "domain": "trigonométrie"},
    {"s": "csc",  "strate": 0, "from": "Cosécante",                   "domain": "trigonométrie"},
    {"s": "arcsin","strate": 0, "from": "Arc sinus",                   "domain": "trigonométrie"},
    {"s": "arccos","strate": 0, "from": "Arc cosinus",                 "domain": "trigonométrie"},
    {"s": "arctan","strate": 0, "from": "Arc tangente",                "domain": "trigonométrie"},
    {"s": "sinh", "strate": 0, "from": "Sinus hyperbolique",          "domain": "trigonométrie"},
    {"s": "cosh", "strate": 0, "from": "Cosinus hyperbolique",        "domain": "trigonométrie"},
    {"s": "tanh", "strate": 0, "from": "Tangente hyperbolique",       "domain": "trigonométrie"},
    {"s": "ln",   "strate": 0, "from": "Logarithme naturel",          "domain": "analyse"},
    {"s": "log",  "strate": 0, "from": "Logarithme (Napier 1614)",    "domain": "analyse"},
    {"s": "log₂", "strate": 0, "from": "Logarithme base 2",           "domain": "information"},
    {"s": "exp",  "strate": 0, "from": "Exponentielle",               "domain": "analyse"},
    {"s": "Γ",    "strate": 0, "from": "Fonction Gamma d'Euler",      "domain": "analyse"},
    {"s": "B",    "strate": 0, "from": "Fonction Bêta B(x,y)",        "domain": "analyse"},
    {"s": "ζ",    "strate": 0, "from": "Zeta de Riemann ζ(s)",        "domain": "nb premiers"},
    {"s": "ξ",    "strate": 0, "from": "Xi — fonction de Riemann complétée", "domain": "nb premiers"},
    {"s": "η",    "strate": 0, "from": "Eta de Dedekind / Dirichlet",  "domain": "nb premiers"},
    {"s": "L(s,χ)","strate": 0, "from": "Fonction L de Dirichlet",     "domain": "nb premiers"},
    {"s": "Ai",   "strate": 0, "from": "Fonction d'Airy",             "domain": "analyse"},
    {"s": "Bi",   "strate": 0, "from": "Fonction d'Airy 2ème espèce",  "domain": "analyse"},
    {"s": "Jₙ",   "strate": 0, "from": "Fonction de Bessel 1ère",      "domain": "analyse"},
    {"s": "Yₙ",   "strate": 0, "from": "Fonction de Bessel 2ème",      "domain": "analyse"},
    {"s": "Pₙ",   "strate": 0, "from": "Polynômes de Legendre",        "domain": "analyse"},
    {"s": "Yₗₘ",  "strate": 0, "from": "Harmoniques sphériques",       "domain": "analyse"},
    {"s": "Hₙ",   "strate": 0, "from": "Polynômes de Hermite",         "domain": "analyse"},
    {"s": "Lₙ",   "strate": 0, "from": "Polynômes de Laguerre",        "domain": "analyse"},
    {"s": "Tₙ",   "strate": 0, "from": "Polynômes de Tchebychev",      "domain": "analyse"},
    {"s": "erf",  "strate": 0, "from": "Fonction d'erreur",            "domain": "probabilités"},
    {"s": "erfc", "strate": 0, "from": "Complémentaire erreur",         "domain": "probabilités"},
    {"s": "Φ",    "strate": 0, "from": "CDF normale standard",          "domain": "probabilités"},
    {"s": "W(x)", "strate": 0, "from": "Fonction W de Lambert",         "domain": "analyse"},
    {"s": "Li(x)","strate": 0, "from": "Logarithme intégral",           "domain": "nb premiers"},
    {"s": "Si(x)","strate": 0, "from": "Sinus intégral",                "domain": "analyse"},
    {"s": "Ci(x)","strate": 0, "from": "Cosinus intégral",              "domain": "analyse"},
    {"s": "Ei(x)","strate": 0, "from": "Exponentielle intégrale",       "domain": "analyse"},
    # --- ALGÈBRE LINÉAIRE ---
    {"s": "det",  "strate": 0, "from": "Déterminant",                 "domain": "algèbre lin"},
    {"s": "tr",   "strate": 0, "from": "Trace d'une matrice",         "domain": "algèbre lin"},
    {"s": "rank", "strate": 0, "from": "Rang d'une matrice",          "domain": "algèbre lin"},
    {"s": "dim",  "strate": 0, "from": "Dimension espace vectoriel",   "domain": "algèbre lin"},
    {"s": "span", "strate": 0, "from": "Espace engendré",              "domain": "algèbre lin"},
    {"s": "A⁻¹",  "strate": 0, "from": "Matrice inverse",              "domain": "algèbre lin"},
    {"s": "Aᵀ",   "strate": 0, "from": "Transposée",                   "domain": "algèbre lin"},
    {"s": "A†",   "strate": 0, "from": "Adjoint / conjugué transposé", "domain": "algèbre lin"},
    {"s": "⊗",    "strate": 0, "from": "Produit tensoriel",            "domain": "algèbre lin"},
    {"s": "⊕ₐ",   "strate": 0, "from": "Somme directe",                "domain": "algèbre lin"},
    {"s": "‖v‖",  "strate": 0, "from": "Norme d'un vecteur",           "domain": "algèbre lin"},
    {"s": "⟨u,v⟩","strate": 0, "from": "Produit scalaire",             "domain": "algèbre lin"},
    {"s": "u×v",  "strate": 0, "from": "Produit vectoriel",            "domain": "algèbre lin"},
    {"s": "λ",    "strate": 0, "from": "Valeur propre (eigenvalue)",   "domain": "algèbre lin"},
    {"s": "Iₙ",   "strate": 0, "from": "Matrice identité n×n",         "domain": "algèbre lin"},
    {"s": "diag", "strate": 0, "from": "Matrice diagonale",            "domain": "algèbre lin"},
    {"s": "⊙",    "strate": 0, "from": "Produit de Hadamard",          "domain": "algèbre lin"},
    # --- ALGÈBRE ABSTRAITE ---
    {"s": "Gal",  "strate": 0, "from": "Groupe de Galois",             "domain": "algèbre"},
    {"s": "Aut",  "strate": 0, "from": "Automorphismes",               "domain": "algèbre"},
    {"s": "Hom",  "strate": 0, "from": "Homomorphismes",               "domain": "algèbre"},
    {"s": "End",  "strate": 0, "from": "Endomorphismes",               "domain": "algèbre"},
    {"s": "Ker",  "strate": 0, "from": "Noyau (morphisme/application linéaire)", "domain": "algèbre"},
    {"s": "Im",   "strate": 0, "from": "Image (morphisme/application linéaire)", "domain": "algèbre"},
    {"s": "≅",    "strate": 0, "from": "Isomorphe",                    "domain": "algèbre"},
    {"s": "⊲",    "strate": 0, "from": "Sous-groupe normal",           "domain": "algèbre"},
    {"s": "G/H",  "strate": 0, "from": "Groupe quotient",              "domain": "algèbre"},
    {"s": "⋊",    "strate": 0, "from": "Produit semi-direct",          "domain": "algèbre"},
    {"s": "GL(n)","strate": 0, "from": "Groupe linéaire général",      "domain": "algèbre"},
    {"s": "SL(n)","strate": 0, "from": "Groupe linéaire spécial",      "domain": "algèbre"},
    {"s": "SO(n)","strate": 0, "from": "Groupe orthogonal spécial",    "domain": "algèbre"},
    {"s": "SU(n)","strate": 0, "from": "Groupe unitaire spécial",      "domain": "algèbre"},
    {"s": "U(1)", "strate": 0, "from": "Groupe unitaire",              "domain": "algèbre"},
    {"s": "SU(2)","strate": 0, "from": "Symétrie spin / isospin",      "domain": "particules"},
    {"s": "SU(3)","strate": 0, "from": "Chromodynamique quantique",    "domain": "particules"},
    {"s": "Sₙ",   "strate": 0, "from": "Groupe symétrique",            "domain": "algèbre"},
    {"s": "Zₙ",   "strate": 0, "from": "Groupe cyclique ℤ/nℤ",         "domain": "algèbre"},
    {"s": "⟨g⟩",  "strate": 0, "from": "Groupe engendré par g",        "domain": "algèbre"},
    {"s": "[G:H]","strate": 0, "from": "Indice sous-groupe",           "domain": "algèbre"},
    {"s": "R[x]", "strate": 0, "from": "Anneau de polynômes",          "domain": "algèbre"},
    {"s": "I⊲R",  "strate": 0, "from": "Idéal dans anneau",            "domain": "algèbre"},
    {"s": "F*/F", "strate": 0, "from": "Extension de corps",           "domain": "algèbre"},
    {"s": "Spec", "strate": 0, "from": "Spectre anneau (Grothendieck, géom algébrique)", "domain": "algèbre"},
    # --- THÉORIE DES CATÉGORIES ---
    {"s": "Ob(C)", "strate": 0, "from": "Objets d'une catégorie",       "domain": "catégories"},
    {"s": "Mor",   "strate": 0, "from": "Morphismes",                   "domain": "catégories"},
    {"s": "∘",     "strate": 0, "from": "Composition morphismes",       "domain": "catégories"},
    {"s": "Funct", "strate": 0, "from": "Foncteur",                     "domain": "catégories"},
    {"s": "Nat",   "strate": 0, "from": "Transformation naturelle",     "domain": "catégories"},
    {"s": "≃",     "strate": 0, "from": "Équivalence catégorielle",     "domain": "catégories"},
    {"s": "lim←",  "strate": 0, "from": "Limite projective",            "domain": "catégories"},
    {"s": "colim→","strate": 0, "from": "Colimite / limite inductive",  "domain": "catégories"},
    {"s": "Yoneda","strate": 0, "from": "Lemme de Yoneda",              "domain": "catégories"},
    {"s": "Adj",   "strate": 0, "from": "Adjonction foncteurs",         "domain": "catégories"},
    {"s": "Set",   "strate": 0, "from": "Catégorie des ensembles",      "domain": "catégories"},
    {"s": "Top",   "strate": 0, "from": "Catégorie espaces topologiques","domain": "catégories"},
    {"s": "Grp",   "strate": 0, "from": "Catégorie des groupes",        "domain": "catégories"},
    {"s": "Ab",    "strate": 0, "from": "Catégorie groupes abéliens",   "domain": "catégories"},
    {"s": "Vect",  "strate": 0, "from": "Catégorie espaces vectoriels", "domain": "catégories"},
    {"s": "↪",    "strate": 0, "from": "Injection / monomorphisme",     "domain": "catégories"},
    {"s": "↠",    "strate": 0, "from": "Surjection / épimorphisme",     "domain": "catégories"},
    # --- TOPOLOGIE ---
    {"s": "τ_top","strate": 0, "from": "Topologie sur X",              "domain": "topologie"},
    {"s": "π₁",   "strate": 0, "from": "Groupe fondamental",           "domain": "topologie"},
    {"s": "πₙ",   "strate": 0, "from": "n-ième groupe d'homotopie",    "domain": "topologie"},
    {"s": "Hₙ_top","strate": 0, "from": "n-ième groupe d'homologie",    "domain": "topologie"},
    {"s": "Hⁿ",   "strate": 0, "from": "n-ième groupe cohomologie",    "domain": "topologie"},
    {"s": "χ",     "strate": 0, "from": "Caractéristique d'Euler",      "domain": "topologie"},
    {"s": "g_top", "strate": 0, "from": "Genre d'une surface",          "domain": "topologie"},
    {"s": "∼",     "strate": 0, "from": "Homotopie / équivalence",      "domain": "topologie"},
    {"s": "S¹",    "strate": 0, "from": "Cercle (1-sphère)",            "domain": "topologie"},
    {"s": "Sⁿ",    "strate": 0, "from": "n-sphère",                     "domain": "topologie"},
    {"s": "T²",    "strate": 0, "from": "Tore",                         "domain": "topologie"},
    {"s": "RP²",   "strate": 0, "from": "Plan projectif réel",          "domain": "topologie"},
    {"s": "K_bot", "strate": 0, "from": "Bouteille de Klein",           "domain": "topologie"},
    {"s": "∂X",   "strate": 0, "from": "Bord topologique",              "domain": "topologie"},
    {"s": "cl(A)", "strate": 0, "from": "Adhérence / fermeture",        "domain": "topologie"},
    {"s": "int(A)","strate": 0, "from": "Intérieur topologique",        "domain": "topologie"},
    # --- GÉOMÉTRIE DIFFÉRENTIELLE ---
    {"s": "gμν",   "strate": 0, "from": "Tenseur métrique (Einstein)",   "domain": "géom diff"},
    {"s": "Rμν",   "strate": 0, "from": "Tenseur de Ricci",              "domain": "géom diff"},
    {"s": "Rμνρσ", "strate": 0, "from": "Tenseur de Riemann",            "domain": "géom diff"},
    {"s": "R_sc",  "strate": 0, "from": "Courbure scalaire",             "domain": "géom diff"},
    {"s": "Tμν",   "strate": 0, "from": "Tenseur énergie-impulsion",     "domain": "géom diff"},
    {"s": "Γᵢⱼₖ",  "strate": 0, "from": "Symboles de Christoffel",      "domain": "géom diff"},
    {"s": "∧_ext", "strate": 0, "from": "Produit extérieur / wedge (formes diff)","domain": "géom diff"},
    {"s": "dω",    "strate": 0, "from": "Dérivée extérieure",            "domain": "géom diff"},
    {"s": "★",     "strate": 0, "from": "Opérateur de Hodge",            "domain": "géom diff"},
    {"s": "£_X",   "strate": 0, "from": "Dérivée de Lie",                "domain": "géom diff"},
    {"s": "ωₐ",    "strate": 0, "from": "Forme de connexion",            "domain": "géom diff"},
    {"s": "Fₐᵦ",   "strate": 0, "from": "Tenseur de courbure (jauge)",   "domain": "géom diff"},
    {"s": "d_ext","strate": 0, "from": "Dérivée extérieure (Cartan 1899)", "domain": "géom diff"},
    # --- THÉORIE DES NOMBRES ---
    {"s": "≡_mod","strate": 0, "from": "Congruence modulo n",          "domain": "nb théorie"},
    {"s": "gcd",  "strate": 0, "from": "Plus grand commun diviseur",   "domain": "nb théorie"},
    {"s": "lcm",  "strate": 0, "from": "Plus petit commun multiple",   "domain": "nb théorie"},
    {"s": "φ_Eul","strate": 0, "from": "Indicatrice d'Euler φ(n)",     "domain": "nb théorie"},
    {"s": "μ_Mob","strate": 0, "from": "Fonction de Möbius μ(n)",      "domain": "nb théorie"},
    {"s": "π(x)", "strate": 0, "from": "Fonction de comptage premiers","domain": "nb théorie"},
    {"s": "σ(n)", "strate": 0, "from": "Somme des diviseurs",          "domain": "nb théorie"},
    {"s": "τ(n)", "strate": 0, "from": "Nombre de diviseurs",          "domain": "nb théorie"},
    {"s": "Λ(n)", "strate": 0, "from": "Fonction de von Mangoldt",     "domain": "nb théorie"},
    {"s": "(a/p)","strate": 0, "from": "Symbole de Legendre",          "domain": "nb théorie"},
    {"s": "ℓ-adic","strate": 0, "from": "Nombres ℓ-adiques",           "domain": "nb théorie"},
    {"s": "ℤₚ",   "strate": 0, "from": "Entiers p-adiques",            "domain": "nb théorie"},
    {"s": "Fₙ",   "strate": 0, "from": "Nombre de Fibonacci",          "domain": "nb théorie"},
    {"s": "Bₙ",   "strate": 0, "from": "Nombre de Bernoulli",          "domain": "nb théorie"},
    {"s": "Cl(K)","strate": 0, "from": "Groupe de classes idéales (Dedekind)", "domain": "nb théorie"},
    {"s": "Cₙ",   "strate": 0, "from": "Nombre de Catalan",            "domain": "combinatoire"},
    {"s": "C(n,k)","strate": 0, "from": "Coefficient binomial",         "domain": "combinatoire"},
    {"s": "χ_chrom","strate": 0, "from": "Nombre chromatique (coloration graphe)", "domain": "combinatoire"},
    {"s": "Kₙ",   "strate": 0, "from": "Graphe complet à n sommets",    "domain": "combinatoire"},
    # --- PROBABILITÉS & STATISTIQUES ---
    {"s": "P(A)",  "strate": 0, "from": "Probabilité événement A",      "domain": "probabilités"},
    {"s": "E[X]",  "strate": 0, "from": "Espérance",                    "domain": "probabilités"},
    {"s": "Var",   "strate": 0, "from": "Variance",                     "domain": "probabilités"},
    {"s": "σ_std", "strate": 0, "from": "Écart-type",                   "domain": "probabilités"},
    {"s": "Cov",   "strate": 0, "from": "Covariance",                   "domain": "probabilités"},
    {"s": "Cor",   "strate": 0, "from": "Corrélation",                  "domain": "probabilités"},
    {"s": "μ_moy", "strate": 0, "from": "Moyenne",                      "domain": "probabilités"},
    {"s": "σ²",    "strate": 0, "from": "Variance (notation)",          "domain": "probabilités"},
    {"s": "χ²",    "strate": 0, "from": "Test chi-carré Pearson",       "domain": "statistiques"},
    {"s": "t",     "strate": 0, "from": "Distribution de Student",      "domain": "statistiques"},
    {"s": "F_dist","strate": 0, "from": "Distribution de Fisher",       "domain": "statistiques"},
    {"s": "N(μ,σ²)","strate":0, "from": "Distribution normale",         "domain": "probabilités"},
    {"s": "Bin",   "strate": 0, "from": "Distribution binomiale",       "domain": "probabilités"},
    {"s": "Poi",   "strate": 0, "from": "Distribution de Poisson",      "domain": "probabilités"},
    {"s": "Exp_d", "strate": 0, "from": "Distribution exponentielle",   "domain": "probabilités"},
    {"s": "Bayes", "strate": 0, "from": "Théorème Bayes P(A|B)",        "domain": "probabilités"},
    {"s": "𝟙",     "strate": 0, "from": "Indicatrice / caractéristique","domain": "probabilités"},
    {"s": "⊥_ind","strate": 0, "from": "Indépendance stochastique (X⊥Y)", "domain": "probabilités"},
    # --- THÉORIE DE L'INFORMATION ---
    {"s": "H(X)",  "strate": 0, "from": "Entropie Shannon",             "domain": "information"},
    {"s": "I(X;Y)","strate": 0, "from": "Information mutuelle",         "domain": "information"},
    {"s": "D_KL",  "strate": 0, "from": "Divergence Kullback-Leibler",  "domain": "information"},
    {"s": "C_Sh",  "strate": 0, "from": "Capacité canal Shannon",       "domain": "information"},
    {"s": "H_Ren", "strate": 0, "from": "Entropie de Rényi",            "domain": "information"},
    # --- PHYSIQUE CLASSIQUE ---
    {"s": "F",     "strate": 0, "from": "Force Newton F=ma",            "domain": "mécanique"},
    {"s": "m",     "strate": 0, "from": "Masse",                        "domain": "mécanique"},
    {"s": "a_acc", "strate": 0, "from": "Accélération",                 "domain": "mécanique"},
    {"s": "v",     "strate": 0, "from": "Vitesse",                      "domain": "mécanique"},
    {"s": "p_mom", "strate": 0, "from": "Quantité de mouvement p=mv",   "domain": "mécanique"},
    {"s": "E_cin", "strate": 0, "from": "Énergie cinétique ½mv²",       "domain": "mécanique"},
    {"s": "V_pot", "strate": 0, "from": "Énergie potentielle",          "domain": "mécanique"},
    {"s": "W_trav","strate": 0, "from": "Travail W=F·d",                "domain": "mécanique"},
    {"s": "P_puis","strate": 0, "from": "Puissance P=W/t",              "domain": "mécanique"},
    {"s": "τ_couple","strate":0,"from": "Couple / torque τ=r×F",        "domain": "mécanique"},
    {"s": "L_ang", "strate": 0, "from": "Moment angulaire L=r×p",       "domain": "mécanique"},
    {"s": "I_iner","strate": 0, "from": "Moment d'inertie",             "domain": "mécanique"},
    {"s": "ω_ang", "strate": 0, "from": "Vitesse angulaire",            "domain": "mécanique"},
    {"s": "θ",     "strate": 0, "from": "Angle",                        "domain": "géométrie"},
    {"s": "g_grav","strate": 0, "from": "Accélération gravité ~9.81",   "domain": "gravitation"},
    {"s": "ρ_dens","strate": 0, "from": "Densité volumique",            "domain": "mécanique"},
    {"s": "P_pres","strate": 0, "from": "Pression",                     "domain": "fluides"},
    # --- LAGRANGIEN / HAMILTONIEN CLASSIQUE ---
    {"s": "ℒ",     "strate": 0, "from": "Lagrangien L=T-V",             "domain": "mécanique analytique"},
    {"s": "ℋ",     "strate": 0, "from": "Hamiltonien classique",        "domain": "mécanique analytique"},
    {"s": "S_act", "strate": 0, "from": "Action S=∫ℒdt",                "domain": "mécanique analytique"},
    {"s": "δS=0",  "strate": 0, "from": "Principe moindre action",      "domain": "mécanique analytique"},
    {"s": "{f,g}", "strate": 0, "from": "Crochet de Poisson",           "domain": "mécanique analytique"},
    {"s": "q",     "strate": 0, "from": "Coordonnée généralisée",       "domain": "mécanique analytique"},
    {"s": "p_gen", "strate": 0, "from": "Impulsion généralisée",        "domain": "mécanique analytique"},
    # --- ÉLECTROMAGNÉTISME ---
    {"s": "E_em",  "strate": 0, "from": "Champ électrique E",           "domain": "électromagn"},
    {"s": "B_em",  "strate": 0, "from": "Champ magnétique B",           "domain": "électromagn"},
    {"s": "V_pot_em","strate":0,"from": "Potentiel électrique V",       "domain": "électromagn"},
    {"s": "A_em",  "strate": 0, "from": "Potentiel vecteur A",          "domain": "électromagn"},
    {"s": "J_em",  "strate": 0, "from": "Densité de courant J",         "domain": "électromagn"},
    {"s": "ρ_ch",  "strate": 0, "from": "Densité de charge ρ",          "domain": "électromagn"},
    {"s": "Φ_B",   "strate": 0, "from": "Flux magnétique",              "domain": "électromagn"},
    {"s": "Fμν",   "strate": 0, "from": "Tenseur électromagnétique",    "domain": "électromagn"},
    {"s": "Aμ",    "strate": 0, "from": "Quadri-potentiel",             "domain": "électromagn"},
    # --- THERMODYNAMIQUE ---
    {"s": "S_ent", "strate": 0, "from": "Entropie S=k·ln(W)",          "domain": "thermo"},
    {"s": "T_temp","strate": 0, "from": "Température",                  "domain": "thermo"},
    {"s": "U_int", "strate": 0, "from": "Énergie interne",              "domain": "thermo"},
    {"s": "Q_chal","strate": 0, "from": "Chaleur",                      "domain": "thermo"},
    {"s": "W_therm","strate":0, "from": "Travail thermodynamique",      "domain": "thermo"},
    {"s": "F_helm","strate": 0, "from": "Énergie libre Helmholtz F=U-TS","domain": "thermo"},
    {"s": "G_gibb","strate": 0, "from": "Enthalpie libre Gibbs G=H-TS","domain": "thermo"},
    {"s": "H_enth","strate": 0, "from": "Enthalpie H=U+PV",            "domain": "thermo"},
    {"s": "Z_part","strate": 0, "from": "Fonction de partition Z",      "domain": "mécanique stat"},
    {"s": "β_inv", "strate": 0, "from": "Température inverse 1/kT",     "domain": "mécanique stat"},
    # --- RELATIVITÉ ---
    {"s": "ds²",   "strate": 0, "from": "Intervalle espace-temps",      "domain": "relativité"},
    {"s": "γ_lor", "strate": 0, "from": "Facteur Lorentz 1/√(1-v²/c²)","domain": "relativité"},
    {"s": "η_μν",  "strate": 0, "from": "Métrique de Minkowski",        "domain": "relativité"},
    {"s": "Gμν",   "strate": 0, "from": "Tenseur d'Einstein Gμν=Rμν-½gμνR","domain": "relativité"},
    {"s": "Λ_cos", "strate": 0, "from": "Constante cosmologique",       "domain": "relativité"},
    {"s": "rs",    "strate": 0, "from": "Rayon de Schwarzschild",       "domain": "relativité"},
    # --- MÉCANIQUE QUANTIQUE ---
    {"s": "ψ",     "strate": 0, "from": "Fonction d'onde",              "domain": "quantique"},
    {"s": "Ĥ",     "strate": 0, "from": "Opérateur hamiltonien",        "domain": "quantique"},
    {"s": "⟨ψ|",   "strate": 0, "from": "Bra (Dirac)",                  "domain": "quantique"},
    {"s": "|ψ⟩",   "strate": 0, "from": "Ket (Dirac)",                  "domain": "quantique"},
    {"s": "⟨ψ|ψ⟩", "strate": 0, "from": "Produit scalaire bra-ket",     "domain": "quantique"},
    {"s": "⟨Â⟩",   "strate": 0, "from": "Valeur moyenne observable",    "domain": "quantique"},
    {"s": "ΔxΔp",  "strate": 0, "from": "Heisenberg ΔxΔp≥ℏ/2",         "domain": "quantique"},
    {"s": "[Â,B̂]", "strate": 0, "from": "Commutateur quantique",        "domain": "quantique"},
    {"s": "ρ_dm",  "strate": 0, "from": "Matrice densité",              "domain": "quantique"},
    {"s": "Û",     "strate": 0, "from": "Opérateur unitaire évolution", "domain": "quantique"},
    {"s": "σₓ",    "strate": 0, "from": "Matrice Pauli σx",             "domain": "quantique"},
    {"s": "σᵧ",    "strate": 0, "from": "Matrice Pauli σy",             "domain": "quantique"},
    {"s": "σ_z",   "strate": 0, "from": "Matrice Pauli σz",             "domain": "quantique"},
    {"s": "|0⟩",   "strate": 0, "from": "Qubit état 0",                 "domain": "quantique"},
    {"s": "|1⟩",   "strate": 0, "from": "Qubit état 1",                 "domain": "quantique"},
    {"s": "H_gate","strate": 0, "from": "Porte Hadamard",               "domain": "quantique"},
    {"s": "CNOT",  "strate": 0, "from": "Porte CNOT",                   "domain": "quantique"},
    # --- QFT / MODÈLE STANDARD ---
    {"s": "ℒ_QFT","strate": 0, "from": "Lagrangien densité QFT",       "domain": "QFT"},
    {"s": "ψ̄",    "strate": 0, "from": "Spineur adjoint de Dirac",     "domain": "QFT"},
    {"s": "γμ",   "strate": 0, "from": "Matrices gamma Dirac",         "domain": "QFT"},
    {"s": "Dμ",   "strate": 0, "from": "Dérivée covariante jauge",     "domain": "QFT"},
    {"s": "Aμ_YM","strate": 0, "from": "Champ de jauge Yang-Mills",    "domain": "QFT"},
    {"s": "φ_Higgs","strate":0,"from": "Champ de Higgs",                "domain": "QFT"},
    {"s": "v_Higgs","strate":0,"from": "VEV Higgs ~246 GeV",            "domain": "QFT"},
    {"s": "αₛ",   "strate": 0, "from": "Constante couplage fort",      "domain": "QFT"},
    {"s": "g_w",  "strate": 0, "from": "Couplage faible",               "domain": "QFT"},
    {"s": "θ_W",  "strate": 0, "from": "Angle de Weinberg",             "domain": "QFT"},
    {"s": "CKM",  "strate": 0, "from": "Matrice CKM (quarks)",          "domain": "QFT"},
    {"s": "PMNS", "strate": 0, "from": "Matrice PMNS (neutrinos)",      "domain": "QFT"},
    # --- NAVIER-STOKES / FLUIDES ---
    {"s": "ν_visc","strate": 0, "from": "Viscosité cinématique",        "domain": "fluides"},
    {"s": "η_visc","strate": 0, "from": "Viscosité dynamique",          "domain": "fluides"},
    {"s": "Re",    "strate": 0, "from": "Nombre de Reynolds",           "domain": "fluides"},
    {"s": "Ma",    "strate": 0, "from": "Nombre de Mach",               "domain": "fluides"},
    {"s": "Fr",    "strate": 0, "from": "Nombre de Froude",             "domain": "fluides"},
    {"s": "NS",    "strate": 0, "from": "Équations Navier-Stokes",      "domain": "fluides"},
    # --- CHIMIE ---
    {"s": "mol",   "strate": 0, "from": "Mole (unité)",                 "domain": "chimie"},
    {"s": "pH",    "strate": 0, "from": "Potentiel hydrogène -log[H+]", "domain": "chimie"},
    {"s": "Kₑq",   "strate": 0, "from": "Constante d'équilibre",        "domain": "chimie"},
    {"s": "ΔG",    "strate": 0, "from": "Enthalpie libre réaction",     "domain": "chimie"},
    {"s": "ΔH",    "strate": 0, "from": "Enthalpie réaction",           "domain": "chimie"},
    {"s": "E°",    "strate": 0, "from": "Potentiel standard Nernst",    "domain": "chimie"},
    # --- ÉLÉMENTS FORMULES CÉLÈBRES ---
    {"s": "E=mc²", "strate": 0, "from": "Einstein 1905",                "domain": "relativité"},
    {"s": "F=ma",  "strate": 0, "from": "Newton 1687",                  "domain": "mécanique"},
    {"s": "eⁱᵖ+1=0","strate":0,"from": "Identité d'Euler",             "domain": "analyse"},
    {"s": "Res",  "strate": 0, "from": "Résidu analyse complexe (Cauchy 1825)", "domain": "analyse"},
    {"s": "a²+b²=c²","strate":0,"from":"Pythagore",                     "domain": "géométrie"},
    {"s": "S=kln W","strate":0, "from": "Boltzmann",                    "domain": "thermo"},
    {"s": "Hψ=Eψ","strate": 0, "from": "Schrödinger",                  "domain": "quantique"},
    {"s": "Gμν=8πGTμν","strate":0,"from":"Einstein field equations",    "domain": "relativité"},
    {"s": "∇·E=ρ/ε₀","strate":0,"from":"Maxwell (Gauss)",              "domain": "électromagn"},
    {"s": "∇·B=0","strate": 0, "from": "Maxwell (pas de monopôle)",    "domain": "électromagn"},
    {"s": "PV=nRT","strate": 0, "from": "Loi gaz parfaits",            "domain": "thermo"},
    # --- COMPLEXITÉ (décidable) ---
    {"s": "P",     "strate": 0, "from": "Classe P temps poly",          "domain": "complexité"},
    {"s": "L_log", "strate": 0, "from": "Espace logarithmique",         "domain": "complexité"},
    {"s": "NC",    "strate": 0, "from": "Nick's Class — parallélisme efficace (NC⊆P)", "domain": "complexité"},
    {"s": "AC",    "strate": 0, "from": "Circuit complexity",            "domain": "complexité"},
    {"s": "SC",    "strate": 0, "from": "Steve's Class",                 "domain": "complexité"},
    # --- CRYPTOGRAPHIE ---
    {"s": "RSA",   "strate": 0, "from": "Rivest-Shamir-Adleman",        "domain": "crypto"},
    {"s": "AES",   "strate": 0, "from": "Advanced Encryption Standard",  "domain": "crypto"},
    {"s": "ECC",   "strate": 0, "from": "Elliptic Curve Cryptography",   "domain": "crypto"},
    {"s": "SHA",   "strate": 0, "from": "Secure Hash Algorithm",         "domain": "crypto"},
    {"s": "ZKP",   "strate": 0, "from": "Zero-Knowledge Proof",          "domain": "crypto"},
    # --- GÉOMÉTRIE EUCLIDIENNE / REPÈRES ---
    {"s": "x",     "strate": 0, "from": "Coordonnée x",                 "domain": "géométrie"},
    {"s": "y",     "strate": 0, "from": "Coordonnée y",                 "domain": "géométrie"},
    {"s": "z",     "strate": 0, "from": "Coordonnée z",                 "domain": "géométrie"},
    {"s": "r",     "strate": 0, "from": "Rayon polaire/sphérique",      "domain": "géométrie"},
    {"s": "∠",     "strate": 0, "from": "Angle",                        "domain": "géométrie"},
    {"s": "⊥_geom","strate": 0, "from": "Perpendiculaire",              "domain": "géométrie"},
    {"s": "∥",     "strate": 0, "from": "Parallèle",                    "domain": "géométrie"},
    {"s": "≅_geom","strate": 0, "from": "Congruence géométrique",       "domain": "géométrie"},
    {"s": "∼_geom","strate": 0, "from": "Similitude",                   "domain": "géométrie"},
    # --- TRANSFORMÉES & TRAITEMENT DU SIGNAL ---
    {"s": "ℱ",     "strate": 0, "from": "Transformée de Fourier",        "domain": "signal"},
    {"s": "ℱ⁻¹",   "strate": 0, "from": "Transformée inverse Fourier",   "domain": "signal"},
    {"s": "ℒ_Lap", "strate": 0, "from": "Transformée de Laplace",        "domain": "signal"},
    {"s": "Z_tr",  "strate": 0, "from": "Transformée en Z (discret)",    "domain": "signal"},
    {"s": "DFT",   "strate": 0, "from": "Transformée de Fourier discrète","domain": "signal"},
    {"s": "FFT",   "strate": 0, "from": "Fast Fourier Transform (Cooley-Tukey 1965)", "domain": "signal"},
    {"s": "∗_conv","strate": 0, "from": "Convolution f∗g",              "domain": "signal"},
    {"s": "⊛",     "strate": 0, "from": "Corrélation croisée",          "domain": "signal"},
    {"s": "δ_Dir", "strate": 0, "from": "Peigne de Dirac (échantillonnage)", "domain": "signal"},
    {"s": "Nyquist","strate":0, "from": "Critère Nyquist-Shannon fₛ≥2B", "domain": "signal"},
    # --- ÉQUATIONS DIFFÉRENTIELLES ---
    {"s": "ODE",   "strate": 0, "from": "Équation diff ordinaire dy/dx=f(x,y)", "domain": "EDP"},
    {"s": "PDE",   "strate": 0, "from": "Équation aux dérivées partielles", "domain": "EDP"},
    {"s": "G_Grn", "strate": 0, "from": "Fonction de Green",            "domain": "EDP"},
    {"s": "∂²u/∂t²","strate":0,"from": "Équation des ondes",            "domain": "EDP"},
    {"s": "∂u/∂t", "strate": 0, "from": "Équation de la chaleur",       "domain": "EDP"},
    {"s": "Sturm", "strate": 0, "from": "Problème Sturm-Liouville",     "domain": "EDP"},
    # --- BIOLOGIE & GÉNÉTIQUE ---
    {"s": "DNA",   "strate": 0, "from": "Acide désoxyribonucléique (Watson-Crick 1953)", "domain": "biologie"},
    {"s": "RNA",   "strate": 0, "from": "Acide ribonucléique",          "domain": "biologie"},
    {"s": "ATP",   "strate": 0, "from": "Adénosine triphosphate (énergie cellulaire)", "domain": "biologie"},
    {"s": "Km",    "strate": 0, "from": "Constante Michaelis-Menten (enzymologie)", "domain": "biologie"},
    {"s": "Vmax",  "strate": 0, "from": "Vitesse max réaction enzymatique", "domain": "biologie"},
    {"s": "LV",    "strate": 0, "from": "Équations Lotka-Volterra (prédateur-proie)", "domain": "biologie"},
    {"s": "HW",    "strate": 0, "from": "Hardy-Weinberg p²+2pq+q²=1",   "domain": "biologie"},
    {"s": "R₀",    "strate": 0, "from": "Taux reproduction base (épidémiologie)", "domain": "biologie"},
    {"s": "SIR",   "strate": 0, "from": "Modèle SIR (Susceptible-Infecté-Rétabli)", "domain": "biologie"},
    {"s": "logist","strate": 0, "from": "Équation logistique dN/dt=rN(1-N/K)", "domain": "biologie"},
    # --- ÉCONOMIE & THÉORIE DES JEUX ---
    {"s": "U_util","strate": 0, "from": "Fonction d'utilité",            "domain": "économie"},
    {"s": "S_D",   "strate": 0, "from": "Offre et demande (Marshall)",   "domain": "économie"},
    {"s": "Nash",  "strate": 0, "from": "Équilibre de Nash (1950)",      "domain": "économie"},
    {"s": "Pareto","strate": 0, "from": "Optimum de Pareto",             "domain": "économie"},
    {"s": "π_payoff","strate":0,"from": "Fonction de payoff (jeux)",     "domain": "économie"},
    {"s": "BS",    "strate": 0, "from": "Black-Scholes (pricing options 1973)", "domain": "finance"},
    {"s": "σ_vol", "strate": 0, "from": "Volatilité (finance)",          "domain": "finance"},
    {"s": "VaR",   "strate": 0, "from": "Value at Risk",                 "domain": "finance"},
    {"s": "CAPM",  "strate": 0, "from": "Capital Asset Pricing Model (Sharpe)", "domain": "finance"},
    {"s": "GDP",   "strate": 0, "from": "Produit intérieur brut Y=C+I+G+NX", "domain": "économie"},
    # --- MACHINE LEARNING / IA ---
    {"s": "∇L",    "strate": 0, "from": "Gradient de la loss (descente de gradient)", "domain": "ML"},
    {"s": "σ_sigm","strate": 0, "from": "Sigmoïde σ(x)=1/(1+e⁻ˣ)",     "domain": "ML"},
    {"s": "softmax","strate":0, "from": "Softmax eˣⁱ/Σeˣʲ",            "domain": "ML"},
    {"s": "ReLU",  "strate": 0, "from": "Rectified Linear Unit max(0,x)","domain": "ML"},
    {"s": "CE",    "strate": 0, "from": "Cross-entropy loss -Σp·log(q)", "domain": "ML"},
    {"s": "SGD",   "strate": 0, "from": "Stochastic Gradient Descent",   "domain": "ML"},
    {"s": "BP",    "strate": 0, "from": "Backpropagation (Rumelhart 1986)", "domain": "ML"},
    {"s": "Attn",  "strate": 0, "from": "Attention Softmax(QKᵀ/√d)V (Vaswani 2017)", "domain": "ML"},
    {"s": "GAN",   "strate": 0, "from": "Generative Adversarial Network (Goodfellow 2014)", "domain": "ML"},
    {"s": "VC_dim","strate": 0, "from": "Dimension VC (Vapnik-Chervonenkis)", "domain": "ML"},
    {"s": "PAC",   "strate": 0, "from": "Probably Approximately Correct (Valiant 1984)", "domain": "ML"},
    # --- PHYSIQUE NUCLÉAIRE & PARTICULES ---
    {"s": "σ_xs",  "strate": 0, "from": "Section efficace (barn)",       "domain": "nucléaire"},
    {"s": "τ_decay","strate":0, "from": "Temps de vie demi-vie",         "domain": "nucléaire"},
    {"s": "λ_decay","strate":0, "from": "Constante de désintégration",   "domain": "nucléaire"},
    {"s": "A_mass","strate": 0, "from": "Nombre de masse",               "domain": "nucléaire"},
    {"s": "Z_at",  "strate": 0, "from": "Numéro atomique",               "domain": "nucléaire"},
    {"s": "β_decay","strate":0, "from": "Désintégration bêta",           "domain": "nucléaire"},
    {"s": "α_decay","strate":0, "from": "Désintégration alpha",          "domain": "nucléaire"},
    {"s": "Feyn",  "strate": 0, "from": "Diagrammes de Feynman (propagateur)", "domain": "QFT"},
    # --- OPTIQUE ---
    {"s": "n_refr","strate": 0, "from": "Indice de réfraction",          "domain": "optique"},
    {"s": "Snell", "strate": 0, "from": "Loi Snell-Descartes n₁sinθ₁=n₂sinθ₂", "domain": "optique"},
    {"s": "λ_wave","strate": 0, "from": "Longueur d'onde",               "domain": "optique"},
    {"s": "ν_freq","strate": 0, "from": "Fréquence",                     "domain": "optique"},
    {"s": "E=hν",  "strate": 0, "from": "Énergie photon (Planck 1900)",  "domain": "quantique"},
    {"s": "Ψ_wav","strate": 0, "from": "Fonction d'onde (Schrödinger 1926)", "domain": "quantique"},
    # --- ASTRONOMIE / COSMOLOGIE ---
    {"s": "M☉",    "strate": 0, "from": "Masse solaire ~2×10³⁰ kg",      "domain": "astronomie"},
    {"s": "L☉",    "strate": 0, "from": "Luminosité solaire ~3.8×10²⁶ W","domain": "astronomie"},
    {"s": "pc",    "strate": 0, "from": "Parsec ~3.26 années-lumière",    "domain": "astronomie"},
    {"s": "z_red", "strate": 0, "from": "Redshift cosmologique",         "domain": "cosmologie"},
    {"s": "Ω_m",   "strate": 0, "from": "Densité matière Ωm~0.3",       "domain": "cosmologie"},
    {"s": "Ω_Λ",   "strate": 0, "from": "Densité énergie noire ΩΛ~0.7", "domain": "cosmologie"},
    {"s": "FLRW",  "strate": 0, "from": "Métrique Friedmann-Lemaître-Robertson-Walker", "domain": "cosmologie"},
    {"s": "a(t)",  "strate": 0, "from": "Facteur d'échelle cosmologique", "domain": "cosmologie"},
    # --- THÉORIE DU CONTRÔLE ---
    {"s": "H(s)",  "strate": 0, "from": "Fonction de transfert",         "domain": "contrôle"},
    {"s": "PID",   "strate": 0, "from": "Contrôleur Proportionnel-Intégral-Dérivé", "domain": "contrôle"},
    {"s": "Bode",  "strate": 0, "from": "Diagramme de Bode (gain/phase)", "domain": "contrôle"},
    {"s": "Nyq_st","strate": 0, "from": "Critère stabilité Nyquist",     "domain": "contrôle"},
    # --- AUTOMATES & LANGAGES FORMELS ---
    {"s": "DFA",   "strate": 0, "from": "Automate fini déterministe",    "domain": "automates"},
    {"s": "NFA",   "strate": 0, "from": "Automate fini non-déterministe","domain": "automates"},
    {"s": "CFG",   "strate": 0, "from": "Grammaire hors-contexte (Chomsky)", "domain": "automates"},
    {"s": "PDA",   "strate": 0, "from": "Automate à pile",               "domain": "automates"},
    {"s": "TM",    "strate": 0, "from": "Machine de Turing (1936)",      "domain": "automates"},
    {"s": "UTM",   "strate": 0, "from": "Machine de Turing universelle", "domain": "automates"},
    {"s": "λ_calc","strate": 0, "from": "Lambda-calcul (Church 1936)",   "domain": "automates"},
    {"s": "Reg",   "strate": 0, "from": "Langages réguliers (Kleene)",   "domain": "automates"},
    {"s": "CFL",   "strate": 0, "from": "Langages hors-contexte",        "domain": "automates"},
    {"s": "Chom",  "strate": 0, "from": "Hiérarchie de Chomsky (4 niveaux)", "domain": "automates"},
    {"s": "PR",   "strate": 0, "from": "Fonctions primitives récursives (Gödel-Herbrand 1934)", "domain": "calculabilité"},
    {"s": "Ack",  "strate": 0, "from": "Fonction Ackermann (non PR, totale récursive, 1928)", "domain": "calculabilité"},
    # --- Théorie de la mesure (Lebesgue 1902) ---
    {"s": "μ_mes", "strate": 0, "from": "Mesure abstraite",                "domain": "mesure"},
    {"s": "σ(F)",  "strate": 0, "from": "σ-algèbre (tribu)",              "domain": "mesure"},
    {"s": "λ_Leb", "strate": 0, "from": "Mesure de Lebesgue (1902)",      "domain": "mesure"},
    {"s": "Lp",    "strate": 0, "from": "Espaces Lp (Riesz 1910)",        "domain": "mesure"},
    {"s": "a.e.",  "strate": 0, "from": "Presque partout (almost everywhere)", "domain": "mesure"},
    {"s": "dμ",    "strate": 0, "from": "Intégration par rapport à μ",    "domain": "mesure"},
    {"s": "RN",    "strate": 0, "from": "Radon-Nikodym dν/dμ (1930)",     "domain": "mesure"},
    # --- Calcul stochastique ---
    {"s": "W(t)",  "strate": 0, "from": "Mouvement brownien (Wiener 1923)", "domain": "stochastique"},
    {"s": "dW",    "strate": 0, "from": "Incréments browniens",           "domain": "stochastique"},
    {"s": "Itô",   "strate": 0, "from": "Intégrale d'Itô (1944)",        "domain": "stochastique"},
    {"s": "SDE",   "strate": 0, "from": "Équation diff. stochastique",    "domain": "stochastique"},
    {"s": "E[·|F]","strate": 0, "from": "Espérance conditionnelle (filtration)", "domain": "stochastique"},
    {"s": "Mart",  "strate": 0, "from": "Martingale (Doob 1953)",         "domain": "stochastique"},
    # --- Optimisation ---
    {"s": "argmin","strate": 0, "from": "Argument du minimum",            "domain": "optimisation"},
    {"s": "argmax","strate": 0, "from": "Argument du maximum",            "domain": "optimisation"},
    {"s": "L_lag", "strate": 0, "from": "Lagrangien (Lagrange 1788)",     "domain": "optimisation"},
    {"s": "KKT",   "strate": 0, "from": "Conditions KKT (Karush-Kuhn-Tucker 1951)", "domain": "optimisation"},
    {"s": "LP",    "strate": 0, "from": "Programmation linéaire (Dantzig 1947)", "domain": "optimisation"},
    {"s": "∇f=0",  "strate": 0, "from": "Condition de stationnarité",     "domain": "optimisation"},
    # --- Analyse fonctionnelle ---
    {"s": "H_Hilb","strate": 0, "from": "Espace de Hilbert (1906)",       "domain": "analyse fonctionnelle"},
    {"s": "B_Ban", "strate": 0, "from": "Espace de Banach (1920)",        "domain": "analyse fonctionnelle"},
    {"s": "⟨·,·⟩_H","strate": 0,"from": "Produit scalaire Hilbert",      "domain": "analyse fonctionnelle"},
    {"s": "X*",    "strate": 0, "from": "Dual topologique",               "domain": "analyse fonctionnelle"},
    {"s": "L²",    "strate": 0, "from": "Espace L² (carré intégrable)",   "domain": "analyse fonctionnelle"},
    {"s": "HB",    "strate": 0, "from": "Hahn-Banach (1929)",             "domain": "analyse fonctionnelle"},
    {"s": "ℓ²",   "strate": 0, "from": "Espace suites carré-sommables", "domain": "analyse fonctionnelle"},
    {"s": "W^k,p","strate": 0, "from": "Espace Sobolev (Sobolev 1938, PDE)", "domain": "analyse fonctionnelle"},
    # STRATE 1 — Σ⁰₁ · Récursivement énumérable
    # ==================================================================
    {"s": "∃",     "strate": 1, "from": "Quantificateur existentiel",    "domain": "logique"},
    {"s": "K",     "strate": 1, "from": "Halting set K={e:φₑ(e)↓}",     "domain": "calculabilité"},
    {"s": "φₑ",    "strate": 1, "from": "e-ième fonction partielle",    "domain": "calculabilité"},
    {"s": "↓",     "strate": 1, "from": "Converge (s'arrête)",          "domain": "calculabilité"},
    {"s": "↑",     "strate": 1, "from": "Diverge (boucle infinie)",     "domain": "calculabilité"},
    {"s": "Wₑ",    "strate": 1, "from": "e-ième ensemble r.e.",         "domain": "calculabilité"},
    {"s": "μy",    "strate": 1, "from": "Opérateur μ recherche",        "domain": "calculabilité"},
    {"s": "≤ₘ",    "strate": 1, "from": "Réduction many-one",          "domain": "calculabilité"},
    {"s": "≤ₜ",    "strate": 1, "from": "Réduction Turing",            "domain": "calculabilité"},
    {"s": "RE",    "strate": 1, "from": "Récursivement énumérable",     "domain": "calculabilité"},
    {"s": "coRE",  "strate": 1, "from": "Complément de RE",             "domain": "calculabilité"},
    {"s": "NP",    "strate": 1, "from": "Non-déterministe polynomial",  "domain": "complexité"},
    {"s": "coNP",  "strate": 1, "from": "Complément de NP",             "domain": "complexité"},
    {"s": "NL",    "strate": 0, "from": "Non-det espace log (NL⊆P, Savitch)", "domain": "complexité"},
    {"s": "L_lang","strate": 0, "from": "Classe L espace log déterministe (L⊆NL⊆P)", "domain": "complexité"},
    {"s": "DTIME","strate": 0, "from": "Temps déterministe DTIME(f(n))", "domain": "complexité"},
    {"s": "NTIME","strate": 0, "from": "Temps non-déterministe NTIME(f(n))", "domain": "complexité"},
    {"s": "DSPACE","strate": 0, "from": "Espace déterministe DSPACE(f(n))", "domain": "complexité"},
    {"s": "NSPACE","strate": 0, "from": "Espace non-déterministe NSPACE(f(n))", "domain": "complexité"},
    {"s": "AC⁰",  "strate": 0, "from": "Circuits profondeur constante taille poly", "domain": "complexité"},
    {"s": "TC⁰",  "strate": 0, "from": "Threshold circuits (majorité)", "domain": "complexité"},
    {"s": "SAT",   "strate": 1, "from": "Satisfiabilité Cook 1971",     "domain": "complexité"},
    {"s": "3SAT",  "strate": 1, "from": "3-SAT NP-complet",             "domain": "complexité"},
    {"s": "3COL",  "strate": 1, "from": "3-coloration graphe",          "domain": "complexité"},
    {"s": "TSP",   "strate": 1, "from": "Voyageur de commerce",         "domain": "complexité"},
    {"s": "CLIQUE","strate": 1, "from": "Problème de la clique",        "domain": "complexité"},
    {"s": "SUBSET","strate": 1, "from": "Subset Sum",                   "domain": "complexité"},
    {"s": "HAM",   "strate": 1, "from": "Chemin hamiltonien",           "domain": "complexité"},
    {"s": "ILP",   "strate": 1, "from": "Integer Linear Programming",   "domain": "complexité"},
    {"s": "BQP",   "strate": 1, "from": "Bounded-error Quantum Poly",   "domain": "quantique"},
    {"s": "NP-C",  "strate": 1, "from": "NP-Complet (Cook-Levin 1971)", "domain": "complexité"},
    {"s": "NP-H",  "strate": 1, "from": "NP-Hard",                      "domain": "complexité"},
    {"s": "VERTEX","strate": 1, "from": "Vertex Cover (Karp 1972)",      "domain": "complexité"},
    {"s": "SETCOV","strate": 1, "from": "Set Cover (Karp 1972)",         "domain": "complexité"},
    {"s": "KNAP",  "strate": 1, "from": "Knapsack / Sac à dos",         "domain": "complexité"},
    {"s": "PART",  "strate": 1, "from": "Partition (Karp 1972)",         "domain": "complexité"},
    {"s": "MAXCUT","strate": 1, "from": "Maximum Cut (Karp 1972)",       "domain": "complexité"},
    {"s": "3DM",   "strate": 1, "from": "3-Dimensional Matching (Karp)", "domain": "complexité"},
    {"s": "GI",    "strate": 1, "from": "Graph Isomorphism (NP, non NP-complet connu)", "domain": "complexité"},
    {"s": "Ladner","strate": 1, "from": "Ladner: si P≠NP ∃ NP-intermédiaire (1975)", "domain": "complexité"},
    {"s": "Cook",  "strate": 1, "from": "Théorème Cook-Levin: SAT est NP-complet (1971)", "domain": "complexité"},
    {"s": "Σ⁰₁",   "strate": 1, "from": "Classe Σ⁰₁ (r.e.) de la hiérarchie", "domain": "calculabilité"},
    {"s": "Π⁰₁",   "strate": 1, "from": "Classe Π⁰₁ (co-r.e.)",       "domain": "calculabilité"},
    {"s": "P/poly","strate": 1, "from": "P avec conseil polynomial (circuits)", "domain": "complexité"},
    # ==================================================================
    # STRATE 2 — Σ⁰₂ · Limite
    # ==================================================================
    {"s": "∀",     "strate": 2, "from": "Quantificateur universel",     "domain": "logique"},
    {"s": "∃∀",    "strate": 2, "from": "Alternance Σ⁰₂",              "domain": "calculabilité"},
    {"s": "TOT",   "strate": 2, "from": "{e : φₑ totale} Π₂-complet",  "domain": "calculabilité"},
    {"s": "FIN",   "strate": 2, "from": "{e : Wₑ fini} Σ₂-complet",    "domain": "calculabilité"},
    {"s": "∅'",    "strate": 2, "from": "Turing jump ∅'",               "domain": "calculabilité"},
    {"s": "∅''",   "strate": 2, "from": "Double saut ∅''",              "domain": "calculabilité"},
    {"s": "Δ⁰₂",   "strate": 2, "from": "Σ⁰₂ ∩ Π⁰₂ (limit computable)", "domain": "calculabilité"},
    {"s": "BPP",   "strate": 2, "from": "Bounded-error Probabilistic (⊆ Σ₂∩Π₂)", "domain": "complexité"},
    {"s": "SZK",   "strate": 2, "from": "Statistical Zero Knowledge (⊆ AM∩coAM)", "domain": "crypto"},
    {"s": "RP",    "strate": 2, "from": "Randomized Polynomial (one-sided error)", "domain": "complexité"},
    {"s": "coRP",  "strate": 2, "from": "Complement RP",                "domain": "complexité"},
    {"s": "ZPP",   "strate": 2, "from": "Zero-error Probabilistic (=RP∩coRP)", "domain": "complexité"},
    {"s": "Post",  "strate": 2, "from": "Théorème Post: Σ⁰ₙ↔∅⁽ⁿ⁾ (hiérarchie=sauts)", "domain": "calculabilité"},
    {"s": "Lim",   "strate": 2, "from": "Shoenfield Limit Lemma (Δ⁰₂=limit computable)", "domain": "calculabilité"},
    {"s": "Low",   "strate": 2, "from": "Degré Low: A'=∅' (faible complexité)", "domain": "calculabilité"},
    {"s": "High",  "strate": 2, "from": "Degré High: A'=∅'' (forte complexité)", "domain": "calculabilité"},
    {"s": "INF",   "strate": 2, "from": "{e : Wₑ infini} Π₂-complet",  "domain": "calculabilité"},
    {"s": "Σ⁰₂",   "strate": 2, "from": "Classe Σ⁰₂ de la hiérarchie", "domain": "calculabilité"},
    {"s": "Π⁰₂",   "strate": 2, "from": "Classe Π⁰₂ de la hiérarchie", "domain": "calculabilité"},
    # ==================================================================
    # STRATE 3 — Σ⁰ₙ · Motif
    # ==================================================================
    {"s": "Σ⁰ₙ",   "strate": 3, "from": "n-ième existentiel",          "domain": "calculabilité"},
    {"s": "Π⁰ₙ",   "strate": 3, "from": "n-ième universel",            "domain": "calculabilité"},
    {"s": "Δ⁰ₙ",   "strate": 3, "from": "Σ⁰ₙ ∩ Π⁰ₙ",                  "domain": "calculabilité"},
    {"s": "∅⁽ⁿ⁾",  "strate": 3, "from": "n-ième saut Turing",          "domain": "calculabilité"},
    {"s": "ΣₖP",   "strate": 3, "from": "k-ième niveau PH existentiel","domain": "complexité"},
    {"s": "ΠₖP",   "strate": 3, "from": "k-ième niveau PH universel",  "domain": "complexité"},
    {"s": "ΔₖP",   "strate": 3, "from": "k-ième niveau PH déterministe (P^Σₖ₋₁)", "domain": "complexité"},
    {"s": "PH",    "strate": 3, "from": "Polynomial Hierarchy ∪ₖΣₖP",  "domain": "complexité"},
    {"s": "#P",    "strate": 3, "from": "Comptage — Valiant 1979",      "domain": "complexité"},
    {"s": "MA",    "strate": 3, "from": "Merlin-Arthur",                "domain": "complexité"},
    {"s": "AM",    "strate": 3, "from": "Arthur-Merlin (Babai 1985)",   "domain": "complexité"},
    {"s": "PP",    "strate": 3, "from": "Probabilistic Polynomial",     "domain": "complexité"},
    {"s": "⊕P",    "strate": 3, "from": "Parité — Parity-P",           "domain": "complexité"},
    {"s": "Σ₂P",   "strate": 3, "from": "2ème niveau existentiel PH",   "domain": "complexité"},
    {"s": "Π₂P",   "strate": 3, "from": "2ème niveau universel PH",     "domain": "complexité"},
    {"s": "Toda",  "strate": 3, "from": "Théorème Toda: PH ⊆ P^#P (1991)", "domain": "complexité"},
    {"s": "QMA",   "strate": 3, "from": "Quantum Merlin-Arthur",        "domain": "quantique"},
    {"s": "#SAT",  "strate": 3, "from": "Compter solutions SAT (#P-complet)", "domain": "complexité"},
    {"s": "GapP",  "strate": 3, "from": "Fonctions de gap (différence de #P)", "domain": "complexité"},
    {"s": "C₌P",   "strate": 3, "from": "Exact counting complexity",    "domain": "complexité"},
    {"s": "COF",   "strate": 3, "from": "{e : Wₑ cofini} Σ₃-complet",  "domain": "calculabilité"},
    {"s": "REC",   "strate": 3, "from": "{e : Wₑ récursif} Σ₃-complet","domain": "calculabilité"},
    # --- Strate 3 : grandes conjectures résolues (théorèmes) ---
    {"s": "FermatWiles","strate": 3, "from": "Dernier théorème Fermat / modularité (Wiles 1995, BCDT 2001)", "domain": "nb théorie"},
    {"s": "Milnor_K",  "strate": 3, "from": "Conjecture Milnor K-théorie — K^M_n(F)/2 ≅ H^n(F,ℤ/2) (Voevodsky 2003)", "domain": "algèbre"},
    {"s": "BlochKato", "strate": 3, "from": "Conjecture Bloch-Kato norm residue — K^M_n(F)/ℓ ≅ H^n(F,μ_ℓ^⊗n) (Rost-Voevodsky 2011)", "domain": "algèbre"},
    {"s": "SatoTate",  "strate": 3, "from": "Conjecture Sato-Tate — distribution Frobenius courbes elliptiques (Taylor et al. 2011)", "domain": "nb théorie"},
    {"s": "KazhLusz",  "strate": 3, "from": "Conjecture Kazhdan-Lusztig — multiplicités modules Verma (Beilinson-Bernstein 1981)", "domain": "algèbre"},
    {"s": "KadSinger", "strate": 3, "from": "Kadison-Singer — extension états purs B(H) (Marcus-Spielman-Srivastava 2013)", "domain": "analyse fonctionnelle"},
    {"s": "VirtHaken", "strate": 3, "from": "Virtual Haken — 3-variétés hyperboliques (Agol 2012, Wise, Kahn-Markovic)", "domain": "topologie"},
    {"s": "KakeyaFin", "strate": 3, "from": "Kakeya corps finis — Besicovitch sets F_q^n (Dvir 2008, méthode polynomiale)", "domain": "combinatoire"},
    {"s": "Onsager_c", "strate": 3, "from": "Conjecture Onsager — Euler C^α conservation énergie ssi α>1/3 (Isett 2018, BDSV 2019)", "domain": "analyse"},
    # --- Strate 3 : TOPOLOGIE — grands théorèmes résolus ---
    {"s": "Poinc3",    "strate": 3, "from": "Conjecture Poincaré dim 3 — toute 3-variété simplement connexe fermée ≅ S³ (Perelman 2003, flot de Ricci)", "domain": "topologie"},
    {"s": "Geomtrz",   "strate": 3, "from": "Géométrisation Thurston — toute 3-variété se décompose en 8 géométries (Perelman 2003)", "domain": "topologie"},
    {"s": "hCobord",   "strate": 3, "from": "h-cobordism theorem — dim ≥ 6 (Smale 1962, Fields Medal). Implique Poincaré généralisé dim ≥ 5.", "domain": "topologie"},
    {"s": "Freed4",    "strate": 3, "from": "Freedman theorem — classification topologique 4-variétés simplement connexes fermées (1982, Fields Medal)", "domain": "topologie"},
    {"s": "SmithConj", "strate": 3, "from": "Smith conjecture — action Zₚ sur S³ a point fixe = nœud trivial (Morgan-Bass 1984)", "domain": "topologie"},
    {"s": "ExoticS7",  "strate": 3, "from": "Sphères exotiques Milnor — S⁷ admet 28 structures diff. non-standard (Milnor 1956, Kervaire-Milnor 1963)", "domain": "topologie"},
    {"s": "Surgery",   "strate": 3, "from": "Théorie chirurgie — classification variétés dim ≥ 5 (Browder-Novikov-Sullivan-Wall 1960s)", "domain": "topologie"},
    # --- Strate 3 : THÉORIE DES NOMBRES — grands théorèmes résolus ---
    {"s": "Mordell",   "strate": 3, "from": "Conjecture Mordell — courbe genre ≥ 2 sur ℚ a nombre fini de points rationnels (Faltings 1983, Fields Medal)", "domain": "nb théorie"},
    {"s": "WeilConj",  "strate": 3, "from": "Conjectures Weil — fonctions zêta variétés /F_q: rationalité (Dwork), fonctionnalité, RH (Deligne 1974, Fields Medal)", "domain": "nb théorie"},
    {"s": "CatalanM",  "strate": 3, "from": "Conjecture Catalan — x^p - y^q = 1 ⟹ 3²-2³=1 seule solution (Mihailescu 2002)", "domain": "nb théorie"},
    {"s": "GoldWeak",  "strate": 3, "from": "Goldbach faible (ternaire) — tout impair > 5 somme de 3 premiers (Helfgott 2013)", "domain": "nb théorie"},
    {"s": "BddGaps",   "strate": 3, "from": "Bounded prime gaps — lim inf (pₙ₊₁-pₙ) < ∞ (Zhang 2013: 7×10⁷, Maynard 2013: 600, Polymath8: 246)", "domain": "nb théorie"},
    {"s": "GrossZag",  "strate": 3, "from": "Formule Gross-Zagier — hauteur point Heegner = L'(E,1) (1986). Clé pour BSD rang 1.", "domain": "nb théorie"},
    {"s": "HerbRibet", "strate": 3, "from": "Herbrand-Ribet — p|Bₖ ⟺ p|#Cl(ℚ(ζₚ))_χ (Herbrand 1932 →, Ribet 1976 ←). Lien Bernoulli/corps cyclotomiques.", "domain": "nb théorie"},
    {"s": "IwasMain",  "strate": 3, "from": "Iwasawa Main Conjecture — structure Λ-modules sur tours cyclotomiques (Mazur-Wiles 1984)", "domain": "nb théorie"},
    {"s": "SerreMod",  "strate": 3, "from": "Conjecture Serre modularité — repr. Galois irréd. impaires mod p sont modulaires (Khare-Wintenberger 2009)", "domain": "nb théorie"},
    {"s": "LaffFnF",   "strate": 3, "from": "Langlands pour corps de fonctions GL_n (Laurent Lafforgue 2002, Fields Medal)", "domain": "nb théorie"},
    # --- Strate 3 : ALGÈBRE — grands théorèmes résolus ---
    {"s": "CFSG",      "strate": 3, "from": "Classification groupes finis simples — 18 familles + 26 sporadiques (~1983, ~10000 pages, Gorenstein program)", "domain": "algèbre"},
    {"s": "Moonshine", "strate": 3, "from": "Monstrous Moonshine — j(τ) et Monster group (Conway-Norton 1979, prouvé Borcherds 1992, Fields Medal)", "domain": "algèbre"},
    {"s": "QuilSusl",  "strate": 3, "from": "Conjecture Serre (Quillen-Suslin) — modules proj. sur k[x₁..xₙ] sont libres (Quillen, Suslin 1976)", "domain": "algèbre"},
    # --- Strate 3 : ANALYSE — grands théorèmes résolus ---
    {"s": "Bieberbach","strate": 3, "from": "Théorème de Branges (ex-conj. Bieberbach) — |aₙ| ≤ n pour fonctions univalentes (De Branges 1985, Acta Math)", "domain": "analyse"},
    {"s": "CarlesonL2","strate": 3, "from": "Convergence p.p. séries Fourier L² — (Carleson 1966, Abel Prize 2006). Étendu Lᵖ p>1 (Hunt 1968).", "domain": "analyse"},
    {"s": "KatoSqrt",  "strate": 3, "from": "Conjecture Kato racine carrée — √(div A grad) a domaine H¹ (Auscher-Hofmann-Lacey-McIntosh-Tchamitchian 2001)", "domain": "analyse"},
    {"s": "CoronaTh",  "strate": 3, "from": "Théorème Corona — Spec maximal H^∞ dense dans le spectre (Carleson 1962)", "domain": "analyse"},
    # --- Strate 3 : GÉOMÉTRIE — grands théorèmes résolus ---
    {"s": "CalabiYau", "strate": 3, "from": "Conjecture Calabi — existence métrique Kähler Ricci-plate si c₁=0 (Yau 1978, Fields Medal)", "domain": "géom diff"},
    {"s": "PosMass",   "strate": 3, "from": "Positive mass theorem — masse ADM ≥ 0 (Schoen-Yau 1979, Witten 1981). Fondamental en RG.", "domain": "géom diff"},
    {"s": "Kepler",    "strate": 3, "from": "Conjecture Kepler — empilement sphères densité max π/(3√2) = FCC/HCP (Hales 2005, Flyspeck 2014 vérifié formellement)", "domain": "géométrie"},
    {"s": "Willmore",  "strate": 3, "from": "Conjecture Willmore — min ∫H²dA pour tores immergés = 2π² (Marques-Neves 2014, min-max)", "domain": "géom diff"},
    {"s": "AtiyahSing","strate": 3, "from": "Théorème index Atiyah-Singer — ind(D) = ∫ch(σ)Td(M) (1963, généralisé K-théorie). Pont analyse↔topologie.", "domain": "géom diff"},
    # --- Strate 3 : COMBINATOIRE — grands théorèmes résolus ---
    {"s": "FourColor", "strate": 3, "from": "Théorème 4 couleurs — tout graphe planaire 4-coloriable (Appel-Haken 1976, Robertson et al. 1997, Gonthier 2005 Coq)", "domain": "combinatoire"},
    {"s": "RobSeym",   "strate": 3, "from": "Graph Minor Theorem — tout ensemble infini de graphes a mineur (Robertson-Seymour 1983-2004, 20 papers)", "domain": "combinatoire"},
    {"s": "GreenTao",  "strate": 3, "from": "Green-Tao — les premiers contiennent des PA de longueur arbitraire (2004). Utilise Szemerédi + transference.", "domain": "combinatoire"},
    {"s": "DensHJ",    "strate": 3, "from": "Density Hales-Jewett — version densité du théorème HJ (Polymath1, 2009/2012)", "domain": "combinatoire"},
    {"s": "Kneser",    "strate": 3, "from": "Conjecture Kneser — χ(KG(n,k)) = n-2k+2 (Lovász 1978, topologie de Borsuk-Ulam appliquée aux graphes)", "domain": "combinatoire"},
    # --- Strate 3 : PROBABILITÉS — grands théorèmes résolus ---
    {"s": "SLE_thm",   "strate": 3, "from": "SLE/percolation — invariance conforme percolation critique sur réseau triangulaire (Smirnov 2001, Fields Medal 2010)", "domain": "probabilités"},
    # --- Strate 3 : LOGIQUE/INDÉPENDANCE — résultats prouvés ---
    {"s": "ParisHarr", "strate": 3, "from": "Paris-Harrington — variante Ramsey indépendante de PA (1977). Premier exemple 'naturel' d'indépendance.", "domain": "logique"},
    {"s": "DPRM",      "strate": 3, "from": "Théorème DPRM — ensembles r.e. = ensembles diophantiens (Davis-Putnam-Robinson 1961, Matiyasevich 1970). H10 négatif.", "domain": "logique"},
    # --- Strate 3 vague 2 : grands théorèmes prouvés (suite) ---
    # Géom algébrique / algèbre commutative
    {"s": "Hironaka",  "strate": 3, "from": "Résolution des singularités en car. 0 — tout variété admet désingularisation (Hironaka 1964, Fields Medal)", "domain": "géom algébrique"},
    {"s": "FundLemma", "strate": 3, "from": "Lemme fondamental Langlands-Shelstad — identité orbitale pour endoscopie (Ngô Bảo Châu 2008, Fields Medal 2010)", "domain": "nb théorie"},
    # Combinatoire additive / théorie ergodique
    {"s": "Szemer",    "strate": 3, "from": "Théorème Szemerédi — tout ensemble de densité positive dans ℕ contient des PA de longueur k (1975, Abel Prize 2012). Preuve ergodique Furstenberg 1977.", "domain": "combinatoire"},
    {"s": "RothAP",    "strate": 3, "from": "Théorème Roth — tout ensemble dense dans ℕ contient des 3-AP (1953, Fields Medal). Méthode cercle de Hardy-Littlewood.", "domain": "combinatoire"},
    # Rigidité géométrique
    {"s": "MostowRig", "strate": 3, "from": "Mostow rigidity — variétés hyperboliques fermées dim ≥ 3 isométriques ssi π₁ isomorphes (1968)", "domain": "géom diff"},
    {"s": "MargSup",   "strate": 3, "from": "Margulis superrigidité — réseaux dans groupes de Lie rang ≥ 2 sont arithmétiques (1975, Fields Medal)", "domain": "géom diff"},
    {"s": "Oppenh",    "strate": 3, "from": "Conjecture Oppenheim — forme quadratique irrationnelle indéfinie ≥3 var. prend valeurs denses (Margulis 1987, flots unipotents)", "domain": "nb théorie"},
    {"s": "Ratner",    "strate": 3, "from": "Théorèmes Ratner — classification mesures/orbites invariantes unipotentes sur espaces homogènes (1990-91)", "domain": "géom diff"},
    # Topologie 3-variétés (compléments)
    {"s": "Tameness",  "strate": 3, "from": "Marden Tameness — variétés hyperboliques de volume infini sont topologiquement apprivoisées (Agol 2004, Calegari-Gabai 2004)", "domain": "topologie"},
    {"s": "EndLam",    "strate": 3, "from": "Ending Lamination — 3-var. hyperbolique déterminée par end invariants (Brock-Canary-Minsky 2012, Thurston conjecture)", "domain": "topologie"},
    # Géom diff (compléments)
    {"s": "DiffSph",   "strate": 3, "from": "1/4-pinched differentiable sphere theorem — variété courbure 1/4-pincée est difféomorphe à Sⁿ (Brendle-Schoen 2009)", "domain": "géom diff"},
    # Algèbre (compléments)
    {"s": "FeitThomp", "strate": 3, "from": "Odd order theorem — tout groupe fini d'ordre impair est résoluble (Feit-Thompson 1963, 255 pages). Premier pas vers CFSG.", "domain": "algèbre"},
    # Théorie des nombres (compléments)
    {"s": "Vinogr3P",  "strate": 3, "from": "Vinogradov — tout impair suffisamment grand est somme de 3 premiers (1937). Méthode cercle. Rendu effectif par Helfgott (GoldWeak).", "domain": "nb théorie"},
    # --- Strate 3 vague 3 : classiques fondamentaux manquants ---
    # Théorie des nombres classique
    {"s": "PNT",       "strate": 3, "from": "Prime Number Theorem — π(x) ~ x/ln(x) (Hadamard & de la Vallée-Poussin 1896, indépendamment). Preuve élémentaire Erdős-Selberg 1949.", "domain": "nb théorie"},
    {"s": "Waring",    "strate": 3, "from": "Problème de Waring — tout entier = somme de g(k) puissances k-ièmes (Hilbert 1909). g(2)=4 Lagrange, g(3)=9 Wieferich-Kempner.", "domain": "nb théorie"},
    {"s": "QRecip",    "strate": 3, "from": "Loi réciprocité quadratique — (p/q)(q/p) = (-1)^{(p-1)(q-1)/4} (Gauss 1801, ~240 preuves connues). Généralisée par Artin, Langlands.", "domain": "nb théorie"},
    {"s": "Dirichlet", "strate": 3, "from": "Théorème Dirichlet — infinité premiers dans progressions arithmétiques a+nd, pgcd(a,d)=1 (1837). Utilise L-fonctions.", "domain": "nb théorie"},
    # Géométrie / empilement (compléments)
    {"s": "Viaz8",     "strate": 3, "from": "Sphere packing dim 8 — réseau E₈ est empilement le plus dense en ℝ⁸ (Viazovska 2016, Fields Medal 2022). Formes modulaires.", "domain": "géométrie"},
    {"s": "Viaz24",    "strate": 3, "from": "Sphere packing dim 24 — réseau de Leech est optimal en ℝ²⁴ (Cohn-Kumar-Miller-Radchenko-Viazovska 2016).", "domain": "géométrie"},
    {"s": "DblBubble", "strate": 3, "from": "Double bubble conjecture — double bulle standard minimise l'aire dans ℝ³ (Hutchings-Morgan-Ritoré-Ros 2002).", "domain": "géométrie"},
    {"s": "Einstein",  "strate": 3, "from": "Einstein problem / monotuile apériodique — existence d'une tuile unique pavant le plan seulement apériodiquement (Smith-Myers-Kaplan-Goodman-Strauss 2023).", "domain": "géométrie"},
    # Algèbre / théorie des groupes (compléments)
    {"s": "BrauerH0",  "strate": 3, "from": "Brauer Height Zero Conjecture — hauteur zéro des caractères dans blocs (Malle-Navarro-Schaeffer Fry-Tiep 2024, Annals of Math).", "domain": "algèbre"},
    {"s": "Nagata",    "strate": 3, "from": "Conjecture Nagata — automorphisme sauvage de k[x,y,z] n'est pas apprivoisé (Shestakov-Umirbaev 2003).", "domain": "algèbre"},
    # Géom diff / dynamique (compléments)
    # Combinatoire / théorie additive (compléments)
    {"s": "ErdDiscrep","strate": 3, "from": "Erdős discrepancy problem — toute suite ±1 a sous-sommes partielles non-bornées (Tao 2015). Utilise analyse de Fourier entropique.", "domain": "combinatoire"},
    {"s": "GuthKatz",  "strate": 3, "from": "Erdős distinct distances — n points dans ℝ² déterminent Ω(n/log n) distances distinctes (Guth-Katz 2010). Polynomial partitioning.", "domain": "combinatoire"},
    {"s": "RamseyExp", "strate": 3, "from": "Ramsey diagonal upper bound — R(k,k) ≤ (4-ε)^k, première amélioration exponentielle depuis 1935 (Campos-Griffiths-Morris-Sahasrabudhe 2023).", "domain": "combinatoire"},
    # --- Strate 3 vague 4 : barrières complexité + probabilités + EDP + topo alg + classiques ---
    # ⚠️ BARRIÈRES COMPLEXITÉ — fondamentaux pour P=NP ⚠️
    {"s": "BGS",       "strate": 3, "from": "Baker-Gill-Solovay — ∃ oracle A: P^A=NP^A, ∃ oracle B: P^B≠NP^B (1975). Relativisation ne peut séparer P de NP.", "domain": "complexité"},
    {"s": "NatProof",  "strate": 3, "from": "Razborov-Rudich Natural Proofs barrier — si OWF existent, pas de preuve 'naturelle' de P≠NP (1997). Combinatorialisation bloquée.", "domain": "complexité"},
    {"s": "Algebriz",  "strate": 3, "from": "Aaronson-Wigderson Algebrization — généralise relativisation, toute preuve P≠NP doit être non-algébrisante (2009).", "domain": "complexité"},
    {"s": "ImmSzel",   "strate": 3, "from": "Immerman-Szelepcsényi — NL = co-NL (1987). Non-déterminisme spatial fermé sous complémentation.", "domain": "complexité"},
    {"s": "SipLaut",   "strate": 3, "from": "Sipser-Lautemann — BPP ⊆ Σ₂P ∩ Π₂P (1983). Randomisation contenue dans PH niveau 2.", "domain": "complexité"},
    {"s": "Perm#P",    "strate": 3, "from": "Valiant permanent — Permanent est #P-complet (1979). Comptage ≠ décision, lien matrices/complexité.", "domain": "complexité"},
    {"s": "ImpWig",    "strate": 3, "from": "Impagliazzo-Wigderson — P = BPP si E requiert circuits expo (STOC 1997). Dureté → dérandomisation.", "domain": "complexité"},
    {"s": "ImpPad",    "strate": 3, "from": "Impagliazzo-Paturi SETH — ETH: 3-SAT pas en 2^{o(n)}, SETH: k-SAT pas en 2^{(1-ε)n} (1999). Base complexité fine.", "domain": "complexité"},
    # Probabilités / Stochastique (domaine quasi-vide !)
    {"s": "BirkErg",   "strate": 3, "from": "Birkhoff ergodic theorem — moyenne temporelle = moyenne spatiale p.p. (1931). Fondement théorie ergodique.", "domain": "probabilités"},
    {"s": "CLT",       "strate": 3, "from": "Central Limit Theorem — (Sₙ-nμ)/σ√n → N(0,1) (Lindeberg 1922, Lévy, Feller). Universalité gaussienne.", "domain": "probabilités"},
    {"s": "SLLN",      "strate": 3, "from": "Strong Law Large Numbers — X̄ₙ → μ p.s. (Kolmogorov 1930). Convergence presque sûre des moyennes.", "domain": "probabilités"},
    {"s": "Donsker",   "strate": 3, "from": "Donsker invariance principle — marche aléatoire renormalisée → mouvement brownien (1951). CLT fonctionnel.", "domain": "probabilités"},
    {"s": "LDP",       "strate": 3, "from": "Large Deviations Principle — P(S̄ₙ∈A) ~ e^{-nI(A)} (Cramér 1938, Varadhan 1966). Taux exponentiels.", "domain": "probabilités"},
    {"s": "OrnIsm",    "strate": 3, "from": "Ornstein isomorphism — shifts de Bernoulli isomorphes ssi même entropie (Ornstein 1970). Classification systèmes aléatoires.", "domain": "probabilités"},
    # EDP (domaine vide !)
    {"s": "DeGNM",     "strate": 3, "from": "De Giorgi-Nash-Moser — solutions équations elliptiques div-forme à coefficients L^∞ sont Hölder (1957-58-60). Résout Hilbert 19ème.", "domain": "EDP"},
    {"s": "NashEmb",   "strate": 3, "from": "Nash embedding theorem — toute variété riemannienne se plonge isométriquement dans ℝ^N (1956). Schéma itératif Nash-Moser.", "domain": "géom diff"},
    {"s": "KAM",       "strate": 3, "from": "KAM theorem — tores quasi-périodiques persistent sous petites perturbations hamiltoniennes (Kolmogorov 1954, Arnold 1963, Moser 1962).", "domain": "mécanique analytique"},
    # Topologie algébrique (manquante)
    {"s": "deRham",    "strate": 3, "from": "de Rham theorem — cohomologie de de Rham ≅ cohomologie singulière (1931). Pont analyse ↔ topologie.", "domain": "topologie"},
    {"s": "BottPer",   "strate": 3, "from": "Bott periodicity — K-théorie topologique est périodique: π_{n+2}(U) ≅ π_n(U), π_{n+8}(O) ≅ π_n(O) (1959).", "domain": "topologie"},
    # Géométrie/Analyse complexe
    {"s": "Uniformiz", "strate": 3, "from": "Uniformization theorem — toute surface de Riemann simplement connexe ≅ S², ℂ ou 𝔻 (Koebe-Poincaré 1907).", "domain": "analyse"},
    {"s": "GrotRR",    "strate": 3, "from": "Grothendieck-Riemann-Roch — ch(f_!(F)) = f_*(ch(F)·Td(T_f)) en K-théorie (1957). Généralise Hirzebruch-RR.", "domain": "géom algébrique"},
    # Théorie des nombres (classiques manquants)
    {"s": "ClassFT",   "strate": 3, "from": "Class Field Theory — abélianisation Gal(K^ab/K) ≅ C_K (Takagi 1920, Artin 1927). Réciprocité non-abélienne = Langlands.", "domain": "nb théorie"},
    # Logique (compléments)
    {"s": "GodelInc",  "strate": 3, "from": "Gödel incompleteness — (1) toute théorie cohérente contenant PA a énoncés indécidables, (2) ne peut prouver sa propre cohérence (1931).", "domain": "logique"},
    # Algèbre classique
    {"s": "NoetherSy", "strate": 3, "from": "Noether theorem — toute symétrie continue d'un lagrangien donne une loi de conservation (1918). Pont algèbre ↔ physique.", "domain": "algèbre"},
    # Information
    {"s": "Shannon2",  "strate": 3, "from": "Shannon coding theorems — (1) source coding: H(X) bits suffisent, (2) channel: capacité C atteignable (1948). Fondement théorie info.", "domain": "information"},
    # --- Strate 3 vague 5 : trous finaux — quantique, circuits, descriptive, automates, stochastique ---
    # ⚠️ COMPLEXITÉ QUANTIQUE — résultat du siècle ⚠️
    {"s": "MIP*RE",    "strate": 3, "from": "MIP* = RE — prouveurs quantiques intriqués = langages r.e. (Ji-Natarajan-Vidick-Wright-Yuen 2020). Réfute Connes embedding, résout Tsirelson.", "domain": "quantique"},
    # Circuit lower bounds (complexité prouvée, pas barrières)
    {"s": "WillACC",   "strate": 3, "from": "Williams — NEXP ⊄ ACC⁰ circuits de taille poly (2011). Première borne inférieure circuits avec portes MODm depuis Razborov-Smolensky 87.", "domain": "complexité"},
    {"s": "RazMono",   "strate": 3, "from": "Razborov — circuits monotones pour CLIQUE exigent taille super-polynomiale 2^{Ω(n^{1/6})} (1985). Méthode d'approximation.", "domain": "complexité"},
    {"s": "RazSmol",   "strate": 3, "from": "Razborov-Smolensky — AC⁰[p] ne contient pas MOD_q pour p≠q premiers (1987). Bornes inférieures circuits à profondeur constante.", "domain": "complexité"},
    {"s": "HasAC0",    "strate": 3, "from": "Håstad switching lemma — PARITY ∉ AC⁰, circuits profondeur d taille 2^{Ω(n^{1/(d-1)})} nécessaires (1987). Tight pour AC⁰.", "domain": "complexité"},
    # Descriptive set theory (domaine vide !)
    {"s": "BorelDet",  "strate": 3, "from": "Borel determinacy — tout jeu de Gale-Stewart à gain Borel est déterminé (Martin 1975). Nécessite remplacement (Friedman 71).", "domain": "descriptive"},
    # Ensembles / Logique (résultats-événements)
    {"s": "CohenInd",  "strate": 3, "from": "Cohen forcing — CH est indépendant de ZFC: ni prouvable ni réfutable (Cohen 1963, Fields 1966). Méthode du forcing.", "domain": "ensembles"},
    # Automates (domaine vide !)
    {"s": "BuchiMSO",  "strate": 3, "from": "Büchi theorem — L est ω-régulier ssi définissable en MSO sur ω (Büchi 1962). Pont logique ↔ automates sur mots infinis.", "domain": "automates"},
    {"s": "MyhNer",    "strate": 3, "from": "Myhill-Nerode — L régulier ssi nombre fini de classes d'équivalence (Myhill 1957, Nerode 1958). Caractérisation algébrique réguliers.", "domain": "automates"},
    {"s": "RabinS2S",  "strate": 3, "from": "Rabin theorem — S2S (théorie monadique 2 successeurs) est décidable (Rabin 1969). Automates d'arbres, implique de nombreux résultats.", "domain": "automates"},
    # Stochastique (domaine vide !)
    {"s": "DoobMart",  "strate": 3, "from": "Doob martingale convergence — toute surmartingale bornée dans L¹ converge p.s. (Doob 1953). Fondement probabilités modernes.", "domain": "stochastique"},
    # Analyse fonctionnelle (presque vide)
    {"s": "BaireCat",  "strate": 3, "from": "Baire category theorem — espace métrique complet n'est pas union dénombrable de fermés d'intérieur vide (Baire 1899). Base Banach-Steinhaus/open mapping.", "domain": "analyse fonctionnelle"},
    {"s": "BanOpen",   "strate": 3, "from": "Banach open mapping + closed graph — surjection continue entre Banach est ouverte; graphe fermé implique continuité (Banach 1932).", "domain": "analyse fonctionnelle"},
    # ==================================================================
    # STRATE 4 — CIEL · AH
    # ==================================================================
    {"s": "AH",      "strate": 4, "from": "Hiérarchie arithmétique",     "domain": "calculabilité"},
    {"s": "∪ₙ",      "strate": 4, "from": "Union tous niveaux",          "domain": "ensembles"},
    {"s": "ω_ord",   "strate": 4, "from": "Premier ordinal infini ω",    "domain": "ordinaux"},
    {"s": "Th(ℕ)",   "strate": 4, "from": "Théorie complète de ℕ",       "domain": "logique"},
    {"s": "∅⁽ω⁾",    "strate": 4, "from": "ω-ième saut",                 "domain": "calculabilité"},
    {"s": "PSPACE",  "strate": 4, "from": "Espace polynomial (Savitch: =NPSPACE)", "domain": "complexité"},
    {"s": "QIP",     "strate": 4, "from": "Quantum Interactive Proof (=PSPACE)", "domain": "quantique"},
    {"s": "EXPTIME", "strate": 4, "from": "Temps exponentiel (⊋ P strict)", "domain": "complexité"},
    {"s": "NEXP",    "strate": 4, "from": "Non-det exponentiel",         "domain": "complexité"},
    {"s": "EXPSPACE","strate": 4, "from": "Espace exponentiel (=NEXPSPACE Savitch)", "domain": "complexité"},
    {"s": "AP",      "strate": 4, "from": "Alternating Polynomial time (=PSPACE)", "domain": "complexité"},
    {"s": "TQBF",    "strate": 4, "from": "True QBF — PSPACE-complet",   "domain": "complexité"},
    {"s": "IP_eq",   "strate": 4, "from": "IP=PSPACE (théorème Shamir 1992)", "domain": "complexité"},
    {"s": "2-EXP",   "strate": 4, "from": "2-EXPTIME doublement exponentiel", "domain": "complexité"},
    {"s": "ELEM",    "strate": 4, "from": "ELEMENTARY ∪ₖ k-EXPTIME",     "domain": "complexité"},
    {"s": "E",       "strate": 4, "from": "DTIME(2^O(n)) temps exp linéaire", "domain": "complexité"},
    {"s": "NE",      "strate": 4, "from": "NTIME(2^O(n))",               "domain": "complexité"},
    {"s": "Tarski",  "strate": 4, "from": "Indéfinissabilité vérité (Tarski 1936)", "domain": "logique"},
    {"s": "ε₀_ord",  "strate": 4, "from": "Ordinal ε₀ = ω^ω^ω^… (Gentzen)", "domain": "ordinaux"},
    {"s": "Ord",  "strate": 0, "from": "Classe des ordinaux (von Neumann)", "domain": "ordinaux"},
    # ==================================================================
    # STRATE 5 — HYPERARITHMÉTIQUE
    # ==================================================================
    {"s": "ω₁ᶜᵏ",   "strate": 5, "from": "Ordinal Church-Kleene",       "domain": "ordinaux"},
    {"s": "∅⁽α⁾",    "strate": 5, "from": "Saut transfinite α",          "domain": "calculabilité"},
    {"s": "Δ¹₁",     "strate": 5, "from": "Analytique Δ¹₁",              "domain": "descriptive"},
    {"s": "Σ¹₁",     "strate": 5, "from": "Analytique existentiel",      "domain": "descriptive"},
    {"s": "Π¹₁",     "strate": 5, "from": "Co-analytique",               "domain": "descriptive"},
    {"s": "O_Kl",    "strate": 5, "from": "O de Kleene",                  "domain": "calculabilité"},
    {"s": "HYP",     "strate": 5, "from": "Hyperarithmétique",            "domain": "calculabilité"},
    {"s": "WO",      "strate": 5, "from": "Bons ordres (Π¹₁-complet)",    "domain": "descriptive"},
    {"s": "Σ¹ₙ",     "strate": 5, "from": "Hiérarchie projective",        "domain": "descriptive"},
    {"s": "Π¹ₙ",     "strate": 5, "from": "Hiérarchie projective dual",   "domain": "descriptive"},
    {"s": "Det",     "strate": 5, "from": "Déterminance (Martin)",        "domain": "ensembles"},
    {"s": "²E",     "strate": 5, "from": "Fonctionnel type-2 Kleene (caractérise HYP)", "domain": "calculabilité"},
    {"s": "KP",     "strate": 5, "from": "Kripke-Platek set theory",      "domain": "logique"},
    {"s": "Lα",     "strate": 5, "from": "Niveaux constructibles admissibles Lω₁ᶜᵏ", "domain": "ensembles"},
    {"s": "Borel",  "strate": 5, "from": "Hiérarchie de Borel (⊂ Δ¹₁)",  "domain": "descriptive"},
    {"s": "AD",     "strate": 5, "from": "Axiome de Déterminance",        "domain": "ensembles"},
    {"s": "Wadge",  "strate": 5, "from": "Degrés de Wadge (raffinement de la hiérarchie)", "domain": "descriptive"},
    {"s": "Spect",  "strate": 5, "from": "Théorème Spector-Gandy (Π¹₁ = HYP en ω₁ᶜᵏ)", "domain": "calculabilité"},
    {"s": "Σ⁰_α",  "strate": 5, "from": "Niveau Borel transfinite Σ⁰α", "domain": "descriptive"},
    # ==================================================================
    # STRATE 6 — PLAFOND · Non-calculable
    # ==================================================================
    {"s": "Ω_Ch",   "strate": 6, "from": "Constante de Chaitin",          "domain": "information"},
    {"s": "BB(n)",  "strate": 6, "from": "Busy Beaver",                   "domain": "calculabilité"},
    {"s": "⊥",      "strate": 6, "from": "Bottom / indécidable",          "domain": "logique"},
    {"s": "G_God",  "strate": 6, "from": "Phrase de Gödel",               "domain": "logique"},
    {"s": "⊢",      "strate": 6, "from": "Prouvabilité",                  "domain": "logique"},
    {"s": "⊬",      "strate": 6, "from": "Non-prouvable dans S",          "domain": "logique"},
    {"s": "K(x)",   "strate": 6, "from": "Complexité Kolmogorov",         "domain": "information"},
    {"s": "HALT",   "strate": 6, "from": "Problème de l'arrêt",           "domain": "calculabilité"},
    {"s": "H10",    "strate": 6, "from": "Hilbert 10th problem indécidable (Matiyasevich 1970, DPRM)", "domain": "calculabilité"},
    {"s": "Σ(n)",   "strate": 6, "from": "Busy Beaver score — max 1s sur bande (Radó 1962)", "domain": "calculabilité"},
    {"s": "WP_grp", "strate": 6, "from": "Word Problem groupes (Novikov 1955, Boone 1959)", "domain": "calculabilité"},
    {"s": "PCP",    "strate": 6, "from": "Post Correspondence Problem (Post 1946)", "domain": "calculabilité"},
    {"s": "Rice",   "strate": 6, "from": "Théorème de Rice (propriété sémantique indécidable)", "domain": "calculabilité"},
    {"s": "ETM",    "strate": 6, "from": "Emptiness {⟨M⟩ : L(M)=∅} indécidable", "domain": "calculabilité"},
    {"s": "EQTM",   "strate": 6, "from": "Equivalence {⟨M₁,M₂⟩ : L(M₁)=L(M₂)} indécidable", "domain": "calculabilité"},
    {"s": "S(n)",   "strate": 6, "from": "Maximum shifts function — max steps (Radó 1962)", "domain": "calculabilité"},
    {"s": "Entsch", "strate": 6, "from": "Entscheidungsproblem (Hilbert 1928, réfuté Turing/Church 1936)", "domain": "logique"},
    {"s": "Diag",   "strate": 6, "from": "Argument diagonal Cantor/Turing", "domain": "calculabilité"},
    {"s": "Kolm",   "strate": 6, "from": "Incompressibilité Kolmogorov (pas d'algo pour trouver le plus court)", "domain": "information"},
    {"s": "Wang",   "strate": 6, "from": "Wang tiling problem indécidable (Berger 1966, Memoirs AMS)", "domain": "calculabilité"},
]
# ============================================================================
# MOTEUR — sans liaisons, juste la carte
# ============================================================================
class StrateEngine:
    def __init__(self):
        self.strates = STRATES
        self.symboles = SYMBOLES
    def total_nodes(self):
        return len(self.symboles)
    def strate_stats(self):
        stats = []
        for st in self.strates:
            syms = [s for s in self.symboles if s["strate"] == st["id"]]
            domains = set(s["domain"] for s in syms)
            stats.append({
                "strate_id": st["id"],
                "name": st["short"],
                "n_symbols": len(syms),
                "n_domains": len(domains),
                "domains": sorted(domains),
            })
        return stats
    def distribute_on_plane(self, n, box_w=3.8, box_d=3.8, shrink=0.85):
        w = box_w * shrink * 0.88
        d = box_d * shrink * 0.88
        if n <= 0: return []
        if n == 1: return [{"x": 0, "z": 0}]
        aspect = w / d
        best_cols, best_rows, best_waste = 1, n, float('inf')
        for cols in range(1, n + 1):
            rows = math.ceil(n / cols)
            cell_w = w / cols
            cell_d = d / rows
            waste = abs(cell_w / cell_d - aspect) + (cols * rows - n) * 0.1
            if waste < best_waste:
                best_waste = waste; best_cols = cols; best_rows = rows
        points = []
        cell_w = w / best_cols
        cell_d = d / best_rows
        for i in range(n):
            col = i % best_cols
            row = i // best_cols
            points.append({
                "x": round(-w/2 + cell_w/2 + col * cell_w, 4),
                "z": round(-d/2 + cell_d/2 + row * cell_d, 4)
            })
        return points
    def export_json(self, path="strates_export.json"):
        data = {"meta": {"total_symbols": self.total_nodes()}, "strates": []}
        for st in self.strates:
            syms = [s for s in self.symboles if s["strate"] == st["id"]]
            positions = self.distribute_on_plane(len(syms))
            sym_data = []
            for i, s in enumerate(syms):
                pos = positions[i] if i < len(positions) else {"x": 0, "z": 0}
                sym_data.append({"s": s["s"], "from": s["from"], "domain": s["domain"], "px": pos["x"], "pz": pos["z"]})
            data["strates"].append({**st, "symbols": sym_data})
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        return data
    def print_report(self):
        print("=" * 60)
        print("  STRATES × SYMBOLES — RAPPORT")
        print("=" * 60)
        print(f"\n  Total: {self.total_nodes()} symboles\n")
        print("─" * 60)
        for st in self.strate_stats():
            print(f"  [{st['strate_id']}] {st['name']:20s} │ {st['n_symbols']:4d} sym │ {st['n_domains']:2d} domaines")
            print(f"      {', '.join(st['domains'][:8])}")
            if len(st['domains']) > 8:
                print(f"      {', '.join(st['domains'][8:])}")
        print("=" * 60)
# ============================================================================
# HTML TEMPLATE
# ============================================================================
HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>P=NP — Tous les Symboles × Strates</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Instrument+Serif:ital@0;1&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
body{background:#08080d;color:#c8ccd4;font-family:'JetBrains Mono',monospace;overflow:hidden;height:100vh;width:100vw}
canvas{display:block;position:fixed;top:0;left:0;z-index:1}
body::after{content:'';position:fixed;top:0;left:0;right:0;bottom:0;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.02'/%3E%3C/svg%3E");pointer-events:none;z-index:2}
#hud{position:fixed;top:18px;left:22px;z-index:10;pointer-events:none}
#hud h1{font-family:'Instrument Serif',serif;font-size:24px;font-weight:400;color:#e8e8f0;margin-bottom:2px}
#hud .sub{font-size:9px;color:#3a3a4a;letter-spacing:2.5px;text-transform:uppercase}
#hud .meta{font-size:9px;color:#334;margin-top:8px}
#info{position:fixed;bottom:24px;left:24px;z-index:10;pointer-events:none;max-width:520px}
#info .sn{font-family:'Instrument Serif',serif;font-size:19px;color:#fff;margin-bottom:2px;transition:color 0.3s}
#info .sf{font-size:12px;color:#8af;margin-bottom:5px}
#info .sd{font-size:10.5px;color:#445;line-height:1.5}
#info .sl{font-size:9px;color:#3a3a4a;margin-top:6px;line-height:1.6;max-height:60px;overflow:hidden}
#legend{position:fixed;top:50%;right:20px;transform:translateY(-50%);z-index:10;display:flex;flex-direction:column;gap:1px;pointer-events:all}
.li{display:flex;align-items:center;gap:8px;padding:4px 10px 4px 6px;border-radius:3px;cursor:pointer;transition:all 0.25s;border:1px solid transparent}
.li:hover{background:rgba(255,255,255,0.03);border-color:rgba(255,255,255,0.06)}
.li.act{background:rgba(255,255,255,0.06);border-color:rgba(255,255,255,0.12)}
.ld{width:8px;height:8px;border-radius:50%;flex-shrink:0;box-shadow:0 0 5px currentColor}
.ll{font-size:9px;letter-spacing:0.6px;text-transform:uppercase;color:#445;transition:color 0.25s;white-space:nowrap}
.li.act .ll,.li:hover .ll{color:#889}
.lc{font-size:8px;color:#334;margin-left:2px}
#hint{position:fixed;bottom:20px;right:20px;z-index:10;font-size:9px;color:#222;letter-spacing:1px;text-align:right;line-height:1.9}
#hint kbd{background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.06);border-radius:2px;padding:1px 4px;font-family:inherit;font-size:8px}
</style>
</head>
<body>
<canvas id="c"></canvas>
<div id="hud">
  <h1>Carte des Symboles</h1>
  <div class="sub">Tous les symboles scientifiques du monde · placés sur leur strate de calculabilité</div>
  <div class="meta" id="meta"></div>
</div>
<div id="info">
  <div class="sn" id="sn">— Survole une strate —</div>
  <div class="sf" id="sf"></div>
  <div class="sd" id="sd"></div>
  <div class="sl" id="sl"></div>
</div>
<div id="legend"></div>
<div id="hint"><kbd>drag</kbd> rotation · <kbd>scroll</kbd> zoom · <kbd>légende</kbd> focus</div>
<script>
const DATA=__DATA_INJECT__;
const ST=DATA.strates;
const cv=document.getElementById('c');const ctx=cv.getContext('2d');
let W,H;function resize(){W=cv.width=innerWidth;H=cv.height=innerHeight}resize();addEventListener('resize',resize);
const BOX={w:3.8,h:3.8,d:3.8},CAM={dist:7.0,scale:420,persp:0.18},SHRINK=0.85;
let yaw=0,yawSpd=0.005,tiltX=-0.32,activeS=-1,zoom=1.0;
let dragging=false,pm={x:0,y:0},autoRot=true,autoT=null,mouseX=0,mouseY=0;
cv.addEventListener('mousedown',e=>{dragging=true;pm={x:e.clientX,y:e.clientY};autoRot=false;clearTimeout(autoT)});
addEventListener('mousemove',e=>{mouseX=e.clientX;mouseY=e.clientY;if(!dragging)return;yaw+=(e.clientX-pm.x)*0.005;tiltX+=(e.clientY-pm.y)*0.004;tiltX=Math.max(-1.3,Math.min(1.3,tiltX));pm={x:e.clientX,y:e.clientY}});
addEventListener('mouseup',()=>{dragging=false;autoT=setTimeout(()=>autoRot=true,3000)});
cv.addEventListener('wheel',e=>{e.preventDefault();zoom*=e.deltaY>0?0.95:1.05;zoom=Math.max(0.3,Math.min(3,zoom))},{passive:false});
cv.addEventListener('touchstart',e=>{if(e.touches.length===1){dragging=true;pm={x:e.touches[0].clientX,y:e.touches[0].clientY};autoRot=false;clearTimeout(autoT)}});
cv.addEventListener('touchmove',e=>{if(!dragging||e.touches.length!==1)return;e.preventDefault();yaw+=(e.touches[0].clientX-pm.x)*0.005;tiltX+=(e.touches[0].clientY-pm.y)*0.004;tiltX=Math.max(-1.3,Math.min(1.3,tiltX));pm={x:e.touches[0].clientX,y:e.touches[0].clientY}},{passive:false});
cv.addEventListener('touchend',()=>{dragging=false;autoT=setTimeout(()=>autoRot=true,3000)});
function project(x,y,z){const cy=Math.cos(yaw),sy=Math.sin(yaw),x1=x*cy+z*sy,z1=-x*sy+z*cy;const cx=Math.cos(tiltX),sx=Math.sin(tiltX),y2=y*cx-z1*sx,z2=y*sx+z1*cx;const sc=CAM.scale*zoom,den=Math.max(0.001,CAM.dist-z2),pf=sc/den,of=sc/CAM.dist,f=of+(pf-of)*CAM.persp;return{x:x1*f+W/2,y:-y2*f+H/2,z:z2,f}}
function rgba(c,a){return`rgba(${c[0]},${c[1]},${c[2]},${a})`}
const CE=[[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]];
function bv(){const h=BOX.w/2,hy=BOX.h/2,hz=BOX.d/2;return[[-h,-hy,-hz],[h,-hy,-hz],[h,hy,-hz],[-h,hy,-hz],[-h,-hy,hz],[h,-hy,hz],[h,hy,hz],[-h,hy,hz]]}
document.getElementById('meta').textContent=`${DATA.meta.total_symbols} symboles · 7 strates`;
const legEl=document.getElementById('legend');
ST.forEach((s,i)=>{const d=document.createElement('div');d.className='li';d.innerHTML=`<div class="ld" style="color:rgb(${s.color});background:rgb(${s.color})"></div><div class="ll">${s.short}</div><div class="lc">${s.symbols.length}</div>`;d.addEventListener('click',()=>{activeS=activeS===i?-1:i;document.querySelectorAll('.li').forEach((el,j)=>el.classList.toggle('act',j===activeS));if(activeS>=0)showInfo(activeS)});d.addEventListener('mouseenter',()=>showInfo(i));legEl.appendChild(d)});
function showInfo(i){const s=ST[i];document.getElementById('sn').textContent=s.name;document.getElementById('sn').style.color=`rgb(${s.color})`;document.getElementById('sf').textContent=s.formula;document.getElementById('sd').textContent=s.desc;const doms=[...new Set(s.symbols.map(x=>x.domain))];document.getElementById('sl').textContent=`[${s.symbols.length} sym · ${doms.length} domaines] ${doms.join(' · ')}`}
function frame(){
  requestAnimationFrame(frame);ctx.clearRect(0,0,W,H);
  const gr=ctx.createRadialGradient(W/2,H/2,0,W/2,H/2,W*0.7);gr.addColorStop(0,'#0d0d14');gr.addColorStop(1,'#050508');ctx.fillStyle=gr;ctx.fillRect(0,0,W,H);
  if(autoRot)yaw+=yawSpd;
  const items=[];
  ST.forEach((st,si)=>{
    const y=st.yr*BOX.h,sh=SHRINK,hw=BOX.w*sh/2,hd=BOX.d*sh/2;
    const qv=[[-hw,y,-hd],[hw,y,-hd],[hw,y,hd],[-hw,y,hd]];
    const pq=qv.map(v=>project(v[0],v[1],v[2]));
    const avgZ=pq.reduce((a,p)=>a+p.z,0)/4;
    let op=st.opacity,bop=0.5,sop=0.8;
    if(activeS>=0){if(si===activeS){op=0.3;bop=0.85;sop=1}else{op=0.015;bop=0.04;sop=0.04}}
    items.push({type:'p',z:avgZ-0.01,si,pts:pq,col:st.color,op,bop});
    st.symbols.forEach(sym=>{const pp=project(sym.px,y,sym.pz);items.push({type:'s',z:pp.z,si,sym,px:pp.x,py:pp.y,pf:pp.f,col:st.color,sop})});
  });
  items.sort((a,b)=>a.z-b.z);
  let ns=null,nd=22;
  items.forEach(it=>{
    if(it.type==='p'){ctx.beginPath();ctx.moveTo(it.pts[0].x,it.pts[0].y);for(let i=1;i<4;i++)ctx.lineTo(it.pts[i].x,it.pts[i].y);ctx.closePath();ctx.fillStyle=rgba(it.col,it.op);ctx.fill();ctx.strokeStyle=rgba(it.col,it.bop);ctx.lineWidth=1;ctx.stroke()}
    if(it.type==='s'){
      const sc=CAM.scale*zoom/CAM.dist;const bs=Math.max(5,Math.min(11,7.5*(it.pf/sc)));
      ctx.font=`600 ${bs}px "JetBrains Mono",monospace`;ctx.textAlign='center';ctx.textBaseline='middle';
      const dx=mouseX-it.px,dy=mouseY-it.py,dist=Math.sqrt(dx*dx+dy*dy);
      if(dist<18&&dist<nd){nd=dist;ns=it}
      if(dist<18){ctx.shadowColor=`rgb(${it.col})`;ctx.shadowBlur=12}
      ctx.fillStyle=rgba(it.col,it.sop);ctx.fillText(it.sym.s,it.px,it.py);ctx.shadowBlur=0}
  });
  if(ns){const tx=ns.px+14,ty=ns.py-12;ctx.font='500 9.5px "JetBrains Mono",monospace';const txt=`${ns.sym.s} ← ${ns.sym.from}`;const m=ctx.measureText(txt);ctx.fillStyle='rgba(0,0,0,0.8)';ctx.fillRect(tx-4,ty-9,m.width+8,15);ctx.strokeStyle=rgba(ns.col,0.4);ctx.lineWidth=0.7;ctx.strokeRect(tx-4,ty-9,m.width+8,15);ctx.fillStyle=rgba(ns.col,0.9);ctx.textAlign='left';ctx.textBaseline='middle';ctx.fillText(txt,tx,ty-1.5)}
  const pv2=bv().map(v=>project(v[0],v[1],v[2]));CE.forEach(e=>{ctx.beginPath();ctx.moveTo(pv2[e[0]].x,pv2[e[0]].y);ctx.lineTo(pv2[e[1]].x,pv2[e[1]].y);ctx.strokeStyle='rgba(60,200,100,0.3)';ctx.lineWidth=1.5;ctx.stroke()});
  pv2.forEach(p=>{ctx.beginPath();ctx.arc(p.x,p.y,1.8,0,Math.PI*2);ctx.fillStyle='rgba(74,222,128,0.25)';ctx.fill()});
  const bot=project(0,-BOX.h/2-0.35,0),top2=project(0,BOX.h/2+0.35,0);
  ctx.font='500 8.5px "JetBrains Mono",monospace';ctx.textAlign='center';
  ctx.fillStyle='rgba(74,222,128,0.3)';ctx.fillText('▼ PLANCHER — Axiomes',bot.x,bot.y);
  ctx.fillStyle='rgba(239,68,68,0.3)';ctx.fillText('▲ PLAFOND — Turing 1936',top2.x,top2.y);
  ctx.font='400 8.5px "JetBrains Mono",monospace';ctx.textAlign='left';ctx.fillStyle='rgba(80,80,100,0.25)';
  ctx.fillText(`${DATA.meta.total_symbols} symboles · 7 strates`,12,H-14);
}
showInfo(0);frame();
</script>
</body>
</html>"""
def main():
    engine = StrateEngine()
    out_path = Path(__file__).parent.parent / "data" / "core" / "strates_export.json"
    data = engine.export_json(str(out_path))
    print(f"\n✅ JSON → {out_path} ({data['meta']['total_symbols']} symboles)")
    engine.print_report()
    if "--html" in sys.argv or True:
        html_path = Path(__file__).parent.parent / "viz" / "strates_cube_live.html"
        json_str = json.dumps(data, ensure_ascii=False)
        html = HTML_TEMPLATE.replace("__DATA_INJECT__", json_str)
        with open(str(html_path), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ HTML → {html_path}")
if __name__ == "__main__":
    main()
