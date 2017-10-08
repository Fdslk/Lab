import os
import sys
import csv
import glob
	
input_path = sys.argv[1]
output_file = sys.argv[2]
output_header = ['filename', 'total_sales', 'average_sales']
csv_out_file = open(output_file, 'a')
filewriter = csv.writer(csv_out_file)
filewriter.writerow(output_header)
files = glob.glob(os.path.join(input_path, 'sales_*'))
for file in files:
	with open(file, 'r') as csv_in_file:
		filereader = csv.reader(csv_in_file)
		output_list = []
		output_list.append(os.path.basename(file))
		header = next(filereader)
		total_sales = 0.0
		number_of_sales = 0.0
		for row in filereader:
			sale_amount = row[3]
			total_sales += float(str(sale_amount).strip('$').replace(',',''))
			number_of_sales += 1
		average_sales = '{0:2f}'.format(total_sales/number_of_sales)
		output_list.append(total_sales)
		output_list.append(average_sales)
		filewriter.writerow(output_list)
csv_out_file.close()