import sys
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]
my_columns = [0, 3]

with open(input_file, 'r') as csv_in_file:
	with open(output_file, 'w') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader)
		header_list = []
		for index in my_columns:
			header_list.append(header[index])
		filewriter.writerow(header_list)
		for row_list in filereader:
			row_list_output = []
			cost = str(row_list[3]).strip('$').replace(',', '')
			if float(cost) <= 500.0:
				for index_value in my_columns:
					row_list_output.append(row_list[index_value])
				filewriter.writerow(row_list_output)