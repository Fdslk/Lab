from sklearn.naive_bayes import GaussianNB
import sys
import numpy as np
import matplotlib.pyplot as plt
from sklearn import cross_validation
def plot_classifier(classifier, x, y):
	x_min, x_max = min(x[:, 0]) - 1.0, max(x[:, 0]) + 1.0
	y_min, y_max = min(x[:, 1]) - 1.0, max(x[:, 1]) + 1.0
	step_size = 0.01
	x_values, y_values = np.meshgrid(np.arange(x_min, x_max, step_size), np.arange(y_min, y_max, step_size))
	mesh_out = classifier.predict(np.c_[x_values.ravel(), y_values.ravel()])
	mesh_out = mesh_out.reshape(x_values.shape)
	plt.figure()
	plt.pcolormesh(x_values, y_values, mesh_out, cmap=plt.cm.gray)
	plt.scatter(x[:,0], x[:,1], c=y, s=80, edgecolors='black', linewidth=1)
	plt.xlim(x_values.min(), x_values.max())
	plt.ylim(y_values.min(), y_values.max())
	plt.xticks((np.arange(int(min(x[:, 0]) - 1), int(max(x[:, 0]) + 1), 1.0)))
	plt.xticks((np.arange(int(min(x[:, 1]) - 1), int(max(x[:, 1]) + 1), 1.0)))
	plt.show()
	
input_file = sys.argv[1]
X = []
Y = []
with open(input_file, 'r') as file:
	for line in file.readlines():
		data = [float(x) for x in line.split(',')]
		X.append(data[:-1])
		Y.append(data[-1])

X = np.array(X)
Y = np.array(Y)

classifier_gaussian = GaussianNB()
classifier_gaussian.fit(X, Y)
y_pred = classifier_gaussian.predict(X)
accuracy = 100.0*(Y == y_pred).sum()/X.shape[0]
print("accuracy of the classifier{0:.2f}%.".format(accuracy))
plot_classifier(classifier_gaussian, X, Y)

x_train, x_test, y_train, y_test = cross_validation.train_test_split(X, Y, test_size=0.25, random_state=5)
classifier_gaussian_new = GaussianNB()
classifier_gaussian_new.fit(x_train, y_train)
y_test_pred = classifier_gaussian_new.predict(x_test)
accuracy = 100.0*(y_test_pred==y_test).sum()/x_test.shape[0]
print("accuracy of the classifier{0:.2f}%.".format(accuracy))
plot_classifier(classifier_gaussian_new, x_test, y_test)

num_validatinons = 5
accuracy = cross_validation.cross_val_score(classifier_gaussian, X, Y, scoring='accuracy', cv=num_validatinons)
print("Accuracy:", str(round(100*accuracy.mean(), 2)),"%")


