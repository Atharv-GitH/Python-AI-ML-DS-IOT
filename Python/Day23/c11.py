

class DemoChild1 :

    def __init__(self):
        print("DemoChild1 Constructor")

class DemoChild2 :
    
    def __init__(self):
        print("DemoChild2 Constructor")
        
class Demo (DemoChild2, DemoChild1):
    def __init__(self):
        super().__init__()
        print("Demo Constructor")

print(type.__dict__)
obj = Demo()
print(Demo.__mro__)
