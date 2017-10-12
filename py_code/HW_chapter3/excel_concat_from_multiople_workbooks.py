import sys
import os
import glob
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date

input_path = sys.argv[1]
output_file = sys.argv[2]
full_path = os.path.join(input_path, '*.xls*')
workbooks = glob.glob(full_path)
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('combination_workbook')
first_header = True
data = []
for input_file in workbooks:
	with open_workbook(input_file) as workbook:
		for worksheet in workbook.sheets():
			if first_header:
				header = worksheet.row_values(0)
				data.append(header)
				first_header = False
			for row_index in range(1, worksheet.nrows):
				row_list = []
				for col_index in range(worksheet.ncols):
					cell_value = worksheet.cell_value(row_index, col_index)
					cell_type = worksheet.cell_type(row_index, col_index)
					if cell_type == 3:
						date_cell = xldate_as_tuple(cell_value, workbook.datemode)
						date_cell = date(*date_cell[0:3]).strftime('%m/%d/%Y')
						row_list.append(date_cell)
					else:
						row_list.append(cell_value)
				if row_list:
					data.append(row_list)
for list_index, output_list in enumerate(data):
	for element_index, element in enumerate(output_list):
		output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)
