# TEST #35: DL × Protein Structure Prediction — IA × Bio

## Données OpenAlex (C108583219 × C18051474)

**DL × PSP:**
| 2005-2010 | 2011 | 2015 | 2016 | 2017 | 2019 | 2020 | 2021 | 2022 | 2025 |
|-----------|------|------|------|------|------|------|------|------|------|
| 0         | 1    | 4    | 9    | 27   | 42   | 48   | 71   | 80   | 65   |

## Bridge paper
- **Baek et al. 2021** (5,350 cit): RoseTTAFold — "Accurate prediction of protein structures" 
- **Dauparas et al. 2022** (1,537 cit): ProteinMPNN — design inverse
- **Yang et al. 2020** (1,512 cit): trpl.AI — interresidue orientations

## Résultat
- DL×PSP: ZÉRO 2005-2010, puis 1→80 = **Pattern 1 (Pont)**
- Pic en 2022 (80) post-AlphaFold2 (2021). Confirme test #15.
- ML×PS (protein structure broad): 104→267, toujours connecté → le ML classique parlait déjà à la protéomique structurale.
- Le pont DL est AlphaFold/RoseTTAFold. Lianes utilisées: {∂, ∫, exp, ∇L, Attn, SGD}

## Validé ✅ — Pattern 1 (Pont) — confirme test #15 AlphaFold avec données plus fines

---

# TEST #36: ML × Synthetic Biology — IA × Bio/Ing

## Données OpenAlex (C119857082 × C191908910)

**ML × SynBio:**
| 2005 | 2008 | 2010 | 2013 | 2016 | 2018 | 2020 | 2022 | 2023 | 2025 |
|------|------|------|------|------|------|------|------|------|------|
| 1    | 2    | 8    | 15   | 15   | 22   | 35   | 49   | 47   | 69   |

**DL × SynBio:**
| 2005-2017 | 2018 | 2019 | 2020 | 2022 | 2023 | 2025 |
|-----------|------|------|------|------|------|------|
| 0         | 2    | 3    | 3    | 12   | 16   | 29   |

## Bridge paper
- **Cui et al. 2024** (797 cit): scGPT — foundation model single-cell → le LLM de la bio
- Pas de bridge paper historique dominant. Le champ est NAISSANT.

## Résultat
- ML×SB: 1→69 = x69, mais nombres ABSOLUS très petits. Max 69 papers/an. C'est un **Pattern 4 (Trou ouvert en cours de remplissage)**.
- DL×SB: ZÉRO → 29. Le deep learning vient juste d'arriver en synthetic biology.
- La connexion passe par les protein language models (scGPT, ESM) — c'est le pont en construction.

## Validé ✅ — Pattern 4 (Trou ouvert) transitionnant vers Pattern 1 — le pont est en construction

---

# TEST #37: Neuromorphic × Deep Learning — Ing × IA

## Données OpenAlex (C151927369 × C108583219)

**Neuromorphic × DL:**
| 2005-2012 | 2013 | 2014 | 2016 | 2018 | 2019 | 2020 | 2022 | 2023 | 2025 |
|-----------|------|------|------|------|------|------|------|------|------|
| 0         | 2    | 5    | 23   | 67   | 67   | 83   | 111  | 107  | 147  |

**Neuromorphic × ML (plus large):**
| 2005 | 2010 | 2014 | 2017 | 2019 | 2021 | 2023 | 2025 |
|------|------|------|------|------|------|------|------|
| 5    | 19   | 75   | 138  | 280  | 463  | 669  | 286  |

## Bridge papers
- **Peng Yao et al. 2020** (2,024 cit): "Fully hardware-implemented memristor CNN" — LE pont hardware
- **Xia & Yang 2019** (1,652 cit): "Memristive crossbar arrays for brain-inspired computing"
- **Feldmann et al. 2019** (1,432 cit): "All-optical spiking neurosynaptic networks"

## Résultat
- N×DL: ZÉRO pendant 8 ans (2005-2012), puis 2→147 = **Pattern 1 (Pont)**
- N×ML: 5→669 = **x134**, croissance continue mais accélérée post-2014 → Pattern 2 dense mais le DL est le catalyseur
- Le pont est le memristor (Yao 2020). Le hardware physique rencontre l'algorithme. Lianes: {exp, ∂, Σ, =}

## Validé ✅ — Pattern 1 (Pont) — memristor = pont physique entre hardware et DL

---

# TEST #38: Molecular Dynamics × ML — Chimie × IA (Zone froide)

## Données OpenAlex (C59593255 × C119857082)

