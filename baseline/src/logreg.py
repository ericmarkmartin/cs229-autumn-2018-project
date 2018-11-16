# TODO: True train-dev-test split

import numpy as np
from sklearn import linear_model
import preprocessing as p

X, y = p.get_binary()
logreg = linear_model.LogisticRegression()
logreg.fit(X[::2], np.ravel(y[::2]))

predictions = logreg.predict(X[1::2])
truth = y[1::2]
predictions = predictions.reshape((-1, 1))

print(predictions.shape)
print(truth.shape)

total = len(truth)
correct = 0
for i in range(len(truth)):
	if predictions[i] == truth[i]:
		correct += 1
print(str(correct) + " correct out of " + str(total) + ": " + str(correct/total))