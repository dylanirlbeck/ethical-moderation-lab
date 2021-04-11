# %% [markdown]
"""
This file will be converted to an actual notebook later
This file may be used to define high-level functions that may warrant discussion
"""

# %%
from lab import __version__
from math import exp, log

print('Content filtering lab, version', __version__)

# ** 
# %% [markdown]
"""
Code block that contains the importing of the library. 
It will already be there, they just have to run it.
"""
# %%
from lab import data_tools, display

# %% [markdown]
"""
Code block that parses data into the program
Put in the labels your group thinks is appropriate for the titles
"""

# %%
training_data = data_tools.parse_data('./data/politics.csv', './data/espn.txt', limit=10)

# %% [markdown]
"""
Code block that displays data
"""
display.display_labelled_data(training_data)
# %%
# Between 10 and 20 of edge case examples to prompt the student
training_data.extend([
    ('y/n', 'A passable title'),
    ('y/n', 'With the upcoming Thursday night NFL game, remember that this presents a simplified view of an entire culture, caricatures facial features based on race, depicts an outdated/inaccurate style of headdress, paints them as warmongering aggressors and overly glamorizes the violent side of their history.')
])

display.display_labelled_data(training_data)

# %% [markdown]
"""
UNOFFICIAL: Code block with a simple class to help with getting data stats
"""

# %% 
training_data_statistics = data_tools.DataStats(training_data)
# %% [markdown]
"""
Code where they implement prior probability
"""

# %%
def prior_probabilities(label):
    k = 1
    num_invalid = len(training_data_statistics.invalid_posts)
    num_valid = len(training_data_statistics.valid_posts)
    num_total = training_data_statistics.num_posts
    if label == 'y':
        return (k + num_valid) / (2*k + num_total)
    elif label == 'n':
        return (k + num_invalid) / (2*k + num_total)
    else:
        raise KeyError('Unsupported label: {}'.format(label))
print(prior_probabilities('n'))
print(prior_probabilities('y'))

# %% [markdown]
"""
Code where they implement feature probability
"""

# %%
def word_given_label_probability(word, label):
    if label == 'y':
        return training_data_statistics.valid_counter[word] / training_data_statistics.total_invalid_words
    elif label == 'n':
        return training_data_statistics.invalid_counter[word] / training_data_statistics.total_invalid_words
    else:
        raise KeyError('Unsupported label: {}'.format(label))
# %% [markdown]
"""
Code where they test the probability of the post being valid and the probability of the post being invalid
Returns a tuple: (p_valid, p_invalid)
"""


# %% 
def submission_probabilities(submission, label):
    # We calculate log probability
    # !!! Might be obsolete
    pass

# %% [markdown]
"""
Code that returns the maximum of the probability of being valid and invalid
"""
# %%
def post_validity(submission, threshold = 0):
    # Your code here!
    word_arr = data_tools.preprocess_submission(submission)
    sum_log_word_given_valid = 0
    sum_log_word_given_invalid = 0
    for word in word_arr:
        word_given_y = word_given_label_probability(word, 'y')
        word_given_n = word_given_label_probability(word, 'n')
        if word_given_y > 0:
            sum_log_word_given_valid += log(word_given_y)
        if word_given_n > 0:
            sum_log_word_given_invalid += log(word_given_n)
    log_ratio = log(prior_probabilities('y')) - log(prior_probabilities('n')) + sum_log_word_given_valid - sum_log_word_given_invalid
    if log_ratio < -1 * threshold:
        return 'n'
    elif log_ratio > -1 * threshold:
        return 'y'
    else:
        return '?'


# %% [markdown]
"""
(UNOFFICIAL) Code that compiles all of the students' functions into a single model object generator thing
It should also process the actual dataset
"""

# %% [markdown] 
"""
Code that returns the array of tuples(label, title) based on the probabilities that we found before
Input: testing dataset

$$ L_aT^eX $$
"""

# %%
from lab.data_tools import parse_unlabeled_csv
testing_data = parse_unlabeled_csv('./data/sports.csv', limit=100)
def filter_posts(posts):
    # your code here!
    result = []
    for submission in testing_data:
        validity = post_validity(submission)
        result.append((validity, submission))

    return result
filtering_result = filter_posts(testing_data)
display.display_labelled_data(filtering_result)

# %% [markdown]
"""
Code block that returns the percentage of labels they predicted correctly
This should *just work*, e.g. it should already be implemented
"""

# %% 
