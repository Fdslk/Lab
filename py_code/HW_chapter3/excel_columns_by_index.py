import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('jan_2013')
my_column = [1, 4]
with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2013')
	data = []
	for row_index in range(worksheet.nrows):
		row_list = []
		for col_index in my_column:
			cell_value = worksheet.cell_value(row_index, col_index)
			cell_type = worksheet.cell_value(row_index,col_index)
			if cell_type == 3:
				date_cell = xldate_as_tuple(cell_value,workbook.datemode)
				date_cell = date(*date[0:3]).strftime('%m/%d/%Y')
				row_list.append(date_cell)
			else:
				row_list.append(cell_value)
		if row_list:
			data.append(row_list)
	for list_index, input_list in enumerate(data):
		for element_index, element in enumerate(input_list):
			output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)