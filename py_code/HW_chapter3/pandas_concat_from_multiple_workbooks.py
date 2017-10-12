import pandas as pd
import glob
import os
import sys

input_path = sys.argv[1]
output_file = sys.argv[2]
full_path = os.path.join(input_path, '*.xls*')
workbooks = glob.glob(full_path)
data_frame = []
for workbook in workbooks:
	all_worksheets = pd.read_excel(workbook, sheetname=None)
	for worksheet_name, data in all_worksheets.items():
		data_frame.append(data)
all_data_concatenated = pd.concat(data_frame, axis=0)
writer = pd.ExcelWriter(output_file)
all_data_concatenated.to_excel(writer, sheet_name='output_file')
writer.save()