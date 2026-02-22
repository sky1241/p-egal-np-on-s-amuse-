"""
TEST YGGDRASIL × 5 PATTERNS — Appliquer les 20 patterns de découverte
aux 794 symboles mathématiques sur l'axe central Yggdrasil.

Question: La structure de la carte des symboles mathématiques
reproduit-elle les mêmes patterns de "vide fertile" que les
20 cas historiques de découvertes scientifiques ?

Sky × Claude — 18 Février 2026
"""
import re
from pathlib import Path
import json
from collections import defaultdict, Counter
from itertools import combinations

# ============================================================================
# 1. CHARGER LES SYMBOLES
# ============================================================================
def load_symbols(filename):
    with open(filename) as f:
        code = f.read()
    syms = re.findall(r'"s":\s*"([^"]+)"', code)
    strates = re.findall(r'"strate":\s*(\d+)', code)
    domains = re.findall(r'"domain":\s*"([^"]+)"', code)
    froms = re.findall(r'"from":\s*"([^"]+)"', code)
    return [{"s": syms[i], "strate": int(strates[i]), "domain": domains[i], 
             "from": froms[i] if i < len(froms) else ""}
            for i in range(len(syms))]

c1 = load_symbols(str(Path(__file__).parent.parent / "engine" / "engine.py"))
c2 = load_symbols(str(Path(__file__).parent.parent / "engine" / "engine_carre2.py"))
print(f"C1 (prouvés): {len(c1)} symboles")
print(f"C2 (conjectures): {len(c2)} symboles")
print(f"TOTAL: {len(c1)+len(c2)} symboles\n")

# ============================================================================
# 2. YGGDRASIL — CENTRES PAR STRATE
# ============================================================================
YGGDRASIL = {
    0: {"centre": "= (degré 0)", "ref": "Kleene-Post 1954"},
    1: {"centre": "K (halting)", "ref": "Post 1944 Σ₁-complet"},
    2: {"centre": "FIN = ∅''", "ref": "Post 1944 Σ₂-complet"},
    3: {"centre": "COF / ∅⁽ⁿ⁾", "ref": "Post 1944 Σₙ-complet"},
    4: {"centre": "∅⁽ω⁾ = Th(ℕ)", "ref": "Davis 1950"},
    5: {"centre": "Kleene O", "ref": "Kleene 1955 Π₁₁-complet"},
    6: {"centre": "AUCUN (incomparable)", "ref": "Kleene-Post 1954"},
}
print("=" * 70)
print("YGGDRASIL — COLONNE VERTÉBRALE")
print("=" * 70)
for s, info in YGGDRASIL.items():
    count_c1 = sum(1 for sym in c1 if sym["strate"] == s)
    count_c2 = sum(1 for sym in c2 if sym["strate"] == s)
    print(f"  S{s}: {info['centre']:20s} | C1:{count_c1:3d} C2:{count_c2:3d} | {info['ref']}")

# ============================================================================
# 3. MATRICE DOMAINE × DOMAINE (CO-OCCURRENCE PAR STRATE)
# ============================================================================
print("\n" + "=" * 70)
print("MATRICE DE CO-OCCURRENCE DOMAINE × STRATE")
print("=" * 70)

# Construire: pour chaque strate, quels domaines sont présents ?
strate_domains = defaultdict(lambda: defaultdict(int))
for sym in c1:
    strate_domains[sym["strate"]][sym["domain"]] += 1

# Pour chaque paire de domaines: combien de strates les connectent ?
all_domains = sorted(set(s["domain"] for s in c1))
domain_size = Counter(s["domain"] for s in c1)

# Matrice de co-présence: deux domaines sont "connectés" s'ils partagent ≥1 strate
domain_strate_sets = defaultdict(set)
for sym in c1:
    domain_strate_sets[sym["domain"]].add(sym["strate"])

# Paires de domaines avec ZERO strate commune
zero_pairs = []
connected_pairs = []
for d1, d2 in combinations(all_domains, 2):
    shared = domain_strate_sets[d1] & domain_strate_sets[d2]
    if len(shared) == 0:
        zero_pairs.append((d1, d2, domain_size[d1], domain_size[d2]))
    else:
        connected_pairs.append((d1, d2, len(shared), domain_size[d1], domain_size[d2]))

