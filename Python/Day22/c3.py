

class Demo:
    
    def __init__(self):
        print("Demo Constructor")
        self.x = 10
        self.y = 20
    
    def disData(self):
        print(self.x)
        print(self.y)

class Memo :
    
    def __init__(self):
        print("Memo Constructor")
    
    def memoFun(self):
        obj = Demo ()
        obj.disData()

obj = Memo ()
obj.memoFun()
