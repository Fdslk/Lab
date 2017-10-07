import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame['Cost'] = data_frame['Cost'].str.strip('$').astype(float)
data_frame_column_by_index = data_frame.iloc[:, [0, 3]]
data_frame_meet_condition = data_frame_column_by_index.loc[data_frame_column_by_index[\
'Cost'] <= 500.0, :]
data_frame_meet_condition.to_csv(output_file, index=False)