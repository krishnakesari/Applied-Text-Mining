# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
## Basic NLP tasks with NLTK
import nltk
from nltk.book import *


# %%
text7
sent7
len(sent7) # Number of sentenses
len(text7) # Number of words
len(set(text7)) # number of unique words
list(set(text7))[:10] # First ten of unique words


# %%
## Frequency of words
dist = FreqDist(text7)
len(dist)


# %%
vocab1 = dist.keys() # Frequency distribution of words- count of number of times
list(vocab1)[:10]


# %%
dist['four']


# %%
freqwords = [w for w in vocab1 if len(w)>5 and dist[w] > 100]
freqwords


# %%
# Normalizing and Stemming
input1 = "List listed lists listing listings"
words1 = input1.lower().split(' ')
words1


# %%
porter = nltk.PorterStemmer()  # Stemming
[porter.stem(t) for t in words1]


# %%
# Lemmatization
udhr = nltk.corpus.udhr.words('English-Latin1')
udhr[:20]


# %%
[porter.stem(t) for t in udhr[:20]] 


# %%
WNlemma = nltk.WordNetLemmatizer()
[WNlemma.lemmatize(t) for t in udhr[:20]]


# %%
# Tokenization
text11 = "Children shouldn't drink a sugary drink before bed."
text11.split(' ')


# %%
nltk.word_tokenize(text11)


# %%
text12 = "This is the first sentence. A gallon of milk in the U.S. costs $2.99. Is this the third sentence? Yes, it is!"
sentences = nltk.sent_tokenize(text12)
len(sentences)


# %%
sentences


# %%
# Advanced NLP tasks with NLTK
## POS Tagging
nltk.help.upenn_tagset('MD')


# %%
text13 = nltk.word_tokenize(text11)
nltk.pos_tag(text13)


# %%
text14 = nltk.word_tokenize("Visiting aunts can be a nuisance")
nltk.pos_tag(text14)


# %%
## Parsing sentence structure
text15 = nltk.word_tokenize("Alice loves Bob")
grammer = nltk.CFG.fromstring("""
S -> NP VP
VP -> V NP
NP -> 'Alice' | 'Bob'
V -> 'loves'
""")

parser = nltk.ChartParser(grammer)
trees = parser.parse_all(text15)
for tree in trees:
    print(tree)


# %%
text16 = nltk.word_tokenize("I saw the man with a telescope")
grammer1 = nltk.data.load("mygrammer.cfg")
grammer1


# %%
parser = nltk.ChartParser(grammer1)
trees = parser.parse_all(text16)
for tree in trees:
    print(tree)


# %%
from nltk.corpus import treebank
text17 = treebank.parsed_sents('wsj_0001.mrg')[0]
print(text17)


# %%
# POS tagging and parsing ambiguity
text18 = nltk.word_tokenize("The old man the boat")
nltk.pos_tag(text18)


# %%
text19 = nltk.word_tokenize("colorless green ideas sleep furiously")
nltk.pos_tag(text19)


# %%


