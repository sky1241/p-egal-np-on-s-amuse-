# STRATE n — LE MOTIF GÉNÉRAL · Σ⁰ₙ · n ALTERNANCES

> *"Chaque alternance de quantificateurs est un étage de brouillard supplémentaire. L'escalier ne finit jamais."*

---

## Définition formelle

Un ensemble S ⊆ ℕ est **Σ⁰ₙ** si :

```
x ∈ S ⟺ ∃y₁ ∀y₂ ∃y₃ ∀y₄ ... Qyₙ  R(x, y₁, y₂, ..., yₙ)
```

où :
- R est une relation décidable (Δ⁰₀)
- Il y a exactement **n blocs** de quantificateurs alternés
- Le premier bloc est **∃** (existentiel)
- Q = ∃ si n est impair, Q = ∀ si n est pair

**Π⁰ₙ** — le miroir : commence par ∀ au lieu de ∃ :

```
x ∈ S ⟺ ∀y₁ ∃y₂ ∀y₃ ∃y₄ ... Qyₙ  R(x, y₁, y₂, ..., yₙ)
```

**Δ⁰ₙ** — l'intersection :

```
S ∈ Δ⁰ₙ ⟺ S ∈ Σ⁰ₙ ET S ∈ Π⁰ₙ
```

## Le théorème de Post — L'escalier complet

**Théorème (Post, 1948 ; Kleene, 1943)** :

Pour tout n ≥ 1 :

```
1. ∅⁽ⁿ⁾ est Σ⁰ₙ-complet
   (le n-ième saut de Turing du vide est le problème le plus dur de Σ⁰ₙ)

2. ℕ \ ∅⁽ⁿ⁾ est Π⁰ₙ-complet
   (son complémentaire est le plus dur de Π⁰ₙ)

3. S ∈ Σ⁰ₙ₊₁ ⟺ S est r.e. relativement à ∅⁽ⁿ⁾
   (chaque strate = ce qui est semi-décidable avec n sauts d'oracle)

4. S ∈ Δ⁰ₙ₊₁ ⟺ S ≤_T ∅⁽ⁿ⁾
   (l'intersection = ce qui est décidable avec n sauts)
```

**Conséquence cruciale** : La hiérarchie **ne collapse pas**.

```
Δ⁰₀ ⊊ Σ⁰₁ ⊊ Δ⁰₂ ⊊ Σ⁰₂ ⊊ Δ⁰₃ ⊊ Σ⁰₃ ⊊ ...
```

Chaque inclusion est STRICTE. Il n'y a pas de raccourci.

## L'escalier — les sauts itérés

```
∅⁽⁰⁾ = ∅                    → Δ⁰₀ (décidable)
∅⁽¹⁾ = ∅' = K               → Σ⁰₁-complet (halting)
∅⁽²⁾ = ∅'' = K'             → Σ⁰₂-complet (halting du halting)
∅⁽³⁾ = ∅''' = K''           → Σ⁰₃-complet
  ⋮
∅⁽ⁿ⁾                        → Σ⁰ₙ-complet
  ⋮
```

Chaque saut ajoute un étage. Chaque étage est strictement plus dur que le précédent. Le saut est l'escalier.

## Exemples par strate

| Strate | Ensemble complet | Problème naturel |
|--------|-----------------|------------------|
| Σ⁰₁ | ∅' = K | "Ce programme s'arrête-t-il ?" |
| Π⁰₁ | ℕ \ K | "Ce programme boucle-t-il à l'infini ?" |
| Σ⁰₂ | ∅'' | "Ce programme s'arrête-t-il sur une infinité d'inputs ?" |
| Π⁰₂ | ℕ \ ∅'' | "Ce programme s'arrête-t-il sur TOUT input ?" (TOT) |
| Σ⁰₃ | ∅''' | "Ce programme calcule-t-il une fonction récursive ?" (REC) |
| Π⁰₃ | ℕ \ ∅''' | "Le domaine de ce programme est-il co-récursif ?" |

## La formule récursive — Le pattern

