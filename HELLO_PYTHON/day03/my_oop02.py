class Car:
    def __init__(self):
        self.speed = 0
        print("생성자")
        
    def excel(self,strength):
        self.speed += strength
        
    def __del__(self):
        print("소멸자")
        
    def __str__(self):
        return "[speed]:"+str(self.speed)

if __name__ == '__main__':   
    c = Car()
    print(c)
    print("speed2:",c.speed)
    c.excel(30)
    print("speed2:",c.speed)
    print(c)
    