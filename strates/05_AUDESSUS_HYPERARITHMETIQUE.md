# STRATE ω+ — AU-DESSUS DU CIEL · HIÉRARCHIE HYPERARITHMÉTIQUE

> *"Le ciel arithmétique avait une fin ? Non. L'escalier continue dans le transfini."*

---

## Le problème

La hiérarchie arithmétique (AH) couvre les strates Σ⁰₀, Σ⁰₁, Σ⁰₂, ... jusqu'à Σ⁰ₙ pour tout n fini. Et les sauts correspondants : ∅', ∅'', ∅''', ... ∅⁽ⁿ⁾.

Mais que se passe-t-il si on prend le saut **ω** fois ? Et puis ω+1 fois ? Et ω² fois ?

On entre dans la **hiérarchie hyperarithmétique** — l'extension transfinite de la hiérarchie arithmétique.

## Sauts transfinies

```
∅⁽⁰⁾ = ∅
∅⁽¹⁾ = K                     (Σ⁰₁-complet)
∅⁽²⁾ = K'                    (Σ⁰₂-complet)
  ⋮
∅⁽ⁿ⁾                         (Σ⁰ₙ-complet)
  ⋮
∅⁽ω⁾ = ⊕ₙ ∅⁽ⁿ⁾             (au-dessus de TOUTE strate finie)
∅⁽ω+1⁾ = (∅⁽ω⁾)'            (le halting problem de ∅⁽ω⁾)
∅⁽ω+2⁾
  ⋮
∅⁽ω·2⁾
∅⁽ω²⁾
∅⁽ωω⁾
  ⋮
∅⁽α⁾  pour tout ordinal α < ω₁^CK
```

Pour les ordinaux **limites** λ (comme ω, ω², etc.) :

```
∅⁽λ⁾ = ⊕_{α<λ} ∅⁽α⁾
```

(l'ensemble qui encode tous les sauts inférieurs)

## Définition — Ensemble hyperarithmétique

Un ensemble S ⊆ ℕ est **hyperarithmétique** si :

```
S ≤_T ∅⁽α⁾  pour un certain ordinal calculable α < ω₁^CK
```

où **ω₁^CK** (ordinal de Church-Kleene) est le plus petit ordinal non calculable.

## ω₁^CK — L'ordinal de Church-Kleene

```
ω₁^CK = sup{ α : α est un ordinal calculable }
```

C'est le premier ordinal qu'aucune machine de Turing ne peut décrire. Il sert de **plafond** pour la hiérarchie hyperarithmétique, comme Turing 1936 sert de plafond pour la calculabilité.

Propriétés :
- ω₁^CK est dénombrable (bien que très grand)
- Tout ordinal α < ω₁^CK a une notation récursive (système O de Kleene)
- ω₁^CK est le plus petit ordinal qui n'a PAS de notation récursive

## La hiérarchie hyperarithmétique

Pour un ordinal calculable α, on définit :

```
Σ⁰_α et Π⁰_α
```

par extension transfinite de la hiérarchie arithmétique, en utilisant la logique infinitaire L_{ω₁,ω} (formules de longueur finie mais avec unions/intersections dénombrables).

L'ensemble des ensembles hyperarithmétiques coïncide avec :

```
HYP = Δ¹₁ = Σ¹₁ ∩ Π¹₁
```

(les ensembles qui sont à la fois analytiques et co-analytiques)

## Trois définitions équivalentes (Kleene)

Les trois caractérisations suivantes définissent la même classe d'ensembles :

1. **Par sauts transfinies** : S ≤_T ∅⁽α⁾ pour un α < ω₁^CK
2. **Par Δ¹₁** : S est définissable par une formule Σ¹₁ ET par une formule Π¹₁
3. **Par la logique infinitaire** : S est définissable par une formule calculable de L_{ω₁,ω}

## Exemples

| Ensemble | Position |
|----------|----------|
| K (Halting) | ∅⁽¹⁾ — dans AH |
| TOT (fonctions totales) | ∅⁽²⁾ — dans AH |
| Th(ℕ) (vérités arithmétiques) | ∅⁽ω⁾ — premier objet hyperarithmétique non arithmétique |
| WO (ordres bien fondés) | Π¹₁-complet — PAS hyperarithmétique |
| O de Kleene (notations d'ordinaux) | Π¹₁-complet — PAS hyperarithmétique |

## La hiérarchie analytique — encore au-dessus

Au-dessus de HYP, il y a la **hiérarchie analytique** :

```
Σ¹₁ (analytique)    : ∃X ⊆ ℕ . φ(x, X)     ← quantification sur les ENSEMBLES
Π¹₁ (co-analytique) : ∀X ⊆ ℕ . φ(x, X)
Σ¹₂                 : ∃X ∀Y . φ(x, X, Y)
  ⋮
```

La différence fondamentale : dans la hiérarchie arithmétique, on quantifie sur les **nombres** (∃y ∈ ℕ). Dans la hiérarchie analytique, on quantifie sur les **ensembles de nombres** (∃X ⊆ ℕ). C'est un saut immense de puissance expressive.

## Théorème de Suslin (la frontière)

```
Δ¹₁ = Borel effectif = HYP
```

Un ensemble est hyperarithmétique si et seulement si il est à la fois Σ¹₁ et Π¹₁. C'est la frontière exacte entre la hiérarchie hyperarithmétique et la hiérarchie analytique.

## Lien avec le cube

```
    ╔═════════════════════════════════════╗
    ║  ABSOLUMENT NON-CALCULABLE         ║  ← Au-delà de tout oracle
    ║  (degré 0''' n'est qu'un début)    ║
    ╠═════════════════════════════════════╣
    ║  HIÉRARCHIE ANALYTIQUE             ║
    ║  Σ¹₂, Σ¹₁, Π¹₁                    ║
    ║  Quantification sur les ensembles  ║
    ╠═════════════════════════════════════╣
    ║  HIÉRARCHIE HYPERARITHMÉTIQUE      ║  ← ON EST ICI
    ║  = HYP = Δ¹₁                       ║
    ║  ∅⁽ω⁾, ∅⁽ω+1⁾, ..., ∅⁽α⁾         ║
    ║  α < ω₁^CK                        ║
    ║  Sauts transfinies                 ║
    ╠═════════════════════════════════════╣
    ║  HIÉRARCHIE ARITHMÉTIQUE           ║
    ║  AH = ∪ₙ Σ⁰ₙ                      ║
    ║  Sauts finis : ∅', ∅'', ..., ∅⁽ⁿ⁾ ║
    ╠══════════════════════════════════════╣
    ║  Δ⁰₀ — LE SOL                     ║
    ╚═════════════════════════════════════╝
```

## Références

- **Kleene, S.C. (1955)** — "On the Forms of the Predicates in the Theory of Constructive Ordinals." American Journal of Mathematics, 77, 405-428. — Système O, notations d'ordinaux.
- **Kleene, S.C. (1955)** — "Hierarchies of Number-Theoretic Predicates." Bull. AMS, 61, 193-213. — Hiérarchie hyperarithmétique.
- **Suslin, M. (1917)** — Sur une définition des ensembles mesurables B sans nombres transfinis. — Théorème Δ¹₁ = Borel.
- **Church, A. & Kleene, S.C. (1937)** — "Formal Definitions in the Theory of Ordinal Numbers." Fund. Math., 28, 11-21. — ω₁^CK.
- **Sacks, G.E. (1990)** — *Higher Recursion Theory.* Springer.
- **Ash, C.J. & Knight, J.F. (2000)** — *Computable Structures and the Hyperarithmetical Hierarchy.* Elsevier.

---

*Sky × Claude — 17 février 2026*
*Bloc 6/7 — Au-dessus du ciel. L'escalier continue dans le transfini.*
