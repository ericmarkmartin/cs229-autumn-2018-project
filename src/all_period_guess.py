import numpy as np
import vectorize
from util import get_vectors, run_model


class AllPeriodGuesser():
    def fit(self, X, y):
        pass

    def predict(self, X):
        return np.zeros(X.shape[0])


train, _, test = get_vectors(vectorize.tokens_to_binary)

apg = AllPeriodGuesser()

run_model(apg, train, test)
