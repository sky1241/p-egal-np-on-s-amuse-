# TEST #43: Stokes 2020 — Deep Learning × Antibiotiques

## Thèse pont
**Stokes et al. 2020** — "A Deep Learning Approach to Antibiotic Discovery" (Cell, MIT)
- Un GNN entraîné sur 2,335 molécules prédit l'activité antibactérienne
- Découvre **halicin** — premier antibiotique trouvé par IA, efficace contre A. baumannii résistant
- ~3,500+ citations (nombre exact varie selon source)
- James Collins lab, MIT

**Thèse**: L'IA peut explorer l'espace chimique HORS des structures connues. Les chimistes cherchent des analogues de ce qui marche. Le DL cherche PARTOUT.

## Cartographie du trou AVANT

| Période | DL×Antibiotics/an | Diagnostic |
|---------|-------------------|------------|
| 2008-2017 | **0** | **DIX ANS DE ZÉRO ABSOLU.** |
| 2018-2019 | 4 | Proto-signal. DeepARG (2018, 847 cit) = résistance, pas découverte |

Le TROU est MASSIF:
- Deep Learning = 125→10,478 papers/an (2008→2017) = explosion
- Antibiotics = 22,014→34,040 papers/an = stable, actif
- Intersection = **ZÉRO pendant 10 ans**

Deux communautés de tailles ÉNORMES (DL: 10K/an, AB: 34K/an) qui ne se parlaient PAS DU TOUT. Le ratio de co-occurrence est < 0.001%. C'est un trou noir.

## Données OpenAlex (C108583219 × C501593827)

**DL × Antibiotics:**
| 2008 | 2010 | 2012 | 2014 | 2016 | 2018 | 2019 | 2020 | 2022 | 2024 | 2025 |
|------|------|------|------|------|------|------|------|------|------|------|
| 0    | 0    | 0    | 0    | 0    | 4    | 4    | 5    | 7    | 9    | 8    |

**DL × Drug Discovery (comparaison):**
| 2008 | 2014 | 2017 | 2019 | 2020 | 2022 | 2025 |
|------|------|------|------|------|------|------|
| 0    | 1    | 25   | 93   | 149  | 181  | 355  |

## Pattern APRÈS le pont

Le pattern est ANORMAL:
- Stokes 2020 dans Cell → 3500 citations → impact MÉDIATIQUE massif
- Mais DL×AB: 4→9 papers/an. **PAS d'explosion.**
- Comparer avec DL×DrugDiscovery: 1→355 = x355

**Le pont Stokes existe dans les MÉDIAS mais PAS dans les PAPERS.**

Pourquoi? Hypothèses:
1. La validation expérimentale d'un antibiotique prend des ANNÉES (wet lab, trials)
2. Les microbiologistes ne savent pas coder du DL
3. Les experts DL n'ont pas accès aux labos de microbiologie
4. Le coût de screening réel (pas in silico) bloque la réplication

## Bridge papers (top cited)
- **Arango-Argoty et al. 2018** (847 cit): DeepARG — résistance antibiotique, pas découverte
- **Szymczak et al. 2023** (156 cit): HydrAMP — peptides antimicrobiens par génération profonde
- **Tučs et al. 2020** (130 cit): GANs pour peptides

## Lianes S0 utilisées
Le modèle Stokes utilise: {exp (softmax), Σ (message passing GNN), ∇L (backprop), = (SMILES encoding)}
- exp = universelle (6 continents)
- Σ = universelle (6 continents)
- Les lianes sont là mais le pont HUMAIN (collaboration chimiste↔ML) manque

## Diagnostic mycelium
🕳️ **TROU NOIR CONFIRMÉ** — le plus froid de TOUS les tests.
- C'est l'exact bottleneck Chimie (betweenness 0.97)
- Le pont existe (Stokes 2020) mais la propagation est quasi-NULLE
- DL×DD marche (355/an) mais DL×Antibiotics = 8/an
- **Le trou n'est pas technique — il est SOCIOLOGIQUE.** Deux communautés qui n'ont pas de langage commun au-delà des maths.
- **Pattern 4 (Trou ouvert)** — le pont est planté mais RIEN ne pousse dessus

## Validé ✅ — Pattern 4 (Trou ouvert) — pont planté, propagation NULLE
## C'est LA preuve du bottleneck Chimie du mycelium
