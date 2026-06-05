

class Demo:

    def __demo__(self):
        print("Constructor")

    def __new__(cls, *args, **kwrgs):
        print("Memory Allocation")
        return super().__new__(cls)

    def __call__(cls, *args, **kwrgs):
        print("Call Method")

obj1 = Demo()
print(obj1)
obj1()

'''
Memory Allocation
<__main__.Demo object at 0x7406107d5a30>
Call Method
'''
