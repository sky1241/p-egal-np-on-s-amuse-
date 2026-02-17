# STRATE 2 — LE DEUXIÈME NUAGE · Σ⁰₂ · LIMITE DU CALCULABLE

> *"Deux couches de brouillard. On peut deviner, se corriger, re-deviner… mais jamais être sûr."*

---

## Définition formelle

Un ensemble S ⊆ ℕ est **Σ⁰₂** si :

```
x ∈ S ⟺ ∃y ∀z R(x, y, z)
```

où R est une relation décidable (Δ⁰₀).

Deux quantificateurs non bornés, alternés : un ∃ suivi d'un ∀. C'est la première vraie alternance.

## Sa sœur — Π⁰₂

```
x ∈ S ⟺ ∀y ∃z R(x, y, z)
```

L'exact miroir : ∀ suivi de ∃.

## L'intersection — Δ⁰₂

```
S ∈ Δ⁰₂ ⟺ S ∈ Σ⁰₂ ET S ∈ Π⁰₂
```

Les ensembles Δ⁰₂ sont exactement les ensembles **limit-calculables** : il existe une suite de machines de Turing qui convergent vers la bonne réponse, mais on ne sait jamais quand elles ont convergé.

## Lien avec le saut de Turing

Par le **théorème de Post** :

```
Σ⁰₂ = les ensembles récursivement énumérables avec oracle ∅'
     = les ensembles r.e. relativement au Halting Problem
```

Autrement dit : si quelqu'un te donnait un oracle qui résout le Halting Problem, les ensembles que tu pourrais semi-décider avec cet oracle seraient exactement Σ⁰₂.

```
∅'' = { e : la machine e, avec oracle ∅', s'arrête sur e }
```

∅'' (le **double saut**) est Σ⁰₂-complet. C'est le problème le plus dur de cette strate — le halting problem du halting problem.

## Exemples concrets

### Π⁰₂-complet : TOT (les fonctions totales)

```
TOT = { e ∈ ℕ : la machine de Turing numéro e s'arrête sur TOUT input }
     = { e : ∀x ∃s (la machine e s'arrête sur x en s étapes) }
```

Pourquoi Π⁰₂ ? La formule est : `∀x ∃s R(e, x, s)` — un ∀ suivi d'un ∃ — c'est la forme Π⁰₂.

**Interprétation** : savoir si un programme s'arrête toujours (sur tout input) est **strictement plus dur** que savoir s'il s'arrête sur un input donné. C'est un étage au-dessus du Halting Problem.

### Σ⁰₂-complet : FIN (les domaines finis)

```
FIN = { e ∈ ℕ : dom(φₑ) est fini }
    = { e : ∃N ∀x > N (la machine e ne s'arrête pas sur x) }
```

Savoir si un programme ne s'arrête que sur un nombre fini d'inputs.

### Σ⁰₂-complet : COF (les domaines co-finis)

```
COF = { e ∈ ℕ : le complémentaire de dom(φₑ) est fini }
    = { e : ∃N ∀x > N (la machine e s'arrête sur x) }
```

### Autres exemples

| Ensemble | Classe | Description |
|----------|--------|-------------|
| TOT | Π⁰₂-complet | Machines qui s'arrêtent sur tout input |
| FIN | Σ⁰₂-complet | Machines avec domaine fini |
| COF | Σ⁰₂-complet | Machines avec co-domaine fini |
| INF | Σ⁰₂-complet | Machines avec domaine infini |
| REC | Σ⁰₃ (pas Σ⁰₂ !) | Machines qui calculent une fonction totale récursive |

## Limite-calculabilité (Shoenfield Limit Lemma)

**Théorème (Shoenfield, 1959)** : Un ensemble S est Δ⁰₂ si et seulement si il est **limit-calculable** :

```
Il existe une fonction totale calculable g(x, s) telle que pour tout x :
    lim_{s→∞} g(x, s) = χ_S(x)
```

où χ_S est la fonction caractéristique de S.

**Interprétation** : pour chaque x, la suite g(x, 0), g(x, 1), g(x, 2), ... finit par se stabiliser sur la bonne réponse (0 ou 1). Mais on ne sait **jamais** à quel moment elle s'est stabilisée. On change d'avis un nombre fini de fois, puis on tombe juste — mais sans jamais savoir qu'on a trouvé.

## Propriétés de fermeture

Si A et B sont Σ⁰₂ :
- A ∪ B est Σ⁰₂ ✅
- A ∩ B est Σ⁰₂ ✅
- ¬A est Π⁰₂ (pas forcément Σ⁰₂) ⚠️

## Structure fine — Les degrés d.r.e.

Entre Σ⁰₁ et Σ⁰₂ il existe une structure riche :
- **Ensembles d-r.e.** (difference of r.e.) : A = B \ C où B, C sont r.e.
- **Ensembles n-r.e.** : différences alternées de n ensembles r.e.
- La hiérarchie d'Ershov : 1-r.e. ⊊ 2-r.e. ⊊ 3-r.e. ⊊ ... ⊊ ω-r.e. = Δ⁰₂

## Lien avec le cube

```
    ┌─────────────────────────────┐
    │    PLAFOND — INDÉCIDABLE    │
    │                              │
    │    ...                       │
    ├──────────────────────────────┤
    │    Σ⁰₂ — ON EST ICI         │  ← Deuxième nuage
    │    ∃y ∀z R(x,y,z)           │
    │    Halting du Halting        │
    │    "Est-ce que ce programme  │
    │     s'arrête TOUJOURS ?"    │
    ├──────────────────────────────┤
    │    Σ⁰₁ — Nuage 1 (Halting)  │
    ├══════════════════════════════╡
    │    Δ⁰₀ — LE SOL             │
    └─────────────────────────────┘
```

## Références

- **Post, E.L. (1944)** — "Recursively Enumerable Sets and Their Decision Problems." — Théorème de Post reliant hiérarchie et sauts.
- **Shoenfield, J.R. (1959)** — "On Degrees of Unsolvability." Annals of Mathematics, 69, 644-653. — Shoenfield Limit Lemma.
- **Ershov, Yu.L. (1968)** — "A Hierarchy of Sets." Algebra and Logic, 7, 25-43. — Hiérarchie d'Ershov.
- **Rogers, H. (1967)** — *The Theory of Recursive Functions and Effective Computability.* MIT Press.
- **Soare, R.I. (2016)** — *Turing Computability.* Springer.

---

*Sky × Claude — 17 février 2026*
*Bloc 3/7 — Le brouillard s'épaissit.*