**MD × ML:**
| 2005 | 2008 | 2010 | 2013 | 2016 | 2018 | 2020 | 2022 | 2023 | 2025 |
|------|------|------|------|------|------|------|------|------|------|
| 84   | 88   | 94   | 119  | 164  | 192  | 300  | 299  | 334  | 462  |

**MD × DL:**
| 2005-2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2025 |
|-----------|------|------|------|------|------|------|------|------|
| 0         | 1    | 6    | 7    | 10   | 18   | 20   | 27   | 76   |

## Bridge papers
- **Maier et al. 2015** (10,559 cit): ff14SB force field — PAS un bridge ML, c'est de la MD pure
- **Greengard & Rokhlin 1987** (4,847 cit): Fast Multipole Method — algorithmique, pas ML
- Le vrai bridge est **Noé et al. 2019** (Science): "Boltzmann generators" — deep learning pour sampling MD

## Résultat
- MD×ML: 84→462 = **x5.5**. Croissance lente mais constante → Pattern 2 (Dense faible)
- MD×DL: ZÉRO → 76. Explosion 2025 (+x4 vs 2023). Le DL arrive dans la dynamique moléculaire.
- La croissance en 2025 (76) vs 2023 (27) = **x2.8 en 2 ans**. Accélération nette.

## Diagnostic mycelium
🧊 Zone froide en RÉCHAUFFEMENT RAPIDE. Même pattern que #33 et #34: le ML classique parlait déjà à la Chimie computationnelle, mais le DL force le pont.

## Validé ✅ — Pattern 2 (Dense) + P1 en formation (DL) — zone froide accélération nette en 2025

---

# TEST #39: Quantum Computer × Quantum Chemistry — Phys × Chimie

## Données OpenAlex (C58053490 × C183971685)

**QComp × Ab initio Quantum Chemistry:**
| 2000-2004 | 2005-2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|-----------|-----------|------|------|------|------|------|------|------|------|------|
| 0-2       | 0-2       | 0    | 1    | 2    | 1    | 1    | 1    | 1    | 1    | **17** |

## Bridge papers
- **Gali 2019** (250 cit): NV center ab initio — niche
- **Thiering & Gali 2018** (161 cit): NV magneto-optical spectrum
- Pas de bridge paper majeur. Le champ n'existe PAS encore.

## Résultat
- QC×QChem: ZÉRO pendant **25 ans** (2000-2024), 0-2 papers/an maximum.
- 2025: **17 papers** — saut brutal x17 vs baseline.
- Quantum computing EXPLOSE (513→9191 = x18). Quantum chemistry est stable (~1400/an).
- **Le trou est EN TRAIN de se combler.** Mais c'est LE TOUT DÉBUT.

## Diagnostic mycelium
🕳️ **TROU NOIR** pendant 25 ans. Phys×Chimie est la 5ème connexion du mycelium (9 lianes), mais quantum computer × quantum chemistry = ZÉRO intersection malgré le nom partagé.
Le saut 2025 (17 papers) est peut-être le signal d'un Pattern 1 naissant. Il faudrait vérifier dans 1-2 ans.
Lianes théoriques partagées: {∫, ∬, ∮, ∇², S_ent, PV=nRT, =, ln, exp}

## Validé ✅ — Pattern 4 (Trou noir) avec signal 2025 — PRÉDICTION: P1 en formation

---

# TEST #40: Reinforcement Learning × Robotics — IA × Ing

## Données OpenAlex (C97541855 × C90509273)

**RL × Robot:**
| 2005 | 2008 | 2010 | 2013 | 2016 | 2017 | 2018 | 2019 | 2020 | 2022 | 2023 | 2025 |
|------|------|------|------|------|------|------|------|------|------|------|------|
| 175  | 182  | 169  | 219  | 227  | 365  | 617  | 945  | 1264 | 1823 | 2251 | 1328 |

## Bridge papers
- **Russell & Norvig 1995** (22,208 cit): AIMA — LE textbook (pas un bridge, c'est un fondement)
- **Arulkumaran et al. 2017** (4,070 cit): "Deep RL: A Brief Survey"
- **Kober et al. 2013** (2,963 cit): "RL in robotics: A survey" — LE bridge paper

## Résultat
- RL×Rob: 175→2251 = **x13**. Jamais ZÉRO. Croissance accélérée post-2016 (DQN/A3C).
- **Pattern 2 (Dense)** — les deux domaines ont TOUJOURS été connectés.
- L'accélération post-2016 vient de DeepMind (DQN 2015, AlphaGo 2016, Sim-to-Real 2018).
- Lianes: {exp, Σ, ∇L, SGD, Bayes, P(A), E[X]}

## Validé ✅ — Pattern 2 (Dense) avec accélération post-2016 — jamais de trou
