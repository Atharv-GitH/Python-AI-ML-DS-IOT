

class Demo:

    def __new__(cls):

        print("memory allocation")
        
        return super().__new__(cls)

    def __init__(self):

        print("constructor")

obj = Demo()

#obj = __new__(Demo)
#__init__(obj)
