from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation
import sklearn.metrics as sm
import matplotlib.pyplot as plt
import numpy as np
import sys
input_file = sys.argv[1]
x = []
y = []
count_leastthan50k = 0
count_morethan50k = 0
num_images_threshold = 10000
fig = plt.figure()
with open(input_file, 'r') as files:
	for line in files.readlines():
		if '?' in line:
			continue
		data = line[:-1].split(',')
		if data[-1] == ' <=50K' and count_leastthan50k < num_images_threshold:
			x.append(data)
			count_leastthan50k += 1
		elif data[-1] == ' >50K' and count_morethan50k < num_images_threshold:
			x.append(data)
			count_morethan50k += 1
		if count_leastthan50k >= num_images_threshold and count_morethan50k >= num_images_threshold:
			break

x = np.array(x)

label_encoder = []
x_encoded = np.empty(x.shape)
count = 0
for i, item in enumerate(x[0]):
	if item.isdigit():
		x_encoded[:, i] = x[:, i]
	else:
		label_encoder.append(preprocessing.LabelEncoder())
		x_encoded[:, i] = label_encoder[count].fit_transform(x[:, i])
		count += 1
		
x = x_encoded[:, :-1].astype(int)
y = x_encoded[:,-1].astype(int)

classifier = GaussianNB()
classifier.fit(x, y)
y_pred = classifier.predict(x)
mae = sm.mean_absolute_error(y, y_pred)
evs = sm.explained_variance_score(y, y_pred)
print("\nmean_absolute_error:{0:.2f}; explained_variance_score:{1:.2f}".format(round(mae, 2), round(evs, 2)))
x_train, x_test, y_train, y_test = cross_validation.train_test_split(x, y, test_size=0.25, random_state=5)
classifier_gaussiannb = GaussianNB()
classifier_gaussiannb.fit(x_train, y_train)
y_test_pred = classifier_gaussiannb.predict(x_test)
mae = sm.mean_absolute_error(y_test, y_test_pred)
evs = sm.explained_variance_score(y_test, y_test_pred)
f1 = cross_validation.cross_val_score(classifier_gaussiannb, x, y, scoring='f1_weighted', cv=5)
print("\nmean_absolute_error:{0:.2f}; explained_variance_score:{1:.2f}".format(round(mae, 2), round(evs, 2)))
print("\nF1 Socre:{0:.2f}%".format(round(100*f1.mean(),2)))

input_data = ['39', 'State-gov', '77516', 'Bachelors', '13', 'Never-married', 'Adm-clerical', 'Not-in-family', 'White, Male', '2174', '0', '40', 'United-States']
input_data_encoded = np.empty(len(input_data))
count = 0
for i, item in enumerate(input_data):
	if item.isdigit():
		input_data_encoded[i] = input_data[i]
	else:
		input_data_encoded[i] = label_encoder[count].transform(np.array([input_data[i]]))
		count += 1

input_data_encoded = np.array([input_data_encoded]).astype(int)
output_class = classifier_gaussiannb.predict(input_data_encoded)
print label_encoder[-1].inverse_transform(output_class)[0]