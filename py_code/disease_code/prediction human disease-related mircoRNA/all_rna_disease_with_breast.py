import sys
import glob
import os
from xlrd import open_workbook
from xlwt import Workbook
input_folder = sys.argv[1]
output_file = sys.argv[2]
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('rna_disease_breast')
input_files = glob.glob(os.path.join(input_folder, '*.xls*'))
data = []
for file in input_files:
	# alentries.xls
	if os.path.basename(file) == 'AllEntries.xls':
		with open_workbook(file) as workbook:
			for worksheet in workbook.sheets():
				for row_index in range(worksheet.nrows):
					row_list = []
					if worksheet.cell_value(row_index, 1) == 'breast cancer':
						row_list.append(worksheet.cell_value(row_index, 0))
					if row_list:
						if row_list not in data:
							data.append(row_list)
	# miRCancerMarch2017.xls
	if os.path.basename(file) == 'miRCancerMarch2017.xls':
		with open_workbook(file) as workbook:
			for worksheet in workbook.sheets():
				header = worksheet.row_values(0)
				for row_index in range(worksheet.nrows):
					row_list = []
					if worksheet.cell_value(row_index, 1) == 'breast cancer':
						row_list.append(worksheet.cell_value(row_index, 0))
					if row_list:
						if row_list not in data:
							data.append(row_list)
	# oncomirdb.xls
	if os.path.basename(file) == 'oncomirdb.xls':
		with open_workbook(file) as workbook:
			for worksheet in workbook.sheets():
				header = worksheet.row_values(0)
				for row_index in range(worksheet.nrows):
					row_list = []
					if worksheet.cell_value(row_index, 2) == 'breast':
						row_list.append(worksheet.cell_value(row_index, 5))
					if row_list:
						if row_list not in data:
							data.append(row_list)
	# rna_disease.xls					
	if os.path.basename(file) == 'rna_disease.xls':
		with open_workbook(file) as workbook:
			for worksheet in workbook.sheets():
				for row_index in range(worksheet.nrows):
					row_list = []
					if worksheet.cell_value(row_index, 2) == 'Breast Neoplasms':
						row_list.append(worksheet.cell_value(row_index, 1))
					if row_list:
						if row_list not in data:
							data.append(row_list)
							
for list_index, output_list in enumerate(data):
	for element_index, element in enumerate(output_list):
		output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)