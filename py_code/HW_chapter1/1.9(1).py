list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]

new_list = list1 + list2 + list3

for i in range(len(new_list)):
	print("{0}-{1}\n".format(i, new_list[i]))