list1 = ['a', 'b', 'c', 'd']
list2 = [1, 2, 3, 4]

new_dict = {}

for i in range(len(list1)):
	if list1[i] not in new_dict:
		new_dict[list1[i]] = list2[i]

for key, value in new_dict.items():
	print ("Key:{0:s}-Value:{1}\n".format(key, value))		
