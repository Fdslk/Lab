import sys
import csv
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]
important_dates = ['1/20/2014', '1/30/2014']
#with open(input_file, 'r') as csv_in_file:
#	with open(output_file, 'w') as csv_out_file:
#		filereader = csv.reader(csv_in_file)
#		filewriter = csv.writer(csv_out_file)
#		header = next(filereader)
#		filewriter.writerow(header)
#		for row_list in filereader:
#			a_date = row_list[4]
#			if a_date in important_dates:
#				filewriter.writerow(row_list)
# ***use the pandas method***
data_frame = pd.read_csv(input_file)
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].\
isin(important_dates), :]
data_frame_value_in_set.to_csv(output_file, index=False)