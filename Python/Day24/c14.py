

class Demo:
    
    def __init__(self):
        self.x = 10
        print("Demo Constructor")

class A(Demo):
    
    def __init__(self):
        print("A Constructor")
        super().__init__()

class B(Demo):
    
    def __init__(self):
        print("B Constructor")
        super().__init__()

class C(Demo):
    
    def __init__(self):
        print("C Constructor")
        super().__init__()

class X(A, B, C):

    def __init__(self):
        print("X Constructor")
        super().__init__()

class Y(A, B, C):

    def __init__(self):
        print("Y Constructor")
        super().__init__()

class Z(X,Y):

    def __init__(self):
        print("Z Constructor")
        super().__init__()

obj = Z()
print(Z.__mro__)
print(obj.x)
