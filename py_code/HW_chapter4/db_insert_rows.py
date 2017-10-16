import sqlite3
import csv
import sys

input_file = sys.argv[1]
con = sqlite3.connect('Supplier.db')
c = con.cursor()
row_count = 0
create_table = """CREATE TABLE IF NOT EXISTS suppliers
					(Supplier_name VARCHAR(40),
					 Invoice_number VARCHAR(20),
					 Part_number VARCHAR(20),
					 Cost FLOAT,
					 Purchase_date DATE);"""
c.execute(create_table)
con.commit()

file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
header = next(file_reader, None)
for row in file_reader:
	data = []
	for col_index in range(len(header)):
		data.append(row[col_index])
	print(data)
	c.execute("INSERT INTO suppliers VALUES(?, ?, ?, ?, ?);", data)
con.commit()

output = c.execute("SELECT * FROM suppliers")
rows = output.fetchall()
for row in rows:
	output = []
	for col_index in range(len(row)):
		output.append(row[col_index])
	print(output)
	row_count += 1
print('Number of the data row:{0:d}'.format(row_count))

