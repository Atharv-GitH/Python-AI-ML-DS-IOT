

class Demo:
    
    def __init__(self):
        print("Demo")
    
    def disp(self):
        print("Demo display")

class X (Demo):
    
    def __init__(self):
        print("X")

class Y (Demo):
    
    def __init__(self):
        print("Y")

class Z(X, Y):
    
    def __init__(self) :
        print("Z")

print(Z.__mro__)            # (Z,X,Y,Demo,object)
obj = Z()
obj.disp()
