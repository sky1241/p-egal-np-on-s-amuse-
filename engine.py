"""
P=NP ON S'AMUSE — MOTEUR STRATES × SYMBOLES
=============================================
Sky × Claude — Février 2026

Le moteur qui cartographie les symboles mathématiques sur la hiérarchie
de calculabilité. Chaque symbole est placé sur sa strate. Les connexions
entre symboles (co-occurrence dans les formules) forment le mycelium.

Usage:
    python engine.py              → génère strates_export.json + rapport console
    python engine.py --analyse    → analyse détaillée des trous et bottlenecks
    python engine.py --html       → génère aussi le HTML autonome
"""

import json
import math
import sys
from collections import defaultdict
from pathlib import Path

# ============================================================================
# STRATES — 7 niveaux de la hiérarchie arithmétique
# ============================================================================

STRATES = [
    {
        "id": 0,
        "name": "SOL · Δ⁰₀ · Décidable",
        "short": "Δ⁰₀ SOL",
        "formula": "R(x) — pas de quantificateur",
        "desc": "Tout ce qu'une machine de Turing peut décider en temps fini. Le plancher.",
        "color": [74, 222, 128],
        "yr": -0.44,
        "opacity": 0.22,
        "formal": {
            "quantifiers": 0,
            "class": "Δ⁰₀ = Σ⁰₀ = Π⁰₀",
            "decidable": True,
            "oracle": None,
        }
    },
    {
        "id": 1,
        "name": "NUAGE 1 · Σ⁰₁ · Halting Problem",
        "short": "Σ⁰₁ HALTING",
        "formula": "∃y R(x, y)",
        "desc": "Semi-décidable. On peut dire oui, jamais non. Le Halting Problem.",
        "color": [96, 165, 250],
        "yr": -0.26,
        "opacity": 0.18,
        "formal": {
            "quantifiers": 1,
            "class": "Σ⁰₁ (r.e.)",
            "decidable": False,
            "oracle": "∅'",
        }
    },
    {
        "id": 2,
        "name": "NUAGE 2 · Σ⁰₂ · Limite",
        "short": "Σ⁰₂ LIMITE",
        "formula": "∃y ∀z R(x,y,z)",
        "desc": "Deviner, corriger, re-deviner… jamais sûr. Ensembles limites.",
        "color": [167, 139, 250],
        "yr": -0.10,
        "opacity": 0.15,
        "formal": {
            "quantifiers": 2,
            "class": "Σ⁰₂",
            "decidable": False,
            "oracle": "∅''",
        }
    },
    {
        "id": 3,
        "name": "NUAGE n · Σ⁰ₙ · Motif Général",
        "short": "Σ⁰ₙ MOTIF",
        "formula": "∃∀∃∀… n alternances",
        "desc": "Chaque alternance = un étage. Post 1944. Saut itéré de Turing.",
        "color": [244, 114, 182],
        "yr": 0.06,
        "opacity": 0.14,
        "formal": {
            "quantifiers": "n",
            "class": "Σ⁰ₙ / Πⁿₙ / PH",
            "decidable": False,
            "oracle": "∅⁽ⁿ⁾",
        }
    },
    {
        "id": 4,
        "name": "CIEL · AH = ∪ₙ Σ⁰ₙ",
        "short": "AH CIEL",
        "formula": "AH = ∪ₙ Σ⁰ₙ — tout le ciel arithmétique",
        "desc": "L'union de tous les nuages. Tout ce qui se dit en arithmétique du 1er ordre.",
        "color": [251, 191, 36],
        "yr": 0.20,
        "opacity": 0.14,
        "formal": {
            "quantifiers": "ω",
            "class": "AH (arithmetical hierarchy)",
            "decidable": False,
            "oracle": "∅⁽ω⁾",
        }
    },
    {
        "id": 5,
        "name": "HYPERARITHMÉTIQUE · ∅⁽ω⁾→∅⁽α⁾",
        "short": "HYP ω₁ᶜᵏ",
        "formula": "∅⁽α⁾ pour α < ω₁^CK",
        "desc": "Kleene, Church-Kleene ω₁^CK, Δ¹₁. L'escalier transfini.",
        "color": [251, 146, 60],
        "yr": 0.34,
        "opacity": 0.18,
        "formal": {
            "quantifiers": "transfinite",
            "class": "HYP ⊂ Δ¹₁",
            "decidable": False,
            "oracle": "∅⁽α⁾, α < ω₁^CK",
        }
    },
    {
        "id": 6,
        "name": "PLAFOND · Turing 1936 · Non-Calculable",
        "short": "∞ PLAFOND",
        "formula": "∄ M décidant l'arrêt — Prouvé.",
        "desc": "Gödel 1931 · Church 1936 · Turing 1936. BB(n). Le mur absolu.",
        "color": [239, 68, 68],
        "yr": 0.46,
        "opacity": 0.28,
        "formal": {
            "quantifiers": "∞",
            "class": "Non-calculable",
            "decidable": False,
            "oracle": "Aucun ne suffit",
        }
    },
]


# ============================================================================
# SYMBOLES — chaque lettre / symbole, sa source, sa strate
# ============================================================================

