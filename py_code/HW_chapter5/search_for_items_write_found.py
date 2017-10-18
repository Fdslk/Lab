import os
import sys
import glob
import csv
from xlrd import open_workbook, xldate_as_tuple
from datetime import date
item_number_file = sys.argv[1]
path_to_folder = sys.argv[2]
output_file = sys.argv[3]
item_number_to_find = []
with open(item_number_file, 'r') as item_number_csv_file:
	filereader = csv.reader(item_number_csv_file)
	for row in filereader:
		item_number_to_find.append(row[0])
csv_out_file = open(output_file, 'a')
filewriter = csv.writer(csv_out_file)
full_path = os.path.join(path_to_folder, '*.*')
files = glob.glob(full_path)
file_number = 0
line_number = 0
count_of_item_numbers = 0
for input_file in files:
	file_number += 1
	if input_file.split('.')[1] == 'csv':
		csv_in_file = open(input_file, 'r')
		filereader = csv.reader(csv_in_file)
		header = next(filereader, None)
		filewriter.writerow(header)
		for row_list in filereader:
			row_of_output = []
			for col_index in range(len(header)):
				if col_index == 3:
					cell_value = str(row_list[col_index]).lstrip('$').replace('.', '').strip()
					row_of_output.append(cell_value)
				else:
					cell_value = str(row_list[col_index]).strip()
					row_of_output.append(cell_value)
			row_of_output.append(os.path.basename(input_file))
			if row_list[0] in item_number_to_find:
				filewriter.writerow(row_of_output)
				count_of_item_numbers += 1
			line_number += 1
	elif input_file.split('.')[1] == 'xls' or\
	input_file.split('.')[1] == 'xlsx':
			workbook = open_workbook(input_file)
			for worksheet in workbook.sheets():
				try:
					header = worksheet.row_values(0)
				except IndexError:
					pass
				for row in range(1, worksheet.nrows):
					row_of_output = []
					for col_index in range(1, worksheet.ncols):
						if worksheet.cell_type(row, col_index) == 3:
							cell_date = xldate_as_tuple(worksheet.cell_value(row, col_index), workbook.datemode)
							cell_date = str(date(*cell_date[0:3])).strip()
							row_of_output.append(cell_date)
						else:
							cell_value = str(worksheet.cell_value(row, col_index)).strip()
							row_of_output.append(cell_value)
					row_of_output.append(os.path.basename(input_file))
					row_of_output.append(worksheet.name)
					item_number = str(worksheet.cell_value(row, 0)).split('.')[0]
					if item_number in item_number_to_find:
						filewriter.writerow(row_of_output)
						count_of_item_numbers += 1
					line_number += 1
print("numbers of files:{0:d}\n".format(file_number))
print("count of item numbers:{0:d}\n".format(count_of_item_numbers))
print("line numbers:{0:d}".format(line_number))
