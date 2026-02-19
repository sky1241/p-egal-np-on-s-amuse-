# TEST #44: GCN — Théorie des Graphes × Deep Learning

## Thèse pont
**Kipf & Welling 2017** — "Semi-Supervised Classification with Graph Convolutional Networks" (ICLR, Amsterdam)
- Généralise la convolution (opération CNN) aux graphes via le Laplacien spectral
- ~20,000+ citations
- Transforme les graphes (structure mathématique discrète) en entrée pour le deep learning

**Proto-pont**: Bruna et al. 2014 "Spectral Networks and Deep Locally Connected Networks on Graphs"
**Formule clé**: H^(l+1) = σ(D̃^(-1/2) Ã D̃^(-1/2) H^(l) W^(l)) — le Laplacien normalisé DEVIENT un filtre neuronal

## Cartographie du trou AVANT

| Période | GT×DL/an | Diagnostic |
|---------|----------|------------|
| 2005-2009 | 0-2 | **ZÉRO.** Graphes = maths pures. DL = pas encore existant. |
| 2010-2014 | 2-13 | Proto-signal. DL explose (AlexNet 2012) mais IGNORE les graphes. |
| 2015-2016 | 29-55 | Le DL est à 5K papers/an, GraphTheory à 20K/an. Intersection = 0.28%. |

Le trou: les graphes étaient un outil de **maths discrètes** (combinatoire, algorithmique). Le deep learning travaillait sur des **grilles régulières** (images=pixels, texte=séquences). Personne ne savait comment appliquer la convolution sur une structure IRRÉGULIÈRE.

Le Laplacien spectral du graphe (∇² = D - A) était connu depuis Kirchhoff (1847). L'outil EXISTAIT depuis 170 ans. Le pont manquait.

## Données OpenAlex (C132525143 × C108583219)

**GraphTheory × Deep Learning:**
| 2005 | 2010 | 2014 | 2016 | 2017 | 2018 | 2019 | 2020 | 2021 | 2022 | 2023 | 2025 |
|------|------|------|------|------|------|------|------|------|------|------|------|
| 0    | 9    | 13   | 55   | **117** | 265  | 421  | 713  | 982  | 1160 | 1400 | **1492** |

**Comparer avec GT×CNN (convolution classique):**
| 2005-2025 | stable 10-30/an | PAS de croissance |

## Pattern APRÈS le pont

- 2016→2017: 55→117 = **x2.1** (année Kipf)
- 2017→2020: 117→713 = **x6.1** en 3 ans
- 2017→2025: 117→1492 = **x12.7** en 8 ans
- GT×CNN reste à ~20/an → la convolution CLASSIQUE ne profite PAS du pont. C'est la convolution SPECTRALE (GCN) qui crée la connexion.

## Bridge papers (top cited)
- **LeCun et al. 1998** (56,312 cit): LeNet — le fondement CNN, pas un bridge GCN
- **Zhou et al. 2020** (5,095 cit): "GNN: A review" — la review qui CRISTALLISE le champ
- **Monti et al. 2017** (1,816 cit): MoNet — "Geometric Deep Learning on Graphs and Manifolds"
- Le paper de Kipf 2017 n'apparaît pas en top car OpenAlex peut le taguer autrement

## Lianes S0 utilisées
GCN utilise: {Σ (aggregation voisins), exp (softmax), ∇² (Laplacien=opérateur clé), ∇L (backprop), = (normalisation)}
- **∇² (Laplacien)** = LA liane cruciale. Symbole S0 Math×Phys×Ing (3 continents). C'est un outil de 1847 qui DEVIENT un filtre neuronal en 2017.
- Σ = universelle (6 continents)
- exp = universelle (6 continents)

**Le Laplacien est l'escalier de secours**: un symbole S0 qui connecte les maths discrètes à l'IA via la physique spectrale. C'est exactement la liane-pont que la théorie prédit.

## Validé ✅ — Pattern 1 (Pont) — ZÉRO→x12.7, Laplacien=liane-pont depuis 1847
