import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn import datasets
from sklearn.metrics import mean_squared_error, explained_variance_score
from sklearn.utils import shuffle
import matplotlib.pyplot as plt

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

housing_data = datasets.load_boston()
x, y = shuffle(housing_data.data, housing_data.target, random_state=7)
num_training = int(len(x) * 0.8)
x_train, y_train = x[:num_training], y[:num_training]
x_test, y_test = x[num_training:], y[num_training:]

dt_regressor = DecisionTreeRegressor(max_depth=4)
dt_regressor.fit(x_train, y_train)

ab_regressor = AdaBoostRegressor(DecisionTreeRegressor(max_depth=4), n_estimators=400, random_state=7)
ab_regressor.fit(x_train, y_train)

y_test_pred_dt = dt_regressor.predict(x_test)
y_test_pred_ab = ab_regressor.predict(x_test)
ab_regressor_mse = round(mean_squared_error(y_test, y_test_pred_ab), 2)
ab_regressor_evs = round(explained_variance_score(y_test, y_test_pred_ab), 2)
dt_regressor_mse = round(mean_squared_error(y_test, y_test_pred_dt), 2)
dt_regressor_evs = round(explained_variance_score(y_test, y_test_pred_dt), 2)
print("\nab_regressor mean_squared_error ={0:.2f}; explained_variance_score={1:.2f}".format(ab_regressor_mse, ab_regressor_evs))
print("\ndt_regressor mean_squared_error={0:.2f}; explained_variance_score={1:.2f}".format(dt_regressor_mse, dt_regressor_evs))

plot_feature_importance(dt_regressor.feature_importances_, 'dt_regressor', housing_data.feature_names)
plot_feature_importance(ab_regressor.feature_importances_, 'ab_regressor', housing_data.feature_names)

