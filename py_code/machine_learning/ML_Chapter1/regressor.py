import sys
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

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
ax1 = fig.add_subplot(2,1,1)
ax1.scatter(X_train, Y_train, color='green')
ax1.plot(X_train, Y_train_pred, color='black', linewidth=4)
ax1.set_title('Train data')

ax2 = fig.add_subplot(2,1,2)
y_test_pred = linear_regressor.predict(X_test)
ax2.scatter(X_test, Y_test, color='green')
ax2.plot(X_test, y_test_pred, color='black', linewidth=4)
ax2.set_title('Test data')
plt.show() 
