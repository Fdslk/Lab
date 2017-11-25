import json 
import numpy as np
from pearson_corelation_coefficience import pearson
from euclidean_score import euclidean_score
from find_similar_user import find_similar_users

def generate_recommedndations(dataset, user):
	if user not in dataset:
		raise TypeError('User' + user + 'not present in the dataset')
	total_score = {}
	similar_sums = {}
	for u in [x for x in dataset if x != user]:
		similar_score = pearson(dataset, user, u)
		if similar_score <= 0:
			continue
		for item in [x for x in dataset[u] if x not in dataset[user] or dataset[user][x] == 0]:
			total_score.update({item: dataset[u][item] * similar_score})
			similar_sums.update({item: similar_score})
	if len(total_score) == 0:
		return ['No recommendations possible']
	movie_ranks = np.array([[total/similar_sums[item], item] for item, total in total_score.items()])
	movie_ranks = movie_ranks[np.argsort(movie_ranks[:, 0])[::-1]]
	recommendations = [movie for _, movie in movie_ranks]
	return recommendations
	
if __name__ == '__main__':
	datafile = 'movie_ratings.json'
	with open(datafile, 'r') as f:
		data = json.loads(f.read())
	user = 'Michael Henry'
	print "\nRecommendations for " + user + ":"
	movies = generate_recommedndations(data, user)
	for i, movie in enumerate(movies):
		print str(i+1) +'. ' + movie