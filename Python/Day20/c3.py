
class Demo :

    x = 10
    y = 20

    def __init__(self,a,b):

        print("constructor")

        self.a = a
        self.b = b

    @classmethod
    def clsFun(cls):

        print("In class method")
        print(cls.x)
        print(cls.y)

    def instaFun(self):

        print("In instance method")
        print(self.a)
        print(self.b)

obj1 = Demo(50,60)
obj1.instaFun()
