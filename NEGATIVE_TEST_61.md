# TEST NÉGATIF #61: Papers Ponts vs Papers Intra-Domaine
## Diversité conceptuelle — OpenAlex concept tagging

---

## Méthode
10 papers PONTS connus (de nos tests) vs 10 papers INTRA-DOMAINE (fondateurs d'un seul champ).
Mesure: nombre de domaines L0, champs L1, et concepts totaux tagués par OpenAlex.

**Limite**: la recherche par titre n'a pas toujours retourné le bon paper. Certains résultats sont des papers connexes mais pas les papers ciblés. Les résultats sont donc INDICATIFS, pas définitifs.

## Résultats

| Mesure | Papers PONTS | Papers INTRA | Différence |
|--------|-------------|-------------|------------|
| L0 domains (avg) | **3.0** | 2.8 | +7% |
| L1 fields (avg) | **5.9** | 3.8 | **+55%** |
| Concepts total (avg) | **17.2** | 13.2 | **+30%** |

## Analyse

### Ce qui FONCTIONNE
**L1 field diversity est le meilleur discriminant.**
Les papers ponts touchent en moyenne 5.9 champs L1 vs 3.8 pour les intra-domaine. C'est +55% — un signal réel.

Exemples:
- AlphaGo (PONT): 7 champs L1 — AI, Algorithm, ML, Math analysis, Stats, Law, Math economics
- DNA Watson-Crick (INTRA): 2 champs L1 — Biochemistry, Polymer science
- Black-Scholes (PONT): 6 champs L1 — Actuarial, Econometrics, Finance, Financial economics, Law, Monetary
- DFT Becke (INTRA): 6 champs L1 — mais TOUS en physique/chimie (Atomic, Computational chem, Condensed matter, Organic, Physical, Quantum)

### Ce qui NE FONCTIONNE PAS
**L0 domain count ne discrimine pas (3.0 vs 2.8).**
Pourquoi? OpenAlex tague TRÈS largement au L0. Un paper de linguistique computationnelle se retrouve tagué "Computer science + Philosophy". Un paper de génomique computationnelle est "Biology + Computer science". Le L0 est trop grossier.

### Ce qu'on NE PEUT PAS tester avec OpenAlex
**Les lianes S0 (symboles mathématiques).** La question "est-ce que les papers ponts utilisent plus de exp, ∂, Σ?" nécessiterait de LIRE les papers et d'identifier les symboles. OpenAlex ne tague pas les outils mathématiques, seulement les concepts thématiques.

## Verdict sur les lianes S0

| Question | Réponse | Preuve |
|----------|---------|--------|
| Les papers ponts touchent plus de domaines? | **OUI** (+55% L1) | OpenAlex, signal réel |
| Les papers ponts utilisent plus de lianes S0? | **PROBABLE mais non prouvé** | Cohérent avec L1, mais pas testable via API |
| Les lianes CAUSENT les ponts? | **Non prouvé** | Corrélation ≠ causalité |

**Pour prouver la causalité des lianes**, il faudrait:
1. Parser le LaTeX/PDF de 100 papers ponts et 100 papers intra
2. Compter les symboles mathématiques utilisés
3. Comparer les distributions
4. Tester statistiquement (Mann-Whitney U)

C'est faisable mais pas avec l'API OpenAlex seule.

## Validé partiellement ✅ — Signal L1 (+55%), lianes S0 non testables via API
