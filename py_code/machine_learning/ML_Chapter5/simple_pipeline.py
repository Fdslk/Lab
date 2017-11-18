from sklearn.datasets import samples_generator
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectKBest, f_regression
from sklearn.pipeline import Pipeline
import matplotlib.pyplot as plt
import numpy as np

X, y = samples_generator.make_classification(n_informative=4, n_features=20, n_redundant=0, random_state=5)
true_positive = 0
plt.figure()
pred_acc = []
selector_k_best = SelectKBest(f_regression, k=10)
classifier = RandomForestClassifier(n_estimators=50, max_depth=4)
pipeline_classifier = Pipeline([('selector', selector_k_best), ('rf', classifier)])
pipeline_classifier.set_params(selector__k=6, rf__n_estimators=25)
for i in range(1, 11):
	pipeline_classifier.fit(X,y)
	prediction = pipeline_classifier.predict(X)
	print "\nPredictions:\n", prediction
	print "\nScore:", pipeline_classifier.score(X, y)
	pred_acc.append(pipeline_classifier.score(X, y))
plt.plot(np.array(range(1, 11)), pred_acc, color='blue', linestyle='-')
plt.ylabel('accuracy')
plt.xlabel('times')
plt.show()
features_status = pipeline_classifier.named_steps['selector'].get_support()
selected_features = []
for count, item in enumerate(features_status):
	if item:
		selected_features.append(count)
print "\nSelected features (0-indexed):", ','.join([str(x) for x in selected_features])