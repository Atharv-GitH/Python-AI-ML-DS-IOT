

class Demo :

    x = 10
    y = 20

    @classmethod
    def fun(cls):

        print("in class method")
        print(Demo.x)
        print(cls.y)

Demo.fun()
