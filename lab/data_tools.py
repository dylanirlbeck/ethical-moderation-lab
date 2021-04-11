import csv
import string
from collections import Counter

def parse_data(politics_fn, sports_fn, limit=300):
    """
    Returns an array of tuples:
        ('y/n', 'Title')
    """
    data = []
    with open(politics_fn) as politics_fp, open(sports_fn) as sports_fp:
        politics_csv = csv.reader(politics_fp, delimiter=',')  
        sports_csv = csv.reader(sports_fp, delimiter=',')
        for i, row in enumerate(politics_csv):
            if i == 0: 
                continue
            data.append(('n', row[1]))
        for i, row in enumerate(sports_csv):
            if i == 0:
                continue
            data.append(('y', row[1]))
    return data

def get_word_validities(data):
    """
    Returns two counter objects as a tuple: (valid_counter, invalid_counter)
        key: word
        value: how often it has appeared in valid/invalid entries
    """
    valid_counter = Counter()
    invalid_counter = Counter()
    for validity, title in data:
        words = title.lower.translate(None, string.punctuation).split() # lowercase, remove punctuation, and split
        for w in words:
            if validity == 'y':
                valid_counter[w] += 1
            elif validity == 'n':
                invalid_counter[w] += 1
    return valid_counter, invalid_counter

print("lab.data_tools imported!")