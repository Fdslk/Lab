import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, sheetname=None)
row_output = []
for worksheet_name, data in data_frame.items():
	row_output.append(data[data['Sale Amount'].astype(float) > 2000.0])
filter_rows = pd.concat(row_output, axis=0)
writer = pd.ExcelWriter(output_file)
filter_rows.to_excel(writer, sheet_name='sale_amount')
writer.save()
