

class Demo :

    x = 10

    @classmethod
    def fun(cls):

        print("in class method")
        print(Demo.x)               # cls.x
        print(x)

Demo.fun()
