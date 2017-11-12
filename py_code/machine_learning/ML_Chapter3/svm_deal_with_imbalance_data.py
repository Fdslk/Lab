from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn import cross_validation
from plot_fun.func import plot
import matplotlib.pyplot as plt
import numpy as np
import sys
input_file = sys.argv[1]
plot1 = plot()
x, y = plot1.load_data(input_file)
x_train, x_test, y_train,y_test = cross_validation.train_test_split(x, y, test_size=0.25, random_state=7)
params_1 = {'kernel':'linear'}
params_2 = {'kernel':'linear', 'class_weight':'balanced'}
params_3 = {'kernel':'poly', 'degree':3}
classifier = SVC(**params_2)
classifier.fit(x_train, y_train)
class_0 = np.array([x[i] for i in range(len(x)) if y[i] == 0])
class_1 = np.array([x[i] for i in range(len(x)) if y[i] == 1])
plt.figure()
plt.scatter(class_0[:,0], class_0[:,1], facecolors='black', edgecolors='black', marker='s')
plt.scatter(class_1[:,0], class_1[:,1], facecolors='None', edgecolors='black', marker='s')
plt.title('data set')
plt.show()
plot1.plot_classifier(classifier, x_train, y_train, 'train dataset')
target_names = ['Class_' + str(int(i)) for i in set(y)]
print "\n" + "*"*15 + "test data" + "*"*15
print classification_report(y_test, classifier.predict(x_test), target_names=target_names)
print "\n" + "*"*15 + "train data" + "*"*15
print classification_report(y_train, classifier.predict(x_train), target_names=target_names)