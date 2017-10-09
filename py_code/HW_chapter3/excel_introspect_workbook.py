import sys
from xlrd import open_workbook

input_file = sys.argv[1]

workbook = open_workbook(input_file)
print(workbook)
print("Number of worksheets:", workbook.nsheets)
for worksheet in workbook.sheets():
	print(worksheet)
	print("worksheet name:", worksheet.name, "\tRows:",\
			worksheet.nrows, "\tColumns:", worksheet.ncols)