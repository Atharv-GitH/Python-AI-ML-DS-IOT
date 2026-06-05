

class SingleTonMeta(type):

    instance = None

    def __call__(cls, *args, **kwargs):
        
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)
        
        return cls.instance

class Demo(metaclass = SingleTonMeta):
    
    def __init__(self):
        print("Constructor")

obj1 = Demo()
obj2 = Demo()

print(obj1)
print(obj2)

'''
Constructor
<__main__.Demo object at 0x7a00b8f8dd90>
<__main__.Demo object at 0x7a00b8f8dd90>
'''
