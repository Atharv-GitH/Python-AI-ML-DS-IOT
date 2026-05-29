
class Demo:

    z = 30

    def __init__(self):
        self.x = 10
        self.y = 20
        print("init x : ",self.x)
        print("init y : ",self.y)

    def instFun(self):
        print("instance method")
        i = 100
        print("instance : ",i)

    @classmethod
    def clsFun(cls):
        print("class method")
        c = 100
        print("class z : ",cls.z)
        print("class c : ",c)
        
    @staticmethod
    def staticFun():
        print("static method")
        s = 1
        print("Static : ",s)

obj = Demo()
print("\n")
obj.instFun()
Demo.instFun(obj)
print("\n")
Demo.clsFun()
obj.clsFun()
print("\n")
Demo.staticFun()
obj.staticFun()
