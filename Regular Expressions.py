# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
tweet = '#Python @python #Python90_12 # Python30_15'


# %%
tweet2 = tweet.split(' ')
tweet2


# %%
import re
[w for w in tweet2 if re.search('#[A-Za-z0-9_]+', w)]


# %%
text12 = 'ouagadougou'
re.findall(r'[aeiou]', text12) # Finding all vowels in the word
re.findall(r'[^aeiou]', text12) # Finding all not vowels in the word


# %%
# Regular expressions with dates
datestr = '23-10-2002\n23/10/2002\n23/10/02'
re.findall(r'\d{2}[/-]\d{2}[/-]\d{4}', datestr)
re.findall(r'\d{2}[/-]\d{2}[/-]\d{2,4}', datestr)


# %%
datestr2 = '23 Oct 2002\n 23 October 2002\n Oct 23, 2002\n October 23, 2002'
re.findall(r'(?:\d{2} )? (?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* (?:\d{2}, )?\d{4}',datestr2)


# %%



# %%


