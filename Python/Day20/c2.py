
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

Demo.clsFun()
