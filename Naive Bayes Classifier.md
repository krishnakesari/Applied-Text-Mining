
# Classifying text search queries

* Likelihood of the class given new information

Prior Probability: Pr(y=Entertainment), Pr(y=CS), Py(y= Zoology)
Posterior Probability: Pr(y=Entertainment|x = "Python")

## Bayes Rule

Posterior probability = Prior probability * Likelihood / Evidence

Pr(y|X) = Pr(y) * Pr(X|y)/Pr(X)

y*= argmax Pr(y|X) = argmax Pr(y)* Pr(X|y)

Given the class label, features are assumed to be independent of each other.

## Learning Parameters

Prior Probabilities - Training data - Number of instances in each class

Likelihood: Pr(Xi | y)   for all features Xi and labels y in Y

### Smoothing

What happens if Pr(Xi | y) = 0 ?  if the feature never occurred before
Solution: Add a dummy count - Add 1 to every feature
Pr(Xi | y) = (k + 1) / (p + n) where n is number of features

### Variations

* Multi-nominal Naive Bayes model
  Each feature value is a count (word occurrence and TF-IDF)

* Bernoulli Naive Bayes model
  Each feature is a binary feature (word is present or absent)
  Doesn't account for significance
