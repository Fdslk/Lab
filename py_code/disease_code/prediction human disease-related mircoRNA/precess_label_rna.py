import sys
from xlrd import open_workbook
from xlwt import Workbook
input_file1 = sys.argv[1]
input_file2 = sys.argv[2]
output_file1 = sys.argv[3]
output_file2 = sys.argv[4]
output_workbook1 = Workbook()
output_worksheet1 = output_workbook1.add_sheet('labeled_rna')
output_workbook2 = Workbook()
output_worksheet2 = output_workbook2.add_sheet('unlabeled_rna')
data1 = []
data2 = []
label_data = []
unlabel_data = []
with open_workbook(input_file1) as workbook1:
	worksheet1 = workbook1.sheet_by_name('rna_disease_breast')
	for row_index in range(worksheet1.nrows):
		cell_value = worksheet1.cell_value(row_index, 0)
		data1.append([cell_value])

with open_workbook(input_file2) as workbook2:
	worksheet2 = workbook2.sheet_by_name('misim')
	for row_index in range(worksheet2.nrows):
		cell_value = worksheet2.cell_value(row_index, 0)
		data2.append([cell_value])

for element in data2:
	if element in data1:
		label_data.append(element)
	else:
		unlabel_data.append(element)
		
for list_index, output_list in enumerate(label_data):
	for element_index, element in enumerate(output_list):
		output_worksheet1.write(list_index, element_index, element)
		
for list_index, output_list in enumerate(unlabel_data):
	for element_index, element in enumerate(output_list):
		output_worksheet2.write(list_index, element_index, element)
output_workbook1.save(output_file1)
output_workbook2.save(output_file2)


