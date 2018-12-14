import numpy as np
import vectorize
from util import get_vectors, run_model, RANDOM_STATE


class ProportionalGuesser():
    def fit(self, X, y):
        self.priors = y

    def predict(self, X):
        np.random.seed(RANDOM_STATE)
        return np.random.choice(self.priors, size=len(X))


train, _, test = get_vectors(vectorize.tokens_to_binary)

pg = ProportionalGuesser()

run_model(pg, train, test)
