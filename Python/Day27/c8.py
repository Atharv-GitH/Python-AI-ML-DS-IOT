

class Demo:
    
    demoInstance = None

    def __new__(cls, *args, **kwargs):
        
        if cls.demoInstance is None:
            cls.demoInstance = super().__new__(cls)
        
        return cls.demoInstance

obj1 = Demo ()
obj2 = Demo ()
obj3 = Demo ()

print(obj1 is obj2)
print(obj1 is obj3)

'''
True
True
'''
