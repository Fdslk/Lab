import sys
import glob
from xlrd import open_workbook
import os
input_path = sys.argv[1]
full_path = os.path.join(input_path, '*.xls*')
workbook_count = 0
workbooks = glob.glob(full_path)
for input_file in workbooks:
	workbook = open_workbook(input_file)
	print('worksheet_name:{0:s}\t'.format(os.path.basename(input_file)))
	print('number of the worksheet:{0:d}\t'.format(workbook.nsheets))
	for worksheet in workbook.sheets():
		print('row:{0:d}\t columns:{1:d}\n'.format(worksheet.nrows, worksheet.ncols))
	workbook_count += 1
print('number of the workbook:{0:d}\t'.format(workbook_count))