SYMBOLES = [
    # -----------------------------------------------------------------------
    # STRATE 0 — SOL · Décidable
    # -----------------------------------------------------------------------
    # Euler: e^(iπ) + 1 = 0
    {"s": "e",   "strate": 0, "from": "Euler e^iπ+1=0",          "domain": "analyse",     "year": 1748},
    {"s": "i",   "strate": 0, "from": "Euler e^iπ+1=0",          "domain": "complexes",   "year": 1748},
    {"s": "π",   "strate": 0, "from": "Euler / géométrie",        "domain": "géométrie",   "year": -250},
    # Einstein: E=mc²
    {"s": "E",   "strate": 0, "from": "Einstein E=mc²",          "domain": "physique",    "year": 1905},
    {"s": "m",   "strate": 0, "from": "Einstein E=mc²",          "domain": "physique",    "year": 1905},
    {"s": "c",   "strate": 0, "from": "Einstein E=mc²",          "domain": "physique",    "year": 1905},
    # Newton: F=ma
    {"s": "F",   "strate": 0, "from": "Newton F=ma",             "domain": "mécanique",   "year": 1687},
    {"s": "a",   "strate": 0, "from": "Newton F=ma",             "domain": "mécanique",   "year": 1687},
    # Pythagore
    {"s": "a²",  "strate": 0, "from": "Pythagore a²+b²=c²",     "domain": "géométrie",   "year": -530},
    {"s": "b²",  "strate": 0, "from": "Pythagore a²+b²=c²",     "domain": "géométrie",   "year": -530},
    {"s": "c²",  "strate": 0, "from": "Pythagore a²+b²=c²",     "domain": "géométrie",   "year": -530},
    # Maxwell
    {"s": "∇×",  "strate": 0, "from": "Maxwell rotationnel",     "domain": "électromagn", "year": 1865},
    {"s": "∇·",  "strate": 0, "from": "Maxwell divergence",      "domain": "électromagn", "year": 1865},
    {"s": "B",   "strate": 0, "from": "Maxwell champ magnétique","domain": "électromagn", "year": 1865},
    # Schrödinger
    {"s": "ψ",   "strate": 0, "from": "Schrödinger Hψ=Eψ",      "domain": "quantique",   "year": 1926},
    {"s": "ℏ",   "strate": 0, "from": "Planck réduite h/2π",     "domain": "quantique",   "year": 1900},
    {"s": "Ĥ",   "strate": 0, "from": "Hamiltonien quantique",   "domain": "quantique",   "year": 1926},
    # Boltzmann
    {"s": "S",   "strate": 0, "from": "Boltzmann S=k·ln(W)",     "domain": "thermo",      "year": 1877},
    {"s": "k",   "strate": 0, "from": "Boltzmann constante",     "domain": "thermo",      "year": 1877},
    {"s": "W",   "strate": 0, "from": "Boltzmann micro-états",   "domain": "thermo",      "year": 1877},
    {"s": "ln",  "strate": 0, "from": "Logarithme naturel",      "domain": "analyse",     "year": 1614},
    # Calcul / Analyse
    {"s": "∫",   "strate": 0, "from": "Leibniz intégrale",       "domain": "analyse",     "year": 1675},
    {"s": "∂",   "strate": 0, "from": "Dérivée partielle",       "domain": "analyse",     "year": 1770},
    {"s": "dx",  "strate": 0, "from": "Leibniz différentielle",  "domain": "analyse",     "year": 1675},
    {"s": "∇",   "strate": 0, "from": "Hamilton gradient/nabla", "domain": "analyse",     "year": 1837},
    {"s": "Δ",   "strate": 0, "from": "Laplacien",               "domain": "analyse",     "year": 1782},
    {"s": "lim",  "strate": 0, "from": "Cauchy/Weierstrass limite","domain":"analyse",     "year": 1821},
    {"s": "Σ",   "strate": 0, "from": "Sommation finie",         "domain": "algèbre",     "year": 1755},
    {"s": "Π",   "strate": 0, "from": "Produit fini",            "domain": "algèbre",     "year": 1755},
    {"s": "Γ",   "strate": 0, "from": "Fonction Gamma d'Euler",  "domain": "analyse",     "year": 1729},
    {"s": "ζ",   "strate": 0, "from": "Riemann ζ(s)",            "domain": "nb premiers", "year": 1859},
    # Ensembles / logique
    {"s": "∈",   "strate": 0, "from": "Cantor appartenance",     "domain": "ensembles",   "year": 1874},
    {"s": "∅",   "strate": 0, "from": "Ensemble vide",           "domain": "ensembles",   "year": 1939},
    {"s": "∪",   "strate": 0, "from": "Union",                   "domain": "ensembles",   "year": 1888},
    {"s": "∩",   "strate": 0, "from": "Intersection",            "domain": "ensembles",   "year": 1888},
    {"s": "⊆",   "strate": 0, "from": "Inclusion",               "domain": "ensembles",   "year": 1890},
    {"s": "ℕ",   "strate": 0, "from": "Nombres naturels",        "domain": "nb",          "year": 1895},
    {"s": "ℤ",   "strate": 0, "from": "Entiers relatifs",        "domain": "nb",          "year": 1895},
    {"s": "ℚ",   "strate": 0, "from": "Rationnels",              "domain": "nb",          "year": 1895},
    {"s": "ℝ",   "strate": 0, "from": "Réels",                   "domain": "nb",          "year": 1895},
    {"s": "ℂ",   "strate": 0, "from": "Complexes",               "domain": "nb",          "year": 1895},
    # Logique propositionnelle
    {"s": "∧",   "strate": 0, "from": "ET logique",              "domain": "logique",     "year": 1910},
    {"s": "∨",   "strate": 0, "from": "OU logique",              "domain": "logique",     "year": 1910},
    {"s": "¬",   "strate": 0, "from": "Négation",                "domain": "logique",     "year": 1910},
    {"s": "→",   "strate": 0, "from": "Implication",             "domain": "logique",     "year": 1910},
    {"s": "↔",   "strate": 0, "from": "Bi-implication",          "domain": "logique",     "year": 1910},
    # Greek letters physique
    {"s": "α",   "strate": 0, "from": "Constante structure fine", "domain": "physique",    "year": 1916},
    {"s": "β",   "strate": 0, "from": "Vitesse relative v/c",    "domain": "relativité",  "year": 1905},
    {"s": "γ",   "strate": 0, "from": "Facteur Lorentz",         "domain": "relativité",  "year": 1905},
    {"s": "δ",   "strate": 0, "from": "Dirac delta δ(x)",        "domain": "distrib",     "year": 1927},
    {"s": "ε",   "strate": 0, "from": "Epsilon voisinage",       "domain": "topologie",   "year": 1821},
    {"s": "θ",   "strate": 0, "from": "Angle trigonométrie",     "domain": "géométrie",   "year": -300},
    {"s": "λ",   "strate": 0, "from": "Lambda calcul Church",    "domain": "calculabilité","year": 1936},
    {"s": "σ",   "strate": 0, "from": "Écart-type / Boltzmann",  "domain": "stats",       "year": 1894},
    {"s": "ρ",   "strate": 0, "from": "Densité",                 "domain": "physique",    "year": 1700},
    {"s": "τ",   "strate": 0, "from": "Tau / couple",            "domain": "mécanique",   "year": 1700},
    {"s": "φ",   "strate": 0, "from": "Nombre d'or (1+√5)/2",   "domain": "nb",          "year": -300},
    {"s": "ω",   "strate": 0, "from": "Fréquence angulaire",     "domain": "physique",    "year": 1750},
    # Opérateurs / fonctions
    {"s": "sin", "strate": 0, "from": "Trigonométrie",           "domain": "géométrie",   "year": -300},
    {"s": "cos", "strate": 0, "from": "Trigonométrie",           "domain": "géométrie",   "year": -300},
    {"s": "log", "strate": 0, "from": "Logarithme Napier",       "domain": "analyse",     "year": 1614},
    {"s": "det", "strate": 0, "from": "Déterminant matrice",     "domain": "algèbre lin", "year": 1750},
    {"s": "√",   "strate": 0, "from": "Racine carrée",           "domain": "arithm",      "year": -1800},
    {"s": "!",   "strate": 0, "from": "Factorielle n!",          "domain": "combinatoire","year": 1808},
    {"s": "∞",   "strate": 0, "from": "Infini potentiel Wallis", "domain": "analyse",     "year": 1655},
    {"s": "=",   "strate": 0, "from": "Égalité Recorde",         "domain": "fondements",  "year": 1557},
    {"s": "+",   "strate": 0, "from": "Addition",                "domain": "arithm",      "year": 1489},
    {"s": "×",   "strate": 0, "from": "Multiplication",          "domain": "arithm",      "year": 1631},
    {"s": "P",   "strate": 0, "from": "Classe P (temps poly)",   "domain": "complexité",  "year": 1971},
    {"s": "χ²",  "strate": 0, "from": "Test chi-carré Pearson",  "domain": "stats",       "year": 1900},
    {"s": "μ₀",  "strate": 0, "from": "Perméabilité vide",       "domain": "électromagn", "year": 1865},
    {"s": "ε₀",  "strate": 0, "from": "Permittivité vide",       "domain": "électromagn", "year": 1865},

    # -----------------------------------------------------------------------
    # STRATE 1 — Σ⁰₁ · Récursivement énumérable
    # -----------------------------------------------------------------------
    {"s": "∃",    "strate": 1, "from": "Quantificateur existentiel",   "domain": "logique",     "year": 1897},
    {"s": "K",    "strate": 1, "from": "Halting set K={e:φₑ(e)↓}",    "domain": "calculabilité","year": 1936},
    {"s": "φₑ",   "strate": 1, "from": "e-ième fonction partielle",   "domain": "calculabilité","year": 1936},
    {"s": "↓",    "strate": 1, "from": "Converge (s'arrête)",         "domain": "calculabilité","year": 1936},
    {"s": "↑",    "strate": 1, "from": "Diverge (boucle infinie)",    "domain": "calculabilité","year": 1936},
    {"s": "Wₑ",   "strate": 1, "from": "e-ième ensemble r.e.",        "domain": "calculabilité","year": 1944},
    {"s": "μy",   "strate": 1, "from": "Opérateur μ recherche",       "domain": "calculabilité","year": 1936},
    {"s": "≤ₘ",   "strate": 1, "from": "Réduction many-one",         "domain": "calculabilité","year": 1944},
    {"s": "≤ₜ",   "strate": 1, "from": "Réduction Turing",           "domain": "calculabilité","year": 1939},
    {"s": "NP",   "strate": 1, "from": "Non-déterministe poly",       "domain": "complexité",  "year": 1971},
    {"s": "coNP", "strate": 1, "from": "Complément de NP",            "domain": "complexité",  "year": 1971},
    {"s": "RE",   "strate": 1, "from": "Récursivement énumérable",    "domain": "calculabilité","year": 1936},
    {"s": "coRE", "strate": 1, "from": "Complément de RE",            "domain": "calculabilité","year": 1936},
    {"s": "SAT",  "strate": 1, "from": "Satisfiabilité Cook 1971",    "domain": "complexité",  "year": 1971},
    {"s": "3COL", "strate": 1, "from": "3-coloration graphe",         "domain": "complexité",  "year": 1972},
    {"s": "TSP",  "strate": 1, "from": "Voyageur de commerce",        "domain": "complexité",  "year": 1972},
    {"s": "BQP",  "strate": 1, "from": "Bounded-error Quantum Poly",  "domain": "quantique",   "year": 1993},

    # -----------------------------------------------------------------------
    # STRATE 2 — Σ⁰₂ · Limite
    # -----------------------------------------------------------------------
    {"s": "∀",    "strate": 2, "from": "Quantificateur universel",     "domain": "logique",     "year": 1897},
    {"s": "∃∀",   "strate": 2, "from": "Alternance Σ⁰₂",             "domain": "calculabilité","year": 1944},
    {"s": "TOT",  "strate": 2, "from": "{e : φₑ est totale}",         "domain": "calculabilité","year": 1944},
    {"s": "FIN",  "strate": 2, "from": "{e : Wₑ est fini}",           "domain": "calculabilité","year": 1944},
    {"s": "COF",  "strate": 2, "from": "{e : Wₑ est cofini}",         "domain": "calculabilité","year": 1944},
    {"s": "REC",  "strate": 2, "from": "{e : Wₑ est récursif}",       "domain": "calculabilité","year": 1944},
    {"s": "∅'",   "strate": 2, "from": "Turing jump premier saut",    "domain": "calculabilité","year": 1939},
    {"s": "∅''",  "strate": 2, "from": "Double saut de Turing",       "domain": "calculabilité","year": 1944},
    {"s": "Δ⁰₂",  "strate": 2, "from": "Intersection Σ⁰₂ ∩ Π⁰₂",    "domain": "calculabilité","year": 1944},
    {"s": "BPP",  "strate": 2, "from": "Bounded-error probabiliste",  "domain": "complexité",  "year": 1977},
    {"s": "IP",   "strate": 2, "from": "Interactive Proof",           "domain": "complexité",  "year": 1985},
    {"s": "SZK",  "strate": 2, "from": "Statistical Zero Knowledge",  "domain": "crypto",      "year": 1986},

    # -----------------------------------------------------------------------
    # STRATE 3 — Σ⁰ₙ · Motif
    # -----------------------------------------------------------------------
    {"s": "Σ⁰ₙ",   "strate": 3, "from": "n-ième existentiel",         "domain": "calculabilité","year": 1944},
    {"s": "Π⁰ₙ",   "strate": 3, "from": "n-ième universel",           "domain": "calculabilité","year": 1944},
    {"s": "Δ⁰ₙ",   "strate": 3, "from": "Intersection Σ⁰ₙ ∩ Π⁰ₙ",    "domain": "calculabilité","year": 1944},
    {"s": "∅⁽ⁿ⁾",  "strate": 3, "from": "n-ième saut de Turing",      "domain": "calculabilité","year": 1944},
    {"s": "ΣₖP",   "strate": 3, "from": "k-ième niveau PH",           "domain": "complexité",  "year": 1977},
    {"s": "ΠₖP",   "strate": 3, "from": "k-ième niveau PH",           "domain": "complexité",  "year": 1977},
    {"s": "PH",    "strate": 3, "from": "Polynomial Hierarchy ∪ₖΣₖP", "domain": "complexité",  "year": 1977},
    {"s": "#P",    "strate": 3, "from": "Comptage — Toda 1991",        "domain": "complexité",  "year": 1979},
    {"s": "MA",    "strate": 3, "from": "Merlin-Arthur",               "domain": "complexité",  "year": 1988},
    {"s": "AM",    "strate": 3, "from": "Arthur-Merlin",               "domain": "complexité",  "year": 1986},
    {"s": "PP",    "strate": 3, "from": "Probabilistic Polynomial",    "domain": "complexité",  "year": 1977},
    {"s": "⊕P",    "strate": 3, "from": "Parité — Parity-P",          "domain": "complexité",  "year": 1986},

    # -----------------------------------------------------------------------
    # STRATE 4 — CIEL · AH
    # -----------------------------------------------------------------------
    {"s": "AH",      "strate": 4, "from": "Hiérarchie arithmétique",    "domain": "calculabilité","year": 1944},
    {"s": "∪ₙ",      "strate": 4, "from": "Union tous niveaux",         "domain": "ensembles",   "year": 1944},
    {"s": "Th(ℕ)",   "strate": 4, "from": "Théorie complète de ℕ",      "domain": "logique",     "year": 1931},
    {"s": "∅⁽ω⁾",    "strate": 4, "from": "ω-ième saut (au-dessus AH)", "domain": "calculabilité","year": 1955},
    {"s": "PSPACE",  "strate": 4, "from": "Espace poly — attracteur",   "domain": "complexité",  "year": 1972},
    {"s": "QIP",     "strate": 4, "from": "Quantum Interactive Proof",   "domain": "quantique",   "year": 2011},
    {"s": "EXPTIME", "strate": 4, "from": "Temps exponentiel",          "domain": "complexité",  "year": 1972},
    {"s": "NEXP",    "strate": 4, "from": "Non-det exponentiel",        "domain": "complexité",  "year": 1972},

    # -----------------------------------------------------------------------
    # STRATE 5 — HYPERARITHMÉTIQUE
    # -----------------------------------------------------------------------
    {"s": "ω₁ᶜᵏ",   "strate": 5, "from": "Ordinal Church-Kleene",      "domain": "ordinaux",    "year": 1938},
    {"s": "∅⁽α⁾",    "strate": 5, "from": "Saut transfinite α",         "domain": "calculabilité","year": 1955},
    {"s": "Δ¹₁",     "strate": 5, "from": "Analytique niveau 1 intersect","domain":"descriptive", "year": 1955},
    {"s": "Σ¹₁",     "strate": 5, "from": "Analytique existentiel",     "domain": "descriptive", "year": 1917},
    {"s": "Π¹₁",     "strate": 5, "from": "Co-analytique",              "domain": "descriptive", "year": 1917},
    {"s": "O",       "strate": 5, "from": "O de Kleene notations ord.", "domain": "calculabilité","year": 1938},
    {"s": "HYP",     "strate": 5, "from": "Ensemble hyperarithmétique", "domain": "calculabilité","year": 1955},
    {"s": "WO",      "strate": 5, "from": "Bons ordres (Π¹₁-complet)", "domain": "descriptive", "year": 1917},

    # -----------------------------------------------------------------------
    # STRATE 6 — PLAFOND · Non-calculable
    # -----------------------------------------------------------------------
    {"s": "∄",     "strate": 6, "from": "N'existe pas (pas d'algo)",    "domain": "calculabilité","year": 1936},
    {"s": "Ω",     "strate": 6, "from": "Constante de Chaitin",         "domain": "information", "year": 1975},
    {"s": "BB",    "strate": 6, "from": "Busy Beaver BB(n)",            "domain": "calculabilité","year": 1962},
    {"s": "⊥",     "strate": 6, "from": "Bottom / indécidable",         "domain": "logique",     "year": 1936},
    {"s": "G",     "strate": 6, "from": "Phrase de Gödel auto-réf.",    "domain": "logique",     "year": 1931},
    {"s": "⊢",     "strate": 6, "from": "Prouvabilité",                 "domain": "logique",     "year": 1879},
    {"s": "⊬",     "strate": 6, "from": "Non-prouvable dans S",         "domain": "logique",     "year": 1931},
    {"s": "K(x)",  "strate": 6, "from": "Complexité de Kolmogorov",     "domain": "information", "year": 1965},
    {"s": "HALT",  "strate": 6, "from": "Problème de l'arrêt",          "domain": "calculabilité","year": 1936},
]


