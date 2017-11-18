import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from sklearn import neighbors, datasets
import sys
input_file = sys.argv[1]
X = []
with open(input_file, 'r') as file:
	for line in file.readlines():
		data = [float(x) for x in line.split(',')]
		X.append(data)
X = np.array(X)
		
x, y = X[:,:-1], X[:,-1].astype(np.int)
plt.figure()
plt.title('Input datapoints')
markers = 'sov<>hp'
mapper = np.array([markers[i] for i in y])
for i in range(x.shape[0]):
	plt.scatter(x[i, 0], x[i, 1], marker=mapper[i], s=50, edgecolors='black', facecolors='none')
	
num_neighbors = 10
step_size = 0.01
classifier = neighbors.KNeighborsClassifier(num_neighbors, weights='distance')
classifier.fit(x, y)
x_min, x_max = x[:, 0].min()-1, x[:, 0].max()+1
y_min, y_max = x[:, 1].min()-1, x[:, 1].max()+1
x_grid, y_grid = np.meshgrid(np.arange(x_min, x_max, step_size), np.arange(y_min, y_max, step_size))
predicted_values = classifier.predict(np.c_[x_grid.ravel(), y_grid.ravel()])
predicted_values = predicted_values.reshape(x_grid.shape)
plt.figure()
plt.pcolormesh(x_grid, y_grid, predicted_values, cmap=cm.Pastel1)

for i in range(x.shape[0]):
	plt.scatter(x[i, 0], x[i, 1], marker=mapper[i], s=50, edgecolors='black', facecolors='none')
plt.xlim(x_grid.min(), x_grid.max())
plt.ylim(y_grid.min(), y_grid.max())
plt.title('k nearest neighbors classifier boundaries')

test_point = [4.5, 3.6]
plt.figure()
plt.title('Test datapoint')
for i in range(x.shape[0]):
	plt.scatter(x[i, 0], x[i, 1], marker=mapper[i], s=50, edgecolors='black', facecolors='none')
	
plt.scatter(test_point[0], test_point[1], marker='x', linewidth=3, s=200, facecolors='black')
dist, indices = classifier.kneighbors(np.array([test_point]))

plt.figure()
plt.title('k nearest neighbors')
for i in indices:
	plt.scatter(x[i, 0], x[i, 1], marker='o', linewidth=3, s=100, facecolors='black')
	
plt.scatter(test_point[0], test_point[1], marker='x', linewidth=3, s=200, edgecolors='black', facecolors='none')

for i in range(x.shape[0]):
	plt.scatter(x[i,0], x[i,1], marker=mapper[i], s=50, edgecolors='black', facecolors='none')

plt.show()
print(classifier.predict(np.array([test_point]))[0])