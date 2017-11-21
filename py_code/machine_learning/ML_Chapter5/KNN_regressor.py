import numpy as np
import matplotlib.pyplot as plt
from sklearn import neighbors

amplitude = 10
num_points = 100
X = amplitude * np.random.rand(num_points, 1) - 0.5 * amplitude

Y = np.sinc(X).ravel()
Y += 0.2 * (0.5 - np.random.rand(Y.size))
plt.figure()
plt.scatter(X, Y, s=40, c='k', facecolors='none')
plt.title('input data')
x_values = np.linspace(-0.5*amplitude, 0.5*amplitude, 10*num_points)[:, np.newaxis]
n_neighbor = 8
knn_regressor = neighbors.KNeighborsRegressor(n_neighbor, weights='distance')
Y_values = knn_regressor.fit(X, Y).predict(x_values)
plt.figure()
plt.scatter(X, Y, s=40, c='k', facecolors='none', label='input data')
plt.plot(x_values, Y_values, c='k', linestyle='--', label='predicted values')
plt.xlim(X.min() - 1, X.max() + 1)
plt.ylim(Y.min() - 0.2, Y.max() + 0.2)
#plt.aopxis('tight')
plt.legend()
plt.title('K Nearest Neighbors Regressor')
plt.show()