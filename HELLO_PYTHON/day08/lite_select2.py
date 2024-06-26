import sqlite3

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


conn = sqlite3.connect("python.db")
conn.row_factory = dict_factory
 
cur = conn.cursor()
cur.execute("select * from emp")

rows = cur.fetchall()
for row in rows:
    print(row)
 
cur.close()
conn.close()