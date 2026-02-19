#!/usr/bin/env python3
"""
MYCELIUM ENGINE — Le réseau souterrain d'Yggdrasil
═══════════════════════════════════════════════════
Adapté de Winter Tree v2 (7912 lignes, 24 briques, 456 tests)
Sources: Bebber 2007, Tero 2010, Latora 2001

Architecture Yggdrasil:
    CIEL (S6)  ── BB(n), Ω ── incompressible
        │
    STRATES (S1-S5) ── conjectures, preuves
        │
    SOL (S0)  ── 549 outils prouvés ── LIANES
        │
    MYCELIUM  ── CE FICHIER ── connexions invisibles entre domaines
        │
    RACINES   ── données OpenAlex, 250M papers

Le mycelium c'est le graphe de co-occurrence entre domaines scientifiques.
Nœuds = continents-métiers (7). Arêtes = lianes (symboles S0 partagés).
Le flux = circulation de connaissances entre professions.

Briques importées de tree/mycelium.py:
    B0: Construction graphe     B5: Betweenness (bottlenecks)
    B1: Meshedness α            B6: Robustesse (attaque séquentielle)
    B2: Efficacité globale      B9: Stratégie phalanx/guerrilla
    B3: Efficacité root         B10: Kirchhoff + Physarum (flux adaptatif)
    B4: Volume-MST ratio        B11: Cold bridges (trous structurels)

Sky × Claude — 19 Février 2026, Versoix
"""

import json
import networkx as nx
import numpy as np
from collections import defaultdict
from pathlib import Path


# ═══════════════════════════════════════════════════════════════════════════════
# DONNÉES — CONTINENTS & LIANES (from yggdrasil-engine/engine/lianes.py)
# ═══════════════════════════════════════════════════════════════════════════════

CONTINENTS = {
    "Mathématiques Pures": {
        "color": "#1e3a8a",
        "domains": [
            "algèbre", "algèbre lin", "analyse", "analyse fonctionnelle",
            "topologie", "géométrie", "géom diff", "combinatoire",
            "nb théorie", "nb premiers", "nombres", "catégories",
            "ensembles", "logique", "mesure", "complexes",
            "arithmétique", "trigonométrie", "ordinaux",
        ]
    },
    "Physique Fondamentale": {
        "color": "#7c3aed",
        "domains": [
            "quantique", "relativité", "QFT", "particules",
            "cosmologie", "gravitation", "nucléaire", "mécanique stat",
            "mécanique", "mécanique analytique", "optique", "astronomie",
        ]
    },
    "Ingénierie & Électricité": {
        "color": "#ea580c",
        "domains": [
            "électromagn", "signal", "contrôle", "fluides",
            "EDP", "thermo", "automates",
        ]
    },
    "Informatique & IA": {
        "color": "#06b6d4",
        "domains": [
            "calculabilité", "complexité", "ML", "crypto",
            "information", "automates",
        ]
    },
    "Finance & Économie": {
        "color": "#eab308",
        "domains": [
            "finance", "économie", "statistiques", "probabilités",
            "stochastique", "optimisation",
        ]
    },
    "Biologie & Médecine": {
        "color": "#84cc16",
        "domains": ["biologie"],
    },
    "Chimie": {
        "color": "#f43f5e",
        "domains": ["chimie"],
    },
}