# ============================================================================
# FORMULES CONNUES — liens entre symboles (= mycelium)
# ============================================================================
# Chaque formule est un groupe de symboles qui co-apparaissent.
# Les connexions entre eux forment les arêtes du graphe mycelium.

FORMULES = [
    {"name": "Euler Identity",          "symbols": ["e", "i", "π", "=", "+"],          "year": 1748},
    {"name": "Einstein E=mc²",          "symbols": ["E", "m", "c", "="],               "year": 1905},
    {"name": "Newton F=ma",             "symbols": ["F", "m", "a", "="],               "year": 1687},
    {"name": "Pythagore",               "symbols": ["a²", "b²", "c²", "=", "+"],       "year": -530},
    {"name": "Boltzmann entropy",       "symbols": ["S", "k", "ln", "W", "="],         "year": 1877},
    {"name": "Schrödinger",             "symbols": ["Ĥ", "ψ", "E", "ℏ", "="],         "year": 1926},
    {"name": "Maxwell div B",           "symbols": ["∇·", "B", "="],                   "year": 1865},
    {"name": "Maxwell rot",             "symbols": ["∇×", "B", "E", "∂", "μ₀", "ε₀"], "year": 1865},
    {"name": "Cauchy limit",            "symbols": ["lim", "ε", "δ"],                  "year": 1821},
    {"name": "Integral/derivative",     "symbols": ["∫", "dx", "∂", "lim"],            "year": 1675},
    {"name": "Riemann zeta",            "symbols": ["ζ", "Σ", "∞", "log"],             "year": 1859},
    {"name": "Gamma function",          "symbols": ["Γ", "∫", "e", "∞"],               "year": 1729},
    {"name": "Golden ratio",            "symbols": ["φ", "√", "+"],                    "year": -300},
    {"name": "Set theory basics",       "symbols": ["∈", "∅", "∪", "∩", "⊆"],          "year": 1874},
    {"name": "Number sets chain",       "symbols": ["ℕ", "ℤ", "ℚ", "ℝ", "ℂ", "⊆"],   "year": 1895},
    {"name": "Propositional logic",     "symbols": ["∧", "∨", "¬", "→", "↔"],          "year": 1910},
    {"name": "Lorentz factor",          "symbols": ["γ", "β", "c", "√"],               "year": 1905},
    {"name": "Lambda calculus",         "symbols": ["λ", "→"],                         "year": 1936},
    {"name": "Halting Problem def",     "symbols": ["K", "φₑ", "↓", "∃"],              "year": 1936},
    {"name": "RE / coRE split",         "symbols": ["RE", "coRE", "K", "Wₑ"],          "year": 1936},
    {"name": "Turing reductions",       "symbols": ["≤ₘ", "≤ₜ", "K"],                 "year": 1939},
    {"name": "NP definition",           "symbols": ["NP", "∃", "P"],                   "year": 1971},
    {"name": "Cook-Levin",              "symbols": ["SAT", "NP", "≤ₘ"],                "year": 1971},
    {"name": "Karp 21 problems",        "symbols": ["SAT", "3COL", "TSP", "NP"],       "year": 1972},
    {"name": "Σ⁰₂ definition",          "symbols": ["∃∀", "∀", "TOT", "FIN"],          "year": 1944},
    {"name": "Turing jump chain",       "symbols": ["∅'", "∅''", "K", "∅⁽ⁿ⁾"],         "year": 1939},
    {"name": "Limit lemma",             "symbols": ["Δ⁰₂", "lim", "∅'"],               "year": 1959},
    {"name": "PH structure",            "symbols": ["PH", "ΣₖP", "ΠₖP", "NP", "coNP"],"year": 1977},
    {"name": "Toda theorem",            "symbols": ["PH", "#P", "P"],                  "year": 1991},
    {"name": "IP = PSPACE (Shamir)",    "symbols": ["IP", "PSPACE"],                   "year": 1992},
    {"name": "QIP = PSPACE",            "symbols": ["QIP", "PSPACE", "BQP"],           "year": 2011},
    {"name": "Arthur-Merlin",           "symbols": ["AM", "MA", "IP", "BPP"],          "year": 1986},
    {"name": "Arithmetical Hierarchy",  "symbols": ["AH", "∪ₙ", "Σ⁰ₙ", "Π⁰ₙ", "Δ⁰ₙ"],"year": 1944},
    {"name": "AH ↔ oracle chain",       "symbols": ["AH", "∅⁽ω⁾", "∅⁽ⁿ⁾", "Th(ℕ)"],   "year": 1944},
    {"name": "Hyperarithmetic",         "symbols": ["ω₁ᶜᵏ", "∅⁽α⁾", "O", "HYP"],      "year": 1955},
    {"name": "Analytical hierarchy",    "symbols": ["Σ¹₁", "Π¹₁", "Δ¹₁", "HYP"],      "year": 1917},
    {"name": "Well-ordering",           "symbols": ["WO", "Π¹₁", "ω₁ᶜᵏ"],              "year": 1917},
    {"name": "Gödel incompleteness",    "symbols": ["G", "⊢", "⊬"],                    "year": 1931},
    {"name": "Chaitin Omega",           "symbols": ["Ω", "K(x)", "HALT"],              "year": 1975},
    {"name": "Busy Beaver",             "symbols": ["BB", "∄", "HALT"],                "year": 1962},
    {"name": "Undecidability trio",     "symbols": ["HALT", "⊥", "∄", "G"],            "year": 1936},
    # Cross-strata connections (mycelium vertical!)
    {"name": "P vs NP",                 "symbols": ["P", "NP", "SAT"],                 "year": 1971},
    {"name": "Decidable → RE",          "symbols": ["P", "RE", "K"],                   "year": 1936},
    {"name": "PH collapse",             "symbols": ["PH", "PSPACE", "P", "NP"],        "year": 1977},
    {"name": "Counting power",          "symbols": ["#P", "PH", "PSPACE"],             "year": 1991},
    {"name": "Quantum landscape",       "symbols": ["BQP", "NP", "P", "PSPACE"],       "year": 1993},
    {"name": "Halting → Gödel",         "symbols": ["HALT", "K", "G", "⊬"],            "year": 1936},
    {"name": "Complexity → computability","symbols": ["PSPACE", "AH", "EXPTIME"],       "year": 1972},
]


