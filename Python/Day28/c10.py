

class SingleTonMeta (type):

    instance = None

    def __call__(cls, *args, **kwargs):
        
        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)
        
        return cls.instance

class Demo:
    
    def __init__(self):
        print("Constructor")

obj1 = Demo()
obj2 = Demo()

print(obj1)
print(obj2)

'''
Constructor
Constructor
<__main__.Demo object at 0x74e05f52db80>
<__main__.Demo object at 0x74e05f52dcd0>
'''