print(f"\nDomaines: {len(all_domains)}")
print(f"Paires possibles: {len(all_domains) * (len(all_domains)-1) // 2}")
print(f"Paires connectées (≥1 strate commune): {len(connected_pairs)}")
print(f"Paires DÉCONNECTÉES (0 strate commune): {len(zero_pairs)}")

# ============================================================================
# 4. PATTERN 1 — PONT (vide fertile entre domaines actifs)
# ============================================================================
print("\n" + "=" * 70)
print("PATTERN 1: PONT — Domaines actifs mais déconnectés")
print("  = Fermat, CRISPR, Immunothérapie, AlphaFold, Isolants topo")
print("  Signal: 2 domaines avec beaucoup de symboles, 0 strate commune")
print("=" * 70)

# Trier par taille combinée (les plus gros domaines déconnectés = plus gros trous)
zero_pairs.sort(key=lambda x: -(x[2] + x[3]))
print(f"\nTop 20 'vides fertiles' (gros domaines sans lien):")
print(f"{'Domaine A':20s} {'|A|':>4s}  {'Domaine B':20s} {'|B|':>4s}  {'Σ':>4s}")
print("-" * 60)
for d1, d2, s1, s2 in zero_pairs[:20]:
    print(f"{d1:20s} {s1:4d}  {d2:20s} {s2:4d}  {s1+s2:4d}")

# ============================================================================
# 5. PATTERN 2 — DENSE (domaine auto-suffisant)
# ============================================================================
print("\n" + "=" * 70)
print("PATTERN 2: DENSE — Domaines avec couverture multi-strate")
print("  = Groupes finis (dense, pas besoin de pont)")
print("  Signal: domaine présent à ≥3 strates différentes")
print("=" * 70)

dense = [(d, len(strates), domain_size[d]) 
         for d, strates in domain_strate_sets.items() if len(strates) >= 3]
dense.sort(key=lambda x: -x[1])
print(f"\n{'Domaine':20s} {'Strates':>8s} {'Symboles':>9s}  Couverture")
print("-" * 65)
for d, ns, sz in dense:
    coverage = sorted(domain_strate_sets[d])
    print(f"{d:20s} {ns:8d} {sz:9d}  S{coverage}")

# ============================================================================
# 6. PATTERN 3 — THÉORIE × OUTIL (asymétrie strate)
# ============================================================================
print("\n" + "=" * 70)
print("PATTERN 3: THÉORIE × OUTIL — Un domaine haut, l'autre bas")
print("  = Higgs (théorie dense S0, trou expérimental)")  
print("  Signal: domaine A principalement S0, domaine B principalement S3+")
print("=" * 70)

# Calculer le "centre de gravité" de chaque domaine sur l'axe Yggdrasil
domain_gravity = {}
for d in all_domains:
    syms_d = [s for s in c1 if s["domain"] == d]
    if syms_d:
        avg = sum(s["strate"] for s in syms_d) / len(syms_d)
        domain_gravity[d] = avg

# Trouver les paires avec la plus grande différence de gravité
asym_pairs = []
for d1, d2 in combinations(all_domains, 2):
    if domain_size[d1] >= 5 and domain_size[d2] >= 5:
        diff = abs(domain_gravity[d1] - domain_gravity[d2])
        shared = domain_strate_sets[d1] & domain_strate_sets[d2]
        if diff > 1.0:  # Au moins 1 strate d'écart en moyenne
            asym_pairs.append((d1, d2, domain_gravity[d1], domain_gravity[d2], diff, len(shared)))

asym_pairs.sort(key=lambda x: -x[4])
print(f"\n{'Domaine A':20s} {'Grav A':>7s}  {'Domaine B':20s} {'Grav B':>7s} {'Δ':>5s} {'Lien':>4s}")
print("-" * 70)
for d1, d2, g1, g2, diff, shared in asym_pairs[:15]:
    label = "🔴" if shared == 0 else f"S×{shared}"
    print(f"{d1:20s} {g1:7.2f}  {d2:20s} {g2:7.2f} {diff:5.2f} {label}")

# ============================================================================
# 7. PATTERN 4 — TROU OUVERT (C2 pont entre C1 domaines)
# ============================================================================
print("\n" + "=" * 70)
print("PATTERN 4: TROU OUVERT — Conjectures C2 qui ponteraient des domaines C1")
print("  = Dark matter↔QG, Fusion TOK↔HTS, Quantum↔Crypto")
print("  Signal: symbole C2 dont le domaine est absent de C1 à cette strate")
print("=" * 70)

