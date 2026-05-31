

class Demo :

    x = 10
    
    def __init__(self):
        print("Demo Constructor")
        self.y = 20
        self.z = 30
    
    def disp(self):
        print("In display")
        print(self.x)
        print(self.y)       #AttributeError: 'DemoChild' object has no attribute 'y'
        print(self.z)

class DemoChild (Demo):
    
    def __init__(self):
        #super().__init__()
        print("DemoChild Constructor")
        
obj1 = Demo()
obj1.disp()
obj2 = DemoChild()
obj2.disp()
