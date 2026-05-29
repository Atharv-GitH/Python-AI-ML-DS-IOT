

class Demo :

    x = 10

    def __init__(self) :

        self.y = 20

    @staticmethod
    def add(a,b):

        print("Add : ",a+b)
        print(x)
        print(y)

Demo.add(10,20)
obj1 = Demo()
obj1.add(50,60)
