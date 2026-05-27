

class Demo :

    def __init__(self):

        print("constructor")
        self.x = 10
        self.y = 20

    def fun(self):
        print("in fun")
        print(self.x)              
        print(self.y)

obj = Demo()
obj.fun()  
#Demo.fun(obj)
