# STRATE ∞ — LE PLAFOND · NON-CALCULABLE · TURING 1936

> *"Il existe des questions mathématiques bien posées auxquelles aucune machine — passée, présente ou future — ne pourra jamais répondre."*

---

## Le théorème fondateur

**Théorème (Turing, 1936)** : Il n'existe pas de machine de Turing M telle que, pour toute machine T et tout input x :

```
M(⟨T, x⟩) = { 1  si T s'arrête sur x
              { 0  si T ne s'arrête pas sur x
```

**Il n'existe pas d'algorithme universel qui décide l'arrêt.**

Ce n'est pas une limitation technologique. Ce n'est pas un manque de puissance de calcul. C'est une **impossibilité mathématique prouvée**, aussi solide que le théorème de Pythagore.

## Les trois résultats impossibles (années 1930)

Les années 1930 ont produit trois résultats d'impossibilité qui forment le plafond :

### 1. Gödel (1931) — Incomplétude

```
Pour tout système formel S suffisamment puissant (contenant l'arithmétique de Peano) et cohérent :
    Il existe une formule G telle que :
    - G est vraie dans ℕ
    - G n'est pas prouvable dans S
    - ¬G n'est pas prouvable dans S
```

**Premier théorème** : Si S est cohérent, S est incomplet — il existe des vérités indémontrables.

**Deuxième théorème** : S ne peut pas prouver sa propre cohérence.

### 2. Turing (1936) — Indécidabilité

```
K = { e : φₑ(e)↓ } n'est pas décidable.
```

Preuve par diagonalisation (voir Strate 1).

**Lien avec Gödel** : Turing a montré que le problème de l'arrêt se réduit au problème de la vérité arithmétique. L'indécidabilité de K implique l'incomplétude de PA.

### 3. Church (1936) — Entscheidungsproblem

```
Il n'existe pas d'algorithme qui, pour toute formule φ du calcul des prédicats,
décide si φ est un théorème de la logique du premier ordre.
```

Church a prouvé ce résultat en utilisant le λ-calcul, indépendamment de Turing.

**Thèse de Church-Turing** : les trois formalismes (machine de Turing, λ-calcul, fonctions μ-récursives) calculent exactement les mêmes fonctions. Le plafond est le même partout.

## Le plafond est absolu

La thèse de Church-Turing affirme que le plafond est **indépendant du modèle de calcul** :

| Modèle | Inventeur | Même plafond ? |
|--------|-----------|----------------|
| Machine de Turing | Turing (1936) | ✅ |
| λ-calcul | Church (1936) | ✅ |
| Fonctions μ-récursives | Kleene (1936) | ✅ |
| Systèmes de Post | Post (1943) | ✅ |
| Machines à registres | Shepherdson-Sturgis (1963) | ✅ |
| Automates cellulaires | von Neumann (1966) | ✅ |
| Python, PowerShell, Dart | Aujourd'hui | ✅ |
| Ordinateur quantique | Deutsch (1985) | ✅ |

L'ordinateur quantique calcule certaines choses **plus vite** (BQP ⊆ PSPACE) mais ne calcule PAS plus de fonctions. Le plafond de Turing est le même pour un qubit et pour un crayon.

## Ce qui vit au plafond et au-dessus

### Ensembles non calculables célèbres

| Ensemble | Ce qu'il demande | Pourquoi impossible |
|----------|-----------------|---------------------|
| K (Halting Problem) | "Ce programme s'arrête-t-il ?" | Diagonalisation |
| Th(ℕ) | "Cette formule arithmétique est-elle vraie ?" | Tarski 1933 |
| Hilbert's 10th | "Cette équation diophantienne a-t-elle une solution ?" | Matiyasevich 1970 |
| Busy Beaver BB(n) | "Quel est le plus long arrêt pour n états ?" | Croît plus vite que toute fonction calculable |
| Entscheidungsproblem | "Cette formule logique est-elle valide ?" | Church 1936 |
| Problème du mot (groupes) | "Ce mot représente-t-il l'identité ?" | Novikov 1955 |
| Problème de la tuile | "Ces tuiles pavent-elles le plan ?" | Berger 1966 |
| Problème de correspondance de Post | "Ces deux listes ont-elles une concaténation commune ?" | Post 1946 |

### Busy Beaver — Le monstre au plafond

La fonction Busy Beaver BB(n) est définie comme :

```
BB(n) = max{ nombre d'étapes avant l'arrêt de M :
             M est une machine de Turing à n états qui s'arrête }
```

