

class Demo:

    def __init__(self):
        print("Demo Constructor")

    def disp(self, x):
        print("First disp")

    def disp(self, a, b):
        print("Second disp")

obj = Demo()
obj.disp(10)
obj.disp(20, 30)

'''
Demo Constructor
TypeError: Demo.disp() missing 1 required positional argument: 'b'
'''
