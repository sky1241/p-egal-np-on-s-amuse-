# STRATE 0 — LE SOL · Δ⁰₀ · DÉCIDABLE

> *"Le sol, c'est tout ce qu'une machine de Turing peut décider en temps fini."*

---

## Définition formelle

Un ensemble S ⊆ ℕ est **décidable** (ou récursif, ou calculable) s'il existe une fonction totale calculable f telle que :

```
f(x) = 1  si x ∈ S
f(x) = 0  si x ∉ S
```

Autrement dit : il existe une machine de Turing M qui, pour **tout** input n :
- S'arrête TOUJOURS (jamais de boucle infinie)
- Retourne 1 si n ∈ S
- Retourne 0 si n ∉ S

## Position dans la hiérarchie arithmétique

```
Δ⁰₀ = Σ⁰₀ = Π⁰₀
```

Au niveau 0, les trois classes sont **identiques**. Il n'y a aucun quantificateur non borné. Toute formule définissant un ensemble Δ⁰₀ utilise uniquement :
- Les opérations arithmétiques de base (+, ×, <)
- Des quantificateurs **bornés** : ∀y < n, ∃y < n

## Formule générale

Un ensemble S est Δ⁰₀ si et seulement si :

```
x ∈ S ⟺ R(x)
```

où R est une relation **décidable** — c'est-à-dire une formule de l'arithmétique de Peano avec uniquement des quantificateurs bornés.

## Propriétés de fermeture

Si A et B sont décidables, alors :
- Le complémentaire ¬A est décidable
- L'union A ∪ B est décidable
- L'intersection A ∩ B est décidable
- L'image de A × B sous la fonction d'appariement de Cantor est décidable
- La préimage de A sous une fonction totale calculable est décidable

**Propriété clé** : S est décidable ⟺ S **et** son complémentaire sont tous les deux récursivement énumérables (Σ⁰₁).

## Exemples d'ensembles décidables

| Ensemble | Pourquoi décidable |
|----------|-------------------|
| ℕ (tous les naturels) | f(x) = 1 pour tout x |
| ∅ (ensemble vide) | f(x) = 0 pour tout x |
| Les nombres premiers | Crible d'Ératosthène — algorithme qui s'arrête toujours |
| Les nombres pairs | f(x) = (x mod 2 == 0) |
| Les nombres de Gödel des preuves valides | Vérification syntaxique en temps fini |
| Tout ensemble fini | Table de lookup |
| Tout ensemble co-fini | Complémentaire d'un ensemble fini |

## Exemples d'ensembles NON décidables (au-dessus du sol)

| Ensemble | Strate |
|----------|--------|
| Le problème de l'arrêt (Halting Problem) | Σ⁰₁ — un étage au-dessus |
| Le 10ème problème de Hilbert (équations diophantiennes) | Σ⁰₁ |
| Les Busy Beaver champions | Au-delà de toute strate arithmétique |

## Théorèmes fondateurs

### Turing (1936) — Existence du non-calculable
Il existe des ensembles qui ne sont PAS décidables. Le problème de l'arrêt est le premier exemple :

```
K = { e : la machine e s'arrête sur l'input e }
```

K est récursivement énumérable (Σ⁰₁) mais **pas** décidable (pas dans Δ⁰₀).

Preuve : par diagonalisation. Si K était décidable, on pourrait construire une machine D telle que :
- D(e) s'arrête ⟺ la machine e ne s'arrête PAS sur e

Mais alors D appliquée à son propre code crée une contradiction. Donc K ∉ Δ⁰₀.

### Rice (1953) — Presque rien n'est décidable
Pour toute propriété **non triviale** P des fonctions calculées par les machines de Turing :

```
{ e : la machine e calcule une fonction ayant la propriété P } est indécidable
```

Autrement dit : on ne peut pas décider algorithmiquement si un programme a une propriété sémantique quelconque (sauf "toujours vrai" ou "toujours faux").

### Church-Turing (1936) — Le sol est universel
Toute fonction "effectivement calculable" (au sens intuitif) est calculable par une machine de Turing. 

Conséquence : Δ⁰₀ ne dépend PAS du modèle de calcul choisi (machine de Turing, λ-calcul, fonctions μ-récursives, RAM, Python, PowerShell...). Le sol est le même partout.

## Lien avec le cube

```
STRATE 0 = LE SOL DU CUBE

    ┌─────────────────────────────┐
    │    PLAFOND — INDÉCIDABLE    │  ← Turing 1936
    │         (non-calculable)     │
    │                              │
    │    ...                       │
    │    Σ⁰₂ — Nuage 2            │
    │    Σ⁰₁ — Nuage 1 (Halting)  │
    │                              │
    ├══════════════════════════════╡
    │    Δ⁰₀ — LE SOL             │  ← ON EST ICI
    │    Tout ce qui est décidable │
    │    Les lettres vivent ici    │
    │    Le mycelium circule ici   │
    └─────────────────────────────┘
```

Le sol est la frontière entre ce qu'on **sait** calculer et ce qu'on ne sait pas. Tout ce qui est en dessous est acquis. Tout ce qui est au-dessus est du brouillard — on peut lister les "oui" mais on ne peut jamais être sûr des "non".

## Degré de Turing

Le sol correspond au degré **0** (zéro) dans la structure des degrés de Turing :
- Degré 0 = la classe de tous les ensembles décidables
- C'est le plus petit degré
- Tout ensemble de degré 0 est calculable par une machine de Turing standard (sans oracle)

## Références

- **Turing, A.M. (1936)** — "On Computable Numbers, with an Application to the Entscheidungsproblem." Proc. London Math. Soc., 2(42), 230-265.
- **Church, A. (1936)** — "An Unsolvable Problem of Elementary Number Theory." American Journal of Mathematics, 58(2), 345-363.
- **Rice, H.G. (1953)** — "Classes of Recursively Enumerable Sets and Their Decision Problems." Trans. AMS, 74(2), 358-366.
- **Kleene, S.C. (1943)** — "Recursive Predicates and Quantifiers." Trans. AMS, 53(1), 41-73.
- **Post, E.L. (1944)** — "Recursively Enumerable Sets of Positive Integers and Their Decision Problems." Bull. AMS, 50, 284-316.
- **Soare, R.I. (2016)** — *Turing Computability: Theory and Applications of Computability.* Springer.

---

*Sky × Claude — 17 février 2026*
*Bloc 1/7 — Le sol sous les pieds.*