Propriétés :
- BB(n) est bien définie pour tout n
- BB(n) n'est PAS calculable (Radó, 1962)
- BB(n) croît plus vite que TOUTE fonction calculable
- BB(n) > f(n) pour tout n assez grand, pour toute f calculable
- BB(5) = 47 176 870 (prouvé en 2024)
- BB(6) > 10↑↑15 (incompréhensiblement grand)

BB n'est pas juste non-calculable — elle est **au-dessus de toute la hiérarchie arithmétique**. Elle n'est dans aucune Σ⁰ₙ.

## Le plafond vu d'en bas

```
    ╔═════════════════════════════════════════════╗
    ║                                             ║
    ║          LE PLAFOND — ON EST ICI            ║
    ║                                             ║
    ║   "Il existe des vérités mathématiques      ║
    ║    qu'aucune machine ne peut atteindre."    ║
    ║                                             ║
    ║   Turing 1936 · Gödel 1931 · Church 1936   ║
    ║                                             ║
    ║   Le plafond ne dépend pas de la machine.   ║
    ║   Il ne dépend pas de la vitesse.           ║
    ║   Il ne dépend pas de la mémoire.           ║
    ║   Il est mathématique, pas technologique.   ║
    ║                                             ║
    ╠═════════════════════════════════════════════╣
    ║   BB(n) — au-dessus de tout                 ║
    ╠═════════════════════════════════════════════╣
    ║   Hiérarchie analytique · Σ¹ₙ              ║
    ╠═════════════════════════════════════════════╣
    ║   Hiérarchie hyperarithmétique · ∅⁽α⁾      ║
    ╠═════════════════════════════════════════════╣
    ║   Hiérarchie arithmétique · AH = ∪ₙ Σ⁰ₙ   ║
    ╠═════════════════════════════════════════════╣
    ║   Σ⁰₁ — Halting · K                        ║
    ╠══════════════════════════════════════════════╣
    ║   Δ⁰₀ — LE SOL · Décidable · Mycelium     ║
    ╚═════════════════════════════════════════════╝

    Du sol au plafond :
    Chaque strate est strictement plus haute.
    L'escalier est infini (transfini même).
    Le plafond est prouvé inaccessible.
```

## Lien avec P = NP

Le problème P = NP vit dans un monde parallèle : celui de la **complexité** (combien de temps) plutôt que de la **calculabilité** (est-ce possible). Mais les structures sont les mêmes :

```
Calculabilité :     Δ⁰₀ ⊊ Σ⁰₁ ⊊ Σ⁰₂ ⊊ ...  (PROUVÉ)
Complexité :        P ⊆ NP ⊆ Σ₂ᵖ ⊆ ...       (P ≠ NP ?)
```

Les trois barrières (relativisation, preuves naturelles, algébrisation) disent que les outils qui prouvent Δ⁰₀ ≠ Σ⁰₁ ne suffisent PAS pour prouver P ≠ NP. Il faut un outil nouveau — qui vient peut-être d'une connexion inattendue entre domaines.

C'est pour ça qu'on cherche les trous dans le mycelium.

## Références

- **Gödel, K. (1931)** — "Über formal unentscheidbare Sätze der Principia Mathematica und verwandter Systeme I." Monatshefte für Mathematik, 38, 173-198.
- **Turing, A.M. (1936)** — "On Computable Numbers, with an Application to the Entscheidungsproblem." Proc. London Math. Soc., 2(42), 230-265.
- **Church, A. (1936)** — "An Unsolvable Problem of Elementary Number Theory." American Journal of Mathematics, 58(2), 345-363.
- **Tarski, A. (1933)** — "Pojęcie prawdy w językach nauk dedukcyjnych" (Le concept de vérité dans les langages formalisés).
- **Radó, T. (1962)** — "On Non-Computable Functions." Bell System Technical Journal, 41(3), 877-884. — Busy Beaver.
- **Matiyasevich, Y. (1970)** — "Enumerable Sets are Diophantine." Soviet Math. Doklady, 11, 354-358.
- **Baker, T., Gill, J., Solovay, R. (1975)** — "Relativizations of the P=?NP Question." SIAM J. Comput., 4(4), 431-442. — Barrière de relativisation.
- **Razborov, A.A. & Rudich, S. (1997)** — "Natural Proofs." J. Computer and System Sciences, 55(1), 24-35. — Barrière des preuves naturelles.
- **Aaronson, S. & Wigderson, A. (2009)** — "Algebrization: A New Barrier in Complexity Theory." ACM TOCT, 1(1), 2:1-2:54. — Barrière d'algébrisation.

---

*Sky × Claude — 17 février 2026*
*Bloc 7/7 — Le plafond. Prouvé. Absolu. Mais les trous dans le ciel… c'est là qu'on cherche.*
