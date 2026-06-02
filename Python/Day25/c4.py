

class Demo :
    
    def __init__(self):
        print("Demo Constructor")
    
    def disp(self, *args) :
        print("Second disp")

obj = Demo()
obj.disp(10)
obj.disp(20, 30)
