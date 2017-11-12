import numpy as np
import matplotlib.pyplot as plt
from sklearn import cross_validation
from sklearn.svm import SVC
from sklearn.metrics import classification_report
import sklearn.metrics as sm 
from plot_fun.func import plot
import sys

plot1 = plot()

input_file = sys.argv[1]
x, y = plot1.load_data(input_file)

class_0 = np.array([x[i] for i in range(len(x)) if y[i] == 0])
class_1 = np.array([x[i] for i in range(len(x)) if y[i] == 1])
fig = plt.figure()
sub1 = fig.add_subplot(1,1,1)
sub1.scatter(class_0[:,0], class_0[:,1], facecolors='black', edgecolors='black', marker='s')
sub1.scatter(class_1[:,0], class_1[:,1], facecolors='None', edgecolors='black', marker='s')
sub1.set_title('input data')
plt.show()

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.25, random_state=5)
params_1 = {'kernel':'linear'}
params_2 = {'kernel':'poly', 'degree':3}
params_3 = {'kernel':'rbf'}
classifier = SVC(**params_3)
classifier.fit(x_train, y_train)
plot1.plot_classifier(classifier, x_train, y_train, 'Train dataset')
y_test_pred = classifier.predict(x_test)
plot1.plot_classifier(classifier, x_test, y_test, 'Test dataset')
target_names = ['Class' + str(int(i)) for i in set(y)]
print "\n" + "#"*30
print "\nClassifier performance on training dataset\n"
print(classification_report(y_train, classifier.predict(x_train), target_names=target_names))
print "\n" + "#"*30
mse = sm.mean_squared_error(y_test, y_test_pred)
evs = sm.explained_variance_score(y_test, y_test_pred)
print("\nmean_squared_error:{0:.2f}, explained_variance_score:{1:2f}".format(round(mse, 2), round(evs, 2)))

print classification_report(y_test, y_test_pred, target_names=target_names)
