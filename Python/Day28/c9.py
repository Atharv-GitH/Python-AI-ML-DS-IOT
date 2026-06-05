

class Demo:

    instance = None
    initialized = False

    def __init__(self):
        
        if not self.initialized:
            print("Constructor")
            self.initialized = True

    def __new__(cls, *args, **kwargs):
        
        if cls.instance is None :
            print("Memory allocation")
            cls.instance = super().__new__(cls)
        
        return cls.instance

obj1 = Demo()
obj2 = Demo ()

print(obj1)
print(obj2)

'''
Memory allocation
Constructor
<__main__.Demo object at 0x763c7918dd00>
<__main__.Demo object at 0x763c7918dd00>
'''
