# TEST #49: Black-Scholes 1973 — Processus Stochastiques × Finance

## Thèse pont
**Black & Scholes 1973** — "The Pricing of Options and Corporate Liabilities" (Journal of Political Economy, ~40,000 citations)
- Utilise le mouvement brownien (Einstein 1905, physique) pour pricer des options financières
- Formule: C = S·N(d₁) - K·e^(-rT)·N(d₂) avec d₁ contenant √T et σ (volatilité)
- Nobel 1997 (Scholes & Merton)

**Proto-pont**: **Bachelier 1900** — "Théorie de la spéculation" (thèse de doctorat, Paris)
- Premier à utiliser le mouvement brownien pour modéliser les prix financiers
- 5 ans AVANT Einstein (1905). Ignoré pendant 60 ans.

**Thèse**: Le mouvement brownien W(t) — inventé pour décrire le pollen dans l'eau — décrit aussi les marchés financiers. La physique statistique DEVIENT un outil de pricing.

## Cartographie du trou AVANT

| Période | SP×FE/an | BM×FE/an | Diagnostic |
|---------|----------|----------|------------|
| 1970-1972 | 0-5 | 0 | **ZÉRO**. Stochastic process = mathématiques pures. Finance = économétrie classique. |
| 1973 | 1 | 0 | Black-Scholes publié. Co-occurrence = **ZÉRO**. |
| 1974-1985 | 0-3 | 0-1 | **13 ANS DE DÉSERT** après le paper. |
| 1986 | 13 | 10 | Premier signal: boom des dérivés, CBOE mature. |

**LE TROU LE PLUS LONG JAMAIS TESTÉ**: 13 ans entre le paper pont (1973) et la première co-occurrence significative (1986). Black-Scholes a été publié, cité, utilisé en PRATIQUE (les traders) mais l'ACADÉMIE n'a pas suivi pendant 13 ans.

**Pourquoi?** Parce que le pont était INDUSTRIEL, pas académique. Les traders utilisaient la formule dès 1973 (le CBOE a ouvert la même année). Mais les chercheurs en finance ne publiaient pas dans des revues de "stochastic processes" et vice-versa.

## Données OpenAlex

**Stochastic Process × Financial Economics:**
| 1970 | 1973 | 1980 | 1986 | 1990 | 2000 | 2010 | 2023 |
|------|------|------|------|------|------|------|------|
| 2    | 1    | 0    | **13** | 14   | 23   | 35   | 41   |

**Brownian Motion × Financial Economics:**
| 1970-1985 | 1986 | 1990 | 2000 | 2008 | 2011 | 2023 |
|-----------|------|------|------|------|------|------|
| 0-1       | **10** | 9    | 16   | 55   | 80   | 58   |

## Pattern APRÈS le pont

- Black-Scholes 1973: AUCUN effet mesurable sur les co-occurrences
- 1986 = décollage réel (13 ans après): produits dérivés + Black Monday + Hull 1988 (textbook)
- BM×FE: 0→80 (pic 2011, post-crise 2008) = **x80 depuis le zéro**
- SP×FE: 0→42 = croissance lente mais continue

**Pic 2008-2011**: la crise financière a FORCÉ les académiques à étudier les processus stochastiques en finance (tail risks, fat tails, volatilité stochastique). La crise = second catalyseur.

## Bridge papers (top cited)
- **Karatzas & Shreve 1998** (921 cit): "Methods of Mathematical Finance" — le TEXTBOOK pont
- **Barndorff-Nielsen 1997** (1,255 cit): "Normal inverse Gaussian processes" — extension du brownien
- **Rogers 1997** (609 cit): "Arbitrage with Fractional Brownian Motion" — test du modèle

**Black-Scholes n'apparaît PAS dans les bridge papers OpenAlex** car il est tagué "economics" et "mathematics" séparément, pas "stochastic process × financial economics". Preuve que le pont était INVISIBLE pour la taxonomie académique pendant des décennies.

## Lianes S0 utilisées
Black-Scholes utilise:
- **W(t)** (Wiener/brownien) = liane Fin×Phys×Math (3 continents) — **LE PONT**
- **exp** (exponentielle dans le pricing) = universelle (6 continents)
- **∂** (EDP de Black-Scholes: ∂V/∂t + ½σ²S²∂²V/∂S²) = 5 continents
- **∫** (intégrale d'Itô) = universelle (6 continents)
- **N(μ,σ²)** (gaussien dans d₁, d₂) = 5 continents
- **ln** (log-normal dans le modèle) = universelle (6 continents)

**6 lianes S0 actives**, dont 3 universelles. C'est le test avec le PLUS de lianes simultanées. Black-Scholes est littéralement un CONCENTRÉ de lianes multi-continents.

## Diagnostic
**Pattern unique: PONT INDUSTRIEL → DÉLAI ACADÉMIQUE → CRISE = CATALYSEUR**

Ce n'est ni P1 ni P2. C'est un nouveau pattern:
- Le pont existe (1973) mais l'académie l'IGNORE pendant 13 ans
- L'industrie l'ADOPTE immédiatement (CBOE)
- Le deuxième catalyseur (crise 2008) force l'académie à rattraper

**Hypothèse: quand un pont est INDUSTRIEL, la co-occurrence académique a un délai de 10-15 ans.** C'est l'inverse du Pattern 1 où le paper CAUSE l'explosion. Ici le paper cause l'ADOPTION INDUSTRIELLE, et l'académie suit avec retard.

## Validé ✅ — Pattern NOUVEAU: pont industriel avec délai académique 13 ans + crise = catalyseur
