

class Demo:

    instance = None

    def __new__(cls, *args, **kwargs):
        
        if cls.instance is None :
            print("Memory allocation")
            cls.instance = super().__new__(cls)
        
        return cls.instance

obj1 = Demo ()
obj2 = Demo ()

print(obj1)
print(obj2)

'''
Memory allocation
<__main__.Demo object at 0x711657425a90>
<__main__.Demo object at 0x711657425a90>
'''
