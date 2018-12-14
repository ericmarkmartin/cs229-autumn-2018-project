from sklearn.linear_model import LogisticRegression
import vectorize
from util import get_vectors, run_model


train, _, test = get_vectors(vectorize.tokens_to_binary)

lr = LogisticRegression(multi_class='multinomial', solver='sag')

run_model(lr, train, test)
