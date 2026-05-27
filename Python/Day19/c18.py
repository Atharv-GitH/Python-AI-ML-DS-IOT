

class Demo :

    x = 10
    y = 20

    @classmethod
    def fun(cls):

        print("in class method")
        print(cls.x)
        print(Demo.y)
        print(x)            # error

Demo.fun()

