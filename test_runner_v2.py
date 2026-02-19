#!/usr/bin/env python3
"""
YGGDRASIL — Harnais de test automatisé
Pull OpenAlex → timeline → pattern → lianes

Tests 33+: Nouvelles découvertes à valider
Focus: zones froides du mycelium (Chimie×IA, etc.)

Sky × Claude — 19 Février 2026
"""

import json
import time
import urllib.request
import urllib.parse
from pathlib import Path
from datetime import datetime

BASE = "https://api.openalex.org"
HEADERS = {"User-Agent": "YggdrasilEngine/2.0 (mailto:sky@yggdrasil.ch)"}
DELAY = 0.15  # Rate limit

# ═══════════════════════════════════════════════════════
# OPENALEX API
# ═══════════════════════════════════════════════════════

def _get(endpoint, params=None):
    url = f"{BASE}/{endpoint}"
    if params:
        url += "?" + urllib.parse.urlencode(params, safe=':,')
    req = urllib.request.Request(url, headers=HEADERS)
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            return json.loads(resp.read())
    except Exception as e:
        print(f"  ⚠ API error: {e}")
        return {}


def find_concept(name):
    """Find OpenAlex concept by name."""
    data = _get("concepts", {"filter": f"display_name.search:{name}", "per_page": 5})
    results = data.get("results", [])
    if results:
        r = results[0]
        return {"id": r["id"], "name": r["display_name"],
                "works": r.get("works_count", 0), "level": r.get("level", -1)}
    return None


def co_occurrence_year(concept_a_id, concept_b_id, year):
    """Count papers with both concepts in a given year."""
    data = _get("works", {
        "filter": f"concepts.id:{concept_a_id},concepts.id:{concept_b_id},publication_year:{year}",
        "per_page": 1,
    })
    time.sleep(DELAY)
    return data.get("meta", {}).get("count", 0)


def concept_year(concept_id, year):
    """Count papers for one concept in a year."""
    data = _get("works", {
        "filter": f"concepts.id:{concept_id},publication_year:{year}",
        "per_page": 1,
    })
    time.sleep(DELAY)
    return data.get("meta", {}).get("count", 0)


def keyword_co_year(kw_a, kw_b, year):
    """Co-occurrence by keyword search (for concepts not in OpenAlex taxonomy)."""
    q = f"{kw_a} {kw_b}"
    data = _get("works", {
        "filter": f"default.search:{urllib.parse.quote(q)},publication_year:{year}",
        "per_page": 1,
    })
    time.sleep(DELAY)
    return data.get("meta", {}).get("count", 0)


def keyword_year(kw, year):
    """Single keyword count per year."""
    data = _get("works", {
        "filter": f"default.search:{urllib.parse.quote(kw)},publication_year:{year}",
        "per_page": 1,
    })
    time.sleep(DELAY)
    return data.get("meta", {}).get("count", 0)


def top_bridge_papers(concept_a_id, concept_b_id, n=5):
    """Find the most cited papers at the intersection."""
    data = _get("works", {
        "filter": f"concepts.id:{concept_a_id},concepts.id:{concept_b_id}",
        "sort": "cited_by_count:desc",
        "per_page": str(n),
    })
    time.sleep(DELAY)
    results = []
    for w in data.get("results", []):
        results.append({
            "title": w.get("title", "?"),
            "year": w.get("publication_year"),
            "citations": w.get("cited_by_count", 0),
            "doi": w.get("doi", ""),
            "authors": [a.get("author", {}).get("display_name", "?")
                        for a in w.get("authorships", [])[:3]],
        })
    return results


# ═══════════════════════════════════════════════════════
# PATTERN DETECTION
# ═══════════════════════════════════════════════════════

