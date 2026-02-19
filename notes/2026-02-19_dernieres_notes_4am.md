# DERNIÈRES NOTES — 19 février 2026, 04:15
## Les trucs qu'on oublie pas

---

## 1. L'ÉCHELLE DE MESURE INTER-DOMAINES

Problème: physique = 500K papers/an, logique = 5K. On peut pas comparer en absolu.

Solution:
```
poids(symbole, année) = citations / population_du_domaine(année)
```

C'est du PIB par habitant, pas du PIB brut.
Indexer sur la population réelle du domaine, corrigée par la croissance temporelle.
Un paper à 100 citations en logique = séisme. En physique = bruit.

---

## 2. ARBRE DE RÉFLEXION (CACHE STRUCTURÉ)

On peut pas charger 250M papers à chaque requête.
Solution: construire un arbre d'index local:

```
Domaine (physique, chimie, logique...)
  └→ Sous-domaine (quantique, organique, ensembles...)
      └→ Mots-clés top (entanglement, catalyst, forcing...)
          └→ IDs OpenAlex pré-calculés
              └→ Co-occurrences pré-calculées par année
```

Claude navigue l'arbre au lieu de chercher dans 250M.
Réduit les tokens. Ne réduit pas la vision.
C'est une carte routière, pas une restriction.

---

## 3. LA MÉTÉORITE CRÉE UN NOUVEAU SYMBOLE S0

**Insight clé: l'impact ne fait pas que un cratère. Il laisse une NOUVELLE PIERRE sur le sol.**

Exemples:
- Fermat tombe (1995) → CRÉE "courbes elliptiques modulaires" comme outil S0 unifié
- Cohen tombe (1963) → CRÉE "forcing" — n'existait pas avant
- Perelman tombe (2003) → CRÉE "Ricci flow + chirurgie" comme technique S0
- Cook-Levin tombe (1971) → CRÉE "NP-complétude" comme concept S0
- Gödel tombe (1931) → CRÉE "diagonalisation" comme méthode S0

**LE CYCLE COMPLET:**
```
Météorite tombe de Sₙ
  → Impact sur S0
  → Cratère (onde de choc, déplacement des symboles voisins)
  → NOUVEAU SYMBOLE S0 apparaît au point d'impact
  → Ce symbole devient l'outil qui fait tomber la PROCHAINE météorite
```

C'est un cycle auto-catalytique. Chaque preuve crée l'outil de la preuve suivante.
La science ne fait pas que remplir des trous — elle FABRIQUE les outils pour remplir les trous suivants.

**C'est pour ça que l'accélération est exponentielle.**
Mais on la prend pas en compte pour l'instant (trop complexe). On note et on y revient.

---

## TODO COMPLET POUR DEMAIN

1. [ ] Carte de densité ρ(x,z) de S0 via OpenAlex
2. [ ] Échelle de mesure inter-domaines (PIB/habitant)
3. [ ] Arbre de réflexion / cache structuré pour OpenAlex
4. [ ] Calibrer Sedov-Taylor sur PINNs (plus gros cratère x706)
5. [ ] Mapper les symboles S0 CRÉÉS par chaque météorite morte
6. [ ] Toggle C1/C2 dans La Pluie (prompt prêt)
7. [ ] Impact économique P≠NP (brevets, crypto, IA)
8. [ ] Masse des symboles (à ne pas confondre avec l'échelle)

---

*"c'est si bête que je vois pas, comme les clés en face de toi"*
*"plus c'est con mieux ça marche"*
*"indexer sur la population réelle — c'est logique non?"*
*— Sky, 04:15, dernier push avant dodo*
