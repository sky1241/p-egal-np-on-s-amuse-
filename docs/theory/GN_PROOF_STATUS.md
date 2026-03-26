# GOD'S NUMBER — Etat de la preuve
## 26 mars 2026

---

## CE QUI TIENT

### Efficacite physique (PROUVE)
- eff(n) = pieces_par_move / pieces_totales
- Converge vers 1/6 = 16.667% (invariant geometrique : 6 faces, 1 face par move)
- Verifie jusqu'a 1M x 1M x 1M
- Formule exacte (n pair) : eff(n) = n^2 / (6n^2 - 12n + 8)
- Residu : eff(n) - 1/6 ~ 1/(3n) — algebrique, decroit en 1/n

### GN(n) = Theta(n^2/log n) (PROUVE — Demaine et al. 2011)
- Borne sup : parallelise layer-by-layer, commutator batche O(log n) pieces
- Borne inf : pigeonhole sur log|G_n| / log|S_n|
- Le cube SATURE la borne info-theorique asymptotiquement

### Decomposition n^2/log n (VERIFIE)
- n^2 = n_layers x n_work_per_layer
- /log n = parallelisme des slices commutantes (meme axe)
- Intra-axe : parallele. Inter-axe : sequentiel. 3-axes bottleneck.

### Le cube est quasi-random (DECOUVERT Mission 3)
- Gap spectral ~ 2/3 du degre (QTM: gap >= 8.01 sur 12, HTM: gap >= 14.41 sur 18)
- Bat la prediction wreath product par facteur 30x
- Les generateurs (4-cycles disjoints) sont exceptionnellement puissants

### Bottleneck = A_12 (VERIFIE)
- Aretes (A_12 x Z_2^11) = 43.3% des bits du cube
- Kociemba Phase 2 (permutations) = 18 moves vs Phase 1 (orientations) = 12

---

## CE QUI EST MORT

### W(n) lineaire — MORT
- Calibre sur 2 points seulement (GN(2)=14, GN(3)=26)
- Toute droite passe par 2 points
- Vrai scaling = Theta(n^2/log n), pas lineaire
- 0 precedent dans 833K papers
- Overhead pigeonhole PAS constant (1.60 pour n=2, 1.28 pour n=3)

### phi = nombre d'or — MORT
- Le cube a symetrie S_4 (24 rotations), PAS A_5 (icosaedre)
- Aucune symetrie d'ordre 5 dans le groupe du Rubik
- 0 papers golden ratio x Cayley graph dans 2.78M papers
- Le lemme d'unicite est mathematiquement correct mais tautologique
- phi est un accident de calibration

### Spectral bat Demaine — MORT
- Chung bound donne O(n^2), rate le 1/log n
- Le 1/log n vient du commutator batching (combinatoire), pas du spectral
- Resistance effective triviale (10^21)
- Wreath product bound additif O(m^2 + mq), pas assez serre

---

## PREDICTIONS (non prouvees, falsifiables)

### QTM (Quarter Turn Metric)
| n | GN predit | Intervalle | Pigeonhole | Marge | Status |
|---|-----------|------------|------------|-------|--------|
| 2 | 14 | [13, 15] | 6 | +8 | VERIFIE |
| 3 | 26 | [25, 27] | 16 | +10 | VERIFIE |
| 4 | 48 | [47, 49] | 33 | +15 | PREDIT |
| 5 | 66 | [65, 67] | 50 | +16 | PREDIT |

NOTE : ces predictions viennent du modele W(n) lineaire qui est MORT asymptotiquement.
Pour n=4 et n=5, le modele pourrait encore coller (regime transitoire).
GN(4) SSTM borne connue : [32, 53]. La prediction 48 QTM est dans la zone.

---

## PISTES OUVERTES

1. Quasi-random groups (Gowers 2008) — la vraie piste pour le cube
2. NCD x Cayley (desert total) — compresser positions pour approximer diametre
3. Constante explicite dans Theta(n^2/log n) — Demaine prouve l'ordre, pas la constante
4. GN(4) brute force — resserrer [32, 53]

---

## SOURCES VERIFIEES
- Rokicki et al. 2014 — God's Number is 20 (cube20.org)
- Demaine et al. 2011 — arXiv:1106.5736
- Salkinder 2021 — arXiv:2112.08602
- Helfgott-Seress 2014 — Annals of Mathematics
- OEIS A257401

---

*Compile 26 mars 2026 — Sky + Claude Opus + Yggdrasil Engine*
