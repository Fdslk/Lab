import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
import numpy as np
	
class plot():
	def __init_(self):
		self = self
		
	def plot_confusion_matrix(self, confusion_mat, data_class):
		plt.imshow(confusion_mat, interpolation='nearest', cmap=plt.cm.Paired)
		plt.title('Confusion matrix')
		plt.colorbar()
		tick_marker = np.arange(data_class)
		plt.xticks(tick_marker, tick_marker)
		plt.yticks(tick_marker, tick_marker)
		plt.xlabel('True Label')
		plt.ylabel('Predict Label')
		plt.show()
		
	def plot_classifier(self, classifier, x, y):
		x_min, x_max = min(x[:, 0]) - 1.0, max(x[:, 0]) + 1.0
		y_min, y_max = min(x[:, 1]) - 1.0, max(x[:, 1]) + 1.0
		step_size = 0.01
		x_values, y_values = np.meshgrid(np.arange(x_min, x_max, step_size), np.arange(y_min, y_max, step_size))
		mesh_out = classifier.predict(np.c_[x_values.ravel(), y_values.ravel()])
		mesh_out = mesh_out.reshape(x_values.shape)
		plt.figure()
		plt.pcolormesh(x_values, y_values, mesh_out, cmap=plt.cm.gray)
		plt.scatter(x[:,0], x[:,1], c=y, s=80, edgecolors='black', linewidth=1)
		plt.xlim(x_values.min(), x_values.max())
		plt.ylim(y_values.min(), y_values.max())
		plt.xticks((np.arange(int(min(x[:, 0]) - 1), int(max(x[:, 0]) + 1), 1.0)))
		plt.xticks((np.arange(int(min(x[:, 1]) - 1), int(max(x[:, 1]) + 1), 1.0)))
		plt.show()