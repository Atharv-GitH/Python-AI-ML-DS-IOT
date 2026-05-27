

class Demo :

    def __init__(self):

        print("constructor")
        self.x = 10
        self.y = 20

    def fun(self):
        print("in fun")
        print(x)                # name error : do you mean self.x
        print(y)                # name error

obj = Demo()
obj.fun()
