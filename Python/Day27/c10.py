

class Demo:
    
    demoInstance = 0

    def __new__(cls, *args, **kwargs):
        
        if cls.demoInstance < 2:
            cls.demoInstance = cls.demoInstance + 1
            return super().__new__(cls)
        
        else:
            print("Object Restricted")

obj1 = Demo ()              # 1000
obj2 = Demo ()              # 2000
obj3 = Demo()               # None

print(obj1)
print(obj2)
print(obj3)

print(obj1 is obj2)         # False
print(obj2 is obj3)         # False

'''
Object Restricted
<__main__.Demo object at 0x796471089df0>
<__main__.Demo object at 0x796471089e20>
None
False
False
'''
