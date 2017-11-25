import json
import numpy as np
from pearson_corelation_coefficience import pearson

def find_similar_users(dataset, user, num_user):
	if user not in dataset:
		raise TypeError('User' + user + 'not present in the dataset')
	scores = np.array([[x, pearson(dataset, user, x)] for x in dataset if user != x])
	scores_sorted = np.argsort(scores[:, 1])
	scores_sorted_dec = scores_sorted[::-1]
	top_k = scores_sorted_dec[0:num_user]
	return scores[top_k]
	
if __name__ == '__main__':
	datafile = 'movie_ratings.json'
	with open(datafile, 'r') as f:
		data = json.loads(f.read())
	user = 'John Carson'
	print"\nUsers similar to " + user + ":\n"
	similar_user = find_similar_users(data, user, 3)
	for item in similar_user:
		print item[0], '\t\t', round(float(item[1]),2)