import click


PERIOD = '.'
QMARK = '?'
EXPOINT = '!'
ALL_PUNC = [PERIOD, QMARK, EXPOINT]


def is_punctuation(char):
    return char in ALL_PUNC


honorifics = [
    'Mr.',
    'Ms.',
    'Mrs.',
    'Dr.',
    'Esq.',
    'Br.',
    'Sr.',
    'Jr.'
]


def get_sentences(words):
    """Given list of whitespace-delimited words, return list of sentences"""
    current_sentence = None
    sentences = []

    for word in words:
        first_is_upper = word[0].isupper()
        secnd_is_upper = len(word) > 1 and word[1].isupper()

        last_is_punc = is_punctuation(word[-1])
        penult_is_punc = len(word) > 1 and is_punctuation(word[-2])

        if len(word) > 2:
            word = word[0] + word[1:-1].replace("'", '') + word[-1]

        if current_sentence is None and (first_is_upper or secnd_is_upper):
            current_sentence = []
            if word[0] in ['"', "'"] and len(word) > 1:
                word = word[1:]

            if last_is_punc or penult_is_punc:
                if word in honorifics:
                    current_sentence.append(word[:-1])
                    continue

                if last_is_punc:
                    word, punc = word[:-1], word[-1]
                else:
                    word, punc = word[:-2], word[-2]

                current_sentence.append(word)
                sentences.append((current_sentence, punc))
                current_sentence = None
                continue

            if word[-1] in [',', ';']:
                current_sentence.append(word[:-1])
                current_sentence.append(word[-1])
                continue

            current_sentence.append(word)
            continue

        if current_sentence is not None and (last_is_punc or penult_is_punc):
            if word in honorifics:
                current_sentence.append(word[:-1])
                continue

            if last_is_punc:
                word, punc = word[:-1], word[-1]
            else:
                word, punc = word[:-2], word[-2]
            current_sentence.append(word)
            sentences.append((current_sentence, punc))
            current_sentence = None
            continue

        if current_sentence is not None and ('"' in word or "'" in word):
            current_sentence = None
            continue

        if current_sentence is not None:
            if word[-1] in [',', ';']:
                current_sentence.append(word[:-1])
                current_sentence.append(word[-1])
                continue
            current_sentence.append(word)

    return sentences


@click.command()
@click.argument('filename', type=click.Path())
@click.argument('output', type=click.Path())
def process_file(filename, output):
    text = open(filename).read().replace('\n', ' ')
    sentences = get_sentences(text.split())
    with open(output, 'w') as file:
        for sentence in sentences:
            file.write(str(sentence) + '\n')


if __name__ == '__main__':
    process_file()
