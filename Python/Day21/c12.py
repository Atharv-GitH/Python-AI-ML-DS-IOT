

class Demo:

    def __new__(cls):
        print("in new")
        return super().__new__(cls)

    def __init__(self):
        print("in init")

    def instFun(self):
        print("in instance")

    @classmethod
    def classFun(cls):
        print("in class")

    @staticmethod
    def staticFun():
        print("in static")

#new calling
obj = type.__call__(Demo)
obj = Demo()
Demo()
obj = Demo.__new__(Demo)
print("***************")
obj.__init__()
Demo.__init__(obj)
Demo()
print("***************")
obj.instFun()
Demo.instFun(obj)
print("***************")
obj.classFun()  
Demo.classFun()
print("***************")
obj.staticFun()  
Demo.staticFun()

