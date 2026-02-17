# STRATE 1 — LE PREMIER NUAGE · Σ⁰₁ · RÉCURSIVEMENT ÉNUMÉRABLE

> *"Le premier étage au-dessus du sol. On peut lister les 'oui', mais on ne sait jamais quand dire 'non'."*

---

## Définition formelle

Un ensemble S ⊆ ℕ est **Σ⁰₁** (récursivement énumérable, r.e., semi-décidable) si :

```
x ∈ S ⟺ ∃y R(x, y)
```

où R est une relation **décidable** (Δ⁰₀).

Autrement dit : il existe une machine de Turing M telle que :
- Si x ∈ S → M **s'arrête** et accepte (en temps fini)
- Si x ∉ S → M **ne s'arrête jamais** ou rejette

**On peut vérifier les "oui". On ne peut pas garantir les "non".**

## Sa sœur jumelle — Π⁰₁

Un ensemble S est **Π⁰₁** (co-récursivement énumérable, co-r.e.) si :

```
x ∈ S ⟺ ∀y R(x, y)
```

C'est l'exact miroir : le complémentaire d'un ensemble Σ⁰₁ est Π⁰₁, et inversement.

## Le lien avec le sol

```
S est décidable (Δ⁰₀)  ⟺  S est Σ⁰₁ ET S est Π⁰₁
                         ⟺  S ET son complémentaire sont tous les deux r.e.
```

C'est le théorème fondamental qui relie le sol au premier nuage. Si tu peux lister les "oui" ET les "non", alors tu peux décider. Mais si tu ne peux lister que les "oui"... tu es coincé dans le brouillard de Σ⁰₁.

## L'habitant principal — Le Halting Problem

Le problème de l'arrêt est l'ensemble :

```
K = { e ∈ ℕ : la machine de Turing numéro e s'arrête sur l'input e }
```

Variante standard (Halting set) :

```
K₀ = { ⟨e, x⟩ : la machine e s'arrête sur l'input x }
```

### Propriétés de K

| Propriété | Valeur |
|-----------|--------|
| Σ⁰₁ ? | ✅ Oui — on simule la machine e, si elle s'arrête on dit "oui" |
| Décidable (Δ⁰₀) ? | ❌ Non — Turing 1936 |
| Π⁰₁ ? | ❌ Non — son complémentaire K̄ n'est PAS r.e. |
| r.e.-complet ? | ✅ Oui — tout ensemble Σ⁰₁ se réduit à K |

### Preuve de l'indécidabilité (Turing 1936)

Par diagonalisation. Supposons qu'il existe une machine H qui décide K :

```
H(e) = 1  si la machine e s'arrête sur e
H(e) = 0  sinon
```

Construisons une machine D :

```
D(e) = { s'arrête    si H(e) = 0  (la machine e ne s'arrête pas)
        { boucle      si H(e) = 1  (la machine e s'arrête)
```

Question : D(D) s'arrête-t-elle ?
- Si D(D) s'arrête → H(D) = 1 → D(D) boucle. **Contradiction.**
- Si D(D) boucle → H(D) = 0 → D(D) s'arrête. **Contradiction.**

Donc H n'existe pas. K n'est pas décidable. ∎

## Caractérisations équivalentes de Σ⁰₁

Un ensemble S est Σ⁰₁ si et seulement si l'une des conditions suivantes est satisfaite :

