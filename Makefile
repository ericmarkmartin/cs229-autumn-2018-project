.PHONY: all clean

IRIS_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
SHERLOCK_URL = "http://www.gutenberg.org/cache/epub/1661/pg1661.txt"

all: data/raw/sherlock.txt

clean:
	rm -f data/raw/*.csv
	rm -f data/raw/*.txt

data/raw/sherlock.txt:
	python data/download.py $(SHERLOCK_URL) $@
	python data/process.py $@ "data/processed/sherlock.txt"
	python data/tokenizer.py "data/processed/sherlock.txt" "data/processed/sherlock_tok.txt"