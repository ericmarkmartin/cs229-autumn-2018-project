from vectorize import train_dev_test_split
import numpy as np


@click.command()
@click.argument(infile, type=click.Path())
@click.argument(outdir, type=click.Path())
def run(infile, outdir):
    train_dev_test_split
    sentences = []
    with open(infile) as file:
        lines = file.readlines()
        X = np.empty((len(lines), 20005), dtype=int)
        y = np.empty((len(lines), 1), dtype=int)
        for i, line in enumerate(lines):
            token, punct = eval(line)
            sentences.append((i, token, punct))



if __name__ == '__main__':

