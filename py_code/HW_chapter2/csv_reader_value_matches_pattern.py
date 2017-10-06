import csv
import sys
import re
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

#pattern = re.compile(r'(?P<my_pattern_group>^001-.*)', re.I)
#with open(input_file, 'r') as csv_in_file:
#	with open(output_file, 'w') as csv_out_file:
#		filereader = csv.reader(csv_in_file)
#		filewriter = csv.writer(csv_out_file)
#		header = next(filereader)
#		filewriter.writerow(header)
#		for row_list in filereader:
#			invoice_number = row_list[1]
#			if pattern.search(invoice_number):
#				filewriter.writerow(row_list)

data_frame = pd.read_csv(input_file)
data_frame_value_matches_pattern = data_frame.loc[data_frame['Invoice Number'].\
str.startswith('001-'),:]
data_frame_value_matches_pattern.to_csv(output_file, index=False)