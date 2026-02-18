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

    # --- ENSEMBLES DE NOMBRES ---

    # --- CONSTANTES FONDAMENTALES ---

    # --- CONSTANTES PHYSIQUES ---

    # --- THÉORIE DES ENSEMBLES ---

    # --- LOGIQUE PROPOSITIONNELLE & PRÉDICATS ---

    # --- ANALYSE / CALCUL ---

    # --- FONCTIONS SPÉCIALES ---

    # --- ALGÈBRE LINÉAIRE ---

    # --- ALGÈBRE ABSTRAITE ---

    # --- THÉORIE DES CATÉGORIES ---

    # --- TOPOLOGIE ---

    # --- GÉOMÉTRIE DIFFÉRENTIELLE ---

    # --- THÉORIE DES NOMBRES ---

    # --- PROBABILITÉS & STATISTIQUES ---

    # --- THÉORIE DE L'INFORMATION ---

    # --- PHYSIQUE CLASSIQUE ---

    # --- LAGRANGIEN / HAMILTONIEN CLASSIQUE ---

    # --- ÉLECTROMAGNÉTISME ---

    # --- THERMODYNAMIQUE ---

    # --- RELATIVITÉ ---

    # --- MÉCANIQUE QUANTIQUE ---

    # --- QFT / MODÈLE STANDARD ---

    # --- NAVIER-STOKES / FLUIDES ---

    # --- CHIMIE ---

    # --- ÉLÉMENTS FORMULES CÉLÈBRES ---

    # --- COMPLEXITÉ (décidable) ---

    # --- CRYPTOGRAPHIE ---

    # --- GÉOMÉTRIE EUCLIDIENNE / REPÈRES ---

    # --- TRANSFORMÉES & TRAITEMENT DU SIGNAL ---

    # --- ÉQUATIONS DIFFÉRENTIELLES ---

    # --- BIOLOGIE & GÉNÉTIQUE ---

    # --- ÉCONOMIE & THÉORIE DES JEUX ---

    # --- MACHINE LEARNING / IA ---

    # --- PHYSIQUE NUCLÉAIRE & PARTICULES ---

    # --- OPTIQUE ---

    # --- ASTRONOMIE / COSMOLOGIE ---

    # --- THÉORIE DU CONTRÔLE ---

    # --- AUTOMATES & LANGAGES FORMELS ---

    # --- Théorie de la mesure (Lebesgue 1902) ---

    # --- Calcul stochastique ---

    # --- Optimisation ---

    # --- Analyse fonctionnelle ---
    # STRATE 1 — Σ⁰₁ · Récursivement énumérable
    # ==================================================================

    # ==================================================================
    # STRATE 2 — Σ⁰₂ · Limite
    # ==================================================================

    # ==================================================================
    # STRATE 3 — Σ⁰ₙ · Motif
    # ==================================================================

    # ==================================================================
    # STRATE 4 — CIEL · AH
    # ==================================================================

    # ==================================================================
    # STRATE 5 — HYPERARITHMÉTIQUE
    # ==================================================================

    # ==================================================================
    # STRATE 6 — PLAFOND · Non-calculable
    # ==================================================================

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
    {"s": "Artin_prim","strate": 0, "from": "Conjecture Artin racine primitive (1927) — tout non-carré est racine primitive mod p pour inf. primes. Hooley 1967: conditionnel GRH.", "domain": "nb théorie", "status": "conjecture"},
    {"s": "Selberg_ev","strate": 0, "from": "Conjecture Selberg valeur propre (1965) — λ₁ ≥ 1/4 pour Γ(N) congruence. Selberg: ≥3/16. Kim-Sarnak 2003: ≥975/4096≈0.238. Impliquée par Ramanujan généralisée.", "domain": "nb théorie", "status": "conjecture"},
    {"s": "GenRam","strate": 0, "from": "Conjecture Ramanujan généralisée — paramètres Satake tempérés pour formes automorphes cuspidales GL_n. Deligne: prouvée GL_2 holomorphe. Ouverte Maass forms et GL_n, n>2. Implique Selberg.", "domain": "nb théorie", "status": "conjecture"},

    # --- Strate 0 : géométrie algébrique / motivique ---
    {"s": "BeilSoule","strate": 0, "from": "Conjecture Beilinson-Soulé (vanishing) — H^p_mot(X,ℤ(q))=0 pour p<0, q≥0. Connue corps finis. Centrale théorie motivique, t-structure sur motifs.", "domain": "géom algébrique", "status": "conjecture"},

    # ═══════════════════════════════════════════════════════════════
    #  RATISSAGE PASS 4 — PROUVÉS récents majeurs
    # ═══════════════════════════════════════════════════════════════

    # --- Prouvés : K-théorie / cohomologie motivique ---

    # --- Prouvés : représentations / Langlands ---
    {"s": "GeomLang","strate": 3, "from": "Conjecture géométrique Langlands catégorique (unramified) — Gaitsgory-Raskin et al. 2024. 800+ pages, 5 papers, 9 auteurs. 30 ans de travail. Hecke eigensheaves.", "domain": "géom algébrique"},

    # --- Prouvés : EDP / fluides ---

    # ═══════════════════════════════════════════════════════════════
    #  RATISSAGE PASS 4 — batch 2 : convexe, birationnel, prouvés majeurs
    # ═══════════════════════════════════════════════════════════════

    # --- Strate 0 : géométrie convexe ---
    {"s": "Mahler_vol","strate": 0, "from": "Conjecture Mahler (1939) — produit volumique |K||K°| minimisé par hypercubes (sym) ou simplexes (non-sym). Prouvée n=2 (Mahler), n=3 (Iriyeh-Shibata 2020). Hanner polytopes = minima locaux.", "domain": "géométrie", "status": "conjecture"},

    # --- Strate 0 : géométrie algébrique / birationnelle ---
    {"s": "Abundance","strate": 0, "from": "Abundance conjecture (MMP) — K_X nef ⟹ K_X semi-ample. Prouvée dim ≤ 3. Compléterait classification birationnelle. Birkar-Cascini-Hacon-McKernan 2010 (cas log general type).", "domain": "géom algébrique", "status": "conjecture"},

    # --- Prouvés : analyse fonctionnelle / combinatoire ---

    # --- Prouvés : théorie des nombres ---

    # --- Prouvés : topologie 3-variétés ---

    # --- Prouvés : combinatoire algébrique ---

    # ═══════════════════════════════════════════════════════════════
    #  RATISSAGE PASS 5 — grands théorèmes prouvés XXe-XXIe siècle
    # ═══════════════════════════════════════════════════════════════

    # --- Topologie : résolus ---

    # --- Théorie des nombres : résolus ---

    # --- Algèbre : résolus ---

    # --- Analyse : résolus ---

    # --- Géométrie diff / géométrie : résolus ---

    # --- Combinatoire : résolus ---

    # --- Probabilités : résolus ---

    # --- Logique : résolus ---

    # ═══════════════════════════════════════════════════════════════
    #  RATISSAGE PASS 5 vague 2 — grands théorèmes manquants
    # ═══════════════════════════════════════════════════════════════

    # ═══════════════════════════════════════════════════════════════
    #  RATISSAGE PASS 5 vague 3 — classiques + percées récentes
    # ═══════════════════════════════════════════════════════════════

    # Théorie des nombres classique

    # Géométrie / empilement
    {"s": "Kakeya3D", "strate": 3, "from": "Kakeya 3D — ensemble Kakeya ℝ³ dim Hausdorff = 3 (Wang-Zahl 2025, preprint). 'Once in a century'.", "domain": "géométrie"},

    # Algèbre

    # Géom diff / dynamique
    {"s": "Zimmer",   "strate": 3, "from": "Conjecture Zimmer — actions réseaux rang ≥ 2 triviales en petite dim (Brown-Fisher-Hurtado 2017).", "domain": "géom diff"},

    # Combinatoire

    # --- Sync vagues 4+5 depuis C1 ---

    # Barrières complexité

    # Circuit lower bounds

    # Quantique

    # Probabilités

    # EDP / Géom diff / Mécanique

    # Topologie

    # Analyse / Géom algébrique

    # Nb théorie / Logique / Algèbre

    # Descriptive / Ensembles

    # Automates

    # Stochastique / Analyse fonctionnelle
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
