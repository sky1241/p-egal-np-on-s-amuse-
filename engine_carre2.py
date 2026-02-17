"""
P=NP ON S'AMUSE — CARRÉ 2 (PROUVÉ + NON PROUVÉ)
=================================================
Sky × Claude — 17 Février 2026

CARRÉ 2 : Tous les symboles du carré 1 (684 prouvés)
+ symboles NON PROUVÉS (conjectures, problèmes ouverts,
théories non fondées, notations émergentes).

Le delta entre carré 1 et carré 2 = carte des découvertes à venir.

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

    # ====================================================================
    # CARRÉ 2 UNIQUEMENT — SYMBOLES NON PROUVÉS
    # Conjectures, problèmes ouverts, théories non fondées
    # Organisé par strate (0 → 6) comme le carré 1
    # ====================================================================

    # ================================================================
    # STRATE 0 — CONJECTURES SUR OBJETS DÉCIDABLES
    # ================================================================

    # --- Problèmes du Millénaire Clay (2000) — strate 0 ---
    {"s": "RH",      "strate": 0, "from": "Hypothèse de Riemann — ζ(s)=0 → Re(s)=½ (1859)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "NS_reg",  "strate": 0, "from": "Navier-Stokes existence et régularité 3D", "domain": "fluides", "status": "open"},
    {"s": "YM_gap",  "strate": 0, "from": "Yang-Mills mass gap (existence + gap >0)", "domain": "QFT", "status": "open"},
    {"s": "Hodge",   "strate": 0, "from": "Conjecture de Hodge (classes cohomologie algébriques)", "domain": "géom diff", "status": "conjecture"},
    {"s": "BSD",     "strate": 0, "from": "Birch et Swinnerton-Dyer (rang courbes elliptiques)", "domain": "nb théorie", "status": "conjecture"},

    # --- Théorie des nombres : conjectures ---
    {"s": "Goldbach","strate": 0, "from": "Tout pair >2 = somme 2 premiers (1742)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "Twin_p", "strate": 0, "from": "∞ paires premiers jumeaux p, p+2", "domain": "nb théorie", "status": "conjecture"},
    {"s": "Collatz","strate": 0, "from": "Conjecture Syracuse/Collatz (1937)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "ABC",    "strate": 0, "from": "Conjecture ABC (Masser-Oesterlé 1985)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "Legendre","strate": 0, "from": "∃ premier entre n² et (n+1)²", "domain": "nb théorie", "status": "conjecture"},
    {"s": "Cramér", "strate": 0, "from": "Gaps entre premiers O(log²p) (1936)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "Lehmer", "strate": 0, "from": "Mesure de Mahler minimale (1933)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "Beal",   "strate": 0, "from": "Conjecture Beal — Aˣ+Bʸ=Cᶻ → gcd>1 (1993)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "Buny",   "strate": 0, "from": "Conjecture Bunyakovsky (polynômes irréductibles → ∞ premiers, 1857)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "ErdStraus","strate": 0, "from": "Conjecture Erdős-Straus — 4/n = 1/x+1/y+1/z (1948)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "Brocard","strate": 0, "from": "Problème Brocard — n!+1 = m² (1876, seuls n=4,5,7 connus)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "Lindelöf","strate": 0, "from": "Hypothèse Lindelöf — ζ(½+it) = O(t^ε) (impliquée par RH)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "Langlands","strate": 0, "from": "Programme de Langlands (1967, partiellement prouvé)", "domain": "nb théorie", "status": "programme"},
    {"s": "Funct_L","strate": 0, "from": "Fonctorialité de Langlands (non prouvé en général)", "domain": "nb théorie", "status": "conjecture"},

    # --- Analyse : conjectures ---
    {"s": "Sendov","strate": 0, "from": "Conjecture Sendov (zéros polynômes, 1959, prouvé n>8 Tao)", "domain": "analyse", "status": "conjecture"},
    {"s": "Kakeya","strate": 0, "from": "Conjecture Kakeya (dimension Besicovitch sets = n)", "domain": "analyse", "status": "conjecture"},
    {"s": "InvSub","strate": 0, "from": "Invariant Subspace Problem (tout opérateur sur Hilbert?)", "domain": "analyse fonctionnelle", "status": "open"},
    {"s": "Schanuel","strate": 0, "from": "Conjecture Schanuel (transcendance, implique Lindemann)", "domain": "analyse", "status": "conjecture"},
    {"s": "Pompeiu","strate": 0, "from": "Problème de Pompeiu (domaines sans propriété, 1929)", "domain": "analyse", "status": "open"},

    # --- Algèbre : conjectures ---
    {"s": "Jacobian","strate": 0, "from": "Conjecture Jacobienne (Keller 1939)", "domain": "algèbre", "status": "conjecture"},
    {"s": "Inv_Gal","strate": 0, "from": "Problème inverse de Galois (tout groupe fini = Gal?)", "domain": "algèbre", "status": "open"},
    {"s": "Köthe",  "strate": 0, "from": "Conjecture Köthe (nil idéal à gauche → nil bilatère)", "domain": "algèbre", "status": "conjecture"},
    {"s": "Dixmier","strate": 0, "from": "Conjecture Dixmier (endomorphisme algèbre Weyl = automorphisme)", "domain": "algèbre", "status": "conjecture"},
    {"s": "Kaplansky","strate": 0, "from": "Conjectures Kaplansky (unit, zero divisor, idempotent group rings)", "domain": "algèbre", "status": "conjecture"},

    # --- Topologie : conjectures ---
    {"s": "Poinc4","strate": 0, "from": "Poincaré lisse dim 4 (dim 3 = Perelman 2003)", "domain": "topologie", "status": "open"},
    {"s": "AndrCurt","strate": 0, "from": "Conjecture Andrews-Curtis (présentations triviales, 1965)", "domain": "topologie", "status": "conjecture"},
    {"s": "Zeeman","strate": 0, "from": "Conjecture Zeeman (contractible 2-complex × I collapsible)", "domain": "topologie", "status": "conjecture"},
    {"s": "Borel_c","strate": 0, "from": "Conjecture Borel (variétés asphériques rigides)", "domain": "topologie", "status": "conjecture"},
    {"s": "Novikov_c","strate": 0, "from": "Conjecture Novikov (invariance classes de Pontryagin supérieures)", "domain": "topologie", "status": "conjecture"},

    # --- Géométrie différentielle : conjectures ---
    {"s": "Hopf_c","strate": 0, "from": "Conjecture Hopf (courbure positive → χ>0 en dim paire)", "domain": "géom diff", "status": "conjecture"},
    {"s": "Chern_c","strate": 0, "from": "Conjecture Chern (variétés affines plates → χ=0)", "domain": "géom diff", "status": "conjecture"},
    {"s": "Yau_c",  "strate": 0, "from": "Conjectures de Yau (géométrie kählérienne, partiellement ouvert)", "domain": "géom diff", "status": "conjecture"},

    # --- Combinatoire / Graphes : conjectures ---
    {"s": "Hadwiger","strate": 0, "from": "Hadwiger — χ(G)≥k → Kₖ mineur (1943)", "domain": "combinatoire", "status": "conjecture"},
    {"s": "Recon",  "strate": 0, "from": "Reconstruction graphe (Kelly-Ulam 1941)", "domain": "combinatoire", "status": "conjecture"},
    {"s": "Frankl", "strate": 0, "from": "Conjecture union-closed (Frankl 1979, partiellement Gilmer 2022)", "domain": "combinatoire", "status": "conjecture"},
    {"s": "EFL",    "strate": 0, "from": "Conjecture Erdős-Faber-Lovász (χ sur hypergraphes linéaires)", "domain": "combinatoire", "status": "conjecture"},
    {"s": "GracTree","strate": 0, "from": "Conjecture graceful tree (Ringel-Kotzig 1967)", "domain": "combinatoire", "status": "conjecture"},
    {"s": "Cycle2c","strate": 0, "from": "Cycle double cover conjecture (Szegedy 1979)", "domain": "combinatoire", "status": "conjecture"},
    {"s": "Barnette","strate": 0, "from": "Conjecture Barnette (polytope simple 3-connexe biparti → hamiltonien)", "domain": "combinatoire", "status": "conjecture"},

    # --- Probabilités / Stochastique : conjectures ---
    {"s": "SLE_univ","strate": 0, "from": "Universalité SLE (convergence modèles discrets → SLE, partiel)", "domain": "probabilités", "status": "conjecture"},
    {"s": "KPZ_univ","strate": 0, "from": "Universalité KPZ (exposants croissance, Kardar-Parisi-Zhang 1986)", "domain": "stochastique", "status": "conjecture"},

    # --- Physique théorique : non prouvé ---
    {"s": "Str_th","strate": 0, "from": "Théorie des cordes (non vérifiée expérimentalement)", "domain": "QFT", "status": "théorie"},
    {"s": "SUSY",  "strate": 0, "from": "Supersymétrie (non détectée au LHC)", "domain": "QFT", "status": "théorie"},
    {"s": "DM",    "strate": 0, "from": "Matière noire (observée indirectement, nature inconnue)", "domain": "cosmologie", "status": "open"},
    {"s": "DE",    "strate": 0, "from": "Énergie noire (nature inconnue, Λ ou dynamique?)", "domain": "cosmologie", "status": "open"},
    {"s": "Grav_q","strate": 0, "from": "Gravité quantique (pas de théorie unifiée)", "domain": "QFT", "status": "open"},
    {"s": "LQG",   "strate": 0, "from": "Loop Quantum Gravity (Rovelli-Smolin, non vérifié)", "domain": "QFT", "status": "théorie"},
    {"s": "Multivers","strate": 0, "from": "Hypothèse multivers (non testable?)", "domain": "cosmologie", "status": "théorie"},
    {"s": "Prot_d","strate": 0, "from": "Décroissance du proton (prédite GUT, non observée)", "domain": "QFT", "status": "open"},
    {"s": "Magn_m","strate": 0, "from": "Monopôle magnétique (Dirac 1931, non détecté)", "domain": "électromagn", "status": "open"},
    {"s": "CP_strong","strate": 0, "from": "Problème CP fort (pourquoi θ~0? axion?)", "domain": "QFT", "status": "open"},
    {"s": "ν_mass","strate": 0, "from": "Masse neutrinos (Majorana/Dirac? mécanisme inconnu)", "domain": "quantique", "status": "open"},
    {"s": "Hier_pb","strate": 0, "from": "Problème de hiérarchie (masse Higgs vs Planck)", "domain": "QFT", "status": "open"},
    {"s": "Axion", "strate": 0, "from": "Axion (particule hypothétique, solution CP fort)", "domain": "QFT", "status": "open"},
    {"s": "Cosm_inf","strate": 0, "from": "Inflation cosmique (Guth 1981, mécanisme exact ouvert)", "domain": "cosmologie", "status": "théorie"},
    {"s": "Baryon","strate": 0, "from": "Baryogénèse (asymétrie matière/antimatière, mécanisme inconnu)", "domain": "cosmologie", "status": "open"},
    {"s": "Penrose","strate": 0, "from": "Censure cosmique (Penrose 1969, singularités nues interdites?)", "domain": "relativité", "status": "conjecture"},
    {"s": "BH_info","strate": 0, "from": "Paradoxe information trou noir (Hawking, non résolu)", "domain": "quantique", "status": "open"},

    # --- Quantique / Information : conjectures ---
    {"s": "QC_adv","strate": 0, "from": "Avantage quantique prouvable (au-delà échantillonnage)", "domain": "quantique", "status": "open"},
    {"s": "AdS/CFT","strate": 0, "from": "Correspondance AdS/CFT (Maldacena 1997, non prouvé)", "domain": "QFT", "status": "conjecture"},
    {"s": "Confinement","strate": 0, "from": "Confinement quarks (QCD, non prouvé analytiquement)", "domain": "QFT", "status": "open"},

    # --- Crypto : conjectures ---
    {"s": "OWF_ex","strate": 0, "from": "Existence one-way functions (base crypto, non prouvé)", "domain": "crypto", "status": "conjecture"},

    # --- Biologie / Émergence ---
    {"s": "Abio",  "strate": 0, "from": "Abiogénèse (origine de la vie, mécanisme inconnu)", "domain": "biologie", "status": "open"},
    {"s": "Consc", "strate": 0, "from": "Problème difficile conscience (Chalmers 1995)", "domain": "biologie", "status": "open"},
    {"s": "Prot_fold","strate": 0, "from": "Protein folding (AlphaFold partiel, théorie manque)", "domain": "biologie", "status": "open"},
    {"s": "RNA_w", "strate": 0, "from": "Hypothèse monde ARN (origine réplication, non prouvé)", "domain": "biologie", "status": "théorie"},

    # --- Complexité strate 0 ---
    {"s": "L≠NL",  "strate": 0, "from": "Conjecture L≠NL", "domain": "complexité", "status": "conjecture"},

    # --- Théorie des nombres : manquants ---
    {"s": "Norm_π","strate": 0, "from": "π est-il nombre normal? (distribution uniforme chiffres)", "domain": "nb théorie", "status": "open"},
    {"s": "Norm_e","strate": 0, "from": "e est-il nombre normal? (distribution uniforme chiffres)", "domain": "nb théorie", "status": "open"},
    {"s": "Gilbreath","strate": 0, "from": "Conjecture Gilbreath (différences itérées des premiers)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "Grimm", "strate": 0, "from": "Conjecture Grimm (composés consécutifs → facteurs distincts)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "Pillai","strate": 0, "from": "Conjecture Pillai (|aˣ-bʸ|→∞ sauf fini, généralise Catalan)", "domain": "nb théorie", "status": "conjecture"},

    # --- Géométrie / Analyse : manquants ---
    {"s": "Hilb16","strate": 0, "from": "16ème problème Hilbert (cycles limites systèmes polynomiaux)", "domain": "systèmes dynamiques", "status": "open"},
    {"s": "MovSofa","strate": 0, "from": "Moving sofa problem (Gerver 1992 borne sup, Romik)", "domain": "géométrie", "status": "open"},
    {"s": "LonelyR","strate": 0, "from": "Lonely runner conjecture (Wills 1968, prouvé k≤7)", "domain": "combinatoire", "status": "conjecture"},
    {"s": "ChromPlane","strate": 0, "from": "Nombre chromatique du plan (4≤χ≤7, Hadwiger-Nelson)", "domain": "combinatoire", "status": "open"},
    {"s": "Irr_π", "strate": 0, "from": "Mesure d'irrationalité de π (μ(π)=2?, borne Salikhov 7.103)", "domain": "nb théorie", "status": "open"},

    # --- Systèmes dynamiques ---
    {"s": "Wein_c","strate": 0, "from": "Conjecture Weinstein (orbites périodiques sur variétés symplectiques)", "domain": "systèmes dynamiques", "status": "conjecture"},
    {"s": "Smale14","strate": 0, "from": "Problèmes de Smale restants (18 problèmes, plusieurs ouverts)", "domain": "systèmes dynamiques", "status": "open"},

    # --- Physique : manquants ---
    {"s": "Arrow_t","strate": 0, "from": "Flèche du temps (pourquoi entropie croît? fondement ouvert)", "domain": "stat mech", "status": "open"},
    {"s": "Meas_pb","strate": 0, "from": "Problème de la mesure QM (effondrement vs many-worlds vs...)", "domain": "quantique", "status": "open"},
    {"s": "Turbulence","strate": 0, "from": "Turbulence complète (pas de théorie fermée, Feynman unsolved)", "domain": "fluides", "status": "open"},

    # --- Strate 0 : ajouts ratissage systématique ---

    # Nb théorie suppléments
    {"s": "γ_irr", "strate": 0, "from": "Euler-Mascheroni γ irrationnel? (conjecturé, ouvert depuis 1734)", "domain": "nb théorie", "status": "open"},
    {"s": "Mersenne∞","strate": 0, "from": "Nombres de Mersenne premiers infinis? (Lenstra-Pomerance-Wagstaff)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "Wieferich∞","strate": 0, "from": "Infiniment de premiers Wieferich? (2^(p-1)≡1 mod p², seulement 1093 et 3511 connus)", "domain": "nb théorie", "status": "open"},
    {"s": "Carmichael","strate": 0, "from": "Conjecture Carmichael — φ(n)=k a toujours ≥2 solutions (1907)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "ErdRecip","strate": 0, "from": "Conjecture Erdős — somme 1/p diverge si A contient progressions arith. (partiel Green-Tao)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "SophGerm∞","strate": 0, "from": "Infiniment de premiers Sophie Germain? (p et 2p+1 premiers)", "domain": "nb théorie", "status": "open"},
    {"s": "Waring_g","strate": 0, "from": "Conjecture Waring — g(k) exact pour tout k (Hilbert prouvé existence, formule exacte partielle)", "domain": "nb théorie", "status": "open"},
    {"s": "Odd_perf","strate": 0, "from": "Existe-t-il un nombre parfait impair? (ouvert depuis l'antiquité)", "domain": "nb théorie", "status": "open"},

    # Combinatoire / graphes suppléments
    {"s": "ErdGyar","strate": 0, "from": "Conjecture Erdős–Gyárfás — cycles longueur 2^k dans graphes cubiques", "domain": "combinatoire", "status": "conjecture"},
    {"s": "Third23","strate": 0, "from": "Conjecture 1/3-2/3 — tout poset non total a comparaison entre 1/3 et 2/3 (Kislitsyn 1968)", "domain": "combinatoire", "status": "conjecture"},
    {"s": "CycleDbl","strate": 0, "from": "Cycle double cover — tout graphe sans pont a couverture double par cycles (Szekeres/Seymour)", "domain": "combinatoire", "status": "conjecture"},
    {"s": "Tutte5fl","strate": 0, "from": "Conjecture Tutte 5-flow — tout graphe sans pont a 5-flow non-nul", "domain": "combinatoire", "status": "conjecture"},

    # Algèbre suppléments
    {"s": "Burnside","strate": 0, "from": "Burnside borné — B(m,n) fini? (ouvert m=2,n=5 par exemple)", "domain": "algèbre", "status": "open"},
    {"s": "AndrCurtis","strate": 0, "from": "Conjecture Andrews-Curtis — présentation triviale réductible (1965, potentiellement faux)", "domain": "algèbre", "status": "conjecture"},
    {"s": "CasasAlv","strate": 0, "from": "Conjecture Casas-Alvero — polynôme partageant racine avec toutes ses dérivées (2001)", "domain": "algèbre", "status": "conjecture"},
    {"s": "CherlinZ","strate": 0, "from": "Conjecture Cherlin-Zilber — groupes simples ω-stables sont algébriques (1970s)", "domain": "algèbre", "status": "conjecture"},

    # Géométrie / Topologie suppléments
    {"s": "Thomson","strate": 0, "from": "Problème Thomson — configuration optimale N points sur sphère (ouvert N>5)", "domain": "géométrie", "status": "open"},
    {"s": "EilGanea","strate": 0, "from": "Conjecture Eilenberg-Ganea — cd(G)=2 implique gd(G)=2? (1957)", "domain": "topologie", "status": "conjecture"},
    {"s": "Smooth4P","strate": 0, "from": "Poincaré lisse dim 4 — S⁴ topologique admet une unique structure lisse? (ouvert)", "domain": "topologie", "status": "open"},

    # Analyse suppléments
    {"s": "Brennan","strate": 0, "from": "Conjecture Brennan — intégrales puissances dérivée applications conformes (1978)", "domain": "analyse", "status": "conjecture"},
    {"s": "Lehmer_M","strate": 0, "from": "Conjecture Lehmer — mesure de Mahler ≥ constante pour non-cyclotomiques (1933)", "domain": "analyse", "status": "conjecture"},

    # Géom diff suppléments
    {"s": "PosOp",  "strate": 0, "from": "Conjecture opérateur courbure positive — variété compacte ≅ espace forme (Hamilton dim 4, ouvert dim>4)", "domain": "géom diff", "status": "conjecture"},
    {"s": "GromovSC","strate": 0, "from": "Questions Gromov courbure scalaire — 101 problèmes (2019+, programme actif)", "domain": "géom diff", "status": "open"},

    # Systèmes dynamiques suppléments
    {"s": "PercolSq","strate": 0, "from": "Seuil percolation carré — forme analytique exacte? (pc≈0.5927, pas de formule fermée)", "domain": "probabilités", "status": "open"},
    {"s": "Mandel_loc","strate": 0, "from": "Ensemble Mandelbrot localement connexe? (MLC conjecture, Douady-Hubbard)", "domain": "systèmes dynamiques", "status": "conjecture"},

    # Physique théorique suppléments
    {"s": "Lepton_u","strate": 0, "from": "Universalité leptonique — pourquoi 3 familles? masse neutrinos (BSM physics)", "domain": "QFT", "status": "open"},
    {"s": "CC_prob","strate": 0, "from": "Problème constante cosmologique — pourquoi Λ≈10⁻¹²² en unités Planck? (fine-tuning)", "domain": "cosmologie", "status": "open"},

    # ================================================================
    # STRATE 1 — CONJECTURES NP / Σ⁰₁
    # ================================================================

    {"s": "P≠NP",  "strate": 1, "from": "Conjecture P≠NP (Cook 1971, Clay $1M)", "domain": "complexité", "status": "conjecture"},
    {"s": "P=NP",  "strate": 1, "from": "Question ouverte P=NP (Cook 1971)", "domain": "complexité", "status": "open"},
    {"s": "NP≠coNP","strate": 1, "from": "Conjecture NP≠coNP", "domain": "complexité", "status": "conjecture"},
    {"s": "P≠PSPACE","strate": 1, "from": "Conjecture P≠PSPACE (seconde en notoriété après P≠NP)", "domain": "complexité", "status": "conjecture"},
    {"s": "NP∩coNP","strate": 1, "from": "NP∩coNP = P ? (ouvert, lié à factoring/LP)", "domain": "complexité", "status": "open"},
    {"s": "UGC",   "strate": 1, "from": "Unique Games Conjecture (Khot 2002, inapproximabilité optimale)", "domain": "complexité", "status": "conjecture"},
    {"s": "ETH",   "strate": 1, "from": "Exponential Time Hypothesis (Impagliazzo-Paturi 2001)", "domain": "complexité", "status": "conjecture"},
    {"s": "SETH",  "strate": 1, "from": "Strong ETH — SAT ne se résout pas en 2^(1-ε)n", "domain": "complexité", "status": "conjecture"},
    {"s": "GI∈P",  "strate": 1, "from": "Graph Isomorphism ∈ P ? (quasi-poly Babai 2015, poly ouvert)", "domain": "complexité", "status": "open"},
    {"s": "Factor∈P","strate": 1, "from": "Factorisation ∈ P ? (classique, pas quantique)", "domain": "complexité", "status": "open"},
    {"s": "BH_conj","strate": 1, "from": "Berman-Hartmanis — tous NP-complets isomorphes (1977)", "domain": "complexité", "status": "conjecture"},
    {"s": "VP≠VNP","strate": 1, "from": "Conjecture Valiant VP≠VNP (permanent vs déterminant, 1979)", "domain": "complexité", "status": "conjecture"},
    {"s": "Nat_barrier","strate": 1, "from": "Natural proofs barrier (Razborov-Rudich 1997, limite technique)", "domain": "complexité", "status": "conjecture"},
    {"s": "NP/poly","strate": 1, "from": "NP ⊄ P/poly ? (conjecture, Karp-Lipton: sinon PH collapse)", "domain": "complexité", "status": "conjecture"},
    {"s": "OWF",   "strate": 1, "from": "One-Way Functions existent? (base crypto, impliqué par P≠NP?)", "domain": "complexité", "status": "conjecture"},
    {"s": "NC≠P",  "strate": 1, "from": "NC ≠ P ? (parallélisme ne résout pas tout)", "domain": "complexité", "status": "conjecture"},
    {"s": "L≠P",   "strate": 1, "from": "L ≠ P ? (espace log ≠ temps poly)", "domain": "complexité", "status": "conjecture"},
    {"s": "RP=P",  "strate": 1, "from": "RP = P ? (dérandomisation one-sided)", "domain": "complexité", "status": "conjecture"},
    {"s": "BPP=P", "strate": 1, "from": "BPP = P ? (dérandomisation two-sided, conjecture standard)", "domain": "complexité", "status": "conjecture"},
    {"s": "L=RL",  "strate": 1, "from": "L = RL ? (dérandomisation espace log, Reingold: SL=L)", "domain": "complexité", "status": "conjecture"},
    {"s": "NL≠P",  "strate": 1, "from": "NL ≠ P ? (non-det espace log ≠ temps poly)", "domain": "complexité", "status": "conjecture"},
    {"s": "3SUM",  "strate": 1, "from": "3SUM conjecture — pas de algo sous-quadratique (fine-grained complexity)", "domain": "complexité", "status": "conjecture"},
    {"s": "APSP",  "strate": 1, "from": "APSP conjecture — all-pairs shortest path cubique (fine-grained)", "domain": "complexité", "status": "conjecture"},

    # ================================================================
    # STRATE 2 — CONJECTURES Π⁰₁ / Σ⁰₂ / CIRCUITS
    # ================================================================

    {"s": "E_lb",  "strate": 2, "from": "Circuit lower bounds pour E (Williams: NEXP⊄ACC⁰, reste ouvert circuits généraux)", "domain": "complexité", "status": "open"},
    {"s": "MCSP",  "strate": 2, "from": "Minimum Circuit Size Problem — NP-complet? (Kabanets-Cai-Chen, ouvert)", "domain": "complexité", "status": "open"},
    {"s": "Derand","strate": 2, "from": "Dérandomisation complète Σ₂ (PRG vs circuits, Nisan-Wigderson framework)", "domain": "complexité", "status": "open"},
    {"s": "NW_hyp","strate": 2, "from": "Hypothèse Nisan-Wigderson (dureté worst-case → dérandomisation)", "domain": "complexité", "status": "conjecture"},
    {"s": "IW_hyp","strate": 2, "from": "Impagliazzo-Wigderson: E dur ↔ BPP=P (2002, partiel)", "domain": "complexité", "status": "conjecture"},
    {"s": "Imp_5w","strate": 2, "from": "5 mondes d'Impagliazzo (Algorithmica→Cryptomania, lequel est le nôtre?)", "domain": "complexité", "status": "open"},
    {"s": "AC⁰_lb","strate": 2, "from": "Lower bounds AC⁰[p] pour tout p premier (au-delà Razborov-Smolensky)", "domain": "complexité", "status": "open"},
    {"s": "Log_depth","strate": 2, "from": "Formula lower bounds — log-depth circuits pour explicit functions (Karchmer-Wigderson)", "domain": "complexité", "status": "open"},
    {"s": "NC_SETH","strate": 2, "from": "NC-SETH — Circuit-SAT on NC circuits pas en (2-ε)ⁿ? (Aaronson, fine-grained)", "domain": "complexité", "status": "conjecture"},
    {"s": "PRG_exist","strate": 2, "from": "PRG inconditionnels existent? (pseudo-random generators sans hypothèse)", "domain": "complexité", "status": "open"},

    # ================================================================
    # STRATE 3 — CONJECTURES PH / Σ⁰ₙ / #P
    # ================================================================

    {"s": "PH_inf","strate": 3, "from": "PH ne collapse pas (∞ niveaux, Stockmeyer, conjecture fondamentale)", "domain": "complexité", "status": "conjecture"},
    {"s": "FP≠#P", "strate": 3, "from": "FP≠#P (compter est plus dur que décider, Valiant)", "domain": "complexité", "status": "conjecture"},
    {"s": "PH⊂PP", "strate": 3, "from": "PH ⊊ PP ? (Toda: PH⊆P^#P, mais PP⊆PSPACE)", "domain": "complexité", "status": "conjecture"},
    {"s": "TC⁰=NC¹","strate": 3, "from": "TC⁰ = NC¹ ? (threshold vs log-depth, ouvert)", "domain": "complexité", "status": "open"},
    {"s": "ΣₖP_sep","strate": 3, "from": "Séparations strictes ΣₖP ⊊ Σₖ₊₁P pour tout k", "domain": "complexité", "status": "conjecture"},
    {"s": "AM=MA", "strate": 3, "from": "AM = MA ? (ordre interaction Arthur-Merlin, conjecture)", "domain": "complexité", "status": "conjecture"},
    {"s": "#P_perm","strate": 3, "from": "Permanent lower bound — perm ∉ NC ? (Valiant 1979, borne super-poly ouverte)", "domain": "complexité", "status": "conjecture"},
    {"s": "PH≠PSPACE","strate": 3, "from": "PH ≠ PSPACE — PH n'a pas de problème complet (si oui, collapse)", "domain": "complexité", "status": "conjecture"},
    {"s": "#P_approx","strate": 3, "from": "#P approximation — FPRAS pour tout #P? (Jerrum-Sinclair partiel)", "domain": "complexité", "status": "open"},
    {"s": "⊕P_NP","strate": 3, "from": "⊕P vs NP — parité vs non-déterminisme (Toda: PH⊆BP⊕P)", "domain": "complexité", "status": "open"},
    {"s": "QSuprem","strate": 3, "from": "Quantum supremacy formelle — échantillonnage impossible si PH ne collapse pas (Aaronson-Arkhipov 2011)", "domain": "complexité", "status": "conjecture"},
    {"s": "FewP","strate": 3, "from": "FewP = P ? — NP avec peu de témoins (Cai-Hemachandra)", "domain": "complexité", "status": "conjecture"},

    # ================================================================
    # STRATE 4 — CONJECTURES PSPACE / ARITHMÉTIQUE
    # ================================================================

    {"s": "PSPACE≠EXP","strate": 4, "from": "PSPACE ≠ EXPTIME ? (conjecture, hiérarchie espace)", "domain": "complexité", "status": "conjecture"},
    {"s": "NEXP_lb","strate": 4, "from": "NEXP lower bounds au-delà ACC⁰ (Williams 2010+, ouvert circuits généraux)", "domain": "complexité", "status": "open"},
    {"s": "Derandom_space","strate": 4, "from": "RL=L ? (dérandomisation espace log, Reingold undirected)", "domain": "complexité", "status": "conjecture"},
    {"s": "Cons_PA","strate": 4, "from": "Con(PA) dans systèmes plus faibles (ouvert au-delà Gentzen ε₀)", "domain": "logique", "status": "open"},
    {"s": "Goldbach_eff","strate": 4, "from": "Goldbach effectif — borne calculable pour exceptions", "domain": "nb théorie", "status": "open"},
    {"s": "QIP_c", "strate": 4, "from": "QIP(2) = QIP ? (nombre tours quantique interactif)", "domain": "complexité", "status": "open"},
    {"s": "EXP≠NEXP","strate": 4, "from": "EXP ≠ NEXP ? (non-déterminisme exponentiel)", "domain": "complexité", "status": "conjecture"},
    {"s": "Vaught","strate": 4, "from": "Conjecture Vaught — nombre modèles dénombrables: ω ou ≤ℵ₀ (1961)", "domain": "logique", "status": "conjecture"},
    {"s": "BQP_PSPACE","strate": 4, "from": "BQP ⊊ PSPACE ? (quantique < espace poly, conjecture)", "domain": "complexité", "status": "conjecture"},
    {"s": "Algebriz","strate": 4, "from": "Barrière algébrisation — tout lower bound doit être non-algébrisant (Aaronson-Wigderson 2009)", "domain": "complexité", "status": "open"},
    {"s": "NEXP⊄P/poly","strate": 4, "from": "NEXP ⊄ P/poly ? (conjecture, impliquerait EXP≠NEXP)", "domain": "complexité", "status": "conjecture"},

    # ================================================================
    # STRATE 5 — CONJECTURES HYPERARITHMÉTIQUE / GRANDS CARDINAUX
    # ================================================================

    # --- Programme Woodin / Ultimate L ---
    {"s": "Large_c","strate": 5, "from": "Cardinaux larges (hiérarchie consistance, non résolu dans ZFC)", "domain": "logique", "status": "open"},
    {"s": "V=Ult", "strate": 5, "from": "V = Ultimate L (Woodin, programme en cours)", "domain": "logique", "status": "programme"},
    {"s": "Ω-conj","strate": 5, "from": "Ω-conjecture (Woodin, base de Ω-logique)", "domain": "logique", "status": "conjecture"},
    {"s": "HOD_conj","strate": 5, "from": "HOD conjecture (Woodin — V proche de HOD sous grands cardinaux?)", "domain": "logique", "status": "conjecture"},
    {"s": "InnerM","strate": 5, "from": "Inner Model Problem (modèle intérieur pour supercompact)", "domain": "logique", "status": "open"},

    # --- Déterminance ---
    {"s": "Det_proj","strate": 5, "from": "Déterminance projective (PD, prouvé sous grands cardinaux, force exacte?)", "domain": "logique", "status": "conjecture"},
    {"s": "Σ²₁_abs","strate": 5, "from": "Σ²₁-absoluteness (invariance modèles de forcing)", "domain": "logique", "status": "open"},
    {"s": "AD_UA", "strate": 5, "from": "AD implique Ultrapower Axiom? (Goldberg, ouvert au-delà ℵω)", "domain": "logique", "status": "conjecture"},

    # --- Axiomes de forcing / Martin ---
    {"s": "PCF_conj","strate": 5, "from": "Conjectures PCF (Shelah, arithmétique cardinale singulière)", "domain": "logique", "status": "conjecture"},
    {"s": "MM++",  "strate": 5, "from": "Martin's Maximum++ (extension axiomes de forcing, implications?)", "domain": "logique", "status": "conjecture"},
    {"s": "PFA_sc","strate": 5, "from": "PFA a force de consistance d'un supercompact? (problème majeur ouvert)", "domain": "logique", "status": "conjecture"},
    {"s": "MSC",   "strate": 5, "from": "Mouse Set Conjecture — déf. ordinale → mouse? (Sargsyan, AD+)", "domain": "logique", "status": "conjecture"},

    # --- Cardinaux extrêmes ---
    {"s": "Reinh", "strate": 5, "from": "Cardinal Reinhardt — inconsistant avec AC? (ouvert sans AC, Berkeley)", "domain": "logique", "status": "open"},
    {"s": "UltraExact","strate": 5, "from": "Cardinaux ultraexacting (Aguilera-Bagaria-Goldberg 2024, vs HOD conjecture)", "domain": "logique", "status": "open"},
    {"s": "Kunen_bound","strate": 5, "from": "Seuil exact Kunen inconsistency — où commence l'inconsistance? (ouvert)", "domain": "logique", "status": "open"},

    # --- Borel / hyperarithmétique ---
    {"s": "Borel_det∞","strate": 5, "from": "Déterminance Borélienne infinie (au-delà ZFC?)", "domain": "logique", "status": "open"},
    {"s": "Martin_conj","strate": 5, "from": "Martin's conjecture — degrés Turing, fonctions régressives (Slaman-Steel, partiel 2024)", "domain": "logique", "status": "conjecture"},

    # ================================================================
    # STRATE 6 — INDÉCIDABLE / INDÉPENDANT DE ZFC / FRONTIÈRES
    # ================================================================

    # --- Busy Beaver : frontière absolue ---
    {"s": "BB5",    "strate": 6, "from": "BB(5) = 47176870 ? (bb5.org 2024, vérification formelle en cours)", "domain": "calculabilité", "status": "open"},
    {"s": "BB6",    "strate": 6, "from": "BB(6) — valeur inconnue, BB(n) indépendant ZFC pour n≥~7", "domain": "calculabilité", "status": "open"},

    # --- Problèmes dont la DÉCIDABILITÉ est ouverte ---
    {"s": "Skolem_pb","strate": 6, "from": "Problème de Skolem — suite récurrence linéaire atteint 0? (Skolem 1934, décidable ordre≤4 seulement)", "domain": "calculabilité", "status": "open"},
    {"s": "Positivity","strate": 6, "from": "Positivity Problem — suite LRS toujours ≥0? (Ouaknine-Worrell, décidable ordre≤5)", "domain": "calculabilité", "status": "open"},
    {"s": "Mort_mat","strate": 6, "from": "Mortalité matrices — produit→0? (indécidable dim≥3 Paterson 1970, dim 2 ouvert)", "domain": "calculabilité", "status": "open"},
    {"s": "PCPH",   "strate": 6, "from": "PCP sur entiers — variante Post Correspondence Problem sur ℤ", "domain": "calculabilité", "status": "open"},
    {"s": "Inf_chess","strate": 6, "from": "Infinite chess — mat forcé sur échiquier ℤ×ℤ? (Brumleve-Hamkins-Schlicht 2012, ouvert)", "domain": "calculabilité", "status": "open"},
    {"s": "Free_mat","strate": 6, "from": "Freeness matrices 3×3 — semi-groupe engendré libre? (Klarner-Birget-Satterfield 1991, indéc dim≥3)", "domain": "calculabilité", "status": "open"},
    {"s": "Orbit_gen","strate": 6, "from": "Orbit Problem généralisé — point atteint par itération matrice? (Kannan-Lipton partiel)", "domain": "calculabilité", "status": "open"},

    # --- Statements indépendants de ZFC (prouvé indépendant, axiome inconnu) ---
    {"s": "Con_ZFC","strate": 6, "from": "Con(ZFC) — consistance ZFC non prouvable dans ZFC (Gödel 1931)", "domain": "logique", "status": "open"},
    {"s": "CH_ind", "strate": 6, "from": "CH indépendant ZFC (Gödel 1940/Cohen 1963, quel axiome adopter?)", "domain": "logique", "status": "open"},
    {"s": "SH",     "strate": 6, "from": "Hypothèse de Suslin — caractérisation ℝ? (indépendant ZFC, Suslin 1920)", "domain": "logique", "status": "open"},
    {"s": "Kaplansky_ZFC","strate": 6, "from": "Conjecture Kaplansky — homomorphisme Banach C(X) continu? (indépendant ZFC, Dales-Solovay 1976)", "domain": "analyse fonctionnelle", "status": "open"},
    {"s": "Whitehead","strate": 6, "from": "Problème Whitehead — tout groupe abélien Whitehead libre? (indépendant ZFC, Shelah 1974)", "domain": "algèbre", "status": "open"},
    {"s": "Borel_mz","strate": 6, "from": "Conjecture Borel mesure zéro — tout strong measure zero dénombrable? (indépendant ZFC)", "domain": "théorie mesure", "status": "open"},
    {"s": "NormMoore","strate": 6, "from": "Normal Moore Space — tout espace Moore normal métrisable? (indépendant ZFC)", "domain": "topologie", "status": "open"},
    {"s": "Calkin", "strate": 6, "from": "Automorphismes extérieurs algèbre Calkin (Farah/Phillips-Weaver, indépendant ZFC)", "domain": "analyse fonctionnelle", "status": "open"},

    # --- Statements indépendants de PA (Peano) ---
    {"s": "Friedman","strate": 6, "from": "Théorèmes de Friedman — énoncés finis indépendants PA/ZFC (TREE(3))", "domain": "logique", "status": "open"},
    {"s": "ParisH", "strate": 6, "from": "Paris-Harrington — Ramsey renforcé indépendant PA (Paris-Harrington 1977)", "domain": "logique", "status": "open"},
    {"s": "Goodstein","strate": 6, "from": "Goodstein theorem — suite→0 prouvable dans PA? (non, Kirby-Paris 1982)", "domain": "logique", "status": "open"},
    {"s": "Kruskal_ind","strate": 6, "from": "Kruskal tree theorem — indépendant PA et prédicativisme (fini form)", "domain": "logique", "status": "open"},

    # --- Frontières Chaitin / Information algorithmique ---
    {"s": "Chaitin_Ω","strate": 6, "from": "Ω de Chaitin — probabilité arrêt, réel non calculable (Chaitin 1975, valeur exacte?)", "domain": "calculabilité", "status": "open"},
    {"s": "K_bound","strate": 6, "from": "Borne Kolmogorov — complexité K(x) non calculable, quelle borne par théorie? (Chaitin)", "domain": "calculabilité", "status": "open"},

    # --- Σ¹₂ et déterminance ---
    {"s": "Σ¹₂_det","strate": 6, "from": "Déterminance Σ¹₂ sans grands cardinaux (ouvert)", "domain": "logique", "status": "open"},

    # ==================================================================
    # RATISSAGE PASS 3 — 17 Fév 2026 soir
    # ==================================================================

    # --- Strate 6 : indécidable/physique ---
    {"s": "SpectGap","strate": 6, "from": "Spectral gap undecidability — gapped/gapless indécidable pour Hamiltoniens 2D (Cubitt-Perez-Garcia-Wolf, Nature 2015)", "domain": "calculabilité", "status": "open"},
    {"s": "H10_Q","strate": 6, "from": "Hilbert 10th sur ℚ — décidabilité Diophantine over rationals? (Mazur-Poonen, ouvert majeur)", "domain": "calculabilité", "status": "open"},

    # --- Strate 0 : nombre théorie ---
    {"s": "Littlewood","strate": 0, "from": "Conjecture Littlewood — inf n·‖nα‖·‖nβ‖=0 (c.1930, Einsiedler-Katok-Lindenstrauss 2006: exceptions dim Hausdorff 0)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "ErdTuran_ab","strate": 0, "from": "Conjecture Erdős-Turán bases additives — base ordre 2 a f(n) non borné (1941)", "domain": "nb théorie", "status": "conjecture"},
    {"s": "Singmaster","strate": 0, "from": "Conjecture Singmaster — multiplicité bornée dans triangle Pascal (1971)", "domain": "nb théorie", "status": "conjecture"},

    # --- Strate 0 : combinatoire ---
    {"s": "ErdHajnal","strate": 0, "from": "Conjecture Erdős-Hajnal — H-free → clique/stable poly(n) (1977/1989, toujours ouverte)", "domain": "combinatoire", "status": "conjecture"},
    {"s": "ErdSzek","strate": 0, "from": "Conjecture Erdős-Szekeres — 2^(n-2)+1 points suffisent pour n-gone convexe (1935)", "domain": "combinatoire", "status": "conjecture"},
    {"s": "ErdSelf","strate": 0, "from": "Conjecture Erdős-Selfridge — covering system moduli distincts contient modulus pair (1950)", "domain": "combinatoire", "status": "conjecture"},
    {"s": "Turan_bfp","strate": 0, "from": "Turán brick factory problem — crossing number K(m,n) = Zarankiewicz? (1952, ouvert)", "domain": "combinatoire", "status": "conjecture"},

    # --- Strate 0 : systèmes dynamiques ---
    {"s": "Furst_x2x3","strate": 0, "from": "Conjecture Furstenberg ×2,×3 — seules mesures ergodiques = Lebesgue ou atomiques (1967, rigidité mesure)", "domain": "systèmes dynamiques", "status": "conjecture"},
    {"s": "QUE","strate": 0, "from": "Quantum Unique Ergodicity — fonctions propres → Lebesgue (Rudnick-Sarnak 1994, Lindenstrauss 2006 arithmétique)", "domain": "systèmes dynamiques", "status": "conjecture"},

    # --- Strate 0 : géométrie algébrique ---
    {"s": "Tate_c","strate": 0, "from": "Conjecture Tate — cycles algébriques ↔ classes Galois-invariantes ℓ-adiques (Tate 1963, analogue Hodge)", "domain": "géom algébrique", "status": "conjecture"},
    {"s": "Groth_std","strate": 0, "from": "Conjectures standard Grothendieck — Lefschetz, Künneth, Hodge standard pour motifs (1968, ouvertes en général)", "domain": "géom algébrique", "status": "conjecture"},
    {"s": "GrotPeriod","strate": 0, "from": "Conjecture périodes Grothendieck — deg.transc(périodes) = dim groupe Galois motivique (Kontsevich-Zagier)", "domain": "géom algébrique", "status": "conjecture"},
    {"s": "Sect_conj","strate": 0, "from": "Section conjecture Grothendieck — points rationnels ↔ sections π₁ (lettre à Faltings 1983)", "domain": "géom algébrique", "status": "conjecture"},

    # --- Strate 0 : physique quantique ---
    {"s": "Haldane","strate": 0, "from": "Conjecture Haldane — chaîne Heisenberg antiferro spin entier est gappée (1983, Nobel 2016, non prouvé rigoureusement)", "domain": "QFT", "status": "conjecture"},
    {"s": "AreaLaw","strate": 0, "from": "Area law conjecture — entropie intrication ∝ surface frontière (prouvé 1D Hastings 2007, ouvert dim>1)", "domain": "QFT", "status": "conjecture"},

    # ═══════════════════════════════════════════════════════════════
    #  RATISSAGE PASS 4 — topologie K-théorie, nb théorie, motivique
    # ═══════════════════════════════════════════════════════════════

    # --- Strate 0 : topologie / K-théorie ---
    {"s": "BaumConnes","strate": 0, "from": "Conjecture Baum-Connes (1982) — assembly map μ: K_*^top(G) → K_*(C*_r(G)) isomorphisme. Prouvée a-T-ménables (Higson-Kasparov 2001), hyperboliques (Lafforgue 2012). Contre-ex. avec coeff. (Higson-Lafforgue-Skandalis 2002). Ouverte en général.", "domain": "topologie", "status": "conjecture"},
    {"s": "FarrellJones","strate": 0, "from": "Conjecture Farrell-Jones (1993) — assembly map K/L-théorie algébrique. Pas de contre-exemples. Implique Novikov, Borel. Prouvée CAT(0), hyperboliques (Bartels-Lück-Reich).", "domain": "topologie", "status": "conjecture"},

    # --- Strate 0 : théorie des nombres ---
    {"s": "Artin_prim","strate": 0, "from": "Conjecture Artin racine primitive (1927) — tout non-carré a≠-1 est racine primitive mod p pour ∞ primes. Hooley 1967: conditionnel GRH. Heath-Brown 1986: au moins un de {2,3,5}.", "domain": "nb théorie", "status": "conjecture"},
    {"s": "Selberg_ev","strate": 0, "from": "Conjecture Selberg valeur propre (1965) — λ₁ ≥ 1/4 pour Γ(N) congruence. Selberg: ≥3/16. Kim-Sarnak 2003: ≥975/4096≈0.238. Impliquée par Ramanujan généralisée.", "domain": "nb théorie", "status": "conjecture"},
    {"s": "GenRam","strate": 0, "from": "Conjecture Ramanujan généralisée — paramètres Satake tempérés pour formes automorphes cuspidales GL_n. Deligne: prouvée GL_2 holomorphe. Ouverte Maass forms et GL_n, n>2. Implique Selberg.", "domain": "nb théorie", "status": "conjecture"},

    # --- Strate 0 : géométrie algébrique / motivique ---
    {"s": "BeilSoule","strate": 0, "from": "Conjecture Beilinson-Soulé (vanishing) — H^p_mot(X,ℤ(q))=0 pour p<0, q≥0. Connue corps finis. Centrale théorie motivique, t-structure sur motifs.", "domain": "géom algébrique", "status": "conjecture"},

    # ═══════════════════════════════════════════════════════════════
    #  RATISSAGE PASS 4 — PROUVÉS récents majeurs
    # ═══════════════════════════════════════════════════════════════

    # --- Prouvés : K-théorie / cohomologie motivique ---
    {"s": "Milnor_K","strate": 3, "from": "Conjecture Milnor K-théorie (1970) — K^M_n(F)/2 ≅ H^n(F,ℤ/2). Voevodsky 2003 (Fields Medal 2002). Utilise A¹-homotopie, opérations Steenrod motiviques."},
    {"s": "BlochKato","strate": 3, "from": "Conjecture Bloch-Kato (norm residue) — K^M_n(F)/ℓ ≅ H^n(F,μ_ℓ^⊗n) pour tout premier ℓ. Rost-Voevodsky 2011. Généralise Milnor. Implique Quillen-Lichtenbaum."},

    # --- Prouvés : représentations / Langlands ---
    {"s": "KazhLusz","strate": 3, "from": "Conjecture Kazhdan-Lusztig (1979) — multiplicités [M_w:L_y] = P_{y,w}(1) polynômes KL. Beilinson-Bernstein 1981, Brylinski-Kashiwara 1981. D-modules, perverse sheaves."},
    {"s": "GeomLang","strate": 3, "from": "Conjecture géométrique Langlands catégorique (unramified) — Gaitsgory-Raskin et al. 2024. 800+ pages, 5 papers, 9 auteurs. 30 ans de travail. Hecke eigensheaves."},

    # --- Prouvés : EDP / fluides ---
    {"s": "Onsager_c","strate": 3, "from": "Conjecture Onsager (1949) — solutions Euler C^{α}: conservation énergie ssi α>1/3. Rigide: Constantin-E-Titi 1994. Flexible: Isett 2018, Buckmaster-De Lellis-Székelyhidi-Vicol 2019 (convex integration)."},

    # ═══════════════════════════════════════════════════════════════
    #  RATISSAGE PASS 4 — batch 2 : convexe, birationnel, prouvés majeurs
    # ═══════════════════════════════════════════════════════════════

    # --- Strate 0 : géométrie convexe ---
    {"s": "Mahler_vol","strate": 0, "from": "Conjecture Mahler (1939) — produit volumique |K||K°| minimisé par hypercubes (sym) ou simplexes (non-sym). Prouvée n=2 (Mahler), n=3 (Iriyeh-Shibata 2020). Hanner polytopes = minima locaux.", "domain": "géométrie", "status": "conjecture"},

    # --- Strate 0 : géométrie algébrique / birationnelle ---
    {"s": "Abundance","strate": 0, "from": "Abundance conjecture (MMP) — K_X nef ⟹ K_X semi-ample. Prouvée dim ≤ 3. Compléterait classification birationnelle. Birkar-Cascini-Hacon-McKernan 2010 (cas log general type).", "domain": "géom algébrique", "status": "conjecture"},

    # --- Prouvés : analyse fonctionnelle / combinatoire ---
    {"s": "KadSinger","strate": 3, "from": "Kadison-Singer (1959) — extension unique d'états purs B(H) vers MASA. Marcus-Spielman-Srivastava 2013. Méthode polynômes entrelacés, interlacing families."},

    # --- Prouvés : théorie des nombres ---
    {"s": "FermatWiles","strate": 3, "from": "Dernier théorème Fermat / modularité (1637/1995) — x^n+y^n=z^n impossible n>2. Wiles 1995 (modularity semi-stable). BCDT 2001 (modularity complète courbes elliptiques sur ℚ)."},
    {"s": "SatoTate","strate": 3, "from": "Conjecture Sato-Tate (1963) — distribution angles Frobenius courbes elliptiques suit mesure sin²θ. Taylor-Barnet-Lamb-Geraghty-Harris-Shepherd-Barron 2011."},

    # --- Prouvés : topologie 3-variétés ---
    {"s": "VirtHaken","strate": 3, "from": "Virtual Haken conjecture (Waldhausen 1968) — toute 3-variété hyperbolique fermée a revêtement fini Haken. Agol 2012, s'appuyant sur Wise (cube complexes spéciaux) et Kahn-Markovic."},

    # --- Prouvés : combinatoire algébrique ---
    {"s": "KakeyaFin","strate": 3, "from": "Kakeya conjecture corps finis (Wolff 1999) — Besicovitch set dans F_q^n a ≥ c_n·q^n éléments. Dvir 2008, méthode polynomiale. Preuve élégante en 1 page."},

    # ═══════════════════════════════════════════════════════════════
    #  RATISSAGE PASS 5 — grands théorèmes prouvés XXe-XXIe siècle
    # ═══════════════════════════════════════════════════════════════

    # --- Topologie : résolus ---
    {"s": "Poinc3",   "strate": 3, "from": "Conjecture Poincaré dim 3 — toute 3-variété simplement connexe fermée ≅ S³ (Perelman 2003, flot de Ricci avec chirurgie). Millennium Problem."},
    {"s": "Geomtrz",  "strate": 3, "from": "Géométrisation Thurston — toute 3-variété se décompose en 8 géométries modèles (Perelman 2003). Implique Poincaré."},
    {"s": "hCobord",  "strate": 3, "from": "h-cobordism theorem dim ≥ 6 (Smale 1962, Fields Medal). Implique conjecture Poincaré généralisée dim ≥ 5."},
    {"s": "Freed4",   "strate": 3, "from": "Freedman theorem — classification topologique 4-variétés simplement connexes fermées (1982, Fields Medal). Forme d'intersection détermine type topologique."},
    {"s": "SmithConj","strate": 3, "from": "Smith conjecture — action Z/pZ sur S³ préservant orientation a ensemble fixe = nœud trivial (Morgan-Bass 1984)."},
    {"s": "ExoticS7", "strate": 3, "from": "Sphères exotiques — S⁷ admet 28 structures différentielles non-standard (Milnor 1956, Kervaire-Milnor 1963)."},
    {"s": "Surgery",  "strate": 3, "from": "Théorie chirurgie — classification variétés dim ≥ 5 via séquence exacte de Sullivan-Wall (Browder-Novikov-Sullivan-Wall 1960s)."},

    # --- Théorie des nombres : résolus ---
    {"s": "Mordell",  "strate": 3, "from": "Conjecture Mordell — courbe genre g ≥ 2 sur ℚ a nombre fini de points rationnels (Faltings 1983, Fields Medal)."},
    {"s": "WeilConj", "strate": 3, "from": "Conjectures Weil — fonctions zêta variétés sur F_q: rationalité (Dwork 1960), fonctionnalité (Grothendieck 1965), RH (Deligne 1974, Fields Medal)."},
    {"s": "CatalanM", "strate": 3, "from": "Conjecture Catalan — x^p - y^q = 1 seule solution en puissances parfaites: 3²-2³=1 (Mihailescu 2002)."},
    {"s": "GoldWeak", "strate": 3, "from": "Goldbach faible/ternaire — tout impair > 5 est somme de 3 premiers (Helfgott 2013, inconditionnel)."},
    {"s": "BddGaps",  "strate": 3, "from": "Bounded gaps between primes — lim inf(pₙ₊₁-pₙ) < ∞ (Zhang 2013: 7×10⁷, Maynard 2013: 600, Polymath8b: 246)."},
    {"s": "GrossZag", "strate": 3, "from": "Formule Gross-Zagier — hauteur Néron-Tate point Heegner = dérivée L'(E,1) (1986). Clé pour BSD analytique rang 1."},
    {"s": "HerbRibet","strate": 3, "from": "Herbrand-Ribet — p|Bₖ ⟺ p divise #classe idéale composante χ (Herbrand 1932 →, Ribet 1976 ←)."},
    {"s": "IwasMain", "strate": 3, "from": "Iwasawa Main Conjecture — structure Λ-modules de Selmer sur tours cyclotomiques ℤₚ (Mazur-Wiles 1984)."},
    {"s": "SerreMod", "strate": 3, "from": "Conjecture Serre modularité — repr. Galois irréductibles impaires mod p proviennent de formes modulaires (Khare-Wintenberger 2009)."},
    {"s": "LaffFnF",  "strate": 3, "from": "Langlands pour GL_n corps de fonctions (Laurent Lafforgue 2002, Fields Medal). Correspondance automorphe ↔ Galois."},

    # --- Algèbre : résolus ---
    {"s": "CFSG",     "strate": 3, "from": "Classification groupes finis simples — 18 familles infinies + 26 sporadiques (~1983, ~10000 pages, programme Gorenstein)."},
    {"s": "Moonshine","strate": 3, "from": "Monstrous Moonshine — coefficients j(τ) = dimensions repr. irréd. du Monster (Conway-Norton 1979, Borcherds 1992, Fields Medal). Vertex algebras."},
    {"s": "QuilSusl", "strate": 3, "from": "Conjecture Serre/Quillen-Suslin — tout module projectif sur k[x₁,...,xₙ] est libre (Quillen 1976, Suslin 1976)."},

    # --- Analyse : résolus ---
    {"s": "Bieberbach","strate": 3, "from": "Conjecture Bieberbach — |aₙ| ≤ n pour fonctions univalentes sur disque (de Branges 1985)."},
    {"s": "CarlesonL2","strate": 3, "from": "Convergence p.p. séries de Fourier dans L² (Carleson 1966). Étendu à Lᵖ p>1 (Hunt 1968)."},
    {"s": "KatoSqrt", "strate": 3, "from": "Conjecture Kato racine carrée — dom(√(div·A·grad)) = H¹ (Auscher-Hofmann-Lacey-McIntosh-Tchamitchian 2001)."},
    {"s": "CoronaTh", "strate": 3, "from": "Théorème Corona — spectre maximal de H^∞(𝔻) est dense dans spectre (Carleson 1962)."},

    # --- Géométrie diff / géométrie : résolus ---
    {"s": "CalabiYau","strate": 3, "from": "Conjecture Calabi — existence métrique Kähler Ricci-plate si c₁(M)=0 (Yau 1978, Fields Medal)."},
    {"s": "PosMass",  "strate": 3, "from": "Positive mass theorem — masse ADM ≥ 0, = 0 ssi Minkowski (Schoen-Yau 1979, Witten 1981)."},
    {"s": "Kepler",   "strate": 3, "from": "Conjecture Kepler — empilement sphères densité max π/(3√2) ≈ 0.7405 = FCC/HCP (Hales 1998/2005, Flyspeck 2014 vérifié Isabelle/HOL)."},
    {"s": "Willmore", "strate": 3, "from": "Conjecture Willmore — min ∫H²dA pour tores immergés dans ℝ³ = 2π² atteint par tore Clifford (Marques-Neves 2014)."},
    {"s": "AtiyahSing","strate": 3, "from": "Théorème index Atiyah-Singer — ind(D) = ∫ch(σ(D))·Td(M) (1963). Pont analyse↔topologie↔géom algébrique."},

    # --- Combinatoire : résolus ---
    {"s": "FourColor","strate": 3, "from": "Théorème 4 couleurs — tout graphe planaire est 4-coloriable (Appel-Haken 1976, Robertson et al. 1997, Gonthier 2005 vérifié Coq)."},
    {"s": "RobSeym",  "strate": 3, "from": "Graph Minor Theorem — tout ensemble infini de graphes finis contient une paire liée par relation de mineur (Robertson-Seymour 1983-2004, 20 papers)."},
    {"s": "GreenTao", "strate": 3, "from": "Green-Tao — les nombres premiers contiennent des progressions arithmétiques de longueur arbitraire (2004). Szemerédi + transference principle."},
    {"s": "DensHJ",   "strate": 3, "from": "Density Hales-Jewett — version densité du théorème combinatoire de Hales-Jewett (Polymath1 2009/2012)."},
    {"s": "Kneser",   "strate": 3, "from": "Conjecture Kneser — χ(KG(n,k)) = n-2k+2 (Lovász 1978). Première application topologie (Borsuk-Ulam) à la combinatoire."},

    # --- Probabilités : résolus ---
    {"s": "SLE_thm",  "strate": 3, "from": "Invariance conforme percolation critique réseau triangulaire (Smirnov 2001, Fields Medal 2010). SLE Schramm-Loewner evolution."},

    # --- Logique : résolus ---
    {"s": "ParisHarr","strate": 3, "from": "Paris-Harrington — variante combinatoire de Ramsey indépendante de l'arithmétique de Peano (1977). Premier exemple 'naturel' d'indépendance."},
    {"s": "DPRM",     "strate": 3, "from": "Théorème DPRM — ensembles récursivement énumérables = ensembles diophantiens (Davis-Putnam-Robinson-Matiyasevich 1970). Résolution négative H10."},
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
    out_path = Path(__file__).parent / "strates_export.json"
    data = engine.export_json(str(out_path))
    print(f"\n✅ JSON → {out_path} ({data['meta']['total_symbols']} symboles)")
    engine.print_report()
    if "--html" in sys.argv or True:
        html_path = Path(__file__).parent / "strates_cube_live.html"
        json_str = json.dumps(data, ensure_ascii=False)
        html = HTML_TEMPLATE.replace("__DATA_INJECT__", json_str)
        with open(str(html_path), "w", encoding="utf-8") as f:
            f.write(html)
        print(f"✅ HTML → {html_path}")


if __name__ == "__main__":
    main()