# ============================================================================
# MOTEUR — Connexions, métriques, analyse
# ============================================================================

class StrateEngine:
    """Moteur de cartographie symboles × strates avec analyse mycelium."""

    def __init__(self):
        self.strates = STRATES
        self.symboles = SYMBOLES
        self.formules = FORMULES

        # Index: symbole → données
        self.sym_index = {}
        for sym in self.symboles:
            self.sym_index[sym["s"]] = sym

        # Graphe d'adjacence (mycelium)
        self.adj = defaultdict(set)
        self.edge_weights = defaultdict(int)  # nombre de co-occurrences
        self.edge_formulas = defaultdict(list)

        self._build_graph()

    def _build_graph(self):
        """Construit le graphe de connexions depuis les formules."""
        for f in self.formules:
            syms = [s for s in f["symbols"] if s in self.sym_index]
            for i, a in enumerate(syms):
                for b in syms[i+1:]:
                    self.adj[a].add(b)
                    self.adj[b].add(a)
                    edge = tuple(sorted([a, b]))
                    self.edge_weights[edge] += 1
                    self.edge_formulas[edge].append(f["name"])

    # ------------------------------------------------------------------
    # Métriques réseau (inspirées du tree engine v2 / Bebber 2007)
    # ------------------------------------------------------------------

    def total_nodes(self):
        return len(self.symboles)

    def total_edges(self):
        return len(self.edge_weights)

    def total_formules(self):
        return len(self.formules)

    def degree(self, sym):
        """Nombre de connexions d'un symbole."""
        return len(self.adj.get(sym, set()))

    def bottleneck_nodes(self, top_n=10):
        """Symboles avec le plus de connexions = bottleneck nodes.
        Équivalent des problèmes NP-complets dans le réseau."""
        degs = [(s["s"], self.degree(s["s"])) for s in self.symboles]
        degs.sort(key=lambda x: -x[1])
        return degs[:top_n]

    def cross_strata_edges(self):
        """Arêtes qui connectent deux strates différentes = mycelium vertical."""
        cross = []
        for edge, weight in self.edge_weights.items():
            a, b = edge
            sa = self.sym_index[a]["strate"]
            sb = self.sym_index[b]["strate"]
            if sa != sb:
                cross.append({
                    "edge": edge,
                    "strates": (sa, sb),
                    "weight": weight,
                    "gap": abs(sa - sb),
                    "formulas": self.edge_formulas[edge]
                })
        cross.sort(key=lambda x: -x["gap"])
        return cross

    def strate_stats(self):
        """Statistiques par strate."""
        stats = []
        for st in self.strates:
            syms = [s for s in self.symboles if s["strate"] == st["id"]]
            internal_edges = 0
            external_edges = 0
            for s in syms:
                for neighbor in self.adj.get(s["s"], set()):
                    ns = self.sym_index.get(neighbor)
                    if ns:
                        if ns["strate"] == st["id"]:
                            internal_edges += 1
                        else:
                            external_edges += 1
            internal_edges //= 2  # chaque arête comptée 2x

            # Domains represented
            domains = set(s["domain"] for s in syms)

            stats.append({
                "strate_id": st["id"],
                "name": st["short"],
                "n_symbols": len(syms),
                "n_internal_edges": internal_edges,
                "n_external_edges": external_edges,
                "n_domains": len(domains),
                "domains": sorted(domains),
                "density": (2 * internal_edges) / (len(syms) * (len(syms)-1)) if len(syms) > 1 else 0,
            })
        return stats

    def meshedness(self):
        """Meshedness du réseau global (Bebber 2007).
        M = (E - N + 1) / (2N - 5) pour graphe planaire.
        On utilise la version simplifiée pour graphe quelconque."""
        n = self.total_nodes()
        e = self.total_edges()
        if n < 3:
            return 0.0
        return (e - n + 1) / (2*n - 5) if (2*n - 5) > 0 else 0.0

    def isolated_symbols(self):
        """Symboles sans aucune connexion = trous potentiels."""
        return [s["s"] for s in self.symboles if self.degree(s["s"]) == 0]

    def trous_analysis(self):
        """Analyse des trous dans la carte.
        Un trou = un domaine sous-représenté ou une strate faiblement connectée."""
        trous = []

        # 1. Strates faiblement connectées à leurs voisines
        stats = self.strate_stats()
        for st in stats:
            if st["n_external_edges"] < st["n_symbols"] * 0.3:
                trous.append({
                    "type": "strate_isolée",
                    "strate": st["name"],
                    "detail": f"Seulement {st['n_external_edges']} liens externes pour {st['n_symbols']} symboles",
                    "severity": "haute" if st["n_external_edges"] < 3 else "moyenne"
                })

        # 2. Domaines présents dans une seule strate
        domain_strates = defaultdict(set)
        for s in self.symboles:
            domain_strates[s["domain"]].add(s["strate"])
        for dom, strats in domain_strates.items():
            if len(strats) == 1 and len([s for s in self.symboles if s["domain"] == dom]) > 2:
                trous.append({
                    "type": "domaine_confiné",
                    "domain": dom,
                    "strate_unique": list(strats)[0],
                    "detail": f"Le domaine '{dom}' n'existe que dans la strate {list(strats)[0]}",
                    "severity": "basse"
                })

        # 3. Symboles isolés
        isolated = self.isolated_symbols()
        if isolated:
            trous.append({
                "type": "symboles_isolés",
                "symbols": isolated,
                "detail": f"{len(isolated)} symboles sans aucune connexion",
                "severity": "haute"
            })

        return trous

    # ------------------------------------------------------------------
    # Distribution spatiale pour le cube
    # ------------------------------------------------------------------

    def distribute_on_plane(self, n, box_w=3.8, box_d=3.8, shrink=0.85):
        """Distribue n points équidistants sur un rectangle."""
        w = box_w * shrink * 0.88
        d = box_d * shrink * 0.88
        if n <= 0:
            return []
        if n == 1:
            return [{"x": 0, "z": 0}]

        aspect = w / d
        best_cols, best_rows, best_waste = 1, n, float('inf')
        for cols in range(1, n + 1):
            rows = math.ceil(n / cols)
            cell_w = w / cols
            cell_d = d / rows
            waste = abs(cell_w / cell_d - aspect) + (cols * rows - n) * 0.1
            if waste < best_waste:
                best_waste = waste
                best_cols = cols
                best_rows = rows

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

    # ------------------------------------------------------------------
    # Export JSON pour le cube HTML
    # ------------------------------------------------------------------

    def export_json(self, path="strates_export.json"):
        """Exporte tout en JSON pour le HTML."""
        data = {
            "meta": {
                "total_symbols": self.total_nodes(),
                "total_edges": self.total_edges(),
                "total_formulas": self.total_formules(),
                "meshedness": round(self.meshedness(), 4),
            },
            "strates": [],
            "edges": [],
        }

        # Strates + symboles positionnés
        for st in self.strates:
            syms = [s for s in self.symboles if s["strate"] == st["id"]]
            positions = self.distribute_on_plane(len(syms))

            sym_data = []
            for i, s in enumerate(syms):
                pos = positions[i] if i < len(positions) else {"x": 0, "z": 0}
                sym_data.append({
                    "s": s["s"],
                    "from": s["from"],
                    "domain": s["domain"],
                    "year": s["year"],
                    "degree": self.degree(s["s"]),
                    "px": pos["x"],
                    "pz": pos["z"],
                })

            data["strates"].append({
                **st,
                "symbols": sym_data,
            })

        # Edges (mycelium connections)
        for edge, weight in self.edge_weights.items():
            a, b = edge
            sa = self.sym_index[a]["strate"]
            sb = self.sym_index[b]["strate"]
            data["edges"].append({
                "a": a, "b": b,
                "weight": weight,
                "strate_a": sa, "strate_b": sb,
                "cross_strata": sa != sb,
                "formulas": self.edge_formulas[edge]
            })

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        return data

    # ------------------------------------------------------------------
    # Rapport console
    # ------------------------------------------------------------------

    def print_report(self):
        """Affiche un rapport complet en console."""
        print("=" * 70)
        print("  P=NP ON S'AMUSE — RAPPORT MOTEUR STRATES")
        print("=" * 70)
        print()
        print(f"  Symboles:   {self.total_nodes()}")
        print(f"  Arêtes:     {self.total_edges()}")
        print(f"  Formules:   {self.total_formules()}")
        print(f"  Meshedness: {self.meshedness():.4f}")
        print()

        print("─" * 70)
        print("  STRATES")
        print("─" * 70)
        for st in self.strate_stats():
            print(f"  [{st['strate_id']}] {st['name']:20s} │ "
                  f"{st['n_symbols']:3d} sym │ "
                  f"{st['n_internal_edges']:3d} int │ "
                  f"{st['n_external_edges']:3d} ext │ "
                  f"d={st['density']:.3f} │ "
                  f"{st['n_domains']} dom")
        print()

        print("─" * 70)
        print("  TOP 15 BOTTLENECK NODES (les SAT du réseau)")
        print("─" * 70)
        for sym, deg in self.bottleneck_nodes(15):
            st = self.sym_index[sym]["strate"]
            fr = self.sym_index[sym]["from"]
            print(f"  {sym:8s} │ degré {deg:3d} │ strate {st} │ {fr}")
        print()

        print("─" * 70)
        print("  MYCELIUM VERTICAL (connexions cross-strata, top 15)")
        print("─" * 70)
        for cx in self.cross_strata_edges()[:15]:
            a, b = cx["edge"]
            print(f"  {a:8s} ↔ {b:8s} │ strates {cx['strates'][0]}→{cx['strates'][1]} │ "
                  f"gap={cx['gap']} │ {', '.join(cx['formulas'][:2])}")
        print()

        print("─" * 70)
        print("  TROUS DANS LA CARTE")
        print("─" * 70)
        trous = self.trous_analysis()
        if not trous:
            print("  Aucun trou détecté.")
        for t in trous:
            sev = {"haute": "🔴", "moyenne": "🟡", "basse": "🟢"}
            print(f"  {sev.get(t['severity'], '?')} [{t['type']}] {t['detail']}")
        print()

        # Symboles isolés
        isolated = self.isolated_symbols()
        if isolated:
            print("─" * 70)
            print(f"  SYMBOLES ISOLÉS ({len(isolated)})")
            print("─" * 70)
            for s in isolated:
                info = self.sym_index[s]
                print(f"  {s:8s} │ strate {info['strate']} │ {info['from']}")
            print()

        print("=" * 70)
        print("  Carte prête. Les trous montrent où chercher.")
        print("=" * 70)


