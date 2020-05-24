# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import nltk
from nltk.corpus import wordnet as wn


# %%
#import nltk
#import ssl

#try:
   #_create_unverified_https_context = ssl._create_unverified_context
#except AttributeError:
  #  pass
#else:
#    ssl._create_default_https_context = _create_unverified_https_context

# nltk.download('wordnet')


# %%
deer = wn.synset('deer.n.01') # Find the 1st meaning on the noun deer
elk = wn.synset('elk.n.01')
horse = wn.synset('horse.n.01')


# %%
# Find path similarity
deer.path_similarity(elk)
deer.path_similarity(horse)


# %%
# Find Lin Similarity
from nltk.corpus import wordnet_ic
brown_ic = wordnet_ic.ic('ic-brown.dat')
semcor_ic = wordnet_ic.ic('ic-semcor.dat')


# %%
deer.lin_similarity(elk, semcor_ic)


# %%
deer.lin_similarity(elk, brown_ic)
deer.lin_similarity(horse,brown_ic)


# %%
# Mesuring Collocation Semantic Similarity
from nltk.collocations import *
text = "Cat into the house and fox jumped"

bigram_measures = nltk.collocations.BigramAssocMeasures()

finder = BigramCollocationFinder.from_words(text)

finder.nbest(bigram_measures.pmi, 10)

