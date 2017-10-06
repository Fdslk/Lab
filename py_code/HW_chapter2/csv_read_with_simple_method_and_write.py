import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as filereader:
	with open(output_file, 'w') as filerwriter:
		header = filereader.readline()
		header = header.strip()
		header_list = header.split(',')
		print(header_list)
		filerwriter.write(','.join(map(str, header_list))+'\n')
		for row in filereader:
			row = row.strip()
			row_list = row.split(',')
			print(row_list)
			filerwriter.write(','.join(map(str,row_list))+'\n')