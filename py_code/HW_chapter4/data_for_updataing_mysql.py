import sys
import csv
import MySQLdb

input_file = sys.argv[1]
conn = MySQLdb.connect(host='localhost', user='root', db='db_test', port=3306)
c = conn.cursor()
update_sql = "update supplier set Cost=%s, Purchase_Date=%s where Supplier_Name=%s"
select_sql = "select * from supplier"
csv_in_file = open(input_file, 'r')
filereader = csv.reader(csv_in_file)
header = next(filereader, None)
for row in filereader:
	data = []
	for col_index in range(len(header)):
		data.append(str(row[col_index]).strip())
	c.execute(update_sql, data)
conn.commit()

c.execute(select_sql)
rows = c.fetchall()
for row in rows:
	out_put = []
	for col_index in range(len(row)):
		out_put.append(row[col_index])
	print(out_put)