# Mapping manuel : symbole → liste de continents qui l'utilisent EN PRATIQUE
# Un symbole utilisé par 6+ continents = liane universelle
# Un symbole utilisé par 3-5 = liane majeure
# 2 = pont, 1 = local
USAGE_OVERRIDES = {
    "=":      ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité","Informatique & IA","Finance & Économie","Biologie & Médecine","Chimie"],
    "∫":      ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité","Finance & Économie","Biologie & Médecine","Chimie"],
    "exp":    ["Mathématiques Pures","Physique Fondamentale","Finance & Économie","Informatique & IA","Biologie & Médecine","Chimie"],
    "ln":     ["Mathématiques Pures","Physique Fondamentale","Finance & Économie","Informatique & IA","Biologie & Médecine","Chimie"],
    "∂":      ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité","Finance & Économie","Biologie & Médecine"],
    "Σ":      ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité","Finance & Économie","Informatique & IA","Biologie & Médecine"],
    "e":      ["Mathématiques Pures","Physique Fondamentale","Finance & Économie","Informatique & IA","Biologie & Médecine"],
    "π":      ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité","Informatique & IA"],
    "∞":      ["Mathématiques Pures","Physique Fondamentale","Informatique & IA","Finance & Économie"],
    "lim":    ["Mathématiques Pures","Physique Fondamentale","Finance & Économie","Ingénierie & Électricité"],
    "∇":      ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité","Informatique & IA"],
    "∇²":     ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité","Chimie"],
    "sin":    ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité","Informatique & IA"],
    "cos":    ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité","Informatique & IA"],
    "λ":      ["Mathématiques Pures","Physique Fondamentale","Informatique & IA","Finance & Économie"],
    "P(A)":   ["Mathématiques Pures","Finance & Économie","Informatique & IA","Biologie & Médecine"],
    "E[X]":   ["Mathématiques Pures","Finance & Économie","Informatique & IA","Biologie & Médecine"],
    "Var":    ["Mathématiques Pures","Finance & Économie","Informatique & IA","Biologie & Médecine"],
    "N(μ,σ²)":["Mathématiques Pures","Finance & Économie","Biologie & Médecine","Physique Fondamentale"],
    "Bayes":  ["Mathématiques Pures","Finance & Économie","Informatique & IA","Biologie & Médecine"],
    "∬":      ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité","Chimie"],
    "∮":      ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité","Chimie"],
    "d/dx":   ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité","Finance & Économie"],
    "O(n)":   ["Mathématiques Pures","Informatique & IA","Finance & Économie","Ingénierie & Électricité"],
    "ε":      ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité","Finance & Économie"],
    "δ":      ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité","Finance & Économie"],
    "Π":      ["Mathématiques Pures","Physique Fondamentale","Finance & Économie","Informatique & IA"],
    "ℱ":      ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité","Informatique & IA"],
    "FFT":    ["Ingénierie & Électricité","Informatique & IA","Physique Fondamentale","Finance & Économie"],
    "∗_conv": ["Ingénierie & Électricité","Informatique & IA","Physique Fondamentale","Mathématiques Pures"],
    "log":    ["Mathématiques Pures","Informatique & IA","Finance & Économie","Biologie & Médecine"],
    "det":    ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité","Informatique & IA"],
    "σ_std":  ["Mathématiques Pures","Finance & Économie","Physique Fondamentale","Biologie & Médecine"],
    "χ²":     ["Mathématiques Pures","Finance & Économie","Biologie & Médecine","Physique Fondamentale"],
    "H(X)":   ["Informatique & IA","Physique Fondamentale","Finance & Économie"],
    "D_KL":   ["Informatique & IA","Physique Fondamentale","Finance & Économie"],
    "W(t)":   ["Finance & Économie","Physique Fondamentale","Mathématiques Pures"],
    "SDE":    ["Finance & Économie","Physique Fondamentale","Biologie & Médecine"],
    "Itô":    ["Finance & Économie","Physique Fondamentale","Mathématiques Pures"],
    "S_ent":  ["Physique Fondamentale","Chimie","Informatique & IA"],
    "F=ma":   ["Physique Fondamentale","Ingénierie & Électricité","Biologie & Médecine"],
    "PV=nRT": ["Physique Fondamentale","Ingénierie & Électricité","Chimie"],
    "∇L":     ["Informatique & IA","Mathématiques Pures","Finance & Économie"],
    "SGD":    ["Informatique & IA","Finance & Économie","Biologie & Médecine"],
    "argmin": ["Mathématiques Pures","Informatique & IA","Finance & Économie"],
    "argmax": ["Mathématiques Pures","Informatique & IA","Finance & Économie"],
    "R₀":     ["Biologie & Médecine","Finance & Économie","Mathématiques Pures"],
    "Nash":   ["Finance & Économie","Informatique & IA","Biologie & Médecine"],
    "∇×":     ["Physique Fondamentale","Ingénierie & Électricité","Mathématiques Pures"],
    "∇·":     ["Physique Fondamentale","Ingénierie & Électricité","Mathématiques Pures"],
    "Re":     ["Ingénierie & Électricité","Physique Fondamentale","Biologie & Médecine"],
    "BS":     ["Finance & Économie","Mathématiques Pures","Physique Fondamentale"],
    "TM":     ["Informatique & IA","Mathématiques Pures","Physique Fondamentale"],
    "Γ":      ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité"],
    "ζ":      ["Mathématiques Pures","Physique Fondamentale","Finance & Économie"],
    "i":      ["Mathématiques Pures","Physique Fondamentale","Ingénierie & Électricité"],
    "GAN":    ["Informatique & IA","Biologie & Médecine","Finance & Économie"],
    "Attn":   ["Informatique & IA","Biologie & Médecine","Finance & Économie"],
    "ℒ":      ["Physique Fondamentale","Mathématiques Pures","Ingénierie & Électricité"],
    "ℋ":      ["Physique Fondamentale","Mathématiques Pures","Informatique & IA"],
}

