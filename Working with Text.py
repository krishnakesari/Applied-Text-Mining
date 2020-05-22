# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
# Working with Text


# %%
text1 = "Ethics are built right into the ideals and objectives of the United Nations "
len(text1)


# %%
text2 = text1.split(' ')
text2
len(text2)


# %%
# Finding specific words
[w for w in text2 if len(w) > 3] # Finding words with size more than 3 letters
[w for w in text2 if w.istitle()] # Capitalized words in text 2
[w for w in text2 if w.endswith('s')] # Words in text 2 that end in 's'


# %%
# Finding unique words
text3 = 'To be or not to be'
text4 = text3.split(' ')
len(text4)


# %%
len(set(text4)) # Counting unique words


# %%
len(set([w.lower() for w in text4])) # Converts strings to lower case


# %%
set([w.lower() for w in text4]) # Seeing unique lower case words


# %%
# Processing free text
text5 = '"Ethics are built right into the ideals and objectives of the United Nations" #UNSG @ NY Society for Ethical Culture bit.ly/2guVelr'
text6 = text5.split(' ')

text6


# %%
[w for w in text6 if w.startswith('#')] # finding words that start with "#"
[w for w in text6 if w.startswith('@')] # finding words that start with "@"


# %%
text7 = '@UN @UN_Women "Ethics are built right into the ideals and objectives of the United Nations" #UNSG @ NY Society for Ethical Culture bit.ly/2guVelr'
text8 = text7.split(' ')


# %%
# Peforming regular expressions
import re

[w for w in text8 if re.search('@[A-Za-z0-9_]+', w)]

# starts with '@' followed by atlease one Capital letter('A-Z'), lower case ('a-z'), number ('0-9') or underscore(_)


# %%



# %%
# Finding Specific words
[w for w in text2 if len(w) > 3] # Words that are greater than 3 letters long in text2
[w for w in text2 if w.istitle()] # Finding Capitalized words
[w for w in text2 if w.endswith('s')] # Words that end with 's'

