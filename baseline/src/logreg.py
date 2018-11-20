# TODO: True train-dev-test split

import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import preprocessing as p

X, y = p.get_bag_of_words(stop_words=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=229)
logreg = linear_model.LogisticRegression()
logreg.fit(X_train, np.ravel(y_train))

predictions = logreg.predict(X_test)
predictions = predictions.reshape((-1, 1))

print(predictions.shape)
print(y_test.shape)

confusion_matrix = np.zeros((2,2))
for i in range(len(y_test)):
	confusion_matrix[y_test[i][0]][predictions[i][0]] += 1


print("Confusion Matrix:\n" + str(confusion_matrix))
print("Accuracy: " + str((confusion_matrix[0][0] + confusion_matrix[1][1]) / np.sum(confusion_matrix)))


precision = confusion_matrix[1][1] / (confusion_matrix[0][1] + confusion_matrix[1][1])
print("Precision: " + str(precision))
recall = confusion_matrix[1][1] / (confusion_matrix[1][0] + confusion_matrix[1][1])
print("Recall: " + str(recall))
f1 = 2 * precision * recall / (precision + recall)
print("F1: " + str(f1))