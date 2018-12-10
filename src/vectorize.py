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
PUNCT = {'.':PERIOD, '?':QMARK, '!':EXPOINT}

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
        y = np.empty((len(lines), len(PUNCT)), dtype=int)   
    else:
        y = np.empty((len(lines), 1), dtype=int)

    for i, line in enumerate(lines):
        tokens, punct = eval(line)
        X[1] = np.zeros((TOKEN_COUNT))
        for token in tokens:
            X[i][int(token)] += 1

        punct = PUNCT[punct]
        if one_hot_y:
            y[i] = np.zeros((len(PUNCT)))
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

def tokens_to_one_hot(filename, one_hot_y=True):
    """
    m is number of examples
    n is number of token
    p is number of punctuation marks
    q is maximum length of an example
    one_hot_y=False: returns X, y as (m, q, n) and (m, 1) numpy arrays of ints
    one_hot_y=True: returns X, y as (m, q, n) and (m, 3) numpy array of ints
    """
    pass


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
    X_train, X_rem, y_train, y_rem = train_test_split(X, y, test_size=test_size+dev_size, random_state=random_state)
    X_dev, X_test, y_dev, y_test = train_test_split(X_rem, y_rem, test_size=test_size/(test_size+dev_size), random_state=random_state)

    return (X_train, y_train), (X_dev, y_dev), (X_test, y_test)


X, y = tokens_to_binary("data/processed/sherlock_tok.txt", one_hot_y=True)
print(X.shape)
print(y.shape)
train, dev, test = train_dev_test_split(X, y, dev_size=0.2, test_size=0.1)
print(train[0].shape)
print(train[1].shape)
print(dev[0].shape)
print(dev[1].shape)
print(test[0].shape)
print(test[1].shape)

print(train[0][50:60])
print(train[1][50:60])