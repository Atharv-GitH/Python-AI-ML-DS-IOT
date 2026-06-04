

class Demo:

    demoInstance = None

    def __init__(self):
        print("Demo constructor")

    def __new__(cls, *args, **kwargs):
        print("Demo New memory")
        
        if cls.demoInstance is None:
            cls.demoInstance = super().__new__(cls)
        
        return cls.demoInstance

obj1 = Demo ()
obj2 = Demo ()

print(obj1 is obj2)

'''
Demo New memory
Demo constructor
Demo New memory
Demo constructor
True
'''
