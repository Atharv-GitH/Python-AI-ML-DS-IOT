
class Demo:

    def __init__(self):
        print("Demo constructor")
        self.x = 10

class DemoChild1(Demo):
    
    def __init__(self):
        super().__init__()
        print("DemoChild1 Constructor")
        self.y = 20

class DemoChild2(DemoChild1):
    
    def __init__(self):
        super().__init__()
        print("DemoChild2 Constructor")
        self.z = 30

obj = DemoChild2()
print(obj.x)
print(obj.y)
print(obj.z)