# Domaines de C2 qui n'existent PAS dans C1
c1_domains = set(s["domain"] for s in c1)
c2_domains = set(s["domain"] for s in c2)
c2_only = c2_domains - c1_domains
print(f"\nDomaines UNIQUEMENT dans C2 (conjectures): {len(c2_only)}")
for d in sorted(c2_only):
    syms = [s["s"] for s in c2 if s["domain"] == d]
    print(f"  {d}: {syms[:5]}...")

# Domaines partagés mais avec symboles C2 à des strates absentes de C1
print(f"\nConjectures C2 qui combleraient un trou de strate:")
c1_domain_strate = defaultdict(set)
for s in c1:
    c1_domain_strate[s["domain"]].add(s["strate"])

bridge_candidates = []
for sym in c2:
    d, st = sym["domain"], sym["strate"]
    if d in c1_domain_strate and st not in c1_domain_strate[d]:
        bridge_candidates.append(sym)

print(f"  {len(bridge_candidates)} symboles C2 à des strates manquantes de leur domaine dans C1")
for sym in bridge_candidates[:15]:
    print(f"  → {sym['s']:15s} domaine={sym['domain']:20s} strate={sym['strate']} ({sym['from'][:50]})")

# ============================================================================
# 8. DELTA C1↔C2 — LA CARTE DES DÉCOUVERTES
# ============================================================================
print("\n" + "=" * 70)
print("DELTA C1↔C2 — OÙ LES CONJECTURES CRÉENT DES PONTS")
print("=" * 70)

# Pour chaque paire de domaines déconnectée dans C1,
# est-ce qu'un symbole C2 les connecterait ?
c2_domain_strate = defaultdict(set)
for s in c2:
    c2_domain_strate[s["domain"]].add(s["strate"])

# Domaines qui deviennent connectés si on ajoute C2
new_connections = 0
for d1, d2, s1, s2 in zero_pairs:
    # Est-ce que C2 ajoute des strates à d1 ou d2 qui les feraient se connecter ?
    d1_full = domain_strate_sets[d1] | c2_domain_strate.get(d1, set())
    d2_full = domain_strate_sets[d2] | c2_domain_strate.get(d2, set())
    if d1_full & d2_full:
        new_connections += 1
        if new_connections <= 10:
            shared_new = d1_full & d2_full
            print(f"  PONT C2: {d1} ↔ {d2} via strate(s) {shared_new}")

print(f"\nPaires déconnectées C1: {len(zero_pairs)}")
print(f"Paires connectées si on ajoute C2: {new_connections}")
print(f"Paires ENCORE déconnectées: {len(zero_pairs) - new_connections}")

# ============================================================================
# 9. RÉSUMÉ FINAL — MAPPING 20 TESTS → SYMBOLES
# ============================================================================
print("\n" + "=" * 70)
print("MAPPING DES 20 TESTS HISTORIQUES → DOMAINES SYMBOLES")
print("=" * 70)

test_mapping = [
    ("Fermat", "nb théorie", "analyse", 1, "Wiles 1995: EC↔MF pont"),
    ("Groupes finis", "algèbre", "algèbre", 2, "Classification dense interne"),
    ("Higgs", "QFT", "mécanique", 3, "Théorie↔expérimental"),
    ("CRISPR", "—", "—", 0, "Biologie (hors carte maths)"),
    ("Dark Matter", "cosmologie", "quantique", 4, "Trou DM↔QG ouvert"),
    ("Deep Learning", "probabilités", "optimisation", 1, "CV↔NLP pont AlexNet"),
    ("Graphène", "—", "—", 5, "Matériaux (hors carte maths)"),
    ("Poincaré", "topologie", "géom diff", 1, "Perelman 2003: trou 18 ans"),
    ("Immunothérapie", "—", "—", 0, "Médecine (hors carte maths)"),
    ("Ondes grav", "géom diff", "mécanique", 3, "GR théorique→détection"),
    ("Supraconducteurs", "quantique", "thermo", 1, "HTS pont post-découverte"),
    ("Quantum×Crypto", "quantique", "complexité", 4, "Trou en transition"),
    ("Microbiome×Psy", "—", "—", 0, "Neuroscience (hors carte maths)"),
    ("Cordes", "QFT", "géom diff", 5, "Dense mais pont expérimental décline"),
    ("AlphaFold", "probabilités", "optimisation", 1, "PF∩DL pont Nobel 2024"),
    ("Blockchain", "complexité", "cryptographie", 1, "BC↔CR pont Nakamoto"),
    ("Exoplanètes", "mécanique", "probabilités", 2, "Croissance intra-domaine"),
    ("Isolants topo", "topologie", "quantique", 1, "Concept nouveau→Nobel 2016"),
    ("Fusion", "thermo", "quantique", 4, "TOK↔HTS trou 40 ans"),
    ("Éco comportementale", "probabilités", "logique", 1, "BE∩CB pont psycho↔éco"),
]

