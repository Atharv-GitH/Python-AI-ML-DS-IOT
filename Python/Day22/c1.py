

class Demo :
    
    def __init__(self):
        self.x = 10
        self.y = 20
    
    def disData(self):
        print(self.x)
        print(self.y)

class Memo :
    
    def __init__(self):
        print("Memo Constructor")
        self.demo = Demo()

obj = Memo ()
obj.demo.disData()