# Reverse map: domain → continents
DOMAIN_TO_CONTINENTS = defaultdict(list)
for continent, info in CONTINENTS.items():
    for domain in info["domains"]:
        DOMAIN_TO_CONTINENTS[domain].append(continent)


def load_symbols(filepath="strates_export.json"):
    """Charge les 794 symboles depuis l'export JSON."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    symbols = []
    for strate in data.get("strates", []):
        sid = strate["id"]
        for sym in strate.get("symbols", []):
            symbols.append({
                "s": sym["s"], "from": sym.get("from", ""),
                "domain": sym.get("domain", ""), "strate": sid
            })
    return symbols


def get_continents_for(symbol):
    """Renvoie la liste des continents qui utilisent ce symbole."""
    s = symbol["s"]
    if s in USAGE_OVERRIDES:
        return USAGE_OVERRIDES[s]
    return DOMAIN_TO_CONTINENTS.get(symbol["domain"], [])


# ═══════════════════════════════════════════════════════════════════════════════
# BRIQUE 0 — CONSTRUCTION DU GRAPHE MYCELIUM
# ═══════════════════════════════════════════════════════════════════════════════

def build_knowledge_graph(liane_data):
    """Construit le graphe: nœuds=continents, arêtes=lianes partagées."""
    G = nx.Graph()
    for name, info in CONTINENTS.items():
        G.add_node(name, color=info["color"],
                   n_domains=len(info["domains"]))

    bridge = defaultdict(list)
    for l in liane_data:
        conts = l.get("continents", [])
        for i, a in enumerate(conts):
            for b in conts[i+1:]:
                bridge[tuple(sorted([a, b]))].append(l["s"])

    for (a, b), symbols in bridge.items():
        if a in G and b in G:
            G.add_edge(a, b, weight=len(symbols), lianes=symbols,
                       conductivity=float(len(symbols)))
    return G


# ═══════════════════════════════════════════════════════════════════════════════
# BRIQUE 1 — MESHEDNESS α (Bebber 2007)
#   α = (L - N + 1) / (2N - 5)
#   0 = arbre pur | 1 = planaire max | >1 = non-planaire
# ═══════════════════════════════════════════════════════════════════════════════

def meshedness(G):
    if not nx.is_connected(G):
        G = G.subgraph(max(nx.connected_components(G), key=len)).copy()
    N, L = G.number_of_nodes(), G.number_of_edges()
    if N < 3: return 0.0
    d = 2 * N - 5
    return (L - N + 1) / d if d > 0 else 0.0


# ═══════════════════════════════════════════════════════════════════════════════
# BRIQUE 2 — EFFICACITÉ GLOBALE (Latora & Marchiori 2001)
#   E_glob = (1/N(N-1)) × Σ (1/d_ij)
# ═══════════════════════════════════════════════════════════════════════════════

def global_efficiency(G):
    N = G.number_of_nodes()
    if N < 2: return 0.0
    total = 0.0
    for s in G.nodes():
        lengths = nx.single_source_shortest_path_length(G, s)
        total += sum(1.0/d for t, d in lengths.items() if t != s and d > 0)
    return total / (N * (N - 1))


# ═══════════════════════════════════════════════════════════════════════════════
# BRIQUE 3 — EFFICACITÉ ROOT (depuis un continent)
#   E_root = (1/(N-1)) × Σ (1/d_root,j)
# ═══════════════════════════════════════════════════════════════════════════════

def root_efficiency(G, root):
    if root not in G: return 0.0
    N = G.number_of_nodes()
    if N < 2: return 0.0
    lengths = nx.single_source_shortest_path_length(G, root)
    return sum(1.0/d for t, d in lengths.items() if t != root and d > 0) / (N-1)


# ═══════════════════════════════════════════════════════════════════════════════
# BRIQUE 4 — VOLUME-MST RATIO (overhead architectural)
# ═══════════════════════════════════════════════════════════════════════════════

def volume_mst_ratio(G):
    if not nx.is_connected(G):
        G = G.subgraph(max(nx.connected_components(G), key=len)).copy()
    if G.number_of_edges() == 0: return 1.0
    for u, v, d in G.edges(data=True):
        d["_inv"] = 1.0 / max(d.get("weight", 1.0), 0.01)
    mst = nx.minimum_spanning_tree(G, weight="_inv")
    total = sum(d.get("weight", 1) for _, _, d in G.edges(data=True))
    mst_t = sum(d.get("weight", 1) for _, _, d in mst.edges(data=True))
    return total / mst_t if mst_t > 0 else 1.0


# ═══════════════════════════════════════════════════════════════════════════════
# BRIQUE 5 — BETWEENNESS CENTRALITY (bottlenecks)
# ═══════════════════════════════════════════════════════════════════════════════

def find_bottlenecks(G, top_n=5):
    bc = nx.betweenness_centrality(G, weight="weight")
    return sorted(bc.items(), key=lambda x: -x[1])[:top_n]


def find_edge_bottlenecks(G, top_n=10):
    ebc = nx.edge_betweenness_centrality(G, weight="weight")
    return sorted([(u,v,s) for (u,v),s in ebc.items()], key=lambda x: -x[2])[:top_n]


# ═══════════════════════════════════════════════════════════════════════════════
# BRIQUE 6 — ROBUSTESSE (suppression séquentielle)
# ═══════════════════════════════════════════════════════════════════════════════

def robustness_test(G, attack="betweenness"):
    G = G.copy(); N0 = G.number_of_nodes()
    if N0 < 2: return [(0.0, 1.0)]
    results = [(0.0, 1.0)]
    for step in range(N0 - 1):
        if G.number_of_nodes() < 2: break
        bc = nx.betweenness_centrality(G)
        target = max(bc, key=bc.get)
        G.remove_node(target)
        if G.number_of_nodes() == 0:
            results.append(((step+1)/N0, 0.0)); break
        largest = max(nx.connected_components(G), key=len)
        results.append(((step+1)/N0, len(largest)/N0))
    return results


def robustness_liane(G, symbol):
    """Que se passe-t-il si on retire UNE liane du réseau?"""
    before = {"efficiency": global_efficiency(G), "meshedness": meshedness(G),
              "connected": nx.is_connected(G), "n_edges": G.number_of_edges()}
    Gp = G.copy()
    to_remove = []
    for u, v, d in Gp.edges(data=True):
        lianes = d.get("lianes", [])
        if symbol in lianes:
            new = [l for l in lianes if l != symbol]
            if not new: to_remove.append((u, v))
            else:
                Gp[u][v]["lianes"] = new
                Gp[u][v]["weight"] = len(new)
                Gp[u][v]["conductivity"] = float(len(new))
    Gp.remove_edges_from(to_remove)
    after = {"efficiency": global_efficiency(Gp), "meshedness": meshedness(Gp),
             "connected": nx.is_connected(Gp) if Gp.number_of_nodes() > 0 else False,
             "n_edges": Gp.number_of_edges(), "edges_killed": len(to_remove)}
    return {"symbol": symbol, "before": before, "after": after,
            "delta_eff": after["efficiency"]-before["efficiency"],
            "delta_alpha": after["meshedness"]-before["meshedness"],
            "fragmented": before["connected"] and not after["connected"]}


# ═══════════════════════════════════════════════════════════════════════════════
# BRIQUE 9 — STRATÉGIE PHALANX / GUERRILLA
# ═══════════════════════════════════════════════════════════════════════════════

def classify_strategy(alpha, e_global, e_root, rob30=None):
    r = {"alpha": round(alpha,4), "e_global": round(e_global,4),
         "e_root": round(e_root,4)}
    if alpha > 0.5 and e_global > 0.7:
        r.update(type="PHALANX", pattern="P2 Dense", desc="Réseau dense — ascenseur central")
    elif alpha < 0.2 and e_global < 0.5:
        r.update(type="GUERRILLA", pattern="P1 Pont", desc="Réseau sparse — escaliers de secours")
    else:
        r.update(type="HYBRID", pattern="P3/P4", desc="Réseau en transition")
    if rob30 is not None: r["rob30"] = round(rob30, 4)
    return r


# ═══════════════════════════════════════════════════════════════════════════════
# BRIQUE 10 — KIRCHHOFF FLOW + PHYSARUM (Tero 2010)
#   dD_e/dt = |Q_e|^μ − decay × D_e
#   μ=1 → shortest path | μ<1 → redondance (Tokyo rail)
# ═══════════════════════════════════════════════════════════════════════════════

def kirchhoff_flow(G, sources):
    if G.number_of_nodes() < 2 or G.number_of_edges() == 0:
        return {"pressures": {}, "flows": {}}
    if not nx.is_connected(G):
        src = [n for n,v in sources.items() if v > 0]
        comp = nx.node_connected_component(G, src[0]) if src and src[0] in G \
               else max(nx.connected_components(G), key=len)
        G = G.subgraph(comp).copy()
        sources = {n:v for n,v in sources.items() if n in G}

    b = dict(sources)
    total = sum(b.values())
    if abs(total) > 1e-10:
        non_src = [n for n in G.nodes() if n not in b]
        if non_src:
            for n in non_src: b[n] = -total / len(non_src)

    nodes = list(G.nodes()); idx = {n:i for i,n in enumerate(nodes)}; N = len(nodes)
    L = np.zeros((N,N)); edata = {}
    for u,v,d in G.edges(data=True):
        cond = d.get("conductivity", d.get("weight", 1.0))
        i,j = idx[u], idx[v]
        L[i,i] += cond; L[j,j] += cond; L[i,j] -= cond; L[j,i] -= cond
        edata[(u,v)] = cond

    bv = np.zeros(N)
    for n,val in b.items():
        if n in idx: bv[idx[n]] = val

    gnd = 0
    for n,val in b.items():
        if val < 0 and n in idx: gnd = idx[n]; break

    mask = np.ones(N, dtype=bool); mask[gnd] = False
    try: p_r = np.linalg.solve(L[np.ix_(mask,mask)], bv[mask])
    except: return {"pressures": {n:0 for n in nodes}, "flows": {}}

    p = np.zeros(N); p[mask] = p_r
    pressures = {nodes[i]: float(p[i]) for i in range(N)}
    flows = {}
    for (u,v), cond in edata.items():
        flows[(u,v)] = float(cond * (p[idx[u]] - p[idx[v]]))
    return {"pressures": pressures, "flows": flows}


def physarum_simulate(G, sources, n_steps=100, mu=1.0, decay=1.0, h=0.1):
    G = G.copy()
    for u,v,d in G.edges(data=True):
        if "conductivity" not in d: d["conductivity"] = d.get("weight", 1.0)
    converged = False
    for step in range(n_steps):
        r = kirchhoff_flow(G, sources)
        flows = r["flows"]
        if not flows: break
        max_delta = 0.0
        for u,v,d in G.edges(data=True):
            D = d.get("conductivity", 1.0)
            Q = flows.get((u,v), flows.get((v,u), 0.0))
            D_new = max(D + h * (abs(Q)**mu - decay*D), 1e-6)
            max_delta = max(max_delta, abs(D_new - D))
            d["conductivity"] = D_new
        if max_delta < 1e-8: converged = True; break

    conds = [(u,v,d.get("conductivity",0)) for u,v,d in G.edges(data=True)]
    if conds:
        med = sorted(c for _,_,c in conds)[len(conds)//2]
        thr = med * 0.1
    else: thr = 0.01
    thick = sorted([(u,v,c) for u,v,c in conds if c > thr], key=lambda x: -x[2])
    dead = [(u,v) for u,v,c in conds if c <= thr]
    return {"thick": thick, "dead": dead, "steps": step+1, "converged": converged}


# ═══════════════════════════════════════════════════════════════════════════════
# ANALYSE COMPLÈTE + EXPORT JSON POUR VIZ
# ═══════════════════════════════════════════════════════════════════════════════

def full_analysis(filepath="strates_export.json"):
    """Lance toute l'analyse mycelium et exporte pour la viz."""
    symbols = load_symbols(filepath)
    s0 = [s for s in symbols if s["strate"] == 0]

    liane_data = []
    for sym in s0:
        conts = get_continents_for(sym)
        n = len(conts)
        ltype = "universal" if n >= 6 else "major" if n >= 4 else "liane" if n >= 3 else "bridge" if n >= 2 else "local"
        liane_data.append({"s": sym["s"], "domain": sym["domain"],
                           "continents": conts, "n": n, "type": ltype})

    G = build_knowledge_graph(liane_data)
    root = "Mathématiques Pures"

    alpha = meshedness(G)
    e_glob = global_efficiency(G)
    e_root = root_efficiency(G, root)
    v_mst = volume_mst_ratio(G)
    bn_nodes = find_bottlenecks(G)
    bn_edges = find_edge_bottlenecks(G)
    rob = robustness_test(G)
    rob30 = next((c for r,c in rob if r >= 0.3), None)
    strat = classify_strategy(alpha, e_glob, e_root, rob30)

    sources = {root: 1.0}
    for n in [x for x in G.nodes() if x != root]:
        sources[n] = -1.0 / (G.number_of_nodes()-1)
    phys = physarum_simulate(G, sources)

    # Liane impact tests
    test_syms = ["=","exp","ln","Σ","∫","∂","e","∇","sin","cos",
                 "Bayes","P(A)","E[X]","Nash","S_ent","FFT","Attn",
                 "H(X)","R₀","λ","GAN","W(t)","ζ","ℒ","χ²"]
    liane_impacts = []
    for sym in test_syms:
        r = robustness_liane(G, sym)
        liane_impacts.append(r)

    # Count lianes by type
    type_counts = defaultdict(int)
    for l in liane_data:
        type_counts[l["type"]] += 1

    # Build export
    bc = nx.betweenness_centrality(G)
    viz = {
        "meta": {
            "title": "Yggdrasil Mycelium — Réseau souterrain",
            "date": "2026-02-19",
            "n_symbols_s0": len(s0),
            "n_lianes_multi": sum(1 for l in liane_data if l["n"] >= 2),
            "type_counts": dict(type_counts),
        },
        "metrics": {
            "meshedness_alpha": round(alpha, 4),
            "global_efficiency": round(e_glob, 4),
            "root_efficiency": round(e_root, 4),
            "volume_mst_ratio": round(v_mst, 4),
            "robustness_30pct": round(rob30, 4) if rob30 else None,
            "strategy": strat,
        },
        "nodes": [],
        "edges": [],
        "physarum": {
            "arteries": [{"from": u, "to": v, "conductivity": round(c, 4)}
                         for u,v,c in phys["thick"][:15]],
            "dead": [{"from": u, "to": v} for u,v in phys["dead"]],
            "converged": phys["converged"],
            "steps": phys["steps"],
        },
        "liane_impact": [
            {"symbol": r["symbol"], "delta_eff": round(r["delta_eff"], 4),
             "delta_alpha": round(r["delta_alpha"], 4),
             "fragmented": r["fragmented"],
             "edges_killed": r["after"]["edges_killed"]}
            for r in liane_impacts
        ],
        "robustness_curve": [(round(r,3), round(c,3)) for r,c in rob],
    }

    for name in G.nodes():
        info = CONTINENTS.get(name, {})
        viz["nodes"].append({
            "id": name, "color": info.get("color", "#888"),
            "n_domains": len(info.get("domains", [])),
            "efficiency": round(root_efficiency(G, name), 4),
            "betweenness": round(bc.get(name, 0), 4),
        })

    for u,v,d in G.edges(data=True):
        w = d.get("weight", 1)
        lianes = d.get("lianes", [])
        pc = next((c for a,b,c in phys["thick"] if {a,b}=={u,v}), 0)
        viz["edges"].append({
            "source": u, "target": v, "weight": w,
            "lianes": lianes,
            "physarum_conductivity": round(pc, 4),
        })

    return viz, G


