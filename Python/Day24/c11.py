

class Demo:
    
    def __init__(self):
        print("Demo")
    
    def disp(self):
        print("Demo display")

class X(Demo):
    
    def __init__(self):
        print("X")

class Y(Demo):
    
    def __init__(self):
        print("Y")

class Z(Demo, X, Y):
    
    def __init__(self):
        print("Z")

print(Z.__mro__)
obj = Z()
obj.disp()

# TypeError: Cannot create a consistent method resolution order (MRO) for bases Demo, X, Y
