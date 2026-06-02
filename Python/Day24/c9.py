

class Demo :
    
    def __init__(self):
        print("Demo")

class X(Demo):
    
    def __init__(self):
        print("X")

class Y(Demo):
    
    def __init__(self) :
        print("Y")

class Z(X, Y):
    
    def __init__(self):
        print("Z")

print(Z.__mro__)
