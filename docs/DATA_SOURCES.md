# SOURCES DE DONNÉES — Pluie pour le Mycelium
## Sky × Claude — 17 Février 2026

---

## OBJECTIF
Faire tomber la pluie (papers scientifiques) sur le graphe des 797+ symboles
pour créer les arêtes de co-occurrence et identifier les trous structurels.

---

## SOURCES PRINCIPALES

### 1. OpenAlex (⭐ PRIORITÉ)
- **URL**: https://openalex.org
- **API**: https://api.openalex.org
- **Coût**: Gratuit, pas de clé requise
- **Volume**: 250M+ works
- **Couverture temporelle**: 1900 → présent
- **Points forts**: Concepts déjà tagués, API REST simple, filtres par année/domaine
- **Exemple d'appel**:
  ```
  https://api.openalex.org/works?filter=publication_year:1980-1990,concept.id:C2777572654&per_page=200
  ```
- **Doc**: https://docs.openalex.org

### 2. Semantic Scholar
- **URL**: https://www.semanticscholar.org
- **API**: https://api.semanticscholar.org/graph/v1
- **Coût**: Gratuit (clé recommandée pour rate limits)
- **Volume**: 200M+ papers
- **Couverture temporelle**: Très large, pré-1991
- **Points forts**: Abstracts disponibles, citations, champs de recherche tagués
- **Exemple d'appel**:
  ```
  GET /paper/search?query=elliptic+curves+modular+forms&year=1980-1990&limit=100
  ```
- **Doc**: https://api.semanticscholar.org

### 3. Zbmath Open
- **URL**: https://zbmath.org
- **API**: https://api.zbmath.org
- **Coût**: Gratuit (open access depuis 2021)
- **Volume**: 4.5M+ publications mathématiques
- **Couverture temporelle**: 1868 → présent
- **Points forts**: MSC (Mathematics Subject Classification) — classification officielle des maths
- **MSC utile pour**: Mapper précisément quel domaine mathématique ↔ quels symboles
- **Doc**: https://api.zbmath.org/docs

### 4. arXiv
- **URL**: https://arxiv.org
- **API**: http://export.arxiv.org/api/query
- **Bulk**: https://info.arxiv.org/help/bulk_data_s3.html (via S3)
- **Coût**: Gratuit
- **Volume**: 2.4M+ papers
- **Couverture temporelle**: 1991 → présent
- **Points forts**: Full text accessible (LaTeX source), symboles extractibles directement du code
- **Limitation**: Pas avant 1991

### 5. JSTOR (backup)
- **URL**: https://www.jstor.org
- **API**: Data for Research (DfR) — https://www.jstor.org/dfr/
- **Coût**: Gratuit pour la recherche
- **Volume**: 12M+ articles
- **Couverture temporelle**: 1800 → présent
- **Points forts**: Journaux historiques numérisés
- **Limitation**: Accès full-text limité, mais métadonnées + n-grams disponibles

### 6. Google Scholar (scraping)
- **URL**: https://scholar.google.com
- **API**: Pas d'API officielle (serpapi.com comme proxy payant)
- **Couverture**: La plus large, tous domaines
- **Limitation**: Scraping fragile, rate limits agressifs
- **Usage**: Vérification manuelle, pas pour le pipeline

---

## STRATÉGIE DE PLUIE

### Phase 1 — Test Fermat (MAINTENANT)
- Source: OpenAlex ou Semantic Scholar
- Période: 1980-1990 (snapshot pré-résolution)
- Domaines: courbes elliptiques, formes modulaires, Galois
- Objectif: ~500-2000 papers, extraire co-occurrences de concepts

### Phase 2 — Validation élargie
- Source: OpenAlex + Zbmath
- Période: 1980-2026 (film complet)
- Objectif: Voir le trou se remplir au fil du temps

### Phase 3 — Pluie globale (si Phase 1-2 positives)
- Source: OpenAlex bulk
- Période: 1950-2026
- Tous domaines
- Objectif: Carte complète, identification des vides fertiles actuels

---

## EXTRACTION DES SYMBOLES

### Méthode 1 — Concepts tagués (rapide)
OpenAlex et Semantic Scholar taguent déjà les concepts.
→ Mapper leurs concepts vers nos 797 symboles.

### Méthode 2 — Abstracts (moyen)
Parser les abstracts pour trouver les symboles grecs et notations mathématiques.
→ Regex sur α, β, γ, Σ, ∫, etc.

### Méthode 3 — LaTeX source (précis mais arXiv only)
Extraire directement du code LaTeX : \alpha, \beta, \sum, \int, etc.
→ Le plus précis mais limité à post-1991.

### Méthode 4 — MSC codes (Zbmath)
Chaque paper a un code MSC (ex: 11G05 = courbes elliptiques).
→ Mapper MSC → symboles associés au domaine.

---

## NOTES

- La fréquence de papers ≠ importance. Finance a 100x plus de papers que calculabilité.
- La pluie est biaisée. En être conscient. Ne PAS utiliser la fréquence brute comme poids.
- La co-occurrence = lien. Deux symboles dans le même paper = arête.
- Un paper qui utilise des symboles de deux domaines différents = pont inter-domaines.
- Les trous = paires de symboles jamais co-occurrents malgré des voisins communs.

---

## LIENS RAPIDES

| Source | API | Gratuit | Pré-1991 | Concepts tagués |
|--------|-----|---------|----------|-----------------|
| OpenAlex | ✅ | ✅ | ✅ | ✅ |
| Semantic Scholar | ✅ | ✅ | ✅ | ✅ |
| Zbmath | ✅ | ✅ | ✅ | ✅ (MSC) |
| arXiv | ✅ | ✅ | ❌ | ❌ (mais LaTeX) |
| JSTOR | ✅ (DfR) | ✅ | ✅ | ❌ |
| Google Scholar | ❌ | — | ✅ | ❌ |
