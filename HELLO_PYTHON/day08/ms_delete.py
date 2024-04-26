import pymssql

# https://velog.io/@hkjs96/2020-11-25-python
conn = pymssql.connect(server="192.168.146.20", user="sa", password="python", database="python")
cur = conn.cursor()

e_id  = 3

sql = f"""
    delete from emp
    where
        e_id = '{e_id}'
"""
cur.execute(sql)   
print(cur.rowcount)
conn.commit()

cur.close()
conn.close()
