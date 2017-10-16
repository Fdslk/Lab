import sys
import csv
import sqlite3

input_file = sys.argv[1]
con = sqlite3.connect('sales.db')
c = con.cursor()
statement = "INSERT INTO sales VALUES(?, ?, ?, ?);"
select_sql = "SELECT * FROM sales;"
update_sql = "UPDATE sales SET amout=?, date=? WHERE customer=?;"
query = """CREATE TABLE IF NOT EXISTS sales
		  (customer VARCHAR(20),
		   product VARCHAR(40),
		   amout FLOAT,
		   date DATE);"""
c.execute(query)
con.commit()
data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
		('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
		('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
		('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]
c.executemany(statement, data)
con.commit()

file_reader = csv.reader(open(input_file, 'r'))
header = next(file_reader)
for row in file_reader:
	data = []
	for col_index in range(len(header)):
		data.append(row[col_index])
	c.execute(update_sql, data)
con.commit()

cursor = c.execute(select_sql)
rows = cursor.fetchall()
for row in rows:
	out_put = []
	for col_index in range(len(row)):
		out_put.append(row[col_index])
	print(out_put)