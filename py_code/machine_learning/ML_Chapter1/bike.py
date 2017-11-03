import csv
import sys
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

filter_type = "red"
filter_index = [1]

def plot_feature_importance(feature_importances, title, feature_name):
	feature_importances = 100.0 * (feature_importances/ max(feature_importances))
	index_sorted = np.flipud(np.argsort(feature_importances))
	pos = np.arange(index_sorted.shape[0]) + 0.5
	
	plt.figure()
	plt.bar(pos, feature_importances[index_sorted], align='center')
	plt.xticks(pos, feature_name[index_sorted])
	plt.ylabel('Relative Importance')
	plt.title(title)
	plt.show()


def load_dataset(filename):
	with open(filename, 'r') as csv_in_file:
		filereader = csv.reader(csv_in_file)
		x, y = [], []
		header = next(filereader)
		x.append(header[2:14])
		for row in filereader:
			x.append(row[2:14])
			y.append(row[-1])
		feature_names = np.array(x[0])
	return np.array(x[1:]).astype(np.float32), np.array(y[1:]).astype(np.float32), feature_names
	
def load_data_csv(filename):
	data_frame = pd.read_csv(filename)
	data_frame_meet_condition = data_frame.loc[data_frame['type'] == "red", :]
	x, y = [], []
	for index, row in data_frame_meet_condition.iterrows():
		if index == 0:
			x.append(row[1:11])
		else:
			x.append(row[1:11])
			y.append(row[12])
	feature_names = np.array(x[0])
	return np.array(x[1:]).astype(np.float32), np.array(y[1:]).astype(np.float32), feature_names
	
x, y, feature_names = load_dataset(sys.argv[1])
x2, y2, feature_names_wine = load_data_csv(sys.argv[2])
x, y = shuffle(x, y, random_state=7)

num_training = int(len(x) * 0.9)
x_train, y_train = x[:num_training], y[:num_training]
x_test, y_test = x[num_training:], y[num_training:]

rf_regressor = RandomForestRegressor(n_estimators=1000, max_depth=10)
rf_regressor.fit(x_train, y_train)
y_test_pred_rf = rf_regressor.predict(x_test)

rf_regressor_mse = round(mean_squared_error(y_test, y_test_pred_rf), 2)
rf_regressor_evs = round(explained_variance_score(y_test, y_test_pred_rf), 2)
print("\nrf_regressor_evs={0:.2f}; rf_regressor_mse={1:.2f}".format(rf_regressor_evs, rf_regressor_mse))

plot_feature_importance(rf_regressor.feature_importances_, 'random forest regressor', feature_names)