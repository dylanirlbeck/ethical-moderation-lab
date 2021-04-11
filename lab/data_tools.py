import csv
import string
from collections import Counter

punctuation_translator = str.maketrans('', '', string.punctuation)

def parse_unlabeled_csv(file_fn, limit=300):
    data = []
    with open(file_fn) as file_fp:
        file_csv = csv.reader(file_fp, delimiter=',')
        for i, row in enumerate(file_csv):
            if i == 0: continue
            data.append(row[1])
    return data

def parse_data(politics_fn, sports_fn, limit=300):
    """
    Returns an array of tuples:
        ('y/n', 'Title')
    """
    data = []
    with open(politics_fn) as politics_fp, open(sports_fn) as sports_fp:
        politics_csv = csv.reader(politics_fp, delimiter=',')  
        for i, row in enumerate(politics_csv):
            if i == 0: 
                continue
            data.append(('n', row[1]))
        for line in sports_fp:
            data.append(('y', line))
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
        words = preprocess_submission(title) # lowercase, remove punctuation, and split
        for w in words:
            if validity == 'y':
                valid_counter[w] += 1
            elif validity == 'n':
                invalid_counter[w] += 1
    return valid_counter, invalid_counter

class DataStats():
    def __init__(self, data):
        self.num_posts = len(data)
        self.valid_counter, self.invalid_counter = get_word_validities(data)
        self.total_valid_words = sum(self.valid_counter[w] for w in self.valid_counter)
        self.total_invalid_words = sum(self.invalid_counter[w] for w in self.invalid_counter)
        self.valid_posts = []
        self.invalid_posts = []
        for d in data:
            if d[0] == 'y':
                self.valid_posts.append(d[1])
            elif d[0] == 'n':
                self.invalid_posts.append(d[1])
    def __getitem__(self, key):
        pass

def preprocess_submission(raw):
    return raw.lower().translate(punctuation_translator).split()

print("lab.data_tools imported!")
