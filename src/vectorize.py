# This file contains helper functions for vectorizing datalists into various formats
# including binary vectors, bag of words, one-hot lists, word2vec, etc
# This file is intended to work with <text>_tok.txt files

# This file also contains functions for getting a train-dev-test split
# Remember, always split before you vectorize!
from sklearn.model_selection import train_test_split
import numpy as np
import random

TOKEN_COUNT = 20000 + 5

PERIOD = 0
QMARK = 1
EXPOINT = 2

NUM_CLASSES = 3

STOP_WORDS = ["a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "he", "in", "is", "it", "its", "of", "on", "that", "the", "to", "was", "were", "will", "with"]

def tokens_to_bag_of_words(filename, one_hot_y=True):
    """
    m is number of examples
    n is number of token
    p is number of punctuation marks
    one_hot_y=False: returns X, y as (m, n) and (m, 1) numpy arrays of ints
    one_hot_y=True: returns X, y as (m, n) and (m, 3) numpy array of ints
    """
    file = open(filename, "r")
    lines = file.readlines()

    X = np.empty((len(lines), TOKEN_COUNT), dtype = int)
    if one_hot_y:
        y = np.empty((len(lines), NUM_CLASSES), dtype=int)   
    else:
        y = np.empty((len(lines), 1), dtype=int)

    for i, line in enumerate(lines):
        tokens, punct = eval(line)
        X[1] = np.zeros((TOKEN_COUNT))
        for token in tokens:
            X[i][int(token)] += 1

        if one_hot_y:
            y[i] = np.zeros((NUM_CLASSES))
            y[i][punct] = 1
        else:
            y[i] = punct

    file.close()
    return X, y

def tokens_to_binary(filename, one_hot_y=True):
    """
    m is number of examples
    n is number of token
    p is number of punctuation marks
    one_hot_y=False: returns X, y as (m, n) and (m, 1) numpy arrays of ints
    one_hot_y=True: returns X, y as (m, n) and (m, 3) numpy array of ints
    """
    X, y = tokens_to_bag_of_words(filename, one_hot_y=one_hot_y)
    for i in range(X.shape[0]):
        X[i] = np.where(X[i] > 0, 1, 0)
    return X, y

def tokens_to_one_hot(filename, max_length, one_hot_y=True):
    # Memory error
    raise NotImplementedError
    """
    m is number of examples
    n is number of token
    p is number of punctuation marks
    q is maximum length of an example
    one_hot_y=False: returns X, y as (m, q, n) and (m, 1) numpy arrays of ints
    one_hot_y=True: returns X, y as (m, q, n) and (m, 3) numpy array of ints
    """
    file = open(filename, "r")
    lines = file.readlines()

    X = np.zeros((len(lines), max_length, TOKEN_COUNT), dtype=int)
    if one_hot_y:
        y = np.empty((len(lines), NUM_CLASSES), dtype=int)   
    else:
        y = np.empty((len(lines), 1), dtype=int)

    max_out = 0
    max_len = 0
    for i, line in enumerate(lines):
        tokens, punct = eval(line)
        if len(tokens) > max_len:
            max_len = len(tokens)
        for j, token in enumerate(tokens):
            X[i][j][int(token)] = 1
            if j == max_length - 1:
                max_out += 1
                break

        if one_hot_y:
            y[i] = np.zeros((NUM_CLASSES))
            y[i][punct] = 1
        else:
            y[i] = punct

    print(max_out)
    print(max_len)
    file.close()
    return X, y

def train_dev_test_split(X, y, dev_size, test_size, random_state=229):
    """
    1 - dev_size - test_size of the data will be training data
    dev_size of the data will be dev data
    test_size of the data will be test data

    Returns 3 tuples each containing two numpy arrays (X and y) 
    X and y will vary in shape depending on vectorization but should both have matching first index (ex count) sizes
    """
    if random_state is None:
        random_state = random.randint(low = -10000, high = 10000)
    t1_size = dev_size + test_size
    t2_size = test_size / (test_size + dev_size)
    X_train, X_rem, y_train, y_rem = train_test_split(X, y, test_size = t1_size, random_state=random_state)
    X_dev, X_test, y_dev, y_test = train_test_split(X_rem, y_rem, test_size = t2_size, random_state=random_state)

    return (X_train, y_train), (X_dev, y_dev), (X_test, y_test)
