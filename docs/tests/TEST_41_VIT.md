# TEST #41: Vision Transformer (ViT) — NLP × Computer Vision

## Thèse pont
**Dosovitskiy et al. 2020** — "An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale" (Google Brain)
- Applique le Transformer (Vaswani 2017, architecture NLP) directement aux images
- Prouve que l'attention pure bat les CNNs sur ImageNet
- ~45,000+ citations (Google Scholar, toutes versions)

**Thèse sous-jacente**: Vaswani et al. 2017 "Attention Is All You Need" (~130,000 citations)
- Architecture Transformer = NLP only à l'origine
- ViT = le pont vers Computer Vision

## Cartographie du trou AVANT

| Période | NLP×CV/an | Diagnostic |
|---------|-----------|------------|
| 2005-2013 | 236→396 | Connexion EXISTANTE mais faible. Image captioning, VQA. |
| 2014-2017 | 411→503 | Croissance lente. NLP=RNN, CV=CNN, architectures SÉPARÉES. |
| Le trou n'est pas un ZÉRO — c'est un MUR ARCHITECTURAL. |

NLP et CV se parlaient (image captioning, visual QA, scene understanding) mais avec des architectures complètement différentes : RNN/LSTM pour le texte, CNN/ResNet pour les images. Le "trou" n'est pas un vide de papers — c'est un vide d'ARCHITECTURE PARTAGÉE.

## Données OpenAlex (C204321447 × C31972630)

**NLP × Computer Vision (co-occurrence):**
| 2005 | 2010 | 2014 | 2017 | 2018 | 2019 | 2020 | 2021 | 2023 | 2024 | 2025 |
|------|------|------|------|------|------|------|------|------|------|------|
| 236  | 358  | 411  | 503  | 681  | 826  | 910  | 1138 | 1648 | 2934 | 3574 |

## Pattern APRÈS le pont

- Pré-Transformer (2005-2017): 236→503 = **x2.1** en 12 ans (lent)
- Post-ViT (2020-2025): 910→3574 = **x3.9** en 5 ans (explosion)
- 2023→2025: 1648→3574 = **x2.2** en 2 ans (accélération LLM+Vision: GPT-4V, Gemini, DALL-E)

## Bridge papers (top cited à l'intersection NLP×CV)
- Zhao et al. 2017 (14,988 cit): PSPNet — scene parsing (pré-Transformer)
- Krishna et al. 2017 (5,029 cit): Visual Genome — le dataset qui FORCE le pont langue↔image
- Le ViT lui-même n'apparaît pas dans les top co-occurrence car OpenAlex le tague "CV" pas "NLP×CV"

## Lianes S0 utilisées
Le Transformer utilise: {exp (softmax), Σ (attention sum), ∇L (backprop), Attn (self-attention), ∂ (gradient), E[X] (layer norm)}
- Attn = liane IA×Bio×Fin (3 continents)
- exp = liane universelle (6 continents) 
- Σ = liane universelle (6 continents)

## Diagnostic
**Pattern 3 (Théorie × Outil)** — pas un Pattern 1 classique.
- La THÉORIE (attention mechanism, Bahdanau 2014) existait
- L'OUTIL (Transformer architecture) manquait
- Le pont ViT (2020) a fusionné l'outil NLP avec le domaine CV
- L'explosion 2023-2025 vient des LLMs multimodaux (GPT-4V, Gemini)

Le trou n'était pas un vide de papers mais un **mur architectural** : deux communautés qui parlaient le même langage mathématique (exp, Σ, ∇L) mais avec des implémentations incompatibles (RNN vs CNN). Le Transformer a unifié l'architecture.

## Validé ✅ — Pattern 3 (Théorie × Outil) — le mur architectural, pas le vide
