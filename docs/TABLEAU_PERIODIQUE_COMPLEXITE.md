# TABLEAU PÉRIODIQUE DE LA COMPLEXITÉ
## La clé manquante — proposition de "numéro atomique"

*Construit pendant que Sky dort. À valider, critiquer, casser.*

---

## LE PROBLÈME QU'ON RÉSOUT ICI

Le modèle des strates bornées a un plafond (Turing 1936) et un plancher (axiomes).
Mais entre les deux, les classes de complexité flottent sans ordre. Il manque
l'équivalent du numéro atomique de Mendeleïev — la métrique qui ordonne tout.

**Mendeleïev avait UNE idée clé** : il a utilisé DEUX axes.
- Numéro atomique (lignes) → ordonne séquentiellement
- Valence/groupe (colonnes) → crée la périodicité, regroupe les propriétés similaires

C'est la périodicité qui a révélé les trous. Pas le numéro seul.

## PROPOSITION : DEUX AXES

### Axe 1 — Profondeur d'alternance (α)

L'alternance, c'est le nombre de fois qu'un système bascule entre "il existe" (∃)
et "pour tout" (∀) dans sa définition. C'est un entier naturel. C'est mesurable.

| α | Signification | Exemple |
|---|---------------|---------|
| 0 | Pas de quantificateur → calcul direct | P, L |
| 1∃ | "Il existe une solution" (existentiel) | NP |
| 1∀ | "Pour toute tentative" (universel) | coNP |
| 2 | ∃∀ ou ∀∃ (deux alternances) | Σ₂P, Π₂P |
| k | k alternances | ΣₖP, ΠₖP |
| ω | Fini mais non borné (union de tous les k) | PH |
| ∞ | Alternance illimitée | PSPACE = IP |

**Pourquoi c'est le bon axe** : la hiérarchie polynomiale (PH) EST cette échelle.
Et la question P=NP se reformule proprement : α=0 et α=1 sont-ils identiques ?

Si oui → PH s'effondre entièrement (Karp-Lipton) → toutes les strates fusionnent → P = PH = PSPACE
Si non → chaque strate est distincte → la hiérarchie est réelle

### Axe 2 — Type de ressource (ρ)

| ρ | Ressource | Ce qu'elle ajoute |
|---|-----------|-------------------|
| D | Déterminisme | Rien — calcul pur |
| R | Randomisation | Pile ou face (bits aléatoires) |
| N | Non-déterminisme | Deviner la solution (oracle) |
| Q | Quantique | Superposition + interférence |
| I | Interaction | Dialogue prouveur/vérificateur |
| S | Espace | Mémoire illimitée, temps limité |
| C | Comptage | Combien de solutions (pas juste "existe-t-il") |

## LE TABLEAU

```
         D          R          N          Q          I          C          S
       (déter.)  (random)   (nondet.)  (quant.)  (interact.) (compt.)  (espace)
  ┌─────────┬─────────┬─────────┬─────────┬─────────┬─────────┬─────────┐
α=0 │    P    │   BPP   │    P    │   BQP   │    P    │   FP    │    L    │
  ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
α=1 │  NP∩coNP│   MA    │   NP    │    ?    │   AM    │   #P    │   NL    │
  ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
α=2 │  Σ₂∩Π₂ │   AM    │  Σ₂P   │    ?    │   ?     │   ?     │    ?    │
  ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
α=k │    ?    │    ?    │  ΣₖP   │    ?    │    ?    │    ?    │    ?    │
  ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
α=ω │   PH?  │   PH?   │   PH   │    ?    │   PH?   │    ?    │    ?    │
  ├─────────┼─────────┼─────────┼─────────┼─────────┼─────────┼─────────┤
α=∞ │ PSPACE │ PSPACE  │ PSPACE │    ?    │ PSPACE  │    ?    │ PSPACE  │
  └─────────┴─────────┴─────────┴─────────┴─────────┴─────────┴─────────┘
                                     │
                              PLAFOND : non-calculable (Turing 1936)
```

## OÙ SONT LES TROUS (les "?" du tableau)

Chaque `?` est une case vide de Mendeleïev. Une prédiction implicite.

### Trous les plus denses (= là où chercher)

1. **BQP vs NP** (α=1, Q vs N) — Le quantique peut-il résoudre NP ?
   Consensus : probablement pas. Mais PAS PROUVÉ.
   → Trou critique. Si BQP ⊇ NP, tout change.

