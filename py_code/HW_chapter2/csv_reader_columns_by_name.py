import sys
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]
my_colums = ['Invoice Number', 'Purchase Date']
columns_index = []

with open(input_file, 'r') as csv_in_file:
	with open(output_file, 'w') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header = next(filereader, None)
		for index in range(len(header)):
			if header[index] in my_colums:
				columns_index.append(index)
		filewriter.writerow(my_colums)
		for row_list in filereader:
			row_list_output = []
			for index in columns_index:
				row_list_output.append(row_list[index])
			filewriter.writerow(row_list_output)