import sys
from xlrd import open_workbook
from xlwt import Workbook

input_file = sys.argv[1]
output_file = sys.argv[2]
breast_neoplasms_row_number = [1]
condition = 'Breast Neoplasms'
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('rna_breast_neoplasms')
with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('rna_disease')
	data = []
	for row_index in range(worksheet.nrows):
		row_list = []
		if worksheet.cell_value(row_index, 2) == condition:
			for col_index in breast_neoplasms_row_number:
				row_list.append(worksheet.cell_value(row_index, col_index))
		if row_list:
			if row_list not in data:
				data.append(row_list)
	for list_index, output_list in enumerate(data):
		for element_index, element in enumerate(output_list):
			output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)