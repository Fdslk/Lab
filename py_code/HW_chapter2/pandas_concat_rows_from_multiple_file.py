import pandas as pd
import sys
import os
import glob

input_path = sys.argv[1]
output_file = sys.argv[2]

files = glob.glob(os.path.join(input_path, 'sales_*'))
all_data_frame = []

for file in files:
	data_frame = pd.read_csv(file, index_col=None)
	all_data_frame.append(data_frame)
data_frame_concat = pd.concat(all_data_frame, axis=0, ignore_index=True)
data_frame_concat.to_csv(output_file, index=False)