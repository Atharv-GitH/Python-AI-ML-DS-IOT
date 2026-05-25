

class Demo:

    #class variable
    x = 10

    def __new__(cls):

        print("in new method")

        return super().__new__(cls)

    def __init__(self):

        print("in init : constructor")

    def disp(self):

        print("in disp")

obj = Demo()

print(obj.x)

obj.disp()
