import cx_Oracle

conn = cx_Oracle.connect('python/python@localhost:1521/xe')
cur = conn.cursor()
e_id  = 5
e_name  = 5
gen  = 5
addr  = 5

sql = f"""
    insert into emp 
    (e_id,e_name,gen,addr)
    values 
    ('{e_id}','{e_name}','{gen}','{addr}')
"""
cur.execute(sql)   
print(cur.rowcount)

cur.close()
conn.commit()
conn.close()