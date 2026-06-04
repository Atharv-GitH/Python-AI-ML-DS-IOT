

class Demo:

    def __init__(self):
        print("In Constructor")

    def __new__(cls, *args, **kwargs):
        print("In memory allocation")
        return super().__new__(cls)

    def __call__(self):
        print("In call method")

obj1 = Demo()
obj1()

'''
In memory allocation
In Constructor
In call method
'''
