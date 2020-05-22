# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
text1 = "You have sentences or strings and they are formed of words or tokens, and words are formed out of characters. On the other side, you have documents and larger files and we're talking about all these constructs and their properties. "
len(text1)


# %%
text2 = text1.split(' ')
len(text2)


# %%
text1 = "You have sentences or strings and they are formed of words or tokens, and words are formed out of characters. On the other side, you have documents and larger files and we're talking about all these constructs and their properties. "
len(text1)

# Splitting Sentence
text2 = text1.split(' ')
len(text2)


# %%
# Words longer than 3 letters
[w for w in text2 if len(w) > 3]


# %%
# Finding Capitalized words 
[w for w in text2 if w.istitle()]


# %%
# Finding words ends with s
[w for w in text2 if w.endswith('s')]


# %%

# Finding Unique words
len(set(text2))


# %%
# Split at 'ou'
text5 = "ouagadougou"
text6 = text5.split('ou')
text6


# %%
# Join at 'ou'
'ou'.join(text6)


# %%
# Getting characters from words
[c for c in text5]


# %%


