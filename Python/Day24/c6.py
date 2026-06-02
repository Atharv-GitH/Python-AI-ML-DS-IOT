

class Demo(object):
    
    def __init__(self):
        self.x = 20
        print("Demo constructor")
        super().__init__()

    def disp(self):
        print("Demo disp")

class A (Demo):
    
    def __init__(self):
        print("A constructor")
        super().__init__()

class B (Demo):
    
    def __init__(self):
        print("B constructor")
        super().__init__()

class C(A,B):
    
    def __init__(self):
        print("C constructor")
        super().__init__()

C()
print(object.__mro__)
print(Demo.__mro__)
print(A.__mro__)
print(B.__mro__)
print(C.__mro__)