1. **Définition logique** : `x ∈ S ⟺ ∃y R(x, y)` avec R décidable
2. **Machine de Turing** : S est accepté par une machine de Turing (qui peut ne pas s'arrêter sur les non-membres)
3. **Domaine** : S est le domaine d'une fonction partielle calculable : `S = dom(φₑ)` pour un certain e
4. **Image** : S est l'image (range) d'une fonction totale calculable, ou S = ∅
5. **Image primitive récursive** : S est l'image d'une fonction primitive récursive, ou S = ∅
6. **Diophantienne** (Matiyasevich 1970) : il existe un polynôme p à coefficients entiers tel que :
   ```
   x ∈ S ⟺ ∃a,b,c,d,e,f,g,h,i ∈ ℕ : p(x, a, b, c, d, e, f, g, h, i) = 0
   ```

La caractérisation 6 est le résultat de Matiyasevich qui résout le 10ème problème de Hilbert : **tout ensemble r.e. est Diophantien**. Conséquence directe : il n'existe pas d'algorithme pour décider si une équation diophantienne a une solution.

## Propriétés de fermeture

Si A et B sont Σ⁰₁ (r.e.), alors :
- A ∪ B est Σ⁰₁ ✅
- A ∩ B est Σ⁰₁ ✅
- Le complémentaire ¬A est Π⁰₁ (pas forcément Σ⁰₁) ⚠️
- L'image de A sous une fonction calculable est Σ⁰₁ ✅
- La préimage de A sous une fonction totale calculable est Σ⁰₁ ✅

**Attention** : Σ⁰₁ n'est PAS fermé sous la complémentation. C'est la différence fondamentale avec Δ⁰₀.

## Exemples d'ensembles Σ⁰₁ (non décidables)

| Ensemble | Description |
|----------|-------------|
| K (Halting Problem) | {e : machine e s'arrête sur e} |
| K₀ | {⟨e,x⟩ : machine e s'arrête sur x} |
| Lne = {M : L(M) ≠ ∅} | Les machines qui acceptent au moins un mot |
| Théorèmes de PA | L'ensemble des théorèmes de l'arithmétique de Peano |
| Ensembles diophantiens | Solutions d'équations polynomiales (Matiyasevich) |
| Ensembles créatifs | r.e. mais "productivement" non récursifs |

## Le saut de Turing — L'escalier vers le nuage 2

Le **saut de Turing** de l'ensemble A est :

```
A' = { e : la machine de Turing numéro e, avec oracle A, s'arrête sur l'input e }
```

Propriétés du saut :
- A est toujours Turing-réductible à A' (on peut "descendre" mais pas "monter")
- A' n'est JAMAIS Turing-réductible à A (le saut est strictement plus dur)
- Le saut de ∅ est K : `∅' = K`
- Le saut de K est K' : le halting problem du halting problem → c'est Σ⁰₂

**Théorème de Post** (la clé de tout l'escalier) :

```
Un ensemble est Σ⁰ₙ₊₁  ⟺  il est r.e. avec oracle ∅⁽ⁿ⁾
```

Autrement dit : chaque strate correspond exactement à un nombre de sauts de Turing. Le saut est l'escalier.

## r.e.-complétude

Un ensemble A est **r.e.-complet** (ou Σ⁰₁-complet) si :
1. A est Σ⁰₁
2. Pour tout ensemble B ∈ Σ⁰₁, il existe une réduction many-one : B ≤ₘ A

```
B ≤ₘ A signifie : il existe une fonction totale calculable f telle que
x ∈ B ⟺ f(x) ∈ A
```

Le Halting Problem K est r.e.-complet. C'est le problème **le plus dur** de Σ⁰₁. Tout problème semi-décidable se traduit en une question sur l'arrêt.

Résultat de Post : il existe des ensembles r.e. qui ne sont **ni** décidables **ni** r.e.-complets. La structure entre le sol et le plafond de Σ⁰₁ est riche et complexe (les degrés de Turing intermédiaires).

## Lien avec le cube

```
    ┌─────────────────────────────┐
    │    PLAFOND — INDÉCIDABLE    │
    │                              │
    │    ...                       │
    │    Σ⁰₂ — Nuage 2            │
    │                              │
    ├──────────────────────────────┤
    │    Σ⁰₁ — ON EST ICI         │  ← Premier nuage
    │    Le brouillard commence    │
    │    On voit les "oui"         │
    │    Les "non" sont invisibles │
    │    K = Halting Problem       │
    ├══════════════════════════════╡
    │    Δ⁰₀ — LE SOL             │
    └─────────────────────────────┘
```

Σ⁰₁ est le premier pas dans l'inconnu. La frontière entre ce qu'on contrôle (le sol) et le brouillard. Le Halting Problem est la porte d'entrée — le problème le plus simple qui soit impossible à décider.

## Références

- **Turing, A.M. (1936)** — "On Computable Numbers..." — Preuve de l'indécidabilité de K.
- **Post, E.L. (1944)** — "Recursively Enumerable Sets and Their Decision Problems." Bull. AMS, 50, 284-316. — Degrés intermédiaires, r.e.-complétude.
- **Kleene, S.C. (1943)** — "Recursive Predicates and Quantifiers." Trans. AMS, 53(1), 41-73. — Hiérarchie arithmétique.
- **Matiyasevich, Y. (1970)** — "Enumerable Sets are Diophantine." Soviet Math. Doklady, 11, 354-358. — Tout ensemble r.e. est diophantien.
- **Rice, H.G. (1953)** — "Classes of Recursively Enumerable Sets and Their Decision Problems." Trans. AMS, 74(2), 358-366.
- **Friedberg, R.M. (1957)** — "Two Recursively Enumerable Sets of Incomparable Degrees of Unsolvability." Proc. Natl. Acad. Sci., 43, 236-238. — Degrés intermédiaires existent.
- **Soare, R.I. (1987)** — *Recursively Enumerable Sets and Degrees.* Springer.

---

*Sky × Claude — 17 février 2026*
*Bloc 2/7 — Le premier nuage. Le brouillard commence.*
