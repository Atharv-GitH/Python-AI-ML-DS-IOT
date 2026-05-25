

class Demo:

    def __new__(cls):

        print("memory allocation")

        return object.__new__(cls)

    def __init__(self):

        print(self)

        print("in init : constructor")

    def disp(self):

        print("")

obj = Demo()
#1.__new__(Demo)
#2.__init__(loc)

print(obj)
