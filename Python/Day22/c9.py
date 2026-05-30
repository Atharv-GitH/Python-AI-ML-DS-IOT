

class Demo :
    
    def __init__(self):
        print("Demo constructor")
        self.x = 10
        self.y = 20
    
    def dispDemo (self):
        print(self.x)
        print(self.y)

class DemoChild (Demo):
    
    def __init__(self):
        super().__init__()
        print("DemoChild constructor")

obj = DemoChild()
obj.dispDemo()
print(obj.__dict__)
