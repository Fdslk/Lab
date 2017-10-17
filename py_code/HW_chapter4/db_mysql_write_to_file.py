import csv
import sys
import MySQLdb

output_file = sys.argv[1]
conn = MySQLdb.connect(host='localhost', user='root', db='db_test', port=3306)
c = conn.cursor()
csv_out_file = open(output_file, 'w')
filewriter = csv.writer(csv_out_file)
select_sql = "select * from supplier where Cost > 700.0"
csv_header = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
filewriter.writerow(csv_header)
c.execute(select_sql)
rows = c.fetchall()
for row in rows:
	filewriter.writerow(row)
