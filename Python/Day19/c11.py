

class Demo :

    x = 10

    def __init__(self) :

        self.y = 20

    @classmethod
    def fun(cls):

        print("in class method")
        print(x)                    # name error : x is not defined
        print(y)                    # error

Demo.fun()
obj = Demo()
obj.fun()
