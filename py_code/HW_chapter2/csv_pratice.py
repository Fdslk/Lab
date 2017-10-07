import sys
import csv
import re
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

class_level = "Phd"
class_list = ['Phd', 'Master']
pattern = re.compile(r'(?P<name>n)', re.I)

#*** usual method to pick up the specail row data***
#with open(input_file, 'r') as csv_in_file:
#	with open(output_file, 'w') as csv_out_file:
#		filereader = csv.reader(csv_in_file)
#		filewriter = csv.writer(csv_out_file)
#		header = next(filereader)
#		filewriter.writerow(header)
#		for row_list in filereader:
#			classer = row_list[2]
#			if classer == class_level:
#				filewriter.writerow(row_list)

#*** pandas to pick up the specail row data***

#data_frame = pd.read_csv(input_file)
#data_frame_value_meet_conditon = data_frame.loc[data_frame['class'].\
#str.contains(class_level),:]
#data_frame_value_meet_conditon.to_csv(output_file) 

#*** data contain in the special data set
#with open(input_file, 'r') as csv_in_file:
#	with open(output_file, 'w') as csv_out_file:
#		filereader = csv.reader(csv_in_file)
#		filewriter = csv.writer(csv_out_file)
#		header = next(filereader)
#		filewriter.writerow(header)
#		for row_list in filereader:
#			a_data = row_list[2]
#			if a_data in class_list:
#				filewriter.writerow(row_list)

#*** pandas method to pick up the special row data***
#data_frame = pd.read_csv(input_file)
#data_frame_value_in_set = data_frame.loc[data_frame['class'].str.strip().\
#isin(class_list),:]
#data_frame_value_in_set.to_csv(output_file)

#*** use the matches-pattern to pick up special data***
with open(input_file, 'r') as csv_in_file:
	with open(output_file, 'w') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		filewriter.writerow(header)
		for row_list in filereader:
			name = row_list[1]
			if pattern.search(name):
				filewriter.writerow(row_list)  


