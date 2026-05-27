

class Demo :

    x = 10
    y = 20

    def __init__(self):

        self.a = 50
        self.b = 60

    @classmethod
    def fun(cls):
        print("in class method")
        print(cls.x)              
        print(cls.y)

    def run(self):

        print("in instance method")
        print(self.a)
        print(self.b)

Demo.fun()
obj = Demo()

#obj.run() or ->
Demo.run(obj)
