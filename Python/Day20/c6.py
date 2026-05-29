

class Demo :

    x = 10
    y = 20

    def __init__(self,a,b):

        print("constructor")
        self.a = a
        self.b = b

    @classmethod
    def clsFun(cls):
        
        print("in class method")
        print(cls.x)
        print(cls.y)
        print(cls.a)

    def instaFun(self):

        print("in instance method")
        print(self.a)
        print(self.b)

Demo.clsFun()
obj1 = Demo(50,60)
obj1.instaFun()
