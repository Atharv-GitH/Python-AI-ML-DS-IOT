

class Demo :
    
    def __init__(self):
        print("Demo constructor")
    
    def dispDemo(self):
        print("Instance method")

class DemoChild (Demo):
    
    def __init__(self) :
        print("DemoChild constructor")

obj = DemoChild()
obj.dispDemo()
