import sys
import csv
import os
import glob

input_path = sys.argv[1]
file_count = 0
file_full_path = os.path.join(input_path, '*.csv')
files = glob.glob(file_full_path)
for input_file in files:
	file_row = 1
	with open(input_file, 'r') as csv_in_file:
		filereader = csv.reader(csv_in_file)
		header = next(filereader, None)
		for row in filereader:
			file_row += 1
	print('{0!s}:\t {1:d} rows\t {2:d} columns\n'.format(\
	os.path.basename(input_file), file_row, len(header)))
	file_count += 1
print("Numbers of the files:{0:d}".format(file_count))