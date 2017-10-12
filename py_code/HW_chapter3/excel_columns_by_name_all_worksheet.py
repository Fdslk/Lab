import sys
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date

input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('select_columns_all_worksheets')
my_columns = ['Customer Name', 'Sale Amount']
first_worksheet = True

with open_workbook(input_file) as workbook:
	data = []
	data.append(my_columns)
	my_columns_index = []
	for worksheet in workbook.sheets():
		if first_worksheet:
			header = worksheet.row_values(0)
			for index in range(len(header)):
				if header[index] in my_columns:
					my_columns_index.append(index)
			first_worksheet = False
		for row_index in range(1, worksheet.nrows):
			row_list = []
			for col_index in my_columns_index:
				cell_value = worksheet.cell_value(row_index, col_index)
				cell_type = worksheet.cell_type(row_index, col_index)
				if cell_type == 3:
					date_cell = xldate_as_tuple(cell_value, workbook.datemode)
					date_cell = data(*date_cell[0:3]).strftime('%m/%d/%Y')
					row_list.append(date_cell)
				else:
					row_list.append(cell_value)
			if row_list:
				data.append(row_list)
	for list_index, input_list in enumerate(data):
		for element_index, element in enumerate(input_list):
			output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)