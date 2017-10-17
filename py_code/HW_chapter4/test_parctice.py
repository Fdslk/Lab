import sys
import csv
import MySQLdb
from xlrd import open_workbook
from datetime import datetime, date
reload(sys)
sys.setdefaultencoding('utf-8')
input_file = sys.argv[1]
conn = MySQLdb.connect(host='localhost', user='user', db='db_test', port=3306)
c = conn.cursor()
create_sql = """create table if not exists NPInter(
				interID VARCHAR(40),
				ncID VARCHAR(20),
				ncType VARCHAR(40),
				ncIdentifier VARCHAR(40),
				ncName VARCHAR(30),
				ParternID VARCHAR(30),
				prType VARCHAR(40),
				prIdentifier VARCHAR(40),
				InteractionPartner VARCHAR(40),
				interDescription VARCHAR(100),
				experiment VARCHAR(100),
				pubmed VARCHAR(30));"""
insert_sql = "insert into NPInter values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
interClass_index = 14
interLevel_index = 15
interClass = 'binding'
interLevel = 'RNA-Protein'
c.execute(create_sql)
conn.commit()
csv_in_file = open(input_file, 'r')
filereader = csv.reader(csv_in_file)
header = next(filereader, None)
starttime = datetime.now()
with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('NPInter')
	for row_index in range(1, worksheet.nrows):
		data = []
		Class = worksheet.cell_value(row_index, interClass_index)
		Level = worksheet.cell_value(row_index, interLevel_index)
		if  Class == interClass and Level == interLevel:
			for col_index in range(0, 12):
				data_cell = str(worksheet.cell_value(row_index, col_index))
				data.append(data_cell)
			print(data)
			c.execute(insert_sql, data)
conn.commit()
endtime = datetime.now()
print(endtime-starttime).seconds
c.close()
conn.close()
		
