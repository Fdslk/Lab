import sys
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]

output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('january_2013_output')
important_date = ['01/24/2013', '01/31/2013']
purchase_date_columns = 4
with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('january_2013')
	data = []
	header = worksheet.row_values(0)
	data.append(header)
	for row_index in range(1, worksheet.nrows):
		row_list = []
		purchase_datetime = xldate_as_tuple(worksheet.cell_value(row_index, purchase_date_columns),\
											workbook.datemode)
		purchase_date = date(*purchase_datetime[0:3]).strftime('%m/%d/%Y')
		if purchase_date in important_date:
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