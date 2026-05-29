

class Demo:

    def __call__(self):
        print("in call")

    def __new__(cls):
        print("in new")
        return super().__new__(cls)
    
    def __init__(self):
        print("in init")

Demo()
obj = Demo()
obj()
