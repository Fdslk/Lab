import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
threshold = 1900.0
my_sheet = [0,1]
row_list = []
data_frame = pd.read_excel(input_file, sheetname=my_sheet)
for worksheet_name, data in data_frame.items():
	row_list.append(data[data['Sale Amount'].astype(float) > threshold])
filtered_row = pd.concat(row_list, axis=0)
writer = pd.ExcelWriter(output_file)
filtered_row.to_excel(writer, sheet_name='set_of_worksheets')
writer.save()