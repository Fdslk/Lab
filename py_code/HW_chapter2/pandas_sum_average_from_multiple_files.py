import os
import sys
import glob
import pandas as pd

input_path = sys.argv[1]
output_file = sys.argv[2]

files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frame = []
for file in files:
	data_frame = pd.read_csv(file, index_col=None)
	total_cost = pd.DataFrame([float(str(value).strip('$').replace(',', ''))\
				 for value in data_frame.loc[:, 'Sale Amount']]).sum()
	average_cost = pd.DataFrame([float(str(value).strip('$').replace(',', ''))
				 for value in data_frame.loc[:, 'Sale Amount']]).mean()
	data = {'file name':os.path.basename(file),
			'total_sales':total_cost,
			'average_sales':average_cost}
	all_data_frame.append(pd.DataFrame(data, \
	columns=['file name', 'total_sales', 'average_sales']))
data_frame_concat = pd.concat(all_data_frame, axis=0, ignore_index=True)
data_frame_concat.to_csv(output_file)