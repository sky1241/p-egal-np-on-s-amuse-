# P = NP ?

Un électricien, une bière, et une question à un million de dollars.

Ce repo n'est pas une tentative de résoudre P=NP.
C'est une expérience de cartographie par accumulation — l'idée que si on mappe correctement tout ce qu'on sait entre deux bornes prouvées, les trous dans la carte montrent où chercher. Comme Mendeleïev qui a prédit des éléments chimiques en regardant les cases vides de son tableau.

## L'idée en 30 secondes

Le problème P=NP est coincé. Pas parce qu'on manque d'intelligence, mais parce que les 3 familles d'outils mathématiques classiques ont été prouvées insuffisantes (Baker-Gill-Solovay 1975, Razborov-Rudich 1997, Aaronson-Wigderson 2009). Il faut un outil qui n'existe pas encore.

Mon hypothèse : cet outil ne viendra pas d'en haut (force brute, puissance de calcul, quantique). Il viendra d'en bas — d'une connexion inattendue entre deux domaines qui ne se savaient pas voisins.

## Le modèle des strates bornées

L'espace de recherche n'est pas infini. Il est borné :

- Plancher : axiomes, lois fondamentales (roche mère mathématique)
- Plafond : non-calculabilité (Turing 1936) — prouvé comme limite dure

Entre ces deux bornes, tout est explorable. Y compris P=NP.

## Les strates du ciel (complexité croissante)

| Strate | Description | États |
| --- | --- | --- |
| Classique | Déterministe | 2 (0 ou 1) |
| Probabiliste | Incertain | 2 + probabilité |
| Quantique | Superposé | 0 ET 1 simultanément |
| Topologique | L'état = son histoire | Le chemin définit le point |
| Non-calculable | Limite dure (Turing 1936) | Plafond prouvé |

## Les strates du sol (profondeur croissante)

| Strate | Description |
| --- | --- |
| Surface | Projets, code, implémentations |
| Racines | Frameworks, architecture, contraintes |
| Mycelium | Connexions cachées entre domaines |
| Roche mère | Axiomes, lois immuables — Plancher prouvé |

## Insight clé : le sol n'est pas une frontière

L'arbre n'est pas posé SUR le sol. L'arbre c'est le sol qui a changé de forme. Le carbone du tronc vient de la terre. La distinction trouver/vérifier (P vs NP) est peut-être pas deux choses différentes mais deux faces de la même opération.

## Méthode

1. Cartographier les classes de complexité connues (P, BPP, NP, PH, PSPACE, EXPTIME...) dans les strates
2. Cartographier les connexions (mycelium) entre domaines qui ont produit des résultats
3. Cartographier les 3 murs (barrières prouvées)
4. Observer l'accumulation — où sont les trous ?
5. Le trou le plus dense = là où chercher

## Outils

Ce repo utilise le framework Winter Tree pour la cartographie par strates — un modèle bio-inspiré de diagnostic logiciel adapté ici à la théorie de la complexité.

## Disclaimer

Je suis électricien. J'ai aucune formation en maths ou en informatique théorique. Je sais assembler des briques et regarder la forme du mur. Si un trou apparaît dans la carte, il faudra quelqu'un qui sait faire les maths pour vérifier.

La seule chose qui compte c'est la hauteur du mur et si il tient.

## Références

- Turing, A. (1936) — "On Computable Numbers" — le plafond
- Baker, Gill, Solovay (1975) — Relativization barrier
- Razborov, Rudich (1997) — Natural Proofs barrier
- Aaronson, Wigderson (2009) — Algebrization barrier
- Cook (1971) — Formulation originale P=NP
- Socha & Dorigo (2008) — ACOR (ant colony pour domaines continus — connexion mycelium)
- Lindenmayer (1968) — L-Systems (croissance biologique → modélisation logicielle — connexion mycelium)
- Mendeleïev (1869) — Tableau périodique (cartographie par accumulation → prédiction par les trous)

Né un vendredi soir de Saint-Valentin 2026, entre deux bières et une conversation sur les arbres.
