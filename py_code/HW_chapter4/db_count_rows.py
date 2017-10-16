import sqlite3
con = sqlite3.connect('Suppliers.db')
query = """CREATE TABLE sales
			(customer VARCHAR(20),
			product VARCHAR(40),
			amount FLOAT,
			date DATE);"""
con.execute(query)
con.commit()

# Insert a few rows of data into the table
data = [('Richard Lucas', 'Notepad', 2.50, '2014-01-02'),
		('Jenny Kim', 'Binder', 4.15, '2014-01-15'),
		('Svetlana Crow', 'Printer', 155.75, '2014-02-03'),
		('Stephen Randolph', 'Computer', 679.40, '2014-02-20')]
statement = "INSERT INTO sales VALUES(?, ?, ?, ?)"
con.executemany(statement, data)
con.commit()

cursor = con.execute("select * from sales")
rows = cursor.fetchall()

row_counter = 0
for row in rows:
	print(row)
	row_counter += 1
print('Number of the row:{0:d}'.format(row_counter))