import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')
cur = conn.cursor()
e_id  = 5
e_name  = 6
gen  = 6
addr  = 6

sql = f"""
    update emp
    set
        e_name = '{e_name}',
        gen = '{gen}',
        addr = '{addr}'
    where
        e_id = '{e_id}'
"""
cur.execute(sql)   
print(cur.rowcount)

cur.close()
conn.commit()
conn.close()