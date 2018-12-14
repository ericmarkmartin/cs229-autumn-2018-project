from sklearn.ensemble import RandomForestClassifier
import vectorize
from util import get_vectors, run_model, RANDOM_STATE


train, _, test = get_vectors(vectorize.tokens_to_binary)

rf = RandomForestClassifier(n_estimators=100, random_state=RANDOM_STATE)

run_model(rf, train, test)
