import copy

DICTIONARY = "data/raw/20k.txt"
MOVIES_POS = "data/raw/rt-polaritydata/rt-polarity.pos"
MOVIES_NEG = "data/raw/rt-polaritydata/rt-polarity.neg"

# Generates a word_to_index and index_to_word dictionary based
# on a text file of words. Does not generate UNK token or filter
# still words. 
def read_dict():
	word_to_index = {}
	index_to_word = {}

	index = 0
	with open(DICTIONARY, "r") as d:
		for line in d:
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
			data.append((line[0:-1], 1))
	return data

# Converts a raw list of tuples from from setences to labels to a 
# list of binary vectors to label
def raw_list_to_binary(raw_list, word_to_index):
	data = []

	i = 0
	for sentence, label in raw_list:
		print(i)
		i += 1
		sentence_vector = [0 for i in range(len(word_to_index))]
		for word in sentence.split():
			if word in word_to_index:
				sentence_vector[word_to_index[word]] = 1
		data.append((sentence_vector, label))
	return data

word_to_index, index_to_word = read_dict()
raw_list = load_movies_as_raw_list()
raw_list_to_binary(raw_list, word_to_index)
