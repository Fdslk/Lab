import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_columns_by_name = data_frame.loc[:,['Invoice Number', 'Purchase Date']]
data_frame_columns_by_name.to_csv(output_file)