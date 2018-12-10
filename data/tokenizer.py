import click

DICTIONARY = "data/external/20k.txt"
NUMBERS = set("0123456789")

PERIOD = 0
QMARK = 1
EXPOINT = 2

PUNCT = {'.': PERIOD, '?': QMARK, '!': EXPOINT}

def read_dict(dictionary):
    word_to_index = {}
    index_to_word = {}

    index = 0
    with open(dictionary, "r") as d:
        for line in d:
            word_to_index[line[0:-1]] = index
            index_to_word[index] = line[0:-1]
            index += 1
    return word_to_index, index_to_word

def tokenize(word, word_to_index, NUMBER, COMMA, SEMICOLON, UNKNOWN, PROPER):
    if word.lower() in word_to_index:
        return word_to_index[word.lower()]
    if any((c in NUMBERS) for c in word):
        return NUMBER
    if word == ",":
        return COMMA
    if word == ";":
        return SEMICOLON
    if word[0].isupper():
        return PROPER
    return UNKNOWN

def tokenize_file(filename, dictionary):
    word_to_index, index_to_word = read_dict(dictionary)
    standard_count = len(word_to_index)
    NUMBER = standard_count
    COMMA = standard_count + 1
    SEMICOLON = standard_count + 2
    UNKNOWN = standard_count + 3
    PROPER = standard_count + 4

    file = open(filename, "r")
    lines = file.readlines()
    tokenized_sentences = []

    for line in lines:
        sentence, punctuation = eval(line)
        new_sentence = []
        new_punctuation = PUNCT[punctuation]
        first = True
        for word in sentence:
            token = tokenize(
                            word,
                            word_to_index,
                            NUMBER,
                            COMMA,
                            SEMICOLON,
                            UNKNOWN,
                            PROPER
                        )

            if first and token == PROPER:
                token = UNKNOWN
            new_sentence.append(token)
            first = False
        tokenized_sentences.append((new_sentence, new_punctuation))

    file.close()
    return tokenized_sentences


@click.command()
@click.argument("filename", type=click.Path())
@click.argument("dictionary", type=click.Path())
@click.argument("output", type=click.Path())
def process_file(filename, dictionary, output):
    tokenized_sentences = tokenize_file(filename, dictionary)
    with open(output, 'w') as out_file:
        for sentence in tokenized_sentences:
            out_file.write(str(sentence) + '\n')


if __name__ == '__main__':
    process_file()
