import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import NearestNeighbors
X = np.array([[1,1], [1, 3], [2, 2], [2.5, 5], [3, 1], [4, 2], [2, 3.5], [3, 3], [3.5, 4]])
num_neighbor = 3
input_point = np.array([2.6, 1.7])
plt.figure()
plt.scatter(X[:,0], X[:,1], marker='o', s=25, color='k')
knn = NearestNeighbors(n_neighbors=num_neighbor, algorithm='ball_tree').fit(X)
distances, indices = knn.kneighbors([input_point])
print "\nk nearest neighbors"
for rank, index in enumerate(indices[0][:num_neighbor]):
	print str(rank+1) + "-->", X[index]
	
plt.figure()
plt.scatter(X[:,0], X[:,1], marker='o', s=25, color='k')
plt.scatter(X[indices][0][:][:,0], X[indices][0][:][:,1], marker='o', s=150, color='k', facecolor='none')
plt.scatter(input_point[0], input_point[1], marker='x', s=150, color='k', facecolor='none')
plt.show()