

class Demo:

    def __new__(cls):

        print("memory allocation")
        
        super().__new__(cls)            # obj is created but we have not returned so no call to init
        
    def __init__(self):

        print("in constructor")

obj = Demo()

#obj = __new__(Demo)
#obj.__init__(obj)
