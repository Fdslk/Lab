import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013')
data_frame_by_columns = data_frame.iloc[:, [1, 4]]
writer = pd.ExcelWriter(output_file)
data_frame_by_columns.to_excel(writer, sheet_name='january_2013')
writer.save()