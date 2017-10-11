import sys
import pandas as pd 

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_excel(input_file, 'january_2013')
data_frame_columns_name = data_frame.loc[:, ['Customer ID', 'Purchase Date']]
writer = pd.ExcelWriter(output_file)
data_frame_columns_name.to_excel(writer, sheet_name='jan_2013')
writer.save()