# -*- coding: utf-8 -*-
import numpy as np
import os
import sys
from collections import defaultdict
from collections import Counter

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
		data = {}
		with open(input_file, 'r') as file:
			for line in file.readlines():
				data[line.split(' ')[0]] = {}
				word_num = (len(line.split(' ')) - 1)
				data[line.split(' ')[0]] = word_num
		return data
		
	def count_term_num(self, input_file):
		# type: (object) -> object
		data = {}
		count = 0
		with open(input_file, 'r') as file:
			for line in file.readlines():
				data[line.split(' ')[0]] = {}
				for row_index in range(1, len(line.split(' '))):
					if line.split(' ')[row_index] not in data[line.split(' ')[0]]:
						data[line.split(' ')[0]][line.split(' ')[row_index]] = 1
					else:
						data[line.split(' ')[0]][line.split(' ')[row_index]] += 1
				count += 1
					#head, words = line.split(' ', 1)
					#data[head] = {}
					#data[head] =  dict(Counter(words.split(' ')))
					#count += 1
		print(count)
		return data
					
	# def count_term_frequency(self, ):
	# def compute_Words_IDF(self):
	# def compute_word_tf_idf(self):
