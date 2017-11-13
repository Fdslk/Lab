import numpy as np
from sklearn import preprocessing
from sklearn import cross_validation
from sklearn.svm import SVC
import sys
input_file = sys.argv[1]
X = []
with open(input_file, 'r') as file:
	for line in file.readlines():
		data = line[:-1].split(',')
		X.append([data[0]] + data[2:])
X = np.array(X)

label_encoder = []
X_encoded = np.empty(X.shape)
for i, item in enumerate(X[0]):
	if item.isdigit():
		X_encoded[:, i] = X[:, i]
	else:
		label_encoder.append(preprocessing.LabelEncoder())
		X_encoded[:, i] = label_encoder[-1].fit_transform(X[:, i])
		
X = X_encoded[:, :-1].astype(int)
Y = X_encoded[:, -1].astype(int)

params = {'kernel':'rbf', 'probability':True, 'class_weight':'balanced'}
classifier = SVC(**params)
classifier.fit(X, Y)
accuracy = cross_validation.cross_val_score(classifier, X, Y, scoring='accuracy', cv=3)
print "Accuracy of the classifer:" + str(round(100*accuracy.mean(), 2)) + "%"
input_data = ['Monday', '12:00:00', '19', '11']
input_data_encoded = [-1]*len(input_data)
count = 0
for i, item in enumerate(input_data):
	if item.isdigit():
		input_data_encoded[i] = int(input_data[i])
	else:
		input_data_encoded[i] = int(label_encoder[count].transform([input_data[i]]))
		count = count + 1
input_data_encoded = np.array([input_data_encoded])
output_class = classifier.predict(input_data_encoded)
print "\noutput_class:" + label_encoder[-1].inverse_transform(output_class)[0]