from plot_fun.func import plot
from sklearn.metrics import confusion_matrix
y_true = [1, 0, 0, 2, 1, 0, 3, 3, 3]
y_pred = [1, 1, 0, 2, 1, 0, 1, 3, 3]
confusion_mat = confusion_matrix(y_true, y_pred)
plot1 = plot()
plot1.plot_confusion_matrix(confusion_mat)
print(confusion_mat)