def print_report(viz):
    m = viz["metrics"]
    print(f"\n{'='*70}")
    print(f"  YGGDRASIL — RAPPORT MYCELIUM")
    print(f"  Le réseau souterrain des connexions scientifiques")
    print(f"{'='*70}\n")
    mc = viz["meta"]
    print(f"  {mc['n_symbols_s0']} symboles S0 | {mc['n_lianes_multi']} lianes multi-continent")
    print(f"  Types: {mc['type_counts']}\n")
    print(f"  ┌────────────────────────────────────────────────┐")
    print(f"  │  Meshedness α:       {m['meshedness_alpha']:<10}               │")
    print(f"  │  Efficacité globale: {m['global_efficiency']:<10}               │")
    print(f"  │  Volume/MST ratio:   {m['volume_mst_ratio']:<10}               │")
    print(f"  │  Robustesse @30%:    {m['robustness_30pct']}                   │")
    print(f"  │  Stratégie: {m['strategy']['type']:>10} — {m['strategy']['desc']}  │")
    print(f"  └────────────────────────────────────────────────┘\n")

    print(f"  ARTÈRES PHYSARUM (flux adaptatif):")
    for a in viz["physarum"]["arteries"][:7]:
        print(f"    🔴 {a['from']:<25} → {a['to']:<25} σ={a['conductivity']}")

    print(f"\n  CONNEXIONS (lianes partagées):")
    for e in sorted(viz["edges"], key=lambda x: -x["weight"]):
        print(f"    {e['source']:<25} × {e['target']:<25} {e['weight']:>3} lianes  phys={e['physarum_conductivity']}")

    print(f"\n  IMPACT SI LIANE RETIRÉE:")
    for li in sorted(viz["liane_impact"], key=lambda x: x["delta_eff"]):
        f = "💀" if li["fragmented"] else "✅"
        print(f"    {li['symbol']:>8}  ΔE={li['delta_eff']:+.4f}  Δα={li['delta_alpha']:+.4f}  {f}  killed={li['edges_killed']}")


if __name__ == "__main__":
    viz, G = full_analysis()
    print_report(viz)
    with open("mycelium_data.json", "w", encoding="utf-8") as f:
        json.dump(viz, f, ensure_ascii=False, indent=2)
    print(f"\n  → mycelium_data.json exporté")
