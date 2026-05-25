

class Demo:

    x = 10

    def __new__(cls):

        print("in new method")

        return object.__new__(cls)

    def __init__(self):

        print("in init : constructor")

    def disp(self):

        print("in disp")

obj = Demo()
#1.__new__(Demo)
#2.__init__(loc)

print(obj.x)

obj.disp()

print(type(Demo))
