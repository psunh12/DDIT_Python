import pymysql
 
conn = pymysql.connect(host='localhost', user='root', password='python',
                       db='python', charset='utf8',port=3305)

e_id = '4'
 
curs = conn.cursor()
sql = f"""
    delete from emp
    where
        e_id = '{e_id}'
"""
cnt = curs.execute(sql)
conn.commit()
print(cnt)
 
curs.close()
conn.close()