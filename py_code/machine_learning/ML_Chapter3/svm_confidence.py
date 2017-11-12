from sklearn.svm import SVC
from sklearn import cross_validation
from plot.func import plot
import numpy as np
import sys
plot1 = plot()
input_file = sys.argv[1]
input_data = np.array([[2, 15], [8, 9], [4.8, 5.2], [4, 4], [2.5, 7], [7.6, 2], [5.4, 5.9]])
x, y = plot1.load_data(input_file)
x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.25, random_state=7)
params_1 = {'kernel':'rbf'}
params_2 = {'kernel':'rbf', 'probability':True}
classifier = SVC(**params_1)
classifier.fit(x_train, y_train)
print "\nDistance from the boundry"
for i in input_data:
	print i , '-->', classifier.decision_function(i)[0]
classifier = SVC(**params_2)
classifier.fit(x_train, y_train)

print "\nConfidence measure"
for i i input_data:
	print i, '-->', classifier.predict_proba(i)[0]
	
plot1.plot_classifier(classifier, input_data, [0]*len(input_data), 'input_data')
