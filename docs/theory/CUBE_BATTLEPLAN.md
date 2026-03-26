# CUBE — Plan de Bataille

## Le Concept en 1 phrase
Un code qui se regenere tout seul par destruction/reconstruction atomique via le mycelium.

## CORRECTION FONDAMENTALE
Le cube c'est PAS un nouveau systeme. C'est la division du mycelium par lui-meme.
Le mycelium a tout cartographie. Le cube = le mycelium qui se subdivise et teste
sa propre connaissance. C'est le mycelium qui se fractionne pour mesurer sa resilience.

---

## Architecture

```
SCAN TOTAL → COPIE LOCALE (jamais toucher le code source du client)
        ↓
MYCELIUM construit a partir du scan (la CARTE des voisins)
        ↓
DECOUPE COPIE (Laplacian RG — suit la structure du code, pas arbitraire)
        ↓
PERPLEXITE (1 appel — tri rapide chaud/tiede/froid)
        ↓
DESTRUCTION/RECONSTRUCTION (11 tentatives — UNIQUEMENT cubes tiedes)
        ↓
VALIDATION (SHA-256 normalise — whitespace strippe avant hash)
        ↓
SCORING (Tononi Degeneracy pre-calcule + proper scoring rules gradient)
        ↓
REMONTE D'UN NIVEAU (88 → 704 → 5632 → ...)
        ↓
RECOMMENCE jusqu'a completion carte totale
        ↓
CONVERGENCE (delta temperature moyenne < 0.01 = stop)
        ↓
PURGE copie locale (mycelium sait reconstruire = copie plus necessaire)
```

### Niveaux de decoupe (exemple 100K lignes)
| Niveau | Tokens/cube | Cubes | Difficulte |
|--------|-------------|-------|------------|
| 1 | 88 | ~1136 | MAX (atomique) |
| 2 | 704 | ~142 | Haute |
| 3 | 5632 | ~18 | Moyenne |
| 4 | 45056 | ~2 | Facile |

Plus tu montes = plus le mycelium a appris des niveaux en dessous = plus c'est facile.

### God's Number
= nombre minimum de VALEURS irreconstructibles (pas de lignes de code).
Le code c'est du texte, trivial a reconstruire. Les valeurs (timeout=3000) c'est le vrai tresor.
Moins y'en a = plus le code est resilient.

---

## Cout = ZERO

| Mode | Comment | Cout | Securite |
|------|---------|------|----------|
| LLM du client | Plugin sur Claude/GPT/Copilot deja paye | 0 | Code sort vers API |
| LLM local | Ollama/Llama sur leur infra | 0 | 100% local |
| Mode L9 | Meme pipeline, mode compress vs reconstruct | 0 | Redirige le tuyau existant |

Le client choisit. On-premise = Ollama. Sinon = leur LLM existant.
Le LLM connait DEJA tous les langages — zero adaptateur, zero pip install.

---

## Securite CRITIQUE

- Le cube travaille sur une COPIE du code, JAMAIS le code source du client
- Scan → copie interne → cube decoupe la copie → code source jamais touche apres le scan
- Apres convergence : PURGE la copie, reste que le mycelium (quelques MB)
- Zero serveur pour nous. Tout est local chez le client.

---

## Les 9 voisins
PAS geometriques. = les 9 cubes avec les co-occurrences les plus fortes dans le mycelium.
Le mycelium EST la carte des voisins.

### Bootstrap
Premier cycle = imports + appels de fonction. C'est declaratif, fiable, deja dans le code.
Les cycles suivants affinent. Pas besoin d'inventer.

---

## Perplexite vs 11 tentatives

| Methode | Vitesse | Fiabilite | Usage |
|---------|---------|-----------|-------|
| Perplexite (1 appel) | 11x plus rapide | ESTIMATION — le LLM peut etre confiant et FAUX | Pre-tri rapide |
| 11 tentatives + SHA-256 | Lent | PREUVE — le hash ment pas | Verification definitive |

**DANGER perplexite seule :** fausse securite. Le LLM reconstruit timeout=5000 avec confiance 0.98 alors que la vraie valeur est 3000. Perplexite dit "froid", SHA-256 dit "CHAUD".
**Strategie :** perplexite pour le tri → 11 tentatives sur TOUT pour la preuve. Zéro raccourci sur les preuves.
Le cube c'est un systeme de PREUVES, pas d'estimations. C'est ce qui le rend vendable.

