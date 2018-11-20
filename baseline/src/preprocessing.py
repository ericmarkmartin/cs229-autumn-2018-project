import random
import numpy as np

DICTIONARY = "data/raw/20k.txt"
MOVIES_POS = "data/raw/rt-polaritydata/rt-polarity.pos"
MOVIES_NEG = "data/raw/rt-polaritydata/rt-polarity.neg"

STOP_WORDS = ["a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "has", "he", "in", "is", "it", "its", "of", "on", "that", "the", "to", "was", "were", "will", "with"]

# Generates a word_to_index and index_to_word dictionary based
# on a text file of words. Does not generate UNK token or filter
# still words. 
def read_dict(stop_words = False):
	word_to_index = {}
	index_to_word = {}

	index = 0
	with open(DICTIONARY, "r") as d:
		for line in d:
			if stop_words and line[0:-1] in STOP_WORDS:
				continue

			word_to_index[line[0:-1]] = index
			index_to_word[index] = line[0:-1]
			index += 1
	return word_to_index, index_to_word

# Loads the movies dataset into a list of tuples from sentences
# to label (+1 for positive, 0 for negative)
def load_movies_as_raw_list():
	data = []
	with open(MOVIES_POS) as f:
		for line in f:
			data.append((line[0:-1], 1))
	with open(MOVIES_NEG) as f:
		for line in f:
			data.append((line[0:-1], 0))
	return data

# Converts a raw list of tuples from from setences to labels to a 
# list of binary vectors to label
def raw_list_to_binary(raw_list, word_to_index):
	X = np.empty((len(raw_list), len(word_to_index)), dtype=int)
	y = np.empty((len(raw_list), 1), dtype=int)

	for i, line in enumerate(raw_list):
		X[i] = np.zeros((len(word_to_index)))
		for word in line[0].split():
			if word in word_to_index:
				X[i][word_to_index[word]] = 1
		y[i] = line[1]
	return X, y

# Converts a raw list of tuples from from setences to labels to a 
# bag-of-words frequency vectorization of the input sentence
def raw_list_to_bag_of_words(raw_list, word_to_index):
	X = np.empty((len(raw_list), len(word_to_index)), dtype=int)
	y = np.empty((len(raw_list), 1), dtype=int)

	for i, line in enumerate(raw_list):
		X[i] = np.zeros((len(word_to_index)))
		for word in line[0].split():
			if word in word_to_index:
				X[i][word_to_index[word]] += 1
		y[i] = line[1]
	return X, y

def get_binary(stop_words=False):
	word_to_index, index_to_word = read_dict(stop_words)
	raw_list = load_movies_as_raw_list()
	X, y = raw_list_to_binary(raw_list, word_to_index)
	return X, y

def get_bag_of_words(stop_words=False):
	word_to_index, index_to_word = read_dict(stop_words)
	raw_list = load_movies_as_raw_list()
	X, y = raw_list_to_bag_of_words(raw_list, word_to_index)
	print(X[0])
	return X, y