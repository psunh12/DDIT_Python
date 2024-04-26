import pymssql

class DaoMem:
    def __init__(self):
        self.conn = pymssql.connect(server="192.168.146.20", user="sa", password="python", database="python")
        self.curs = self.conn.cursor(as_dict=True)
    
    def selectList(self):
        sql = "select * from mem"
        self.curs.execute(sql)
        
        list = self.curs.fetchall()
        return list
  
    def select(self,m_id):
        sql = f"""
            select 
                m_id,m_name,tel,email
            from 
                mem
            where
                m_id = '{m_id}'
        """
        self.curs.execute(sql)
        
        vo = self.curs.fetchone()
        return vo
  
    def insert(self,m_id,m_name,tel,email):
        sql = f"""
            insert into mem
            (m_id,m_name,tel,email)
            values 
            ('{m_id}','{m_name}','{tel}','{email}')
        """
        self.curs.execute(sql)
        self.conn.commit()
        return self.curs.rowcount
    
    def update(self,m_id,m_name,tel,email):
        sql = f"""
            update mem
            set
                m_name = '{m_name}',
                tel = '{tel}',
                email = '{email}'
            where
                m_id = '{m_id}'
        """
        self.curs.execute(sql)
        self.conn.commit()
        return self.curs.rowcount
    
    def delete(self,m_id):
        sql = f"""
            delete from mem
            where
                m_id = '{m_id}'
        """
        self.curs.execute(sql)
        self.conn.commit()
        return self.curs.rowcount
    
    def __del__(self):
        self.curs.close()
        self.conn.close()
        
if __name__ == '__main__':
    de = DaoMem()
    cnt = de.delete('3')
    print(cnt)
    
    
    
    
    
    
    
    