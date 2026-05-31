

class DemoChild1 :

    def __init__(self):
        super().__init__()
        print("DemoChild1 Constructor")

class DemoChild2 :

    def __init__(self): 
        super().__init__()
        print("DemoChild2 Constructor")

class Demo (DemoChild1, DemoChild2):

    def __init__(self):
        super().__init__()
        print("Demo Constructor")

obj = Demo()
print(Demo.__mro__)
