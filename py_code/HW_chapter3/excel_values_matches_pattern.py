import sys
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
import re
from datetime import date

input_file = sys.argv[1]
output_file = sys.argv[2]
pattern = re.compile(r'(?P<group_name>^J.*)')
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013_output')
customer_name_column_index = 1
with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2013')
	data = []
	header = worksheet.row_values(0)
	data.append(header)
	for row_index in range(1, worksheet.nrows):
		row_list = []
		if pattern.search(worksheet.cell_value(row_index, customer_name_column_index)):
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
	for list_index, input_list in enumerate(data):
		for element_index, element in enumerate(input_list):
			output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)