def detect_pattern(timeline, bridge_year=None):
    """
    Classify co-occurrence timeline into P1-P5.

    P1 PONT:     Zero period → bridge paper → explosion
    P2 DENSE:    Continuous growth, no zero period
    P3 THÉORIE:  Theory active, tool gap, then connection
    P4 OUVERT:   Zero period → still zero or barely starting
    P5 ANTI:     Was growing, now declining
    """
    years = sorted(timeline.keys())
    if not years:
        return {"pattern": "NO_DATA", "confidence": 0}

    values = [timeline[y] for y in years]
    n = len(values)

    # Detect zero period
    zero_years = [y for y in years if timeline[y] <= 2]
    active_years = [y for y in years if timeline[y] > 2]

    # Growth metrics
    if len(values) > 3:
        first_third = sum(values[:n//3]) / max(n//3, 1)
        last_third = sum(values[-(n//3):]) / max(n//3, 1)
        growth_ratio = last_third / max(first_third, 0.1)
    else:
        growth_ratio = 1

    # Max and where it occurs
    max_val = max(values) if values else 0
    max_year = years[values.index(max_val)] if max_val > 0 else None

    # Recent trend (last 3 years)
    if len(values) >= 4:
        recent = values[-3:]
        earlier = values[-6:-3] if len(values) >= 7 else values[:3]
        recent_avg = sum(recent) / len(recent)
        earlier_avg = sum(earlier) / max(len(earlier), 1)
        recent_trend = recent_avg / max(earlier_avg, 0.1)
    else:
        recent_trend = 1

    # Classify
    pattern = "UNKNOWN"
    confidence = 0

    # P5: Anti-signal (declining)
    if recent_trend < 0.5 and max_val > 10:
        pattern = "P5_ANTI_SIGNAL"
        confidence = min(0.9, 1 - recent_trend)

    # P2: Dense (no zero, continuous growth)
    elif len(zero_years) < len(years) * 0.15 and growth_ratio > 1.5:
        pattern = "P2_DENSE"
        confidence = min(0.9, growth_ratio / 10)

    # P1: Bridge (zeros → explosion)
    elif len(zero_years) > 3 and growth_ratio > 5:
        pattern = "P1_PONT"
        confidence = min(0.95, growth_ratio / 50)
        # Find bridge year (transition from zero to growth)
        if bridge_year is None:
            for i, y in enumerate(years):
                if timeline[y] > 5 and i > 0 and all(timeline[years[j]] <= 2 for j in range(max(0, i-3), i)):
                    bridge_year = y
                    break

    # P4: Open hole (zeros and still low)
    elif len(zero_years) > len(years) * 0.5 and max_val < 20:
        pattern = "P4_TROU_OUVERT"
        confidence = 0.7

    # P3: Theory × Tool (moderate growth after long buildup)
    elif growth_ratio > 2 and growth_ratio < 20:
        pattern = "P3_THEORIE_OUTIL"
        confidence = 0.6

    else:
        pattern = "P2_DENSE" if growth_ratio > 1.2 else "P4_TROU_OUVERT"
        confidence = 0.4

    return {
        "pattern": pattern,
        "confidence": round(confidence, 2),
        "growth_ratio": round(growth_ratio, 1),
        "max_val": max_val,
        "max_year": max_year,
        "zero_years": len(zero_years),
        "active_years": len(active_years),
        "recent_trend": round(recent_trend, 2),
        "bridge_year": bridge_year,
    }


# ═══════════════════════════════════════════════════════
# LIANES CROSS-REF
# ═══════════════════════════════════════════════════════

LIANE_DB = {
    # symbol: (continents_used, n_continents)
    "=":     (["Math", "Phys", "Ing", "IA", "Fin", "Bio", "Chim"], 7),
    "∫":     (["Math", "Phys", "Ing", "Fin", "Bio", "Chim"], 6),
    "exp":   (["Math", "Phys", "Fin", "IA", "Bio", "Chim"], 6),
    "ln":    (["Math", "Phys", "Fin", "IA", "Bio", "Chim"], 6),
    "Σ":     (["Math", "Phys", "Ing", "Fin", "IA", "Bio"], 6),
    "∂":     (["Math", "Phys", "Ing", "Fin", "Bio"], 5),
    "e":     (["Math", "Phys", "Fin", "IA", "Bio"], 5),
    "∇":     (["Math", "Phys", "Ing", "IA"], 4),
    "sin":   (["Math", "Phys", "Ing", "IA"], 4),
    "cos":   (["Math", "Phys", "Ing", "IA"], 4),
    "P(A)":  (["Math", "Fin", "IA", "Bio"], 4),
    "E[X]":  (["Math", "Fin", "IA", "Bio"], 4),
    "Var":   (["Math", "Fin", "IA", "Bio"], 4),
    "Bayes": (["Math", "Fin", "IA", "Bio"], 4),
    "FFT":   (["Ing", "IA", "Phys", "Fin"], 4),
    "Nash":  (["Fin", "IA", "Bio"], 3),
    "S_ent": (["Phys", "Chim", "IA"], 3),
    "Attn":  (["IA", "Bio", "Fin"], 3),
    "GAN":   (["IA", "Bio", "Fin"], 3),
    "H(X)":  (["IA", "Phys", "Fin"], 3),
    "D_KL":  (["IA", "Phys", "Fin"], 3),
    "W(t)":  (["Fin", "Phys", "Math"], 3),
    "R₀":    (["Bio", "Fin", "Math"], 3),
    "SGD":   (["IA", "Fin", "Bio"], 3),
    "∇L":    (["IA", "Math", "Fin"], 3),
    "ℒ":     (["Phys", "Math", "Ing"], 3),
    "ζ":     (["Math", "Phys", "Fin"], 3),
    "TM":    (["IA", "Math", "Phys"], 3),
    "SDE":   (["Fin", "Phys", "Bio"], 3),
}


def identify_lianes(domain_a_continent, domain_b_continent, known_symbols=None):
    """
    Which S0 lianes bridge between two continents?
    """
    bridges = []
    for sym, (conts, n) in LIANE_DB.items():
        if domain_a_continent in conts and domain_b_continent in conts:
            bridges.append({"symbol": sym, "n_continents": n})

    bridges.sort(key=lambda x: -x["n_continents"])

    return {
        "n_lianes": len(bridges),
        "lianes": [b["symbol"] for b in bridges],
        "top_liane": bridges[0]["symbol"] if bridges else None,
        "multi_continent": len([b for b in bridges if b["n_continents"] >= 3]),
        "has_liane": len(bridges) > 0,
    }


# ═══════════════════════════════════════════════════════
# TEST DEFINITIONS
# ═══════════════════════════════════════════════════════

TESTS = [
    {
        "id": 33,
        "name": "Diffusion Models (Image Gen)",
        "desc": "Thermodynamique statistique → génération d'images IA",
        "domain_a": {"search": "diffusion model", "continent": "Phys"},
        "domain_b": {"search": "image generation", "continent": "IA"},
        "co_search": "diffusion model image generation",
        "expected_bridge": "Sohl-Dickstein 2015 / Ho 2020 (DDPM)",
        "expected_pattern": "P1",
        "lianes_expected": ["S_ent", "exp", "∇", "∂"],
        "years": range(2012, 2026),
        "mode": "keyword",
    },
    {
        "id": 34,
        "name": "Graph Neural Networks",
        "desc": "Théorie des graphes → deep learning",
        "domain_a": {"search": "graph theory", "concept": "C132525143", "continent": "Math"},
        "domain_b": {"search": "neural network", "concept": "C50644808", "continent": "IA"},
        "co_search": "graph neural network",
        "expected_bridge": "Kipf & Welling 2017 (GCN)",
        "expected_pattern": "P1",
        "lianes_expected": ["Σ", "exp", "∇L", "SGD"],
        "years": range(2010, 2026),
        "mode": "keyword",
    },
    {
        "id": 35,
        "name": "Quantum Error Correction (Surface Codes)",
        "desc": "Topologie algébrique → calcul quantique",
        "domain_a": {"search": "topological code", "continent": "Math"},
        "domain_b": {"search": "quantum computing", "continent": "Phys"},
        "co_search": "surface code quantum error correction",
        "expected_bridge": "Kitaev 2003 / Fowler 2012",
        "expected_pattern": "P3",
        "lianes_expected": ["ℋ", "exp", "Σ"],
        "years": range(2000, 2026),
        "mode": "keyword",
    },
    {
        "id": 36,
        "name": "Protein Language Models",
        "desc": "NLP (Transformers) → biologie structurale",
        "domain_a": {"search": "language model transformer", "continent": "IA"},
        "domain_b": {"search": "protein structure prediction", "continent": "Bio"},
        "co_search": "protein language model",
        "expected_bridge": "Rives 2021 (ESM) / Lin 2023 (ESMFold)",
        "expected_pattern": "P1",
        "lianes_expected": ["Attn", "exp", "SGD", "∇L"],
        "years": range(2015, 2026),
        "mode": "keyword",
    },
    {
        "id": 37,
        "name": "Neural ODEs",
        "desc": "Équations différentielles → réseaux de neurones",
        "domain_a": {"search": "ordinary differential equation", "concept": "C2780693532", "continent": "Math"},
        "domain_b": {"search": "deep learning", "concept": "C108583219", "continent": "IA"},
        "co_search": "neural ordinary differential equation",
        "expected_bridge": "Chen et al. 2018 (NeurIPS best paper)",
        "expected_pattern": "P1",
        "lianes_expected": ["∂", "∫", "exp", "∇L"],
        "years": range(2014, 2026),
        "mode": "keyword",
    },
    {
        "id": 38,
        "name": "AI Drug Discovery",
        "desc": "IA × Chimie — ZONE FROIDE du mycelium",
        "domain_a": {"search": "artificial intelligence", "concept": "C154945302", "continent": "IA"},
        "domain_b": {"search": "drug discovery", "concept": "C109155844", "continent": "Chim"},
        "co_search": "artificial intelligence drug discovery",
        "expected_bridge": "Stokes 2020 (antibiotic by AI) / Jumper 2021",
        "expected_pattern": "P1",
        "lianes_expected": ["exp", "ln", "="],
        "years": range(2010, 2026),
        "mode": "keyword",
        "cold_bridge": True,  # Zone froide mycelium
    },
    {
        "id": 39,
        "name": "Topological Data Analysis",
        "desc": "Topologie algébrique → data science",
        "domain_a": {"search": "persistent homology", "continent": "Math"},
        "domain_b": {"search": "data analysis machine learning", "continent": "IA"},
        "co_search": "topological data analysis persistent homology",
        "expected_bridge": "Carlsson 2009 / Edelsbrunner 2010",
        "expected_pattern": "P3",
        "lianes_expected": ["Σ", "∫", "exp"],
        "years": range(2005, 2026),
        "mode": "keyword",
    },
    {
        "id": 40,
        "name": "Neuromorphic Computing",
        "desc": "Neurosciences → architecture processeur",
        "domain_a": {"search": "spiking neural network", "continent": "Bio"},
        "domain_b": {"search": "neuromorphic computing chip", "continent": "Ing"},
        "co_search": "neuromorphic computing spiking",
        "expected_bridge": "Intel Loihi 2018 / IBM TrueNorth 2014",
        "expected_pattern": "P3",
        "lianes_expected": ["exp", "∂", "Σ"],
        "years": range(2008, 2026),
        "mode": "keyword",
    },
    {
        "id": 41,
        "name": "DFT + ML (Computational Chemistry)",
        "desc": "Chimie quantique × Machine Learning — ZONE FROIDE",
        "domain_a": {"search": "density functional theory", "concept": "C62354560", "continent": "Chim"},
        "domain_b": {"search": "machine learning", "concept": "C119857082", "continent": "IA"},
        "co_search": "density functional theory machine learning",
        "expected_bridge": "Behler 2007 (NNP) / SchNet 2017",
        "expected_pattern": "P1",
        "lianes_expected": ["exp", "∇", "Σ", "∂"],
        "years": range(2005, 2026),
        "mode": "keyword",
        "cold_bridge": True,
    },
    {
        "id": 42,
        "name": "Blockchain × Cryptography (Post-Quantum)",
        "desc": "Crypto post-quantique → blockchain résistante",
        "domain_a": {"search": "post quantum cryptography", "continent": "IA"},
        "domain_b": {"search": "blockchain", "continent": "Fin"},
        "co_search": "post quantum cryptography blockchain",
        "expected_bridge": "NIST PQC 2022 / Ethereum transition",
        "expected_pattern": "P4",
        "lianes_expected": ["exp", "P(A)", "H(X)"],
        "years": range(2015, 2026),
        "mode": "keyword",
    },
]


# ═══════════════════════════════════════════════════════
# RUNNER
# ═══════════════════════════════════════════════════════

def run_test(test, verbose=True):
    """Run a single test: pull data, detect pattern, cross-ref lianes."""
    tid = test["id"]
    if verbose:
        print(f"\n{'='*70}")
        print(f"  TEST #{tid}: {test['name']}")
        print(f"  {test['desc']}")
        print(f"{'='*70}\n")

    result = {"id": tid, "name": test["name"], "desc": test["desc"]}

    # ── Pull timeline ──
    years = list(test["years"])
    timeline_co = {}
    timeline_a = {}
    timeline_b = {}

    mode = test.get("mode", "keyword")

    if verbose:
        print(f"  Pulling {len(years)} years of data from OpenAlex...")

    for y in years:
        if mode == "concept":
            ca = test["domain_a"].get("concept")
            cb = test["domain_b"].get("concept")
            if ca and cb:
                timeline_co[y] = co_occurrence_year(ca, cb, y)
                timeline_a[y] = concept_year(ca, y)
                timeline_b[y] = concept_year(cb, y)
        else:
            # Keyword mode
            kw_co = test.get("co_search", "")
            kw_a = test["domain_a"]["search"]
            kw_b = test["domain_b"]["search"]
            timeline_co[y] = keyword_co_year(kw_a, kw_b, y)
            timeline_a[y] = keyword_year(kw_a, y)
            timeline_b[y] = keyword_year(kw_b, y)

        if verbose and (y - years[0]) % 5 == 0:
            print(f"    {y}: co={timeline_co.get(y, '?')}  A={timeline_a.get(y, '?')}  B={timeline_b.get(y, '?')}")

    result["timeline_co"] = timeline_co
    result["timeline_a"] = timeline_a
    result["timeline_b"] = timeline_b

    # ── Print timeline ──
    if verbose:
        print(f"\n  Timeline co-occurrence:")
        for y in years:
            v = timeline_co.get(y, 0)
            bar = "█" * min(int(v / max(max(timeline_co.values(), default=1), 1) * 40), 40)
            print(f"    {y} | {v:>7,} {bar}")

    # ── Detect pattern ──
    pattern_info = detect_pattern(timeline_co)
    result["pattern"] = pattern_info

    if verbose:
        print(f"\n  PATTERN: {pattern_info['pattern']} (confidence={pattern_info['confidence']})")
        print(f"    Growth ratio: x{pattern_info['growth_ratio']}")
        print(f"    Max: {pattern_info['max_val']:,} papers ({pattern_info['max_year']})")
        print(f"    Zero years: {pattern_info['zero_years']} / Active: {pattern_info['active_years']}")
        print(f"    Recent trend: {pattern_info['recent_trend']}")
        if pattern_info.get("bridge_year"):
            print(f"    Bridge year detected: {pattern_info['bridge_year']}")

    # ── Cross-ref lianes ──
    cont_a = test["domain_a"]["continent"]
    cont_b = test["domain_b"]["continent"]
    liane_info = identify_lianes(cont_a, cont_b)
    result["lianes"] = liane_info

    # Check expected lianes
    expected = test.get("lianes_expected", [])
    found = set(liane_info["lianes"]) & set(expected)
    result["liane_match"] = len(found) / max(len(expected), 1)

    if verbose:
        print(f"\n  LIANES ({cont_a} × {cont_b}):")
        print(f"    {liane_info['n_lianes']} lianes S0 trouvées: {', '.join(liane_info['lianes'][:15])}")
        print(f"    Multi-continent (≥3): {liane_info['multi_continent']}")
        print(f"    Expected match: {len(found)}/{len(expected)} ({', '.join(found)})")
        if test.get("cold_bridge"):
            print(f"    🧊 ZONE FROIDE DU MYCELIUM")

    # ── Expected pattern match ──
    expected_p = test.get("expected_pattern", "")
    detected_p = pattern_info["pattern"][:2]
    result["pattern_match"] = expected_p == detected_p

    if verbose:
        match_str = "✅" if result["pattern_match"] else f"⚠️ (expected {expected_p}, got {detected_p})"
        print(f"\n  RÉSULTAT: {match_str}")
        print(f"    Expected: {test.get('expected_bridge', '?')}")

    return result


def run_all(tests=None, verbose=True):
    """Run all tests and produce summary."""
    if tests is None:
        tests = TESTS

    results = []
    for t in tests:
        r = run_test(t, verbose=verbose)
        results.append(r)

    # Summary
    print(f"\n\n{'='*70}")
    print(f"  RÉSUMÉ — {len(results)} TESTS")
    print(f"{'='*70}\n")

    for r in results:
        p = r["pattern"]
        match = "✅" if r.get("pattern_match") else "⚠️"
        cold = "🧊" if r.get("desc", "").find("FROIDE") >= 0 else "  "
        print(f"  #{r['id']:>2}  {match} {cold}  {r['name']:<40}  "
              f"{p['pattern']:<20} x{p['growth_ratio']}  "
              f"lianes={r['lianes']['n_lianes']}")

    # Save
    outpath = Path("tests_33_plus.json")
    with open(outpath, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2, default=str)
    print(f"\n  → {outpath}")

    return results


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        # Run specific test by id
        tid = int(sys.argv[1])
        test = next((t for t in TESTS if t["id"] == tid), None)
        if test:
            run_test(test)
        else:
            print(f"Test #{tid} not found")
    else:
        run_all()
