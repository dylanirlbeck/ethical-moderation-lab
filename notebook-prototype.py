# This file will be converted to an actual notebook later
# This file may be used to define high-level functions that may warrant discussion
# %%
from lab import __version__
from math import exp

print('Content filtering lab, version', __version__)

# %%
def filter_content(posts):
    """
    Returns the list of submissions that are okay to post.
    """
    return []

# %%
def filter_content_human_review(posts):
    """
    Returns a tuple:
        First element: list of submissions that are okay to post.
        Second element: list of submissions requiring human review.
    """
    requires_review = len(posts)
    return ([], requires_review)
# %%
def calculate_human_review_efficiency(number_of_posts):
    """
    Returns the probability (between 0 and 1) that any given post is correctly reviewed, given the number of posts. (Simulates fatigue)
    """
    # Simple calculation about effectiveness of posts
    return exp(-1 * number_of_posts)
# %%
def success_of_filter(posts, solution):
    """
    Returns the percentage (between 0 and 1) of posts correctly classified, given the original posts and the posts that were supposed to get through 
    filter_content_human_review will be used in this function.
    """
