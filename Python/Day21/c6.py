
class Demo:

    z = 30

    def __init__(self):
        self.x = 10
        self.y = 20

    def instFun(self):
        print("instance method")

    @classmethod
    def clsFun(cls):
        print("class method")

    @staticmethod
    def staticFun():
        print("static method")

obj = Demo()
Demo.instFun()              # TypeError: Demo.instFun() missing 1 required positional argument: 'self'
