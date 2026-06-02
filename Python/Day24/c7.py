

class Demo:

    def __init__(self):
        print("Demo Constructor")
        super().__init__()

class A (Demo):
    
    def __init__(self):
        print("A Constructor")
        super().__init__()

class B (Demo):
    
    def __init__(delf):
        print("B Constructor")
        super().__init__()

class C(Demo):
    
    def __init__(delf):
        print("C Constructor")
        super().__init__()

class X(A,B):
    
    def __init__(self):
        print("X Constructor")
        super().__init__()

class Y(B,C):
    
    def __init__(self):
        print("Y Constructor")
        super().__init__()

class Z(X,Y):

    def __init__(self):
        print("Z constructor")
        super().__init__()

#Z()
print(Z.__mro__)

