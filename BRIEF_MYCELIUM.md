# BRIEF — Modèle Mycelium P=NP
## Sky × Claude — 17 Février 2026

---

## VISION

Les 684 symboles scientifiques = **nœuds fixes** d'un réseau (mycelium).
Les papers scientifiques = **la pluie** qui tombe sur ces nœuds.
Chaque paper qui utilise 2+ symboles crée une **arête** (connexion) entre eux.

**But : faire émerger les formules pas encore découvertes.**
Pas prédire la formule elle-même → prédire **quels symboles vont se retrouver
ensemble** dans une future publication. Pointer un doigt : "cherchez là".

---

## ARCHITECTURE : DEUX CARRÉS

### Carré A (engine.py) — LE SOL DUR
- 684 symboles **prouvés uniquement**
- Validés scientifiquement (4 tours de vérification)
- 7 strates × 52 domaines × 0 doublons
- Chaque lettre = un nœud unique = point de connexion entre domaines

### Carré B (engine_carre2.py) — LE CIEL BRUMEUX  
- Copie du carré A + symboles **non prouvés**
- Conjectures (Riemann, Goldbach, P≠NP, Collatz, etc.)
- Problèmes ouverts (Navier-Stokes, Hodge, BSD, etc.)
- Théories non fondées / notations émergentes
- Hypothèses physiques non confirmées

### Le delta entre les deux cartes = la carte des découvertes à venir

- **Même vide fertile dans A et B** → robuste, va émerger
- **Vide fertile dans B invisible dans A** → un symbole non prouvé crée un pont
  entre domaines prouvés qui ne se parlent pas autrement
- **Vide fertile dans A rempli dans B** → la conjecture EST la réponse,
  juste pas encore démontrée

---

## FORMULES SciSci (MOTEUR DE PRÉDICTION)

### Sources validées :
1. **Wang-Song-Barabási (Science 2013)** — fitness + aging + citations
   - Πᵢ(t) ~ ηᵢ cᵢ(t) Pᵢ(t)
   - Impact ultime : cᵢ∞ = m(e^lᵢ - 1)

2. **D-index (Wu-Wang-Evans, Nature 2019)** — disruption
   - D = (nᵢ - nⱼ) / (nᵢ + nⱼ + nₖ)
   - Paper disruptif = connecte sans reprendre l'existant

3. **Uzzi z-scores (Science 2013)** — paires atypiques
   - z = (obs - exp) / sd
   - Hits = cœur conventionnel + queue atypique

4. **Q-model (Sinatra et al, Science 2016)** — opportunité × capacité
   - c₁₀ = Q × p

5. **SemNet (Krenn & Zeilinger, PNAS 2020)** — précédent validé
   - Co-occurrence concepts quantique → prédiction connexions futures ✅

---

## ORGANISATION SPATIALE

### Décision : PAS de placement manuel
La topologie émerge de la pluie (co-occurrence dans les papers).
Les symboles qui apparaissent souvent ensemble se rapprochent naturellement.
→ Vérifier ensuite si ça correspond à la dépendance logique.

### Centre de gravité par strate :
- Strate 0 : = (Recorde 1557) — racine absolue
- Strate 1 : K (halting set) ou ∃
- Strate 2 : ∅' (Turing jump)
- Strate 3 : PH
- Strate 4 : ω
- Strate 5 : ω₁ᶜᵏ
- Strate 6 : HALT

### Note sur la fréquence de papers :
Fréquence = popularité, PAS importance.
Utile APRÈS pour la prédiction (zone morte vs zone fertile),
PAS pour la carte elle-même. Carte ≠ territoire.

---

## VALIDATION DU MODÈLE

Le modèle est validé si :
> Une théorie nouvellement publiée utilise des symboles
> que le modèle avait identifiés comme "vide fertile"
> (connexion probable mais pas encore réalisée).

On prédit pas la vérité → on prédit la **structure** de la prochaine découverte.

---

## TODO
- [ ] Remplir carré B avec symboles non prouvés (conjectures, open problems)
- [ ] Pipeline arXiv → extraction symboles → pluie sur les deux carrés
- [ ] Implémenter link prediction (Common Neighbors, Adamic-Adar, Jaccard)
- [ ] Implémenter scoring SciSci (fitness, D-index, z-scores)
- [ ] Comparer delta carré A vs carré B
- [ ] Test rétroactif : prendre papers 2020, prédire connexions 2025, vérifier
