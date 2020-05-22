# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd


# %%
time_sentences = ["Monday: The doctor's appointment is at 2:45pm.", 
                  "Tuesday: The dentist's appointment is at 11:30 am.",
                  "Wednesday: At 7:00pm, there is a basketball game!",
                  "Thursday: Be back home by 11:15 pm at the latest.",
                  "Friday: Take the train at 08:10 am, arrive at 09:00am."]
df = pd.DataFrame(time_sentences, columns = ['text'])
df


# %%
# Find the number of characters for each string in df['text']
df['text'].str.len()


# %%
# Find the number of tokens for each string in df['text']
df['text'].str.split().str.len()


# %%
# Find which strings contian the word 'appointment'
df['text'].str.contains('appointment')


# %%
# Find how many times a digit occurs in each string
df['text'].str.count(r'\d')


# %%
# Find all occurances of digits
df['text'].str.findall(r'\d')


# %%
# Group and find the hours and minutes
df['text'].str.findall(r'(\d?\d):(\d\d)')


# %%
# Replace weekdays with '???'
df['text'].str.replace(r'\w+day\b', '???')


# %%
# Replace weekdays with 3 letter abbrevations
df['text'].str.replace(r'(\w+day\b)', lambda x: x.groups()[0][:3])


# %%
# Create new columns from first match of extracted groups
df['text'].str.extract(r'(\d?\d):(\d\d) ?([ap]m)')


# %%
# Extract the entire time, the hours, the minutes, and the period with group names
df['text'].str.extractall(r'(?P<time>(?P<hour>\d?\d):(?P<minute>\d\d) ?(?P<period>[ap]m))')


# %%


