import vectorize
import numpy as np
import scipy as sp
from sklearn import linear_model, metrics


X, y = vectorize.tokens_to_bag_of_words("../data/processed/merged_tok.txt", one_hot_y=False)
(X_train, y_train), (X_dev, y_dev), (X_test, y_test) = vectorize.train_dev_test_split(X, y, dev_size=0.05, test_size=0.05)

print("Making logreg")
logreg = linear_model.LogisticRegression(multi_class='multinomial', solver='sag')
print("Fitting logreg")
logreg.fit(X_train, np.ravel(y_train))
print("Making predictions")
predictions = logreg.predict(X_dev)

print(metrics.classification_report(y_dev, predictions, target_names=["PERIOD", "QMARK", "EXPOINT"]))
print("Micro: " + str(metrics.precision_recall_fscore_support(y_dev, predictions, average='micro')))
print("Macro: " + str(metrics.precision_recall_fscore_support(y_dev, predictions, average='macro')))
print("Weighted: " + str(metrics.precision_recall_fscore_support(y_dev, predictions, average='weighted')))

conf_matrix = metrics.confusion_matrix(y_dev, predictions) 
print(conf_matrix)