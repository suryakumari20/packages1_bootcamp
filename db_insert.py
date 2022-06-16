import sqlite3
conn=sqlite3.connect('BOOTCAMP.db')
conn.execute("insert into participants values(2216103,'ram charan teja','cseai','Btech')")
conn.execute("insert into participants values(2216101,'yashe','cseai','Btech')")
conn.execute("insert into participants values(2216102,'akshay rao','cseai','Btech')")
conn.commit()
conn.close()