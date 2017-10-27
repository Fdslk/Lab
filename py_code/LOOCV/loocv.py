from sklearn import cross_validation
# import numpy as np
# X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
# Y = np.array([1, 2, 1, 2])
# labels = np.array([1, 1, 2, 2])
# lol = cross_validation.LeaveOneLabelOut(labels)
# print len(lol)
# print lol
# for train_index,test_index in lol:
	# print("Train:", train_index, "TEST:", test_index)
	# X_train, X_test = X[train_index], X[test_index]
	# Y_train, Y_test = Y[train_index], Y[test_index]
	# print(X_train, X_test, Y_train, Y_test)
#coding=utf-8
from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
import numpy as np
from sklearn.model_selection import LeaveOneOut  
from sklearn.model_selection import LeavePOut
X= np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
y= np.array([1, 2, 3, 4])
kf= KFold(n_splits=2)
kf.get_n_splits(X)
print(kf) 
for train_index, test_index in kf.split(X):
	print("TRAIN:",train_index, "TEST:", test_index)
	X_train,X_test = X[train_index], X[test_index]
	y_train,y_test = y[train_index], y[test_index]
	print("X_train:", X_train, "X_test:", X_test, "y_train:", y_train, "y_test:", y_test, "\n")


X= [1, 2, 3, 4]  
loo= LeaveOneOut()  
for train, test in loo.split(X):  
	print("%s%s" % (train, test))  
	
	
X= np.ones(4)  
lpo= LeavePOut(p=1)  
for train, test in lpo.split(X):  
	print("%s%s" % (train, test))  

	
labels = [1,1,2,2,3,3]  
lolo=cross_validation.LeaveOneLabelOut(labels)  
for train, test in lolo:  
	print("%s%s" % (train, test))  
