import numpy as np
from sklearn import preprocessing
from sklearn import cross_validation
from sklearn.svm import SVR
import sklearn.metrics as sm 
import sys
input_file = sys.argv[1]
X = []
count = 0
with open(input_file, 'r') as file:
	for line in file.readlines():
		data = line[:-1].split(',')
		X.append(data)

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
Y = X_encoded[:,-1].astype(int)

params = {'kernel':'rbf', 'C':10.0, 'epsilon':0.2}
classifier = SVR(**params)
classifier.fit(X, Y)
Y_pred = classifier.predict(X)
print "Mean absolute error = ", round(sm.mean_absolute_error(Y, Y_pred), 2)

X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X, Y, test_size=0.25, random_state=7)
classifier.fit(X_train, Y_train)
Y_test_pred = classifier.predict(X_test)
print "Mean absolute error = ", round(sm.mean_absolute_error(Y_test, Y_test_pred), 2)

input_data =  ['Thursday','20:50','Arizona','yes']
input_data_encoded = [-1]*len(input_data)
for i, item in enumerate(input_data):
	if item.isdigit():
		input_data_encoded[i] = int(input_data[i])
	else:
		input_data_encoded[i] = int(label_encoder[count].transform([input_data[i]]))
		count += 1
input_data_encoded = np.array([input_data_encoded])
out_class = classifier.predict(input_data_encoded)
print("\npredict traffic = {0:d}".format(int(out_class)))