import sys
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date
import os
import glob

input_path = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('test_practice')
salse_amount_index = 3
threshold = 1800.0
full_path = os.path.join(input_path, '*.xls*')
workbooks = glob.glob(full_path)
first_file = True
data = []
title = ['workbook', 'worksheet']
for input_file in workbooks:
	with open_workbook(input_file) as workbook:
		for worksheet in workbook.sheets():
			worksheet_list = []
			if first_file:
				header = worksheet.row_values(0)
				title = title + header
				data.append(title)
				first_file = False
			for row_index in range(1, worksheet.nrows):
				row_list = []
				sale_amount = worksheet.cell_value(row_index, salse_amount_index)
				if sale_amount > threshold:
					row_list.append(os.path.basename(input_file))
					row_list.append(worksheet.name)
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
					worksheet_list.append(row_list)
			if worksheet_list:
				data.extend(worksheet_list)
for list_index, output_list in enumerate(data):
	for element_index, element in enumerate(output_list):
		output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)