

class Demo:

    def __init__(self):
        print("Constructor")

    def __new__(cls, *args, **kwargs):
        print("Memory allocation")
        return super().__new__(cls)

    def __call__(cls, *args, **kwargs):
        print("Call method")

obj1 = Demo()
print(obj1)
obj1()

'''
Memory allocation
Constructor
<__main__.Demo object at 0x735c80829a00>
Call method
'''
