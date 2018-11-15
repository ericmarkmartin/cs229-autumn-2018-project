.PHONY: all clean

IRIS_URL = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
STANFORD_TOMATOES_URL = "http://nlp.stanford.edu/~socherr/stanfordSentimentTreebank.zip"
TWITTER_URL = "http://cs.stanford.edu/people/alecmgo/trainingandtestdata.zip"
MOVIES_URL = "http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz"
20K_URL = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/20k.txt"

all: data/raw/iris.csv data/raw/tomatoes.zip data/raw/twitter.zip data/raw/movies.tar.gz data/raw/20k.txt

clean:
	rm data/raw/*.csv
	rm data/raw/*.zip
	rm data/raw/*.tar.gz

data/raw/iris.csv: 
	python data/download.py $(IRIS_URL) $@

data/raw/tomatoes.zip: 
	python data/download.py $(STANFORD_TOMATOES_URL) $@
	mkdir -p data/raw/tomatoes
	unzip tomatoes.zip -d tomatoes

data/raw/twitter.zip:
	python data/download.py $(TWITTER_URL) $@
	mkdir -p data/raw/twitter
	unzip twitter.zip -d twitter

data/raw/movies.tar.gz:
	python data/download.py $(MOVIES_URL) $@
	tar -xzf movies.tar.gz

data/raw/20k.txt:
	python data/download.py $(20K_URL) $@