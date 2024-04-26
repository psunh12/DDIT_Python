import pymssql

# https://velog.io/@hkjs96/2020-11-25-python
conn = pymssql.connect(server="192.168.146.20", user="sa", password="python", database="python")
cur = conn.cursor()

cur.execute('select * from emp')
rows = cur.fetchall()
print(rows)

cur.close()
conn.close()
