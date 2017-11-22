import json
import sys
import numpy as np

input_file = sys.argv[1]

def pearson(dataset, user1, user2):
	if user1 not in dataset:
		raise TypeError('user1' + user1 + 'not in the dataset')
	if user2 not in dataset:
		raise TypeError('user2' + user2 + 'not in the dataset')
	rated_by_both = {}
	for item in dataset[user1]:
		if item in dataset[user2]:
			rated_by_both[item] = 1
	if len(rated_by_both) == 0:
		return 0
	
	user1_sum = np.sum(dataset[user1][item] for item in rated_by_both)
	user2_sum = np.sum(dataset[user2][item] for item in rated_by_both)
	
	ave_user1 = user1_sum/float(len(rated_by_both))
	ave_user2 = user2_sum/float(len(rated_by_both))
	
	user1_sub = np.array([dataset[user1][item] - ave_user1 for item in rated_by_both])
	user2_sub = np.array([dataset[user2][item] - ave_user2 for item in rated_by_both])
	E_1_2 = np.sum([user1_sub[index]*user2_sub[index] for index in range(len(rated_by_both))])
	S_1 = np.sum([np.square(user1_sub[index]) for index in range(len(rated_by_both))])
	S_2 = np.sum([np.square(user2_sub[index]) for index in range(len(rated_by_both))])
	
	if S_1*S_2 == 0:
		return 0
	return E_1_2/(np.sqrt(S_1)*np.sqrt(S_2))
	
if __name__ == '__main__':
	with open(input_file, 'r') as f:
		data = json.loads(f.read())
	user1 = 'John Carson'
	user2 = 'Michelle Peterson'
	print(pearson(data, user1, user2))