

class Demo:

    #class variable
    x = 10

    def __new__(cls):

        print("in new method")

        return object.__new__(cls)

    def __init__(self):

        print("in init : constructor")

Demo()              # internally calls  => __new__() & __init__()
