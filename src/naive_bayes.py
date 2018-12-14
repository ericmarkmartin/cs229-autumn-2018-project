from sklearn.naive_bayes import BernoulliNB
import vectorize
from util import get_vectors, run_model


train, _, test = get_vectors(vectorize.tokens_to_binary)

nb = BernoulliNB()

run_model(nb, train, test)