# ============================================================================
# MAIN
# ============================================================================

def main():
    engine = StrateEngine()

    # Toujours exporter le JSON
    out_path = Path(__file__).parent / "strates_export.json"
    data = engine.export_json(str(out_path))
    print(f"\n✅ JSON exporté → {out_path}")
    print(f"   {data['meta']['total_symbols']} symboles, "
          f"{data['meta']['total_edges']} arêtes, "
          f"meshedness={data['meta']['meshedness']}")

    if "--analyse" in sys.argv or len(sys.argv) == 1:
        print()
        engine.print_report()

    if "--html" in sys.argv:
        html_path = Path(__file__).parent / "strates_cube_live.html"
        generate_html(data, str(html_path))
        print(f"\n✅ HTML exporté → {html_path}")


def generate_html(data, path):
    """Génère le HTML autonome avec les données injectées."""
    json_str = json.dumps(data, ensure_ascii=False)
    html = HTML_TEMPLATE.replace("__DATA_INJECT__", json_str)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)


# ============================================================================
# HTML TEMPLATE (autonome, données injectées)
# ============================================================================

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>P=NP — Strates × Symboles × Mycelium</title>
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;700&family=Instrument+Serif:ital@0;1&display=swap');
*{margin:0;padding:0;box-sizing:border-box}
body{background:#08080d;color:#c8ccd4;font-family:'JetBrains Mono',monospace;overflow:hidden;height:100vh;width:100vw}
canvas{display:block;position:fixed;top:0;left:0;z-index:1}
body::after{content:'';position:fixed;top:0;left:0;right:0;bottom:0;background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.02'/%3E%3C/svg%3E");pointer-events:none;z-index:2}
#hud{position:fixed;top:18px;left:22px;z-index:10;pointer-events:none}
#hud h1{font-family:'Instrument Serif',serif;font-size:24px;font-weight:400;color:#e8e8f0;margin-bottom:2px}
#hud .sub{font-size:9px;color:#3a3a4a;letter-spacing:2.5px;text-transform:uppercase}
#hud .meta{font-size:9px;color:#334;margin-top:8px;line-height:1.7}
#info{position:fixed;bottom:24px;left:24px;z-index:10;pointer-events:none;max-width:520px}
#info .sn{font-family:'Instrument Serif',serif;font-size:19px;color:#fff;margin-bottom:2px;transition:color 0.3s}
#info .sf{font-size:12px;color:#8af;margin-bottom:5px}
#info .sd{font-size:10.5px;color:#445;line-height:1.5}
#info .sl{font-size:9.5px;color:#445;margin-top:6px;line-height:1.6}
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
#toggle-myc{position:fixed;top:18px;right:20px;z-index:10;font-size:9px;color:#445;cursor:pointer;padding:4px 10px;border:1px solid #222;border-radius:3px;background:rgba(0,0,0,0.3);transition:all 0.2s}
#toggle-myc:hover{border-color:#555;color:#889}
#toggle-myc.on{border-color:rgba(140,100,255,0.4);color:rgba(140,100,255,0.7)}
</style>
</head>
<body>
<canvas id="c"></canvas>
<div id="hud">
  <h1>Symboles × Strates × Mycelium</h1>
  <div class="sub">Chaque symbole mathématique · placé où il vit · connecté par les formules</div>
  <div class="meta" id="meta"></div>
</div>
<div id="info">
  <div class="sn" id="sn">— Survole une strate —</div>
  <div class="sf" id="sf"></div>
  <div class="sd" id="sd"></div>
  <div class="sl" id="sl"></div>
</div>
<div id="legend"></div>
<div id="toggle-myc" onclick="toggleMyc()">MYCELIUM</div>
<div id="hint"><kbd>drag</kbd> rotation · <kbd>scroll</kbd> zoom · <kbd>légende</kbd> focus · <kbd>mycelium</kbd> connexions</div>
<script>
const DATA = __DATA_INJECT__;
const ST = DATA.strates;
const EDGES = DATA.edges;

const cv=document.getElementById('c');const ctx=cv.getContext('2d');
let W,H;function resize(){W=cv.width=innerWidth;H=cv.height=innerHeight}resize();addEventListener('resize',resize);

const BOX={w:3.8,h:3.8,d:3.8};const CAM={dist:7.0,scale:420,persp:0.18};const SHRINK=0.85;
let yaw=0,yawSpd=0.006,tiltX=-0.32,activeS=-1,showMyc=false,zoom=1.0;
let dragging=false,pm={x:0,y:0},autoRot=true,autoT=null,mouseX=0,mouseY=0;

cv.addEventListener('mousedown',e=>{dragging=true;pm={x:e.clientX,y:e.clientY};autoRot=false;clearTimeout(autoT)});
addEventListener('mousemove',e=>{mouseX=e.clientX;mouseY=e.clientY;if(!dragging)return;yaw+=(e.clientX-pm.x)*0.005;tiltX+=(e.clientY-pm.y)*0.004;tiltX=Math.max(-1.3,Math.min(1.3,tiltX));pm={x:e.clientX,y:e.clientY}});
addEventListener('mouseup',()=>{dragging=false;autoT=setTimeout(()=>autoRot=true,3000)});
cv.addEventListener('wheel',e=>{e.preventDefault();zoom*=e.deltaY>0?0.95:1.05;zoom=Math.max(0.35,Math.min(2.8,zoom))},{passive:false});
cv.addEventListener('touchstart',e=>{if(e.touches.length===1){dragging=true;pm={x:e.touches[0].clientX,y:e.touches[0].clientY};autoRot=false;clearTimeout(autoT)}});
cv.addEventListener('touchmove',e=>{if(!dragging||e.touches.length!==1)return;e.preventDefault();yaw+=(e.touches[0].clientX-pm.x)*0.005;tiltX+=(e.touches[0].clientY-pm.y)*0.004;tiltX=Math.max(-1.3,Math.min(1.3,tiltX));pm={x:e.touches[0].clientX,y:e.touches[0].clientY}},{passive:false});
cv.addEventListener('touchend',()=>{dragging=false;autoT=setTimeout(()=>autoRot=true,3000)});

function project(x,y,z){
  const cy=Math.cos(yaw),sy=Math.sin(yaw),x1=x*cy+z*sy,z1=-x*sy+z*cy;
  const cx=Math.cos(tiltX),sx=Math.sin(tiltX),y2=y*cx-z1*sx,z2=y*sx+z1*cx;
  const sc=CAM.scale*zoom,den=Math.max(0.001,CAM.dist-z2),pf=sc/den,of=sc/CAM.dist,f=of+(pf-of)*CAM.persp;
  return{x:x1*f+W/2,y:-y2*f+H/2,z:z2,f};
}
function rgba(c,a){return`rgba(${c[0]},${c[1]},${c[2]},${a})`}
const CUBE_EDGES=[[0,1],[1,2],[2,3],[3,0],[4,5],[5,6],[6,7],[7,4],[0,4],[1,5],[2,6],[3,7]];
function boxVerts(){const h=BOX.w/2,hy=BOX.h/2,hz=BOX.d/2;return[[-h,-hy,-hz],[h,-hy,-hz],[h,hy,-hz],[-h,hy,-hz],[-h,-hy,hz],[h,-hy,hz],[h,hy,hz],[-h,hy,hz]]}

// Build symbol position lookup
const symPos={};
ST.forEach(st=>{
  st.symbols.forEach(sym=>{
    const y=st.yr*BOX.h;
    symPos[sym.s]={x:sym.px, y, z:sym.pz, strate:st.id, col:st.color};
  });
});

// Meta
document.getElementById('meta').innerHTML=
  `${DATA.meta.total_symbols} symboles · ${DATA.meta.total_edges} arêtes · ${DATA.meta.total_formulas} formules · meshedness ${DATA.meta.meshedness}`;

// Legend
const legEl=document.getElementById('legend');
ST.forEach((s,i)=>{
  const d=document.createElement('div');d.className='li';
  d.innerHTML=`<div class="ld" style="color:rgb(${s.color});background:rgb(${s.color})"></div><div class="ll">${s.short}</div><div class="lc">${s.symbols.length}</div>`;
  d.addEventListener('click',()=>{activeS=activeS===i?-1:i;document.querySelectorAll('.li').forEach((el,j)=>el.classList.toggle('act',j===activeS));if(activeS>=0)showInfo(activeS)});
  d.addEventListener('mouseenter',()=>showInfo(i));
  legEl.appendChild(d);
});

function showInfo(i){
  const s=ST[i];
  document.getElementById('sn').textContent=s.name;
  document.getElementById('sn').style.color=`rgb(${s.color})`;
  document.getElementById('sf').textContent=s.formula;
  document.getElementById('sd').textContent=s.desc;
  document.getElementById('sl').textContent=`[${s.symbols.length} symboles]  ${s.symbols.map(x=>x.s).join('  ')}`;
}

function toggleMyc(){showMyc=!showMyc;document.getElementById('toggle-myc').classList.toggle('on',showMyc)}

function frame(){
  requestAnimationFrame(frame);
  ctx.clearRect(0,0,W,H);
  const gr=ctx.createRadialGradient(W/2,H/2,0,W/2,H/2,W*0.7);
  gr.addColorStop(0,'#0d0d14');gr.addColorStop(1,'#050508');
  ctx.fillStyle=gr;ctx.fillRect(0,0,W,H);
  if(autoRot)yaw+=yawSpd;

  const items=[];

  // Strate planes
  ST.forEach((st,si)=>{
    const y=st.yr*BOX.h;
    const sh=SHRINK,hw=BOX.w*sh/2,hd=BOX.d*sh/2;
    const qv=[[-hw,y,-hd],[hw,y,-hd],[hw,y,hd],[-hw,y,hd]];
    const pq=qv.map(v=>project(v[0],v[1],v[2]));
    const avgZ=pq.reduce((a,p)=>a+p.z,0)/4;
    let op=st.opacity,bop=0.5;
    if(activeS>=0){if(si===activeS){op=0.35;bop=0.9}else{op=0.02;bop=0.06}}
    items.push({type:'plane',z:avgZ-0.01,si,pts:pq,col:st.color,op,bop});

    // Symbols
    st.symbols.forEach(sym=>{
      const pp=project(sym.px,y,sym.pz);
      let sop=0.85;if(activeS>=0){sop=si===activeS?1.0:0.06}
      items.push({type:'sym',z:pp.z,si,sym,px:pp.x,py:pp.y,pf:pp.f,col:st.color,sop,deg:sym.degree});
    });
  });

  items.sort((a,b)=>a.z-b.z);

  let nearSym=null,nearD=22;

  items.forEach(it=>{
    if(it.type==='plane'){
      ctx.beginPath();ctx.moveTo(it.pts[0].x,it.pts[0].y);
      for(let i=1;i<4;i++)ctx.lineTo(it.pts[i].x,it.pts[i].y);
      ctx.closePath();ctx.fillStyle=rgba(it.col,it.op);ctx.fill();
      ctx.strokeStyle=rgba(it.col,it.bop);ctx.lineWidth=1.2;ctx.stroke();
    }
    if(it.type==='sym'){
      const bs=Math.max(7,Math.min(14,9*(it.pf/(CAM.scale*zoom/CAM.dist))));
      // Scale by degree (more connected = slightly bigger)
      const degScale = 1 + Math.min(it.deg * 0.02, 0.4);
      ctx.font=`600 ${bs*degScale}px "JetBrains Mono",monospace`;
      ctx.textAlign='center';ctx.textBaseline='middle';
      const dx=mouseX-it.px,dy=mouseY-it.py,dist=Math.sqrt(dx*dx+dy*dy);
      if(dist<20&&dist<nearD){nearD=dist;nearSym=it}
      if(dist<20){ctx.shadowColor=`rgb(${it.col})`;ctx.shadowBlur=14}
      ctx.fillStyle=rgba(it.col,it.sop);ctx.fillText(it.sym.s,it.px,it.py);
      ctx.shadowBlur=0;
    }
  });

  // Mycelium edges
  if(showMyc){
    EDGES.forEach(e=>{
      const a=symPos[e.a],b=symPos[e.b];
      if(!a||!b)return;
      if(activeS>=0&&a.strate!==activeS&&b.strate!==activeS)return;
      const pa=project(a.x,a.y,a.z),pb=project(b.x,b.y,b.z);
      const isCross=e.cross_strata;
      ctx.beginPath();ctx.moveTo(pa.x,pa.y);
      // Curved line for cross-strata
      if(isCross){
        const mx=(pa.x+pb.x)/2+Math.sin(yaw*2)*15,my=(pa.y+pb.y)/2;
        ctx.quadraticCurveTo(mx,my,pb.x,pb.y);
      }else{ctx.lineTo(pb.x,pb.y)}
      ctx.strokeStyle=isCross?'rgba(180,100,255,0.12)':'rgba(100,180,100,0.06)';
      ctx.lineWidth=Math.min(e.weight*0.6,2.5);ctx.stroke();
    });
  }

  // Tooltip
  if(nearSym){
    const s=nearSym;const tx=s.px+16,ty=s.py-14;
    ctx.font='500 10px "JetBrains Mono",monospace';
    const txt=`${s.sym.s} ← ${s.sym.from} [deg:${s.sym.degree}]`;
    const m=ctx.measureText(txt);
    ctx.fillStyle='rgba(0,0,0,0.8)';ctx.fillRect(tx-4,ty-10,m.width+8,16);
    ctx.strokeStyle=rgba(s.col,0.4);ctx.lineWidth=0.8;ctx.strokeRect(tx-4,ty-10,m.width+8,16);
    ctx.fillStyle=rgba(s.col,0.9);ctx.textAlign='left';ctx.textBaseline='middle';ctx.fillText(txt,tx,ty-2);
  }

  // Cube wireframe
  const bv=boxVerts(),pv=bv.map(v=>project(v[0],v[1],v[2]));
  CUBE_EDGES.forEach(e=>{
    ctx.beginPath();ctx.moveTo(pv[e[0]].x,pv[e[0]].y);ctx.lineTo(pv[e[1]].x,pv[e[1]].y);
    ctx.strokeStyle='rgba(60,200,100,0.35)';ctx.lineWidth=1.8;ctx.stroke();
  });
  pv.forEach(p=>{ctx.beginPath();ctx.arc(p.x,p.y,2,0,Math.PI*2);ctx.fillStyle='rgba(74,222,128,0.3)';ctx.fill()});

  // Labels
  const bot=project(0,-BOX.h/2-0.35,0),top2=project(0,BOX.h/2+0.35,0);
  ctx.font='500 9px "JetBrains Mono",monospace';ctx.textAlign='center';
  ctx.fillStyle='rgba(74,222,128,0.35)';ctx.fillText('▼ PLANCHER — Axiomes',bot.x,bot.y);
  ctx.fillStyle='rgba(239,68,68,0.35)';ctx.fillText('▲ PLAFOND — Turing 1936',top2.x,top2.y);

  ctx.font='400 9px "JetBrains Mono",monospace';ctx.textAlign='left';
  ctx.fillStyle='rgba(80,80,100,0.3)';
  ctx.fillText(`${DATA.meta.total_symbols} sym · ${DATA.meta.total_edges} edges · mesh=${DATA.meta.meshedness}`,12,H-14);
}
showInfo(0);frame();
</script>
</body>
</html>"""


if __name__ == "__main__":
    main()