### Estimation temps (300K lignes)
- 3M tokens ÷ 88 = ~34,000 cubes
- Full test : 34,000 × 11 = 374,000 appels ≈ 60h 24/7 ≈ 1 semaine en mode creux
- Avec perplexite pre-tri : ~30h (mais sans garantie complete)

---

## Valeurs critiques (le vrai tresor)
Le code (texte) = trivial a reconstruire.
Les VALEURS (timeout=3000, retry=3) = le vrai savoir non-documente.
Les cubes chauds au niveau atomique = les magic numbers irreplacables.

### Le mycelium croise avec l'historique git
mycelium.observe() croise git blame/git log pour lier valeurs a leur origine.
"La co-occurrence entre ce timeout et l'incident de 2024"
Le mycelium sait POURQUOI la valeur est la, pas juste qu'elle existe.

---

## Mecanismes de protection

### Rollback automatique
Snapshot des poids AVANT chaque cycle. Delta trop gros = rollback.
Meme principe que le WAL — checkpoint avant, rollback si merde.

### Seuil de convergence
Temperature moyenne de tous les cubes. Delta entre 2 cycles < 0.01 = stop.
Le reseau a plus rien a apprendre.

### Concurrence cube vs dev
File watcher — si fichier ouvert dans l'IDE, cube skip. Revient plus tard.
Le hook IDE sait deja quels fichiers sont ouverts.

### Stockage resultats
Table cube_cycles dans mycelium.db. Resultat par cube par niveau.
1136 cubes × 5 niveaux = 5680 lignes. Rien pour SQLite.
Purge vieux cycles apres convergence.

---

## Scheduling
- Async dans les creux (meme logique que checkpoints WAL)
- Quand personne push → cube bosse
- Quand ca rush → cube s'arrete
- Premiere semaine = bruite (mycelium vierge). Semaine 2+ = mature.

---

## Stack complete (V2 Muninn)

| Composant | Role | Status |
|-----------|------|--------|
| Muninn core | Compression memoire LLM, mycelium | FAIT |
| Scan repo | Nourrit le mycelium depuis le code | FAIT |
| Meta-mycelium | Cross-repo, ~/.muninn/ | FAIT |
| Chiffrement AES-256 | Securite locale | FAIT |
| Credential redaction | Detection passive | FAIT |
| Forge | Auto-debug (Kalman, delta, mutation) | FAIT |
| Cube | Destruction/reconstruction | A CODER |
| Forge ← Muninn | Debug cible par temperature | A BRANCHER |
| Auto-repair Forge | 3 patchs, mutation test, dev valide | A CODER |
| Feedback loop | Bug fixe → nourrit mycelium → prediction | A CODER |
| Tree | Visu zones chaudes | FAIT (a brancher) |
| Hooks multi-LLM | GPT, Copilot, Claude, Ollama | A CODER |
| Scheduling async | Cube dans les creux | A CODER |
| LLMProvider interface | Backends: ollama, llama, mistral, phi, claude, gpt | A CODER |

---

## Les 18 points a coder (avec updates Ygg)

### FORGE (3 points)
1. **Lien Muninn → Forge** — temperature guide le debug, Forge cible au lieu de scanner tout
2. **Auto-repair** — genere 3 patchs, mutation testing valide, dev approuve
3. **Feedback loop** — chaque bug fixe nourrit le mycelium, prediction a 6 mois

### CUBE - LE MOTEUR (5 points)
4. **Subdivision** — Laplacian RG (suit la structure, pas arbitraire) jusqu'a 88 tokens
5. **Reconstruction** — 9 voisins mycelium + LLM, perplexite en pre-tri + 11 tentatives pour preuve
6. **Validation** — SHA-256 normalise + proper scoring rules gradient
7. **Scoring cubes chauds** — Tononi Degeneracy pre-calcule AVANT destruction
8. **Remontee par niveaux** — 88 → 704 → 5632, carte se dessine automatiquement