Pour passer de la strate n à n+1, on ajoute un quantificateur :

```
Σ⁰ₙ :   ∃∀∃∀...  (n blocs, commence par ∃)
            ↓ ajouter un ∃ devant
Σ⁰ₙ₊₁ : ∃∀∃∀∃... (n+1 blocs)
```

Ou en termes d'oracle :

```
Σ⁰ₙ₊₁ = { ensembles r.e. avec oracle ∅⁽ⁿ⁾ }
```

## Propriétés universelles (pour tout n)

1. **Fermeture** : Σ⁰ₙ est fermé sous ∪, ∩, et projection existentielle
2. **Non-fermeture** : Σ⁰ₙ n'est PAS fermé sous complémentation (sinon Σ⁰ₙ = Π⁰ₙ et la hiérarchie collapserait)
3. **Complétude** : ∅⁽ⁿ⁾ est many-one complet dans Σ⁰ₙ
4. **Séparation stricte** : Σ⁰ₙ ⊊ Σ⁰ₙ₊₁ (conséquence directe du théorème de Post)
5. **Réduction** : pour tout S ∈ Σ⁰ₙ₊₁, il existe T ∈ Σ⁰₁ tel que S = { x : ∃y T(x,y) } avec T décidable relativement à ∅⁽ⁿ⁾

## Contraction des quantificateurs

**Théorème (contraction)** : Plusieurs quantificateurs adjacents du même type peuvent être réduits à un seul :

```
∃y₁ ∃y₂ ... ∃yₖ R(x, y₁, ..., yₖ)  ⟺  ∃z R'(x, z)
```

grâce à la fonction d'appariement de Cantor. Seules les **alternances** comptent, pas le nombre de quantificateurs au sein d'un bloc.

## Topologie — Les nuages sont des espaces

Dans l'espace de Cantor (2^ℕ) ou de Baire (ℕ^ℕ) :
- Σ⁰₁ = les ensembles **ouverts** (effectivement)
- Π⁰₁ = les ensembles **fermés**
- Σ⁰₂ = les ensembles **F_σ** (union dénombrable de fermés)
- Π⁰₂ = les ensembles **G_δ** (intersection dénombrable d'ouverts)
- Σ⁰ₙ = les ensembles de la n-ième couche de la hiérarchie de Borel

La hiérarchie arithmétique est la version "effective" de la hiérarchie de Borel.

## Lien avec le cube

```
    ┌─────────────────────────────┐
    │    PLAFOND — INDÉCIDABLE    │
    │                              │
    │    Σ⁰ₙ₊₁  ← +1 alternance  │
    │      ↑  saut de Turing       │
    │    Σ⁰ₙ   ← ON EST ICI      │  ← n alternances
    │      ↑  saut de Turing       │
    │    Σ⁰ₙ₋₁                    │
    │      ↑                       │
    │    ...                       │
    │      ↑                       │
    │    Σ⁰₂  (∃∀)                │
    │      ↑                       │
    │    Σ⁰₁  (∃) — Halting       │
    ├══════════════════════════════╡
    │    Δ⁰₀ — LE SOL             │
    └─────────────────────────────┘

    L'escalier est le saut de Turing.
    Chaque marche = une alternance de quantificateurs.
    L'escalier ne finit jamais.
```

## Références

- **Kleene, S.C. (1943)** — "Recursive Predicates and Quantifiers." Trans. AMS, 53(1), 41-73. — Définition de la hiérarchie.
- **Mostowski, A. (1946)** — "On Definable Sets of Positive Integers." Fund. Math., 34, 81-112. — Définition indépendante.
- **Post, E.L. (1948)** — "Degrees of Recursive Unsolvability." Bull. AMS, 54, 641-642. — Connexion hiérarchie ↔ degrés.
- **Rogers, H. (1967)** — *Theory of Recursive Functions and Effective Computability.* MIT Press. — Référence encyclopédique.

---

*Sky × Claude — 17 février 2026*
*Bloc 4/7 — Le motif se répète. L'escalier n'a pas de fin.*
