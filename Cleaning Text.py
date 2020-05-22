# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
text = ' A quick brown fox jumped over the lazy dog. '
text.split(' ')


# %%
# Removing white spaces
text = text.strip()
text.split(' ')


# %%
# Find text
# count from start
text.find('o')
# count from end
text.rfind('o')


# %%
# Replace text
text.replace('o', 'O')


# %%
# Reading txt file
f = open('text.txt', 'r')
f.readline()
f.seek(0)
# f.read() to see all text
text = f.read()
len(text)


# %%
# remove new line character (\n)
# text.rstrip()


# %%
# Split lines
text = text.splitlines()
len(text)


# %%


