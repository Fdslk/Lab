import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
important_date = ['01/24/2013', '01/31/2013']
data_frame = pd.read_excel(input_file, 'january_2013')
data_frame_meet_condition = data_frame[data_frame['Purchase Date'].isin(important_date)]
writer = pd.ExcelWriter(output_file)
data_frame_meet_condition.to_excel(writer, sheet_name='jan_13_output')
writer.save()

