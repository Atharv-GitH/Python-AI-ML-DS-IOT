

class Demo :
    
    def __init__(self):
        print("Demo Constructor")
    
    def disp(self, a, b) :
        print("First disp")
    
    def disp(self, x) :
        print("Second disp")

obj = Demo()
obj.disp(10)
obj.disp(20, 30)

'''
Demo Constructor
Second disp
TypeError: Demo.disp() takes 2 positional arguments but 3 were given
'''
