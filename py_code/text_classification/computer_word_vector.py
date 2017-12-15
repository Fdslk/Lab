import numpy as np

class select_feature():
	
	def __init__(self):
		pass
	def compute_total_DocNum(self, input_file):
		docnum = 0
		with open(input_file, 'r') as file:
			for line in file.readlines():
				docnum += 1
		return docnum
		
	def count_Words(self, input_file):
		data = []
		with open(input_file, 'r') as file:
			for line in file.readlines():
				row_list = []
				row_list.append(line.split(' ')[0])
				word_num = (len(line.split(' ')) - 1)
				row_list.append(str(word_num))
				if row_list:
					data.append(row_list)
		return data
	#s = b'\xe8\xae\xa1\xe7\xae\x97\xe6\x9c\xba\xe8\xaf\xbe'
	#print(s.decode('utf-8'))			
	# def count_term_frequency(self):
	# def compute_Words_IDF(self):
	# def compute_word_tf_idf(self):
		