import sys
import csv

input_file = sys.argv[1]
output_file = sys.argv[2]
headlist = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
with open(input_file, 'r') as csv_in_file:
	with open(output_file, 'w') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		filewriter.writerow(headlist)
		for row_list in filereader:
			filewriter.writerow(row_list)