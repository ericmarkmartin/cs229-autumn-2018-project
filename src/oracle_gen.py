import click

PERIOD = '.'
QMARK = '?'
EXPOINT = '!'
SAVE = 's'
ANSWERS = [PERIOD, QMARK, EXPOINT, SAVE]


PUNCT = {PERIOD: 0, QMARK: 1, EXPOINT: 2}


def prettify(sentence):
    return ' '.join(sentence).replace(', ', ',')


def get_sentences(infile):
    lines = []
    sentences = []
    with open(infile) as file:
        lines = file.readlines()

    for line in lines:
        i, sentence, correct = eval(line)
        sentences.append((i, sentence, correct))

    return sentences


def mark_answer(answers, i, answer, correct):
    record = (i, answer, correct)
    answers.append(record)


def get_answer(sentence):
    return easy_input(sentence, answer=ANSWERS)


def easy_input(question, answer=None, default=None):
    """Ask a question, return an answer.

    <question> is a string that is presented to the user.
    <answer> is a list of strings presented as a choice. User may type only first letters
    <default> is the presumed answer if the user just hits <Enter>.

    """

    if answer is None :
        answer = ['yes', 'no']
    else:
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


def save(answers, outfile):
    with open(outfile, 'w') as file:
        for answer in answers:
            file.write(str(answer) + '\n')


@click.command()
@click.argument('infile', type=click.Path())
@click.argument('outfile', type=click.Path())
def run(infile, outfile):
    answers = []
    sentences = get_sentences(infile)
    for i, sentence, correct in sentences:
        answer = get_answer(sentence)
        if answer not in PUNCT:
            save(answers, outfile)
            return
        mark_answer(answers, i, PUNCT[answer], correct)

    print('Thank you. All done! Saving your answers')
    save(answers, outfile)



if __name__ == '__main__':
    run()

