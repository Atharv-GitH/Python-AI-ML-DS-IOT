

class Demo:

    def __new__(cls):

        print("memory allocation")
        
        #return super().__new__(cls)        object is not created so no call to init
        
    def __init__(self):

        print("in constructor")

obj = Demo()

#obj = __new__(Demo)
#obj.__init__(obj)
