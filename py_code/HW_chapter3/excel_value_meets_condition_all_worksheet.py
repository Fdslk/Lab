import sys
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook
from datetime import date

input_file = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('pick_up_all_row_from_workbook', cell_overwrite_ok=True)
sale_amount_index = 3
sale_threshold = 2000.0
first_worksheet = True
with open_workbook(input_file) as workbook:
	data = []
	for worksheet in workbook.sheets():
		if first_worksheet:
			header = worksheet.row_values(0)
			data.append(header)
			first_worksheet = False
		for row_index in range(1, worksheet.nrows):
			row_list = []
			sale_amount = worksheet.cell_value(row_index, sale_amount_index)
			if sale_amount > sale_threshold:
				for col_index in range(worksheet.ncols):
					cell_value = worksheet.cell_value(row_index, col_index)
					cell_type = worksheet.cell_type(row_index, col_index)
					if cell_type == 3:
						date_value = xldate_as_tuple(cell_value, workbook.datemode)
						date_value = date(*date_value[0:3]).strftime('%m/%d/%Y')
						row_list.append(date_value)
					else:
						row_list.append(cell_value)
				if row_list:
					data.append(row_list)
		for list_index, output_list in enumerate(data):
			for element_index, element in enumerate(output_list):
				output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)