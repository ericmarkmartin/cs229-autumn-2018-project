import click


ANSWERS = ['.', '?', '!']


def prettify(sentence):
    return ' '.join(sentence).replace(', ', ',')


def get_sentences():
    lines = []
    sentences = []
    with open('../data/interim/merged.txt') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        sentence, punctuation = eval(line)
        sentences.append(i, sentence, punctuation, None)

    return sentences


def mark_answer(sentences, i, answer):
    sentences[i][-1] = answer


def prompt_for_answer(sentence):
    return easy_input(sentence, answer=ANSWERS)


def easy_input(question, answer=None, default=None):
    """Ask a question, return an answer.

    <question> is a string that is presented to the user.
    <answer> is a list of strings presented as a choice. User may type only first letters
    <default> is the presumed answer if the user just hits <Enter>.

    """

    if answer is None :
        answer = ['yes', 'no']
    else :
        answer = [i.lower() for i in answer]

    # if <default> is None or <default> is not an expected answers
    # <default> will be the first of the expected answers
    if default is None or default not in answer :
        default = answer[0]

    prompt = '/'.join([
        "\x1b[1;1m{0}\x1b[1;m".format(i.capitalize()) if i == default else i
        for i in answer
    ])

    while True :
        choice = input("{0} [{1}]: ".format(question, prompt)).lower()

        if default is not None and choice == '':
            return default
        if choice in answer :
            return choice

        valid_answer = { i[:len(choice)] : i for i in answer }

        if len(valid_answer) < len(answer) :
            print(" -- Ambiguous, please use a more detailed answer.")
        elif choice in valid_answer :
            return valid_answer[choice]
        else:
            print(" -- Please answer only with {0} or {1}.".format(", ".join(answer[:-1]), answer[-1]))


if __name__ == '__main__' :