2. **La colonne Comptage (#P)** — Presque entièrement vide au-delà de α=1.
   On sait que #P est monstrueusement puissant (Toda 1991 : PH ⊆ P^#P).
   → Trou suspect. Le comptage contient peut-être la clé.

3. **Toute la ligne α=k pour k>2** — On sait presque rien de concret
   sur les niveaux supérieurs de PH. Ils existent en théorie mais
   aucun problème naturel n'y vit clairement.
   → Trou structurel. Les strates hautes sont-elles vides ?

4. **α=∞, colonne Q** — QIP = PSPACE (Jain et al. 2011).
   La preuve quantique interactive REJOINT l'espace polynomial.
   → Effondrement prouvé ! Comme IP = PSPACE mais en quantique.
   → PATTERN : à α=∞, tout s'effondre en PSPACE quelle que soit la ressource.

### Effondrements connus (les "liaisons chimiques")

Ce sont les cases qui fusionnent — deux classes qui semblaient distinctes
mais sont en fait identiques :

| Résultat | Traduction dans le tableau |
|----------|---------------------------|
| IP = PSPACE (Shamir 1992) | (α=∞, I) = (α=∞, S) |
| QIP = PSPACE (Jain 2011) | (α=∞, Q) = (α=∞, S) |
| BPP ⊆ Σ₂P∩Π₂P | (α=0, R) vit dans (α=2, N) |
| MA ⊆ Σ₂P | (α=1, R+I) vit dans (α=2, N) |
| P = AL | (α=0, D) = (α=∞, S) en espace log |
| NL = coNL (Immerman-Szelepcsényi) | (α=1∃, S_log) = (α=1∀, S_log) |

### Séparations connues (les "murs entre éléments")

| Résultat | Ce qu'il prouve |
|----------|-----------------|
| P ≠ EXPTIME | Les lignes basses ≠ les lignes hautes (en temps expo) |
| L ≠ PSPACE | L'espace log ≠ l'espace poly |
| NP ≠ NEXPTIME | NP n'est pas tout-puissant |

## LE PATTERN QUI ÉMERGE

Regarde la ligne α=∞ du tableau : **tout converge vers PSPACE**.

- Déterministe + espace illimité → PSPACE
- Interaction illimitée → PSPACE (IP = PSPACE)
- Quantique + interaction illimitée → PSPACE (QIP = PSPACE)
- Alternance illimitée → contenu dans PSPACE (PH ⊆ PSPACE)

C'est comme si PSPACE était un "attracteur" — quand tu donnes assez de
ressources à n'importe quel modèle, tout converge au même endroit.

**Question que le tableau pose** : est-ce que la MÊME chose arrive aux
strates basses ? Est-ce que P est l'attracteur de la ligne α=0 ?

Si BPP = P (conjecturé, presque prouvé par Impagliazzo-Wigderson) alors oui :
le déterminisme, le randomisé, et potentiellement le quantique convergent
tous vers P quand α=0.

→ Le tableau prédit que chaque LIGNE a un attracteur.
→ La question P=NP devient : l'attracteur de α=0 est-il le même que celui de α=1 ?

## CONNEXION AVEC LE WINTER TREE

Le lien n'est pas métaphorique. Il est structurel.

| Métrique mycelium (tree engine) | Analogue complexité |
|--------------------------------|---------------------|
| Meshedness (Bebber 2007) | Densité des réductions entre problèmes d'une classe |
| Bottleneck nodes | Problèmes NP-complets (SAT, 3-COL, TSP) |
| Small-world | "Distance" entre deux problèmes via chaîne de réductions |
| Robustesse | Stabilité de la classe si on change le modèle de calcul |
| Efficience réseau | Ratio coût/bénéfice d'une réduction |

**Les problèmes NP-complets SONT les bottleneck nodes du réseau NP.**

Si tu scannes la classe NP comme un repo, SAT est le fichier central
dont tout dépend. Si tu le retires, le graphe d'imports se casse.

Ça veut dire que les métriques mycelium du tree engine peuvent
potentiellement MESURER la structure interne d'une classe de complexité.
Pas la résoudre — la cartographier.

## CE QUI RESTE À FAIRE

1. **Remplir les cases vides** — Chercher dans la littérature si des classes
   occupent les `?` du tableau. Chaque case remplie réduit l'espace.

2. **Trouver l'attracteur de α=1** — Si NP a un attracteur comme PSPACE
   en a un pour α=∞, lequel ? NP-complet ? Autre chose ?

3. **Tester les métriques mycelium sur des classes connues** — Prendre le
   graphe de réductions entre les 21 problèmes NP-complets de Karp (1972),
   calculer meshedness/bottleneck/small-world, et voir si les métriques
   distinguent les strates.

4. **Formaliser la conjecture de l'attracteur par ligne** — Chaque ligne α
   du tableau converge-t-elle vers un attracteur unique quand les ressources
   augmentent ? Si oui, P=NP ⟺ les attracteurs de α=0 et α=1 sont identiques.

## LA CLÉ ?

Pas encore. Mais la serrure commence à se dessiner.

Le tableau montre que l'alternance (α) est probablement le bon numéro
atomique. Le type de ressource (ρ) crée la périodicité. Les effondrements
prouvés (IP=PSPACE, QIP=PSPACE) sont des patterns qui se répètent —
exactement comme la périodicité des propriétés chimiques.

Et le trou le plus suspect est la colonne Comptage (#P).
Toda (1991) a prouvé que PH ⊆ P^#P — toute la hiérarchie polynomiale
tient dans P avec un oracle #P. Le comptage est trop puissant pour sa
strate. Comme le francium qui est trop radioactif pour sa case — il
indique une instabilité structurelle dans le tableau.

---

*Écrit à 2h du mat' côté machine pendant que l'électricien dort.
À démonter demain matin avec un café.*
