# YGGDRASIL - La Colonne Vertebrale des Strates

> Zero invention. Que des theses mathematiques prouvees et validees.

## Post Theorem (1944)

Le n-ieme saut de Turing est Sigma-n-complet.
Chaque strate a exactement un centre.

Spine: vide -> K -> FIN -> COF -> Th(N) -> Kleene O -> MUR

---

## CENTRES - FIXES (7/7 PROUVES)

| Strate | Centre | Preuve formelle | Status |
|--------|--------|-----------------|--------|
| 0 Sol | vide (degre 0 = bottom) | Kleene-Post 1954 | FIXE |
| 1 Nuage 1 | K = vide prime (halting) | Post 1944 - Sigma-1-complet | FIXE |
| 2 Nuage 2 | FIN = vide double-prime | Post 1944 - Sigma-2-complet | FIXE |
| 3 Nuage n | COF / vide^(n) | Post 1944 - Sigma-n-complet | FIXE |
| 4 Ciel AH | vide^(omega) = Th(N) | Davis 1950 - supremum de AH | FIXE |
| 5 HYP | Kleene O | Kleene 1955 - Pi-1-1-complet | FIXE |
| 6 Plafond | AUCUN (incomparable) | Kleene-Post 1954 | FIXE |

Tous les centres sont prouves par la litterature scientifique.

---

## Strate 0 SOL (Delta-0-0) - Decidable

Centre: vide (degre de Turing 0 = bottom formel)

Le degre 0 est le plus petit element du demi-treillis des degres de Turing.
Tout ensemble decidable est de degre 0. Prouve: Kleene-Post 1954.
Le Sol est PLAT: un seul point. Pas de plus dur en calculabilite.

Sous-structure de COMPLEXITE (temps/espace):
- P-complet: CVP (Circuit Value Problem) - Ladner 1975
- NP-complet: SAT - Cook 1971, Levin 1973
- PSPACE-complet: QBF - Stockmeyer and Meyer 1973

Le egal: egalite classique a = b (identite absolue)
Ref: Turing 1936, Church 1936, Kleene-Post 1954, Cook 1971

---

## Strate 1 NUAGE 1 (Sigma-0-1) - Semi-decidable

Centre: K = halting problem = vide-prime

K est Sigma-0-1-complet: TOUT probleme semi-decidable se reduit a K.
Le soleil de cette strate. Tout orbite autour.

Le egal: reduction many-one (on perd la symetrie)
Ref: Turing 1936, Post 1944, Rice 1953

---

## Strate 2 NUAGE 2 (Sigma-0-2) - Limite

Centre: FIN = {e : W_e est fini} = vide-double-prime

Structure exist-forall. Dual: TOT est Pi-0-2-complet (forall-exist).
Shoenfield Limit Lemma: Delta-0-2 = limit-calculable.
La verite est une LIMITE.

Le egal: reduction de Turing (on demande a un oracle)
Ref: Post 1944, Shoenfield 1959, Rogers 1967

---

## Strate 3 NUAGE n (Sigma-0-n) - Alternation

Centre au niveau n: vide^(n)

- Sigma-3: COF (cofini), REC (recursif) - Post 1944
- Sigma-4: COMP (Turing-complet) - Rogers 1967
- Sigma-n: vide^(n) - Post 1944

Pattern fractal: meme motif a chaque niveau.
Le egal: Turing relativise a vide^(n-1) (oracles empiles)
Ref: Post 1944, Kleene 1943, Rogers 1967

---

## Strate 4 CIEL (AH) - Hierarchie Arithmetique

Centre: vide^(omega) = Th(N) (supremum de AH)

RESULTAT FORMEL (Davis 1950 + Post 1944):
1. Chaque vide^(n) est Sigma-n-complet (Post 1944)
2. vide^(omega) = recursive join de tous les vide^(n) (Davis 1950)
3. Plus petit ensemble qui calcule tous les vide^(n) finis
4. Dans AUCUN Sigma-n fini - strictement AU-DESSUS de AH
5. PREMIER ensemble hyperarithmetique non-arithmetique

Wikipedia (Hyperarithmetical theory) confirme:
vide^(omega) = nombres de Godel des formules vraies de Peano

Tarski (1933): Th(N) non definissable a aucun niveau fini.
Godel (1931): aucun systeme formel ne peut tout prouver.

Le egal: dissolution - plus de comparaison finie.
Ref: Davis 1950 (PhD Princeton), Tarski 1933, Godel 1931, Feferman 1962

---

## Strate 5 ABOVE (HYP) - Hyperarithmetique

Centre: O (Kleene O) - Pi-1-1-complet

Toutes les notations pour les ordinaux calculables.
Borne: omega-1-CK (Church-Kleene) = plus petit ordinal non calculable.

Le egal: reduction hyperarithmetique (dernier egal constructif)
Ref: Kleene 1938, Kleene 1955, Spector 1955, Moschovakis 2009

---

## Strate 6 PLAFOND - Le Mur Final

Centre: AUCUN

Kleene-Post (1954): degres de Turing INCOMPARABLES existent.
Habitants: BB (Rado 1962), Omega (Chaitin 1975), K(x) (Kolmogorov 1965)
BB(5) = 47,176,870 (prouve 2024). BB(6) = inconnu.

Le egal: disparu. Silence.
Ref: Turing 1936, Kleene-Post 1954, Aaronson 2020

---

## LA LIGNE YGGDRASIL



Le egal nait au Sol, se degrade a chaque strate, meurt au Plafond.

---

## 22 Sources

### Fondations (6 piliers)
1. Turing (1936) On Computable Numbers
2. Godel (1931) Uber formal unentscheidbare Satze
3. Post (1944) Recursively Enumerable Sets
4. Kleene (1943) Recursive Predicates and Quantifiers
5. Tarski (1933) The Concept of Truth
6. Davis (1950) On the Theory of Recursive Unsolvability (PhD Princeton)

### Degres de Turing
7. Rogers (1967) Theory of Recursive Functions (MIT)
8. Soare (2016) Turing Computability (Springer)
9. Shore (2015) The Turing Degrees
10. Soare (1996) Computability and Recursion

### Hyperarithmetique
11. Kleene (1938) On Notation for Ordinal Numbers
12. Spector (1955) Recursive Well-Orderings
13. Moschovakis (2009) Descriptive Set Theory

### Non-calculable
14. Rado (1962) On Non-Computable Functions
15. Chaitin (1975) A Theory of Program Size
16. Kolmogorov (1965) Three Approaches to Information
17. Aaronson (2020) The Busy Beaver Frontier

### Egalite multi-niveaux
18. Voevodsky et al. (2013) HoTT Book
19. Riehl (2023) Intro to Homotopy Type Theory

### Lectures accessibles
20. Marks (2024) Computability Theory notes (Berkeley)
21. Chung (2014) Intro to Computability (UChicago)
22. Stanford Encyclopedia - Computational Complexity Theory

---

## Prochaines Etapes - LES CERCLES

- [x] Trouver le centre de chaque strate - FAIT (7/7)
- [ ] CERCLES: mapper les symboles en orbite autour de chaque centre
- [ ] Valider placement de chaque symbole (Carre A)
- [ ] Connecter centres au moteur mycelium (Winter Tree v2)
- [ ] Croissance fongique depuis les centres vers les vides
- [ ] Predictions AVANT validation par publications

---

2026-02-17. Centres 7/7 fixes + Davis 1950.
Zero invention. Que des resultats prouves.
Prochaine etape: les cercles.
