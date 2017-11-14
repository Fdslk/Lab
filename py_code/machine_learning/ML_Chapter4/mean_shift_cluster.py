import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
import matplotlib.pyplot as plt
from itertools import cycle
import sys
input_file = sys.argv[1]
data = []
with open(input_file, 'r') as file:
	for line in file.readlines():
		X = [float(x) for x in line.split(',')]
		data.append(X)

data = np.array(data)
bandwidth = estimate_bandwidth(data, quantile=0.1, n_samples=len(data))
meanshift_estimator = MeanShift(bandwidth=bandwidth, bin_seeding=True)
meanshift_estimator.fit(data)
labels = meanshift_estimator.labels_
centroids = meanshift_estimator.cluster_centers_
num_cluster = len(np.unique(labels))
print "Number of clusters in input data: ", num_cluster
plt.figure()
marker = '.*xv'
for i, marker in zip(range(num_cluster), marker):
	plt.scatter(data[labels==i, 0], data[labels==i, 1], marker=marker, color='k')
	centroid = centroids[i]
	plt.plot(centroid[0], centroid[1], marker='o', markerfacecolor='k', markeredgecolor='k', markersize=15)
plt.title('Cluster and their centroids')
plt.show()