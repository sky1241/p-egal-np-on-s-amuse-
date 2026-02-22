# TEST #23: Transformer Architecture — Attention × NLP × Vision

## Données OpenAlex

**transformer + attention mechanism (total papers/an):**
| 2010 | 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2022 | 2024 |
|------|------|------|------|------|------|------|------|------|
| 7    | 7    | 12   | 9    | 47   | 201  | 420  | 2191 | 4109 |

**transformer × language model (NLP bridge):**
| 2015 | 2016 | 2017 | 2018 | 2019 | 2020 | 2022 | 2024 |
|------|------|------|------|------|------|------|------|
| 19   | 19   | 19   | 66   | 497  | 1476 | 3576 | 5896 |

**vision transformer × image (CV bridge):**
| 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2024 |
|------|------|------|------|------|------|------|
| 20   | 24   | 40   | 80   | 689  | 2034 | 3589 |

## Bridge paper
- **Vaswani et al. 2017**: "Attention Is All You Need" — **~160 000+ citations** (Semantic Scholar) / **~204 000+ (Google Scholar)** — papier le plus cité en IA
- ⚠️ CORRECTION: le chiffre initial (6 488) provenait d'une requête OpenAlex filtrée. Le vrai total est ~30x supérieur.
- Pont entre sequence-to-sequence models et parallel computation
- Puis 2e pont: Dosovitskiy et al. 2020 (ViT) = NLP→Computer Vision

## Résultat
- Pré-bridge (2010-2017): quasi-ZÉRO (<12 papers/an)
- Post-bridge NLP: 19→5896 = **x310**
- Post-bridge Vision: 20→3589 = **x179** (avec 3 ans de retard, 2e pont ViT 2020)
- **Pattern 1: PONT ✅** — deux continents (NLP sequences + parallel architectures), UN paper les fusionne, explosion PUIS propagation cross-domaine vers vision (2e pont)

## Validé ✅ — Pattern 1 (Pont) + propagation cross-domaine
