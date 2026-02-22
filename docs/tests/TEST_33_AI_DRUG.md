# TEST #33: ML × Drug Discovery — Zone froide Chimie × IA

## Données OpenAlex (concepts: C119857082 × C74187038)

**ML × Drug Discovery (co-occurrence):**
| 2005 | 2008 | 2010 | 2013 | 2016 | 2018 | 2019 | 2020 | 2021 | 2023 | 2025 |
|------|------|------|------|------|------|------|------|------|------|------|
| 70   | 122  | 147  | 193  | 202  | 356  | 494  | 715  | 823  | 1048 | 1125 |

**DL × Drug Discovery (co-occurrence plus fine):**
| 2005 | 2010 | 2014 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2023 | 2025 |
|------|------|------|------|------|------|------|------|------|------|------|
| 0    | 0    | 1    | 12   | 25   | 66   | 93   | 149  | 196  | 232  | 355  |

## Bridge papers
- **Vamathevan et al. 2019** (2,690 cit): "Applications of machine learning in drug discovery and development" — review qui cristallise le pont
- **Mysinger et al. 2012** (2,307 cit): DUD-E benchmark — outil qui permet le pont ML→docking
- **Egan & Merz 2000** (1,872 cit): prediction ADME avec stats multivariées — proto-pont

## Résultat

**Deux signaux superposés:**
- ML×DD: croissance continue 70→1125 = **x16** en 20 ans. PAS de zéro. La Chimie parlait déjà au ML classique (random forests, SVM pour QSAR). → **Pattern 2 (Dense)**
- DL×DD: ZÉRO jusqu'en 2015, puis 1→355 = explosion post-AlexNet. Le Deep Learning est le VRAI pont, pas le ML classique. → **Pattern 1 (Pont)**

**Le pont DL est Stokes et al. 2020** (Cell): premier antibiotique découvert par deep learning (halicin). Mais la cristallisation du champ vient de Vamathevan 2019.

## Diagnostic mycelium
🧊 Zone froide confirmée mais EN RÉCHAUFFEMENT.
- ML×DD = x16 (lent, dense) : les QSAR existaient depuis les années 90
- DL×DD = x355 (explosion) : le deep learning force le pont
- Le bottleneck Chimie (betweenness 0.97) se réduit côté IA, mais les 4 lianes {=, ln, exp, S_ent} restent le seul vocabulaire partagé.

## Validé ✅ — Pattern 2 (ML) + Pattern 1 en formation (DL) — zone froide en réchauffement
