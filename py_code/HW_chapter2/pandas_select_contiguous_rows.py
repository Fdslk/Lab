import sys
import pandas as pd

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file, header=None)
print data_frame
data_frame = data_frame.drop([0,1,2,16,17,18])
print data_frame
data_frame.columns = data_frame.iloc[0] # 相当于把第三行设置为首行
data_frame = data_frame.reindex(data_frame.index.drop(3))# 在把原来的第三行删除
print data_frame
data_frame.to_csv(output_file)