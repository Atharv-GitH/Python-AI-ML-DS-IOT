

class Demo:

    def __init__(self):
        print("Constructor")

    def __new__(cls):
        print("Memory allocation")
        return super().__new__(cls)

obj1 = Demo()
obj2 = Demo()

'''
Memory allocation
Constructor
Memory allocation
Constructor
'''
