import os
import sys
import glob
from datetime import date
from xlrd import open_workbook, xldate_as_tuple
from xlwt import Workbook

input_path = sys.argv[1]
output_file = sys.argv[2]
full_path = os.path.join(input_path, '*.xls*')
workbooks = glob.glob(full_path)
output_workbook = Workbook()
output_worksheet = output_workbook.add_sheet('sum_average_output')
all_data = []
sale_amount_index = 3
header = ['workbook', 'worksheet', 'worksheet_sum', 'worksheet_average', 'workbook_total', 'workbook_average']
all_data.append(header)
for input_file in workbooks:
	with open_workbook(input_file) as workbook:
		workbook_total_sales = []
		number_of_workbook = []
		workbook_output = []
		for worksheet in workbook.sheets():
			worksheet_list = []
			worksheet_sale_total = 0
			number_of_worksheet = 0
			worksheet_list.append(os.path.basename(input_file))
			worksheet_list.append(worksheet.name)
			for row_index in range(1, worksheet.nrows):
				try:
					sale_amount = float(str(worksheet.cell_value(row_index, sale_amount_index)).strip('$').replace(',', ''))
					worksheet_sale_total += sale_amount
					number_of_worksheet += 1
				except:
					worksheet_sale_total += 0
					number_of_worksheet += 0
			average_worksheet = '%.2f'%(worksheet_sale_total/number_of_worksheet)
			worksheet_list.append(worksheet_sale_total)
			worksheet_list.append(average_worksheet)
			workbook_total_sales.append(worksheet_sale_total)
			number_of_workbook.append(float(number_of_worksheet))
			workbook_output.append(worksheet_list)
		workbook_total = sum(workbook_total_sales)
		workbook_average = workbook_total/sum(number_of_workbook)
		for element_list in workbook_output:
			element_list.append(workbook_total)
			element_list.append(workbook_average)
		all_data.extend(workbook_output)
for list_index, output_list in enumerate(all_data):
	for element_index, element in enumerate(output_list):
		output_worksheet.write(list_index, element_index, element)
output_workbook.save(output_file)