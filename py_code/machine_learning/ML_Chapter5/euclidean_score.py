import json
import numpy as np
import sys
input_file = sys.argv[1]
def euclidean_score(dataset, user1, user2):
	if user1 not in dataset:
		raise TypeError('User1' + user1 + 'not present in the dataset')
	if user2 not in dataset:
		raise TypeError('User2' + user2 + 'not present in the dataset')
	rated_by_both = {}
	for item in dataset[user1]:
		if item in dataset[user2]:
			rated_by_both[item] = 1
	if len(rated_by_both) == 0:
		return 0
	squared_differences = []
	for item in dataset[user1]:
		if item in dataset[user2]:
			squared_differences.append(np.square(dataset[user1][item] - dataset[user2][item]))
	return 1/(1 + np.sqrt(np.sum(squared_differences)))
	
if __name__ == '__main__':
	datafile = input_file
	with open(datafile, 'r') as f:
		data = json.loads(f.read())
	user1 = 'John Carson'
	user2 = 'Melissa Jones'
	print(euclidean_score(data, user1, user2))