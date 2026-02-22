# TEST #42: DDPM — Physique Statistique × Modèles Génératifs

## Thèse pont
**Ho et al. 2020** — "Denoising Diffusion Probabilistic Models" (UC Berkeley)
- Applique les processus de diffusion (thermodynamique hors-équilibre) à la génération d'images
- ~15,000+ citations
- Proto-pont: **Sohl-Dickstein et al. 2015** "Deep Unsupervised Learning using Nonequilibrium Thermodynamics"

**Thèse**: Un processus physique (diffusion brownienne = ajout de bruit) peut être INVERSÉ par un réseau de neurones pour générer des données. La physique statistique DEVIENT un algorithme de génération.

## Cartographie du trou AVANT

| Période | SP×GM/an | Diagnostic |
|---------|----------|------------|
| 2010-2012 | 0-2 | **ZÉRO**. Physique statistique et modèles génératifs = mondes séparés |
| 2013-2016 | 4-6 | Quasi-ZÉRO. Deep Boltzmann Machines (Hinton 2009) = seul pont |
| 2017-2019 | 3-11 | Proto-signal. Sohl-Dickstein 2015 plante la graine |

Le TROU: la physique statistique (30K papers/an) et les modèles génératifs (300→2000 papers/an) ne se parlaient PAS. Le seul pont historique était les Boltzmann Machines (Hinton), qui empruntaient le NOM de la physique mais pas les MATHS.

Sohl-Dickstein 2015 a posé l'idée (diffusion = génération) mais PERSONNE n'a suivi pendant 5 ans.

## Données OpenAlex

**StatPhys (C121864883) × GenModel (C167966045):**
| 2010 | 2013 | 2016 | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | 2025 |
|------|------|------|------|------|------|------|------|------|------|
| 2    | 6    | 5    | 11   | **26** | 22   | 27   | 57   | 66   | **228** |

**DiffProcess (C68710425) × GenModel:**
| 2010-2020 | 2021 | 2022 | 2023 | 2025 |
|-----------|------|------|------|------|
| **0**     | 3    | 15   | 26   | 45   |

## Pattern APRÈS le pont

- **Ho 2020** = année charnière: SP×GM passe de 11 (2019) à 26 (2020) = x2.4
- 2020→2025: 26→228 = **x8.8** en 5 ans
- DiffProcess×GenModel: **ZÉRO pendant 10 ans** puis 3→45
- 2025 = explosion: 228 papers, x3.5 vs 2024

## Bridge papers (top cited)
- **Salakhutdinov & Hinton 2009** (1,769 cit): Deep Boltzmann Machines — le proto-pont physique↔génération
- **Xu et al. 2022** (171 cit): GeoDiff — diffusion pour conformations moléculaires (propagation vers Chimie!)
- **Henighan et al. 2020** (149 cit): Scaling Laws — lois d'échelle physique↔ML

## Lianes S0 utilisées
DDPM utilise: {exp (score matching), ∂ (SDE reverse), ∫ (forward process), W(t) (Wiener/brownien), S_ent (entropie), N(μ,σ²) (gaussien)}
- exp = universelle (6 continents)
- W(t) = liane Fin×Phys×Math (3 continents)
- S_ent = liane Phys×Chim×IA (3 continents)
- SDE = liane Fin×Phys×Bio (3 continents)

**4 lianes S0 multi-continents actives dans le pont.** La formule "Découverte = Liane + Pont + Timing" se vérifie:
- Liane: W(t), S_ent, exp, ∂
- Pont: Ho 2020
- Timing: 5 ans après Sohl-Dickstein, quand la puissance GPU le permettait

## Validé ✅ — Pattern 1 (Pont) — ZÉRO 10 ans puis x8.8 post-Ho 2020
