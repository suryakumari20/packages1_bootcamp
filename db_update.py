import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')

query='''update participants set name='yash' where g_id=2016101'''
conn.execute(query)
print(conn.total_changes)
conn.commit()
conn.close()