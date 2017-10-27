#encoding:utf-8
import sys
import glob
import os
from math import exp, log, sqrt
from datetime import date, time, datetime, timedelta
from operator import itemgetter

#input_file = sys.argv[1]
#filereader = open(input_file, 'r')
#for row in filereader:
#	print row.strip()
#filereader.close()

## 读取文件的新方法 使用with##
#input_file = sys.argv[1]
#with open(input_file, 'r') as filereader
#for row in filereader:
#	print("{}".format(row.strip())

inputPath = sys.argv[1]
for input_file in glob.glob(os.path.join(inputPath, '*.csv')):
	with open(input_file, 'r') as filereader:
		for row in filereader:
			print("{}".format(row.strip()))