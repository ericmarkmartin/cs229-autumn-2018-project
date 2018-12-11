import click
from vectorize import train_dev_test_split
from sklearn.model_selection import train_test_split
import numpy as np


@click.command()
@click.argument('infile', type=click.Path())
@click.argument('outdir', type=click.Path())
def run(infile, outdir):
    sentences = []
    with open(infile) as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            sentence, punct = eval(line)
            sentence = ' '.join(sentence).replace(' ,', ',')
            sentences.append((i, sentence, punct))

    dev_size, test_size = 0.05, 0.05

    random_state = 229
    t1_size = dev_size + test_size
    t2_size = test_size / (test_size + dev_size)
    _, rem = train_test_split(sentences, test_size=t1_size, random_state=random_state)
    _, test = train_test_split(rem, test_size=t2_size, random_state=random_state)

    r = np.arange(len(test))
    np.random.shuffle(r)
    idx_splits = np.array_split(r, 50)
    for i, idx_split in enumerate(idx_splits):
        with open(outdir + str(i) + '.txt', 'w') as file:
            for idx in idx_split:
                file.write(str(test[idx]) + '\n')




if __name__ == '__main__':
    run()
