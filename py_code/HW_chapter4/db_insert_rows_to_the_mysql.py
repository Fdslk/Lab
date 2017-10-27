import MySQLdb
import sys
import csv
from datetime import date, datetime

input_file = sys.argv[1]
con = MySQLdb.connect(host='localhost', port=3306, user='root', db='db_test')
c = con.cursor()
insert_sql = "INSERT INTO supplier VALUES(%s, %s, %s, %s, %s);"
select_sql = "select * from supplier"
with open(input_file, 'r') as csv_in_file:
	filereader = csv.reader(csv_in_file)
	header = next(filereader, None)
	for row in filereader:
		data = []
		for col_index in range(len(header)):
			if col_index < 4:
				data.append(str(row[col_index]).lstrip('$').replace(',', '').strip())
			else:
				a_date = datetime.date(datetime.strptime(\
				str(row[col_index]), '%m/%d/%y'))
				a_date = a_date.strftime('%Y-%m-%d')
				data.append(insert_sql, a_date)
		print(data)
		c.execute(, data)
con.commit()
print("")
c.execute(select_sql)
rows = c.fetchall()
for row in rows:
	output = []
	for col_index in range(len(row)):
		output.append(row[col_index])
	print(output)
c.close()
con.close()
