

class Demo :

    a = 50

    def __init__(self,x,y) :

        print("constructor")
        self.x = x 
        self.y = y

    @classmethod
    def clsFun(cls):

        print("in class method")

    def instaFun(self):

        print("in instance method")

Demo.clsFun()
Demo.instaFun()                         # error
