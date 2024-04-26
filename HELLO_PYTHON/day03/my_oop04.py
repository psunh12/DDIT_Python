class Musk:
    def __init__(self):
        self.cnt_stock = 100
    def straw(self):
        self.cnt_stock += 1
    
class JDragon:
    def __init__(self):
        self.money = 400
    def buyPhone(self,cnt):
        self.money += cnt
        
class SugarBoy:
    def __init__(self):
        self.cnt_chain = 1200
    def paper(self,cnt):
        self.cnt_chain +=1
        
class Chowon(Musk,JDragon,SugarBoy):
    def __init__(self):     
        Musk.__init__(self)
        JDragon.__init__(self)
        SugarBoy.__init__(self)



if __name__ == '__main__':
    cw = Chowon()
    print("cnt_stock:",cw.cnt_stock)
    print("money:",cw.money)
    print("cnt_chain:",cw.cnt_chain)
    cw.buyPhone(1)
    cw.paper(1)
    cw.straw()
    print("cnt_stock:",cw.cnt_stock)
    print("money:",cw.money)
    print("cnt_chain:",cw.cnt_chain)
    
    
    
    