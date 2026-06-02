

class A(object):
    
    def __init__(self):
        print("A constructor")
        super().__init__()

class B(object):
    
    def __init__(self):
        print("B constructor")

class C(A,B):
    
    def __init__(self):
        print("C constructor")
        super().__init__()

C()
