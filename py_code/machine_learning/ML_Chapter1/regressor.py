import sys
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
import cPickle as pickle
import sklearn.metrics as sm
from sklearn.preprocessing import PolynomialFeatures

input_file = sys.argv[1]
X = []
Y = []
with open(input_file, 'r') as data:
	for line in data.readlines():
		xt ,yt = [float(i) for i in line.split(',')]
		X.append(xt)
		Y.append(yt)

num_training = int(0.8*len(X))
num_test = len(X) - num_training
X_train = np.array(X[:num_training]).reshape((num_training, 1))
Y_train = np.array(Y[:num_training])
X_test = np.array(X[num_training:]).reshape((num_test, 1))
Y_test = np.array(Y[num_training:])

linear_regressor = linear_model.LinearRegression()
linear_regressor.fit(X_train,Y_train)
Y_train_pred = linear_regressor.predict(X_train)

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax1.scatter(X_train, Y_train, color='green')
ax1.plot(X_train, Y_train_pred, color='black', linewidth=4)
ax1.set_title('Train data')

ax2 = fig.add_subplot(2,2,2)
y_test_pred = linear_regressor.predict(X_test)
ax2.scatter(X_test, Y_test, color='green')
ax2.plot(X_test, y_test_pred, color='black', linewidth=4)
ax2.set_title('Test data')

output_model_file = 'saved_model.pkl'
with open(output_model_file, 'w') as f:
	pickle.dump(linear_regressor, f)
	
with open(output_model_file, 'r') as f:
	model_linregr = pickle.load(f)

y_test_pred_new = model_linregr.predict(X_test)
print"\nNew mean absolute error = ", round(sm.mean_absolute_error(Y_test, y_test_pred_new), 2)
ax3 = fig.add_subplot(2, 2, 3)
ax3.scatter(X_test, Y_test, color='green')
ax3.plot(X_test, y_test_pred_new, color='black', linewidth=4)
ax3.set_title('new')

ridge_regressor = linear_model.Ridge(alpha=0.5, fit_intercept=True, max_iter=10000)
ridge_regressor.fit(X_train, Y_train)
y_test_pred_ridge = ridge_regressor.predict(X_test)
print("\nRidge_regressor mean absolute error = {0:.2f}".format(round(sm.mean_absolute_error(Y_test, y_test_pred_ridge), 2)))
ax4 = fig.add_subplot(2, 2, 4)
ax4.scatter(X_test, Y_test, color='green')
ax4.plot(X_test, y_test_pred_ridge, color='black', linewidth=4)
ax4.set_title('ridge_regressor')

ploynomial = PolynomialFeatures(degree=3)
X_train_transformed = ploynomial.fit_transform(X_train)
ploy_linear_model = linear_model.LinearRegression()
ploy_linear_model.fit(X_train_transformed, Y_train)
Y_train_pred_ploy = ploy_linear_model.predict(X_train_transformed)
print("\nploy_regressor mean absolute error = {0:.2f}".format(round(sm.mean_absolute_error(Y_train, Y_train_pred_ploy), 2)))
plt.show()

