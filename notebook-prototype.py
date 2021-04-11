# %% [markdown]
# This file will be converted to an actual notebook later
# This file may be used to define high-level functions that may warrant discussion
# %%
from lab import __version__
from math import exp

print('Content filtering lab, version', __version__)

# ** 
# %% [markdown]
# Code block that contains the importing the library. 
# It will already there, they just have to run it.
# %%
from lab import data_tools, display

# %% [markdown]
# Code block that parses data into the program
# Put in the labels your group thinks is appropriate for the titles

# %%
training_data = data_tools.parse_data('data.txt')

# %% [markdown]
# Code block that displays data


# %%
# Between 10 and 20 of edge case examples to prompt the student
training_data.extend([
    ('y/n', 'A passable title'),
    ('y/n', 'With the upcoming Thursday night NFL game, remember that this presents a simplified view of an entire culture, caricatures facial features based on race, depicts an outdated/inaccurate style of headdress, paints them as warmongering aggressors and overly glamorizes the violent side of their history.')
])

display.display_training_data(training_data)

# %% [markdown]
# Code where they implement prior probability


# %%
def prior_probability(data):
    # Your code here!
    pass


# %% [markdown]
# Code where they implement feature probability


# %%
def feature_probability(data):
    # Your code here!
    pass

# %% [markdown]
# Code where they test the probability of the post being valid and the probability of the post being invalid


# %% [markdown]
# Code that returns the maximum of the probability of being valid and invalid


# %% [markdown]
# Code that returns the array of tuples(label, title) based on the probabilities that we found before
# Input: testing dataset


# %%
def filter_posts():
    # your code here!
    pass


# Code block that returns the percentage of labels they predicted correctly
# This should *just work*, e.g. it should already be implemented


