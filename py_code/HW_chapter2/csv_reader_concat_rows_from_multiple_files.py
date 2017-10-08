import sys
import csv
import os
import glob

input_path = sys.argv[1]
output_file = sys.argv[2]

first_file = True

file_full_path = os.path.join(input_path, 'sales_*')
files = glob.glob(file_full_path)
for input_file in files:
	print (input_file)
	with open(input_file, 'r') as csv_in_file:
		with open(output_file, 'a') as csv_out_file:
			filereader = csv.reader(csv_in_file)
			filewriter = csv.writer(csv_out_file)
			if first_file:
				for row in filereader:
					filewriter.writerow(row)
				first_file = False
			else:
				header = next(filereader, None)
				for row in filereader:
					filewriter.writerow(row)
