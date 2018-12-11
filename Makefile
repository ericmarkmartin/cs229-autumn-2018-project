.PHONY: all clean

RAW_DIR = data/raw
INTERIM_DIR = data/interim
PROCESSED_DIR = data/processed
EXTERNAL_DIR = data/external

XMAS_CAROL_URL = "https://www.gutenberg.org/files/46/46-0.txt"
PRIDE_PREJ_URL = "https://www.gutenberg.org/files/1342/1342-0.txt"
TALE_TWO_CITIES_URL = "https://www.gutenberg.org/files/98/98-0.txt"
FRANKENSTEIN_URL = "https://www.gutenberg.org/files/84/84-0.txt"
MOBY_DICK_URL = "https://www.gutenberg.org/files/2701/2701-0.txt"
MODEST_PROPOSAL_URL = "https://www.gutenberg.org/ebooks/1080.txt.utf-8"
HEART_DARKNESS_URL = "https://www.gutenberg.org/files/219/219-0.txt"
DRACULA_URL = "https://www.gutenberg.org/ebooks/345.txt.utf-8"
SHERLOCK_URL = "https://www.gutenberg.org/ebooks/1661.txt.utf-8"
ALICE_WNDERLND_URL = "https://www.gutenberg.org/files/11/11-0.txt"

DICTIONARY_URL = "https://raw.githubusercontent.com/first20hours/google-10000-english/master/20k.txt"

BOOK_TXT = data/raw/xmas_carol.txt \
	data/raw/pride_prej.txt \
	data/raw/tale_two_cities.txt \
	data/raw/frankenstein.txt \
	data/raw/moby_dick.txt \
	data/raw/modest_proposal.txt \
	data/raw/heart_darkness.txt \
	data/raw/dracula.txt \
	data/raw/sherlock.txt \
	data/raw/alice_wnderlnd.txt

PARSED_TXT = data/interim/xmas_carol.parsed.txt \
	data/interim/pride_prej.parsed.txt \
	data/interim/tale_two_cities.parsed.txt \
	data/interim/frankenstein.parsed.txt \
	data/interim/moby_dick.parsed.txt \
	data/interim/modest_proposal.parsed.txt \
	data/interim/heart_darkness.parsed.txt \
	data/interim/dracula.parsed.txt \
	data/interim/sherlock.parsed.txt \
	data/interim/alice_wnderlnd.parsed.txt


all: data/processed/merged_tok.txt

clean:
	rm -f data/raw/*.txt
	rm -f data/interim/*.txt
	rm -f data/external/*.txt
	rm -f data/processed/*.txt

data/raw/xmas_carol.txt:
	python data/download.py $(XMAS_CAROL_URL) $@

data/raw/pride_prej.txt:
	python data/download.py $(PRIDE_PREJ_URL) $@

data/raw/tale_two_cities.txt:
	python data/download.py $(TALE_TWO_CITIES_URL) $@

data/raw/frankenstein.txt:
	python data/download.py $(FRANKENSTEIN_URL) $@
	
data/raw/moby_dick.txt:
	python data/download.py $(MOBY_DICK_URL) $@

data/raw/modest_proposal.txt:
	python data/download.py $(MODEST_PROPOSAL_URL) $@

data/raw/heart_darkness.txt:
	python data/download.py $(HEART_DARKNESS_URL) $@

data/raw/dracula.txt:
	python data/download.py $(DRACULA_URL) $@

data/raw/sherlock.txt:
	python data/download.py $(SHERLOCK_URL) $@

data/raw/alice_wnderlnd.txt:
	python data/download.py $(ALICE_WNDERLND_URL) $@

data/interim/%.parsed.txt: data/raw/%.txt $(BOOK_TXT)
	python data/process.py $< $@

data/interim/merged.txt: $(PARSED_TXT)
<<<<<<< HEAD
	cat $^ > $@
=======
	sed -e "s/latin1/utf8/" $^ > $@
>>>>>>> 50235e0... Update makefile with double quotes for johnny boi

data/external/20k.txt:
	python data/download.py $(DICTIONARY_URL) $@

data/processed/merged_tok.txt: data/interim/merged.txt data/external/20k.txt
	python data/tokenizer.py $^ $@
