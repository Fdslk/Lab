from xlrd import open_workbook
import sys
import pandas as pd
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')
input_file = sys.argv[1]
conn = MySQLdb.connect(host='localhost', user='user', db='db_test', port=3306)
c = conn.cursor()
create_sql = """create table if not exists Pro_NPInter(Num VARCHAR(10),
											Protein_Name Varchar(40));"""
insert_sql = "insert into Pro_NPInter values(%s, %s)"
interClass_index = 14
interLevel_index = 15
interClass = 'binding'
interLevel = 'RNA-Protein'
c.execute(create_sql)
conn.commit()
data = []
rna_no = 0
with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('NPInter')
	for row_index in range(1, worksheet.nrows):
		Class = worksheet.cell_value(row_index, interClass_index)
		Level = worksheet.cell_value(row_index, interLevel_index)
		row_list = []
		if  Class == interClass and Level == interLevel:
			if str(worksheet.cell_value(row_index, 7)) not in data:
				data.append(str(worksheet.cell_value(row_index, 7)))
				rna_no += 1
				row_list.append(rna_no)
				row_list.append(str(worksheet.cell_value(row_index, 7)))
				c.execute(insert_sql, row_list)
conn.commit()
c.close()
conn.close()