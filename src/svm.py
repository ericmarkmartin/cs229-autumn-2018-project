from sklearn.linear_model import SGDClassifier
import vectorize
from util import get_vectors, run_model, RANDOM_STATE

train, _, test = get_vectors(vectorize.tokens_to_bag)

svm = SGDClassifier(random_state=RANDOM_STATE)

run_model(svm, train, test)
