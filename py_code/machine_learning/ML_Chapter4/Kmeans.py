import numpy as np
import matplotlib.pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans
import sys
input_file = sys.argv[1]
X = []
Y = []
Data = []
num_clusters = 4
with open(input_file, 'r') as file:
	for line in file.readlines():
		data = [float(x) for x in line.split(',')]
		X.append(data[0])
		Y.append(data[-1])
		Data.append(data)
Data = np.array(Data)
		
plt.figure()
x_min, x_max = min(X)-1, max(X)+1
y_min, y_max = min(X)-1, max(X)+1

kmeans = KMeans(init='k-means++', n_clusters=num_clusters, n_init=10)
kmeans.fit(Data)
step_size = 0.01
x_values, y_values = np.meshgrid(np.arange(x_min, x_max, step_size), np.arange(y_min, y_max, step_size))
predict_labels = kmeans.predict(np.c_[x_values.ravel(), y_values.ravel()])
predict_labels = predict_labels.reshape(x_values.shape)
plt.clf()
plt.imshow(predict_labels, interpolation='nearest', 
			extent=(x_values.min(), x_values.max(), y_values.min(), y_values.max()),
			cmap=plt.cm.Paired,
			aspect='auto', origin='lower')
plt.scatter(X, Y, marker='o', facecolors='none', edgecolors='k', s=30)
centroids = kmeans.cluster_centers_
plt.scatter(centroids[:,0], centroids[:,1], marker='o', s=200, linewidths=3, color='k', zorder=10, facecolors='black')
plt.title('Centoids and boundaries obtained using KMeans')
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
plt.xticks(())
plt.yticks(())
plt.show()
			