from xlrd import open_workbook
import sys
import pandas as pd
import MySQLdb
reload(sys)
sys.setdefaultencoding('utf-8')
input_file = sys.argv[1]
conn = MySQLdb.connect(host='localhost', user='user', db='db_test', port=3306)
c = conn.cursor()
create_sql = """create table if not exists interaction_rna_pro(Protein_No VARCHAR(20),
															RNA_No VARCHAR(20))"""
c.execute(create_sql)
conn.commit()
select_rna = "select * from rna_npinter where RNA_Name = %s"
select_pro = "select * from pro_npinter where Protein_name = %s"
insert_sql = "insert into interaction_rna_pro values(%s, %s)"
pro_data = []
interClass_index = 14
interLevel_index = 15
interClass = 'binding'
interLevel = 'RNA-Protein'
with open_workbook(input_file) as workbook:
	worksheet = workbook.sheet_by_name('NPInter')
	for row_index in range(1, worksheet.nrows):
		Class = worksheet.cell_value(row_index, interClass_index)
		Level = worksheet.cell_value(row_index, interLevel_index)
		pro_name = str(worksheet.cell_value(row_index, 7))
		row_list = []
		if  Class == interClass and Level == interLevel:
			if pro_name not in pro_data:
				pro_data.append(pro_name)
				c.execute(select_pro, pro_name)
				rows = c.fetchall()
				pro_no = rows[0][0]
				row_list.append(pro_no)
				rna_name = str(worksheet.cell_value(row_index, 4))
				c.execute(select_rna, rna_name)
				rows = c.fetchall()
				rna_no = rows[0][0]
				row_list.append(rna_no)
				c.execute(insert_sql, row_list)
			elif pro_name in pro_data:
				c.execute(select_pro, pro_name)
				rows = c.fetchall()
				pro_no = rows[0][0]
				row_list.append(pro_no)
				rna_name = str(worksheet.cell_value(row_index, 4))
				c.execute(select_rna, rna_name)
				rows = c.fetchall()
				rna_no = rows[0][0]
				row_list.append(rna_no)
				c.execute(insert_sql, row_list)
conn.commit()
c.close()
conn.close()