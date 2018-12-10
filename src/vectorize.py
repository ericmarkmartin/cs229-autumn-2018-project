# This file contains helper functions for vectorizing datalists into various formats
# including binary vectors, bag of words, one-hot lists, word2vec, etc
# This file is intended to work with <text>_tok.txt files

# This file also contains functions for getting a train-dev-test split
# Remember, always split before you vectorize!

TOKEN_COUNT = 20000 + 5

PERIOD = 0
QMARK = 1
EXPOINT = 2
PUNCT = {'.':PERIOD, '?':QMARK, '!':EXPOINT}

import numpy as np
import random

STOP_WORDS = ["a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "he", "in", "is", "it", "its", "of", "on", "that", "the", "to", "was", "were", "will", "with"]

def tokenize_to_binary(filename, one_hot_y=False):
    """
    m is number of examples
    n is number of token
    p is number of punctuation marks
    ont_hot_y=False: returns X, y as (m, n) and (m, 1) numpy arrays of ints
    ont_hot_y=True: returns X, y as (m, n) and (m, 3) numpy array of ints
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
            X[i][int(token)] = 1

        punct = PUNCT[punct]
        if one_hot_y:
            y[i] = np.zeros((len(PUNCT)))
            y[i][punct] = 1
        else:
            y[i] = punct

    file.close()
    return X, y