

class Demo:

    instance = None

    def __init__(self):
        print("Constructor")

    def __new__(cls, *args, **kwargs):
        
        if cls.instance is None :
            print("Memory allocation")
            cls.instance = super().__new__(cls)
        
        return cls.instance

obj1 = Demo ()
obj2 = Demo()

print(obj1)
print(obj2)

'''
Memory allocation
Constructor
Constructor
<__main__.Demo object at 0x775771089be0>
<__main__.Demo object at 0x775771089be0>
'''
