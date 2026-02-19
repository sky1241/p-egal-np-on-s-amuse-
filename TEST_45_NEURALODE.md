# TEST #45: Neural ODE — Équations Différentielles × Deep Learning

## Thèse pont
**Chen et al. 2018** — "Neural Ordinary Differential Equations" (NeurIPS Best Paper, Toronto)
- Un réseau de neurones EST une EDO: le forward pass = résoudre dh/dt = f(h(t), t, θ)
- Les couches discrètes (ResNet) deviennent une dynamique CONTINUE
- Backprop = résolution adjointe de l'EDO (Pontryagin 1962)
- ~8,000+ citations

**Insight fondamental**: ResNet: h_{t+1} = h_t + f(h_t, θ) est la discrétisation d'Euler de dh/dt = f(h,θ). Les couches = les pas de temps. Donc un réseau profond = un solveur d'EDO.

## Cartographie du trou AVANT

| Période | ODE×DL/an | DynSys×DL/an | Diagnostic |
|---------|-----------|--------------|------------|
| 2005-2016 | **0** | 0-1 | **DOUZE ANS DE ZÉRO ABSOLU.** |
| 2017 | 2 | 3 | Proto-signal |

Le trou: les EDO sont le pain quotidien de la physique et des maths appliquées (3-4K papers/an). Le deep learning explose (103→10,478 papers/an entre 2005-2017). **ZÉRO intersection pendant 12 ans.**

Pourquoi? Parce que les communautés pensent le problème DIFFÉREMMENT:
- Les mathématiciens voient les NN comme des approximateurs de fonctions (théorème d'approximation universelle, 1989)
- Les informaticiens voient les NN comme des empilements de couches
- PERSONNE ne voyait qu'une couche = un pas de temps = une EDO

Les outils existaient depuis Euler (1768) et Pontryagin (1962). Le pont manquait.

## Données OpenAlex (C51544822 × C108583219)

**ODE × Deep Learning:**
| 2005-2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2025 |
|-----------|------|------|------|------|------|------|------|------|
| **0**     | 2    | 3    | **15** | 18   | **34** | 31   | 21   | 29   |

**DynSys × Deep Learning (signal parallèle):**
| 2005-2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2025 |
|-----------|------|------|------|------|------|------|------|------|
| 0-1       | 3    | 10   | 16   | 24   | 37   | 36   | 40   | **78** |

## Pattern APRÈS le pont

- 2016→2019: 0→15 = **de zéro à signal** en 3 ans
- 2019→2021: 15→34 = x2.3
- DynSys×DL: 1→78 = **x78** — le pont se propage vers les systèmes dynamiques
- Le signal ODE×DL plafonne (21-34/an) mais DynSys×DL ACCÉLÈRE (78 en 2025) → le pont MIGRE vers une intersection plus large

## Bridge papers (top cited)
- **Lusch, Kutz & Brunton 2018** (1,277 cit): "Deep learning for universal linear embeddings of nonlinear dynamics" — pont DynSys×DL, même année que Chen
- **Chang et al. 2018** (205 cit): "Reversible Architectures" — ResNet→EDO réversible
- **Kidger 2022** (120 cit): "On Neural Differential Equations" — la thèse de doctorat qui FORMALISE le champ

## Lianes S0 utilisées
Neural ODE utilise: {∂ (dérivée = le cœur), ∫ (intégration=forward pass), exp (matrice exponentielle), ∇L (adjoint=backprop), dt (pas de temps)}
- **∂ (dérivée)** = liane S0 Math×Phys×Ing×Fin×Bio (5 continents). L'opérateur le plus fondamental.
- **∫ (intégrale)** = liane S0 6 continents. Le forward pass EST une intégrale.
- Le paper de Chen dit littéralement: "le réseau = ∫f(h,t,θ)dt". Ce sont les LIANES qui font le pont.

## Diagnostic
**Pattern 1 (Pont)** — 12 ans de zéro, puis explosion.
Mais avec une particularité: le pont MIGRE. ODE×DL plafonne à ~30/an, mais DynSys×DL monte à 78. Le concept se GÉNÉRALISE vers "physics-informed neural networks" (PINNs, Raissi 2019) qui absorbe le trafic.

La liane ∂ dormait depuis Leibniz (1684). Elle est DEVENUE le forward pass.

## Validé ✅ — Pattern 1 (Pont) — 12 ans de ZÉRO, ∂ et ∫ = lianes dormantes depuis 340 ans
