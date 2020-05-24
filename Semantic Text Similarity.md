
# Which pair of words are most similar

1. group similar words into sematic concepts
2. Textual entailment (one sentence draws meaning from another sentence) or paraphrasing (rewriting with same meaning)

## WordNet package for words interlinked by  semantic relations
- Includes synonyms, hypernyms etc.

* WordNet uses information hierarchy 

### Path Similarity 
* Finds the shortest path between the two concepts
* PathSim(deer, elk) = 0.5

### Lowest Common Subsumer (LCS)
* Finds the closest ancestor to both concepts / closest group
* LCS(deer,elk) = deer

### Lin Similarity
* Similarity measure based on the information contained in the LSC of the two concepts

LinSim(u,v)  = 2 * log P(LCS(u,v)) / (log P(u) + log P(v)

P(u) is given by the information content learnt over a large corpus

## Collocations and Distributional Similarity
* Two words appear in similar contexts are more likely to be semantically related
* Context based on words before and after
* Specific relation to the target word

*  Strength of association of words & Co-Location
* How frequent the individual words

Point wise Mutual Information PMI(w,c) = log[P(w,c)/P(w)P(c)]  