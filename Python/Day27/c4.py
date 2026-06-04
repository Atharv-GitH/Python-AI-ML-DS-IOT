

class Demo:

    def __init__(self):
        print("Demo constructor")

    def __new__(cls, *args, **kwargs):
        print("Demo New memory")
        #return super().__new__(cls)

obj1 = Demo ()
obj2 = Demo ()

print(obj1 is obj2)

'''
Demo New memory
Demo New memory
True
'''
