

class Demo:

    def __demo__(self):
        print("Constructor")

    def __new__(cls, *args, **kwrgs):
        print("Memory Allocation")
        return super().__new__(cls)

obj1 = Demo()
print(obj1)
obj1()

'''
Memory Allocation
<__main__.Demo object at 0x7b56114dfc50>
TypeError: 'Demo' object is not callable
'''
