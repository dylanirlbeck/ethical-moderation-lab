import csv
import string
import random
from collections import Counter

# See https://stackoverflow.com/questions/34293875/how-to-remove-punctuation-marks-from-a-string-in-python-3-x-using-translate/34294022
punctuation_translator = str.maketrans('', '', string.punctuation)


def parse_unlabeled_espn(file_fn, limit=300):
    r"""
    Takes an input filename file_fn, where the format of the file is just submission titles on each line.
    This is suitable for ESPN posts into a text file (you can just select, copy and paste the ESPN text into a file)
    There may be a few things you need to do to normalize the format:
    - remove the section headers
    - remove the four whitespaces leading each line (a simple search-and-replace will suffice)
    - remove the date indicators, which are surrounded by space. The regex for this is:
        \(.*?\)
      and just search and replace that
    """
    data = []
    with open(file_fn) as file_fp:
        for line in file_fp:
            data.append(line.strip())
    return data


def parse_unlabeled_reddit_feed(file_fn, limit=300):
    # Use in conjunction with fetch-and-label.py
    """
    The unlabelled reddit feed output is generated from fetch-and-label.py.
    Because we only use it now to fetch from r/politics, I commented out all of the 
    manual validation that you might have to do. By default, each line will be of form:
        n: Insert Headline Here
    """
    data = []
    with open(file_fn) as file_fp:
        for line in file_fp:
            data.append(line.strip().split(': ', 1)[1])
    return data


def parse_unlabeled_csv(file_fn, limit=300):
    """
    The source csv files are directly from the Kaggle dataset (politics.csv, sports.csv).
    The columns are: row_number, headline, (other irrelevant fields)
    """
    data = []
    with open(file_fn) as file_fp:
        file_csv = csv.reader(file_fp, delimiter=',')
        for i, row in enumerate(file_csv):
            if i == 0:
                continue
            data.append(row[1])
    return data


def parse_data(politics_fn, sports_fn, limit=300):
    """
    Inputs:
        politics_fn: filename of politics source file (see parse_unlabeled_csv for formatting)
        sports_fn: filename of sports source file (see parse_unlabeled_espn for formatting)
        limit: the maximum number of entries to process for both politics and sports
    Returns: An array of tuples.
            (label, 'Title of headine')
        where label is one of 'y' or 'n'
    """
    data = []
    with open(politics_fn) as politics_fp, open(sports_fn) as sports_fp:
        politics_csv = csv.reader(politics_fp, delimiter=',')
        for i, row in enumerate(politics_csv):
            if i == 0:
                continue
            elif i == limit:
                break
            data.append(('n', row[1]))
        for i, line in enumerate(sports_fp):
            if i == limit:
                break
            data.append(('y', line))

    # The shuffle is for illustrative purposes: we want the students to see a
    # diversity of posts when displaying the data.
    #
    random.shuffle(data)
    return data


def get_word_validities(data):
    """
    A helper function used by DataStats
    Inputs: An array of tuples (see returns of parse_data)
    Returns: Two counter objects as a tuple: (valid_counter, invalid_counter)
        key: word
        value: how often it has appeared in valid/invalid entries
    """
    valid_counter = Counter()
    invalid_counter = Counter()
    for validity, title in data:
        # lowercase, remove punctuation, and split
        words = preprocess_submission(title)
        for w in words:
            if validity == 'y':
                valid_counter[w] += 1
            elif validity == 'n':
                invalid_counter[w] += 1
    return valid_counter, invalid_counter


class DataStats():
    """
    A class used to ease the students' experience for getting meaningful values
    Members:
        num_posts: number of submissions in data
        valid_counter: counter storing # of occurrences of each word in valid submissions
        invalid_counter: similar to valid_counter, but for invalid submissions
        total_valid_words: total number of words in all valid submissions
        total_invalid_words: similar to total_valid_words, but for invalid submissions
        valid_posts: all valid submissions
        invalid_posts: similar to valid_posts, but for invalid submissionss
    """

    def __init__(self, data):
        """
        Inputs: Array of tuples (see output of parse_data)
        """
        self.num_posts = len(data)
        self.valid_counter, self.invalid_counter = get_word_validities(data)
        self.total_valid_words = sum(
            self.valid_counter[w] for w in self.valid_counter)
        self.total_invalid_words = sum(
            self.invalid_counter[w] for w in self.invalid_counter)
        self.valid_posts = []
        self.invalid_posts = []
        for d in data:
            if d[0] == 'y':
                self.valid_posts.append(d[1])
            elif d[0] == 'n':
                self.invalid_posts.append(d[1])


def preprocess_submission(raw):
    """
    Helper method used by parse_data to remove punctuation. We wouldn't want "Democrat," "Democrat", "Democrat?" to count as separate words
    See https://stackoverflow.com/questions/34293875/how-to-remove-punctuation-marks-from-a-string-in-python-3-x-using-translate/34294022
    """
    return raw.lower().translate(punctuation_translator).split()
