import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', charset='utf8',port=3305)

e_id = '4'
e_name = '6'
gen = '6'
addr = '6'
 
curs = conn.cursor()
sql = f"""
    update emp
    set
        e_name = '{e_name}',
        gen = '{gen}',
        addr = '{addr}'
    where
        e_id = '{e_id}'
"""
cnt = curs.execute(sql)
conn.commit()
print(cnt)
 
curs.close()
conn.close()