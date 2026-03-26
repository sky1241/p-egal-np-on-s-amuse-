# PROMPT RECHERCHE — God's Number / Rubik's Cube

## Axiome 0 — Le cube est un jouet
Un cube est résolu ou il l'est pas. Y'a pas de "à moitié résolu". Tu prends une face, tu tournes. C'est UN geste. La seule métrique qui existe c'est le nombre de fois que ta main bouge. UN cube, UN God's Number par taille. Le reste c'est du bruit académique.

Conséquence : toute source qui donne un résultat, VÉRIFIER dans quelle métrique. On veut la métrique physique : 1 geste = 1 move (HTM : un 180° = 1 move, car ta main bouge une fois).

## Objectif
Trouver le pont entre la géométrie du cube (faces, symétries, pièces) et le diamètre de son graphe d'états (God's Number). Ratisser maths, physique, informatique. On trie après.

## Ce qu'on a déjà
- GN(2) = 11, GN(3) = 20 — prouvés en HTM
- GN(4) ≥ 31 (borne basse) — MÉTRIQUE NON VÉRIFIÉE, c'est le trou
- Croissance Ω(n²/log n) — prouvé par pigeonhole sur papier
- 11 + 20 = 31 — récurrence Fibonacci ? coïncidence ?
- Formule linéaire GN(n) = 9n - 7 : donne 29 pour n=4, potentiellement vivante si la borne 31 est dans une autre métrique
- Sandwich φ-Cantor-φ : deux forces (chaos = espace d'états exponentiel, ordre = moves latérales) en miroir
- Le ±1 : chaque move est +1 ou -1 sur ta distance au résolu, le reste (7 sur 9 pour n=2) est latéral
- Ratio productif : 2 moves utiles sur 9(n-1) total — le gaspillage augmente avec n
- φ est l'unique base auto-cohérente du système miroir (lemme)

## Axes de recherche

### 1. LA BORNE DU 4×4 — PRIORITÉ ABSOLUE
- Calcul EXACT du pigeonhole pour GN(4×4×4) EN HTM
- Nombre de positions S exact
- Nombre de moves m exact EN HTM (1 geste = 1 move)
- Montrer le calcul complet : log_m(S) = combien ?
- Si le résultat est ≤ 29 : la formule linéaire survit
- Si le résultat est > 29 : elle est morte, on passe à autre chose
- Chercher TOUTE source qui montre le calcul, pas juste le résultat

### 2. DISTRIBUTION DES POSITIONS PAR PROFONDEUR
- Pour 2×2 : combien de positions à distance 1, 2, 3, ..., 11 du résolu ?
- Pour 3×3 : même chose, distances 1 à 20
- Ces données EXISTENT (bruteforce fait)
- La forme de cette distribution = la forme du graphe
- C'est là que le Cantor se cache (ou pas)

### 3. LE RATIO LATÉRAL
- Sur les 9 moves du 2×2 depuis une position aléatoire : combien mènent +1, combien -1, combien 0 (même profondeur) ?
- Ce ratio est-il constant ou varie-t-il avec la profondeur ?
- Même question pour le 3×3 (18 moves)
- C'est le 7/9 — à vérifier avec des vraies données

### 4. RÉCURRENCE FIBONACCI DES GN
- GN(2)=11, GN(3)=20, 11+20=31
- Existe-t-il d'autres suites de diamètres de Cayley graphs qui suivent Fibonacci ?
- Le ratio GN(n+1)/GN(n) converge-t-il vers φ dans d'autres contextes ?

### 5. PHYSIQUE — Connexions
- Analogies cube / systèmes physiques (spin, lattice, réseau cristallin)
- Mixing time vs diamètre : quelle relation ?
- Percolation et transitions de phase sur le graphe du cube
- Entropy / thermodynamique du cube
- Modèles de Potts, Ising sur groupes de permutations

### 6. RÉSEAUX ÉLECTRIQUES ET GRAPHES
- Resistance distance = analogue au diamètre
- Kirchhoff / Laplacien du graphe de Cayley
- Courant dans un réseau = chemin optimal dans le graphe
- Le cube vu comme un circuit : chaque position est un noeud, chaque move est un fil

### 7. THÉORIE DE L'INFORMATION
- Kolmogorov complexity d'une position
- Compression optimale = solve optimal ? (même chose ?)
- Bits minimum pour décrire une position = moves minimum ?

### 8. THÉORIE DES GROUPES
- Groupe de Rubik : ordre exact par taille de cube
- Graphe de Cayley : diamètre, expansion, spectre
- Symétries réductrices : combien, pourquoi
- Cosets de Rokicki pour le 3×3

### 9. PAIR / IMPAIR
- Différence structurelle cube pair vs impair (pas de centre fixe vs centre fixe)
- Impact mesuré sur le God's Number
- Parité dans les groupes de permutations

### 10. GRAPHES EXPANDERS
- Le cube est-il un bon expander ?
- Ramanujan graphs : le cube en est-il un ?
- Spectral gap → borne sur le diamètre (Alon-Boppana)
- Si bon expander → bornes serrées → pigeonhole suffisant

### 11. QUANTUM
- Quantum walks sur graphes de Cayley
- Grover appliqué au cube
- Avantage quantum sur le calcul de GN ?

### 12. NOMBRE D'OR φ
- φ dans la théorie des groupes
- φ dans les quasi-cristaux (Penrose tilings)
- Fibonacci et expansion de graphes
- φ comme constante structurelle (pas décorative)

## Format attendu
Pour chaque source :
- Titre + auteur + année
- Résultat clé (1-2 lignes)
- Lien/référence
- Métrique utilisée (HTM/QTM/STM/OBTM/pas précisé)
- Fiabilité (prouvé / conjecturé / heuristique)
- Tags : [borne] [distribution] [ratio] [fibonacci] [physique] [circuit] [info] [groupe] [pair-impair] [expander] [quantum] [phi]

## Mots-clés
God's Number HTM, Rubik's cube diameter, Cayley graph diameter, pigeonhole principle cube exact calculation, 4x4x4 positions HTM, n×n×n cube lower bound proof, cube state distribution by depth, distance distribution Rubik, lateral moves ratio Cayley graph, Fibonacci recurrence diameter sequence, resistance distance graph, Kirchhoff Laplacian Cayley, Kolmogorov complexity permutation, quantum walk Cayley graph, Ramanujan graph expander diameter, spectral gap permutation group, mixing time Rubik cube, pair impair cube parity God's Number, effective resistance graph diameter, devil's staircase combinatorics
