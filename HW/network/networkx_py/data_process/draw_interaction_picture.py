import networkx as nx
import matplotlib.pyplot as plt
import MySQLdb
from datetime import datetime
conn = MySQLdb.connect(host='localhost', user='user', db='db_test', port=3306)
c = conn.cursor()
select_sql = "select * from interaction_rna_pro"
c.execute(select_sql)
rows = c.fetchall()
data = []
G = nx.Graph()
starttime = datetime.now()
for row in rows:
	data.append(row)
print(data)
G.add_edges_from(data)
nx.draw(G)
plt.show()
endtime = datetime.now()
diff = (endtime - starttime).seconds
print('total time:{0:d}s'.format(diff))
c.close()
conn.close()