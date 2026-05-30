

class Demo :

    z = 30
    
    def __init__(self):
        print("Demo constructor")
        self.x = 10
        self.y = 20
    
    def dispDemo(self):
        print(self.x)
        print(self.y)

class DemoChild (Demo):
    
    def __init__(self):
        super().__init__()
        print("DemoChild constructor")

obj = DemoChild()
obj.dispDemo()
print(obj.z)
print(Demo.__dict__)
print(DemoChild.__dict__)
print(obj.__dict__)
