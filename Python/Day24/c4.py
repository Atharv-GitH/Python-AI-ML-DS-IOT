

class Demo (object):
    
    def __init__(self):
        print("Demo constructor")
        super().__init__()

class A (Demo):
    
    def __init__(self):
        print("A constructor")
        super().__init__()

class B(Demo):
    
    def __init__(self):
        print("B constructor")
        super().__init__()

class C(A,B):
    
    def __init__(self):
        print("C constructor")
        super().__init__()

C()
