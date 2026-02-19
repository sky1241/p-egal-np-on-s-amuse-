# TEST #46: PINNs — Équations aux Dérivées Partielles × Deep Learning

## Thèse pont
**Raissi, Perdikaris & Karniadakis 2019** — "Physics-Informed Neural Networks: A Deep Learning Framework for Solving Forward and Inverse Problems Involving Nonlinear PDEs" (JCP, Brown University)
- Intègre les lois physiques (EDP) DIRECTEMENT dans la loss function du réseau
- Le réseau apprend à respecter ∂u/∂t + N[u] = 0 comme contrainte, pas comme donnée
- ~13,000+ citations

**Proto-pont**: Han, Jentzen & E 2018 (1,622 cit) "Solving high-dimensional PDE using deep learning" — le premier à montrer que DL bat les méthodes classiques pour les EDP en haute dimension

**Thèse**: Les EDP sont INSOLUBLES analytiquement dans la plupart des cas réels (turbulence, climat, matériaux). Les méthodes numériques (FEM, FDM) sont O(n³) en dimension. Un réseau de neurones peut CONTOURNER la malédiction de la dimensionnalité en encodant la physique dans sa structure.

## Cartographie du trou AVANT

| Période | PDE×DL/an | Phys×DL/an | Diagnostic |
|---------|-----------|------------|------------|
| 2005-2012 | **0** | 13→65 | ZÉRO pour PDE×DL. La physique large parle au DL mais PAS les EDP. |
| 2013-2016 | 0-3 | 96→813 | Phys×DL explose (AlexNet 2012). PDE reste à ZÉRO. |
| 2017 | 5 | 1,807 | Proto-signal. |

Le trou est CHIRURGICAL: la physique au sens large adopte le DL massivement (15→10K), mais les EDP — le cœur mathématique de la physique — restent à ZÉRO pendant 12 ans.

Pourquoi? Les physiciens des EDP ont leur propre arsenal (FEM, spectral, Monte Carlo). Le DL est vu comme une boîte noire sans garantie physique. Le pont manquant = comment injecter ∂u/∂t + N[u] = 0 dans un gradient descent.

## Données OpenAlex (C93779851 × C108583219)

**PDE × Deep Learning:**
| 2005 | 2010 | 2014 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2025 |
|------|------|------|------|------|------|------|------|------|------|------|------|
| 0    | 0    | 1    | 3    | 5    | **16** | 26   | 38   | **66** | 83   | **97** | 59   |

**Physics × Deep Learning (comparaison large):**
| 2005 | 2010 | 2017 | 2020 | 2023 |
|------|------|------|------|------|
| 15   | 53   | 1,807 | 6,671 | 10,588 |

## Pattern APRÈS le pont

- Pré-pont (2005-2016): PDE×DL = 0-3 pendant 12 ans
- 2018 = année charnière: Han et al. (JCP) + Raissi (arxiv preprint)
- 2018→2023: 16→97 = **x6** en 5 ans
- Phys×DL: 1807→10588 = **x5.9** sur la même période → les EDP suivent le rythme global Phys×DL

## Bridge papers (top cited)
- **Han, Jentzen & E 2018** (1,622 cit): LE premier bridge — DL pour EDP haute dimension
- **Berg & Nyström 2018** (623 cit): DNN pour EDP en géométries complexes
- **Raissi 2018** (438 cit): "Deep Hidden Physics Models" — le preprint qui deviendra PINNs

## Lianes S0 utilisées
PINNs utilise: {∂ (dérivées partielles = LE cœur), ∇² (Laplacien), ∫ (conditions aux limites), exp (activation), ∇L (backprop), Σ (discrétisation)}
- **∂** = liane 5 continents (Math×Phys×Ing×Fin×Bio). L'opérateur ∂u/∂t est LITTÉRALEMENT dans la loss function.
- **∇²** = Laplacien, liane Math×Phys×Ing. Déjà vu en Test #44 (GCN).
- Les deux tests (#44 GCN et #46 PINNs) utilisent les MÊMES lianes (∂, ∇², Σ) pour des ponts DIFFÉRENTS.

## Diagnostic
**Pattern 1 (Pont)** — 12 ans de zéro, percée 2018, explosion continue.
Mais comparé au test #45 (Neural ODE), le signal PDE×DL est 3x plus fort (97 vs 34) car les EDP ont plus d'applications industrielles (turbulence, météo, matériaux).

La liane ∂ apparaît dans TROIS tests consécutifs (#44 GCN, #45 Neural ODE, #46 PINNs). C'est l'opérateur-pont le plus actif de la période 2017-2023.

## Validé ✅ — Pattern 1 (Pont) — 12 ans de ZÉRO, ∂ = liane triple-pont 2017-2023
