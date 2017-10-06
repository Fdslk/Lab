import sys
import csv
# get the relative pathway of the input&output file
input_file = sys.argv[1]
output_file = sys.argv[2]
# process file 
with open(input_file, 'r') as csv_in_file:
	with open(output_file, 'w') as csv_out_file:
		filereader = csv.reader(input_file)
		filewriter = csv.writer(output_file)
		# read the head line(head title)
		header = next(filereader)
		filewriter.writerow(header)
		for row_list in filereader:
			supplier = str(row_list[0].strip())
			cost = str(row_list[3].strip('$').replace(',', '')
			# pick up the wanted data
			if supplier == 'Supplier Z' or float(cost) > 600.0:
				filewriter.writerow(row_list)