print(f"\n{'#':>2s} {'Test':20s} {'Dom A':15s} {'Dom B':15s} {'Pat':>3s} {'C1?':>5s} {'Shared':>6s} {'Verdict'}")
print("-" * 95)

valid = 0
mapped = 0
for i, (name, d1, d2, pattern, note) in enumerate(test_mapping, 1):
    if d1 == "—":
        print(f"{i:2d} {name:20s} {'—':15s} {'—':15s} {pattern:3d} {'HORS':>5s} {'—':>6s} Domaine hors carte maths")
        continue
    
    mapped += 1
    s1 = domain_size.get(d1, 0)
    s2 = domain_size.get(d2, 0)
    
    if d1 == d2:
        shared = len(domain_strate_sets.get(d1, set()))
        verdict = "DENSE ✅" if shared >= 3 else "FAIBLE ⚠️"
    else:
        shared_strates = domain_strate_sets.get(d1, set()) & domain_strate_sets.get(d2, set())
        shared = len(shared_strates)
        
        if pattern == 1:  # Pont
            verdict = "TROU→PONT ✅" if shared <= 1 else f"Lien×{shared} (pas trou)"
        elif pattern == 2:  # Dense
            verdict = "DENSE ✅" if shared >= 2 else "PAS DENSE ⚠️"
        elif pattern == 3:  # Théorie×Outil
            g1 = domain_gravity.get(d1, 0)
            g2 = domain_gravity.get(d2, 0)
            verdict = f"Δgrav={abs(g1-g2):.1f} ✅" if abs(g1-g2) > 0.5 else f"Δgrav={abs(g1-g2):.1f} ⚠️"
        elif pattern == 4:  # Trou ouvert
            verdict = "TROU OUVERT ✅" if shared <= 1 else f"Lien×{shared} (connecté)"
        elif pattern == 5:  # Anti-signal
            verdict = "DENSE MAIS FRAGILE ✅" if shared >= 2 else "PAS DENSE"
        else:
            verdict = "?"
    
    if "✅" in verdict:
        valid += 1
    
    print(f"{i:2d} {name:20s} {d1:15s} {d2:15s} {pattern:3d} {s1:3d}+{s2:<2d} {shared:6d} {verdict}")

print(f"\n{'='*70}")
print(f"RÉSULTATS: {mapped} tests mappés, {valid}/{mapped} patterns confirmés")
print(f"Tests hors carte maths: {20 - mapped}")

# ============================================================================
# 10. PRÉDICTIONS — VIDES FERTILES SUR YGGDRASIL
# ============================================================================
print("\n" + "=" * 70)
print("🎯 PRÉDICTIONS — TOP VIDES FERTILES SUR L'AXE YGGDRASIL")
print("  Domaines actifs (≥10 symboles chacun) avec ZÉRO strate commune")
print("  = Là où chercher le prochain pont de découverte")
print("=" * 70)

big_holes = [(d1, d2, s1, s2) for d1, d2, s1, s2 in zero_pairs 
             if s1 >= 10 and s2 >= 10]
big_holes.sort(key=lambda x: -(x[2]*x[3]))  # Produit des tailles

print(f"\n{'Domaine A':20s} {'|A|':>4s}  {'Domaine B':20s} {'|B|':>4s}  {'Score':>6s}  Strates A → Strates B")
print("-" * 85)
for d1, d2, s1, s2 in big_holes[:15]:
    sa = sorted(domain_strate_sets[d1])
    sb = sorted(domain_strate_sets[d2])
    score = s1 * s2
    print(f"{d1:20s} {s1:4d}  {d2:20s} {s2:4d}  {score:6d}  S{sa} → S{sb}")

print(f"\n✅ {len(big_holes)} vides fertiles majeurs identifiés")
print("Un paper qui connecte ces paires = Pattern 1 (pont de découverte)")
