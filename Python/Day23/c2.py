

class Demo:

    x = 10
    
    def __init__(self):
        print("Demo Constructor")
        self.y = 20
        self.z = 30
    
    def disp(self):
        print("In display")
        print(self.x)
        print(self.y)
        print(self.z)

class DemoChild (Demo):
    
    def __init__(self):
        super().__init__()
        print("DemoChild Constructor")

print(Demo.__dict__)
obj1 = Demo ()
print(obj1.__dict__)

