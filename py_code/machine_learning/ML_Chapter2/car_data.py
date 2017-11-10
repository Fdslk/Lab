from sklearn import preprocessing
from sklearn.ensemble import RandomForestClassifier
from sklearn import cross_validation
import sys
import numpy as np
from sklearn.learning_curve import validation_curve
from sklearn.learning_curve import learning_curve
import matplotlib.pyplot as plt

input_file = sys.argv[1]
x = []
count = 0
with open(input_file, 'r') as file:
	for line in file.readlines():
		data = line[:-1].split(',')
		x.append(data)
		
x = np.array(x)

label_encoder = []
X_encoded = np.empty(x.shape)
for i, item in enumerate(x[0]):
	label_encoder.append(preprocessing.LabelEncoder())
	X_encoded[:, i] = label_encoder[-1].fit_transform(x[:, i])
	print(i)
	
X = X_encoded[:, :-1].astype(int)
Y = X_encoded[:, -1].astype(int)

params = {'n_estimators': 200, 'max_depth': 8, 'random_state':7}
classifier = RandomForestClassifier(**params)
classifier.fit(X, Y)

accuracy = cross_validation.cross_val_score(classifier, X, Y, scoring='accuracy', cv=3)
print("Accuracy of the classifier:"+str(round(100*accuracy.mean(), 2))+"%")

input_data = ['vhigh', 'vhigh', '2', '2', 'small', 'low']
input_data_encoded = np.empty(len(input_data))
for i, item in enumerate(input_data):
	input_data_encoded[i] = label_encoder[i].transform(np.array([input_data[i]]))

input_data_encoded = np.array([input_data_encoded.astype(int)])
output_class = classifier.predict(input_data_encoded)
print "Output class:", label_encoder[-1].inverse_transform(output_class)[0]

classifier = RandomForestClassifier(max_depth=4, random_state=7)
parameter_grid = np.linspace(25, 200, 8).astype(int)
train_scores, validation_scores = validation_curve(classifier, X, Y, "n_estimators", parameter_grid, cv=5)
print "\nParam: n_estimators\nTraining scores:\n", train_scores
print "\nParam: n_estimators\nValidation scores\n", validation_scores

fig = plt.figure()
sub1 = fig.add_subplot(3,1,1)
sub1.plot(parameter_grid, 100*np.average(train_scores, axis=1), color='black')
sub1.set_title('Train Curve')
sub1.set_xlabel('Number of estimators')
sub1.set_ylabel('Accuracy')

classifier = RandomForestClassifier(n_estimators=20, random_state=7)
parameter_grid = np.linspace(2, 20, 5).astype(int)
train_scores, validation_scores = validation_curve(classifier, X, Y, 'max_depth', parameter_grid, cv=5)
print "\nParam: max_depth\nTraining scores:\n", train_scores
print "\nParam: max_depth\nValidation scores\n", validation_scores

sub2 = fig.add_subplot(3,1,2)
sub2.plot(parameter_grid, 100*np.average(train_scores, axis=1), color='black')
sub2.set_title('Validation Curve')
sub2.set_xlabel('Maximum depth of the tree')
sub2.set_ylabel('Accuracy')

classifier = RandomForestClassifier(random_state=7)
parameter_grid = np.array([200, 500, 800, 1100])
train_sizes_abs, train_scores, validation_scores = learning_curve(classifier, X, Y, train_sizes=parameter_grid, cv=5)
print "Learning Curve\n"
print "\nTraining Score\n", train_scores
print "\nValidation Score\n", validation_scores

sub3 = fig.add_subplot(3,1,3)
sub3.plot(parameter_grid, 100*np.average(train_scores, axis=1), color='black')
sub3.set_title('Learning Score')
sub3.set_xlabel('Number of Training samples')
sub3.set_ylabel('Accuracy')
plt.show()