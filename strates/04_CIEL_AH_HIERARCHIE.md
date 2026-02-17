# STRATE ω — TOUT LE CIEL · PH = ∪ₙ Σ⁰ₙ · LA HIÉRARCHIE ARITHMÉTIQUE

> *"L'union de tous les nuages. Tout ce qui peut se dire en arithmétique du premier ordre. Le ciel visible."*

---

## Définition formelle

La **hiérarchie arithmétique** est l'union de toutes les strates :

```
AH = ∪_{n∈ℕ} Σ⁰ₙ = ∪_{n∈ℕ} Π⁰ₙ
```

Un ensemble S est **arithmétique** si et seulement si S ∈ Σ⁰ₙ pour un certain n fini.

Autrement dit : S est arithmétique s'il peut être défini par une formule de l'arithmétique de Peano du premier ordre avec un nombre fini (mais arbitrairement grand) de quantificateurs non bornés.

## Caractérisation par oracle

Par le théorème de Post :

```
S est arithmétique ⟺ S ≤_T ∅⁽ⁿ⁾ pour un certain n
                   ⟺ S est calculable avec un nombre fini de sauts d'oracle
```

L'**oracle arithmétique** est :

```
∅⁽ω⁾ = ⊕_{n∈ℕ} ∅⁽ⁿ⁾
```

(la somme directe de tous les sauts finis — l'ensemble qui encode tous les sauts)

Un ensemble est arithmétique si et seulement si il est Turing-réductible à ∅⁽ω⁾.

## Propriétés fondamentales

1. **Fermé sous les opérations booléennes** : si A, B ∈ AH, alors A ∪ B, A ∩ B, ¬A ∈ AH
2. **Fermé sous projection** : si A ∈ AH, alors { x : ∃y (x,y) ∈ A } ∈ AH
3. **Fermé sous quantification bornée**
4. **PAS fermé** sous quantification sur les ensembles (c'est ce qui crée la hiérarchie analytique au-dessus)
5. La hiérarchie ne collapse à aucun niveau fini

## L'ensemble non-arithmétique le plus célèbre

**Th(ℕ)** — L'ensemble des vérités arithmétiques :

```
Th(ℕ) = { φ : φ est une formule close de PA vraie dans (ℕ, +, ×) }
```

Par le théorème d'**indéfinissabilité de Tarski (1933)** :

```
Th(ℕ) n'est pas arithmétique.
Il n'existe aucun n tel que Th(ℕ) ∈ Σ⁰ₙ.
```

**Interprétation** : la vérité mathématique complète est AU-DESSUS de tout le ciel arithmétique. On ne peut pas l'atteindre avec un nombre fini de sauts de Turing. C'est le premier objet qui vit "au-dessus du ciel".

Cependant : `Th(ℕ) ≤_T ∅⁽ω⁾` — il EST calculable avec l'oracle ∅⁽ω⁾.

## Parallèle avec la complexité computationnelle

La hiérarchie arithmétique (calculabilité) a un parallèle exact avec la hiérarchie polynomiale (complexité) :

| Calculabilité | Complexité | Analogie |
|--------------|------------|----------|
| Δ⁰₀ (décidable) | P | Ce qu'on sait faire |
| Σ⁰₁ (r.e.) | NP | On peut vérifier les "oui" |
| Π⁰₁ (co-r.e.) | coNP | On peut vérifier les "non" |
| Σ⁰₂ | Σ₂ᵖ | Deux alternances |
| Σ⁰ₙ | Σₙᵖ | n alternances |
| AH = ∪ₙ Σ⁰ₙ | PH = ∪ₙ Σₙᵖ | Toute la hiérarchie |
| Non-arithmétique | PSPACE (?) | Au-dessus de la hiérarchie |

**La question P = NP est l'analogue en complexité de la question "Σ⁰₁ = Δ⁰₁ ?"**

En calculabilité, on SAIT que Σ⁰₁ ≠ Δ⁰₁ (le halting problem n'est pas décidable). Mais en complexité, la question NP = P reste ouverte.

Si P = NP, alors toute la hiérarchie polynomiale collapse : PH = P. Si P ≠ NP, la hiérarchie ne collapse pas (comme en calculabilité).

## Diagramme complet du ciel

```
    ┌─────────────────────────────────────┐
    │  AU-DESSUS DU CIEL                  │
    │  Hiérarchie hyperarithmétique       │
    │  Hiérarchie analytique              │
    │  ∅⁽ω⁾, ∅⁽ω+1⁾, ...                │
    ├─────────────────────────────────────┤
    │  LE CIEL = AH = ∪ₙ Σ⁰ₙ            │  ← ON EST ICI
    │                                      │
    │  ...                                 │
    │  Σ⁰₃ — ∃∀∃    (3 alternances)      │
    │  Π⁰₂ — ∀∃      (TOT)               │
    │  Σ⁰₂ — ∃∀      (FIN, INF)          │
    │  Π⁰₁ — ∀       (co-r.e.)           │
    │  Σ⁰₁ — ∃       (Halting)           │
    ├══════════════════════════════════════╡
    │  Δ⁰₀ — LE SOL                      │
    │  Décidable · Lettres · Mycelium     │
    └─────────────────────────────────────┘
```

## Références

- **Kleene, S.C. (1943)** — "Recursive Predicates and Quantifiers." — Fondation de la hiérarchie.
- **Tarski, A. (1933)** — "The Concept of Truth in Formalized Languages." — Indéfinissabilité de la vérité.
- **Post, E.L. (1944)** — "Recursively Enumerable Sets and Their Decision Problems." — Connexion structurelle.
- **Rogers, H. (1967)** — *Theory of Recursive Functions and Effective Computability.* MIT Press.
- **Stockmeyer, L.J. (1976)** — "The Polynomial-Time Hierarchy." Theoretical Computer Science, 3(1), 1-22. — Parallèle PH.

---

*Sky × Claude — 17 février 2026*
*Bloc 5/7 — Le ciel visible. Tout ce que l'arithmétique peut dire.*