### LLM & INFRA (6 points)
9. **Support LLM locaux** — interface LLMProvider (Ollama/Llama/Mistral/Phi/Claude/GPT)
10. **Plugin client** — se branche sur LEUR LLM, zero cout
11. **Cut L9 meme pipeline** — mode compress vs reconstruct dans le meme tuyau
12. **Hooks multi-LLM** — ChatGPT, Copilot, Ollama, etc.
13. **Scheduling async** — tourne dans les creux, s'arrete quand ca rush
14. **Securite local vs API** — flag local_only, le client choisit

### GRATIS (1 point)
15. **Multi-langage** — rien a coder, le LLM sait deja

### VISU & FINITION (3 points)
16. **Tree heatmap** — visu cubes chauds/froids par niveau
17. **V9A++ Planaire** — code auto-regenerant, le couronnement
18. **Detection valeurs critiques** — les cubes que le LLM rate = les magic numbers

---

## Plan d'execution

### Jour 1-2: POC perplexite + destruction sur Muninn
- [ ] Prendre 1 module de Muninn (le serpent qui se bouffe la queue)
- [ ] Decouper en cubes de 88 tokens (Laplacian RG)
- [ ] Perplexite en pre-tri
- [ ] Detruire cubes tiedes, reconstruire depuis 9 voisins
- [ ] Valider SHA-256
- [ ] Si ca marche → le concept est prouve

### Jour 3-4: Integration cube → mycelium + NCD
- [ ] Feedback loop: resultats destruction nourrissent le mycelium
- [ ] Temperature auto-calculee par taux d'echec reconstruction
- [ ] Remontee par niveaux (88 → 704 → 5632)
- [ ] Convergence detection (delta < 0.01)

### Jour 5-6: Hooks multi-LLM
- [ ] Adaptateur Claude CLI
- [ ] Adaptateur GPT API
- [ ] Adaptateur Copilot
- [ ] Adaptateur Ollama (local)

### Jour 7: Tree heatmap + Laplacian RG
- [ ] Brancher Tree sur les zones chaudes du cube
- [ ] Visualisation temps reel des cubes chauds/froids
- [ ] Integration Laplacian RG dans le decoupage

### Jour 8-10: Polish + tests
- [ ] Run complet sur Muninn (serpent qui se bouffe la queue)
- [ ] Run complet sur un repo externe
- [ ] Benchmarks: temps, precision, nombre de cubes chauds

---

## Formules existantes qui supportent
- Candes-Recht-Tao 2009: matrix completion, seuil garanti de reconstruction exacte
- Code = rang effectif r bas (patterns, conventions) → seuil atteignable
- Kolmogorov: complexite minimale = plancher incompressible
- Graham inverse: contrainte de reduction maximale

---

## Concepts fondamentaux

### Les poids deviennent des PREUVES
Avant le cube: "A et B apparaissent ensemble" (co-occurrence passive)
Apres les cycles: "A est VITAL pour B" / "A peut etre reconstruit depuis B,C,D" (preuve de dependance)

### C'est de l'IMMUNOLOGIE
Pas du debug. On rend le systeme malade EXPRES pour qu'il developpe des anticorps.

### C'est de la PLOMBERIE pas de la recherche
Les pieces existent DEJA. Zero recherche fondamentale. Du branchement.

### Ca existe NULLE PART
Auto-repair avec validation par mutation testing. Combinaison inedite.

---

## Le Pitch (quand c'est pret)
- "Votre code se regenere tout seul"
- "Le programme apprend en cassant et reconstruisant en boucle"
- "Ca tourne en local. Ca coute rien en plus"
- "Au bout d'un mois il connait votre code mieux que vos devs"
- "Vous aurez bientot un backup gratuit et intelligent qui sait exactement ou et quoi reconstruire"

---

## Metaphores (pour vendre, pas pour coder)
- **Planaire**: coupe un morceau, il repousse
- **Rubik's Cube**: God's Number = minimum pour tout resoudre
- **Mycelium**: le reseau souterrain qui fait tout repousser
- **Systeme immunitaire**: tu rends le code malade expres pour qu'il developpe des anticorps
- **Opus Magnum**: chaque puzzle a un minimum de pieces = plancher incompressible
- **Outer Wilds**: le canon orbital = trajectoire optimale dans l'espace des solutions
