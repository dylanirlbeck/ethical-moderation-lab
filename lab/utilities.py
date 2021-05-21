def prior_probability(label, datastats):
    """
    Inputs:
        label (str): The label to calculate the prior for.
        datastats (TODO)

    Returns:
        prob (float): The prior probability for `label`.
    """
    num_invalid = len(datastats.invalid_posts)
    num_valid = len(datastats.valid_posts)
    num_total = datastats.num_posts

    if label == 'y':
        return num_valid / num_total
    elif label == 'n':
        return num_invalid / num_total

    raise KeyError('Unsupported label: {}'.format(label))


def probability_word_given_label(word, label, datastats):
    """
    Function input: label
    Global/implicit input: datastats (DataStats object)
    Output: P(Word | Type=label)
    """
    if label == 'y':
        return datastats.valid_counter[word] / datastats.total_valid_words
    elif label == 'n':
        return datastats.invalid_counter[word] / datastats.total_invalid_words
    else:
        raise KeyError('Unsupported label: {}'.format(label))


def post_validity(submission, threshold=0):
    """
    Input: A particular submission (title of a post)
    Threshold: a threshold for tuning to mark for manual review
    """
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
    log_ratio = log(prior_probabilities('y')) - log(prior_probabilities('n')
                                                    ) + sum_log_word_given_valid - sum_log_word_given_invalid
    if log_ratio < -1 * threshold:
        return 'n'
    elif log_ratio > -1 * threshold:
        return 'y'
    else:
        # manual review
        return '?'


def validate_labels(data):
    """
    Inputs:
        data (list(tuple)): Data

    Throws error if data is invalid.
    """
    for elem in data:
        if elem[0] != 'y' or elem[0] != 'n':
            raise Exception("The data labels must be either 'y' or 'n'!")
