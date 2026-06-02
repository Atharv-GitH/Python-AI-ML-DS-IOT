

class Parent :
    
    def __init__(self):
        print("Parent Constructor")
    
    def career (self, x):
        print("Doctor")

class Child (Parent):
    
    def __init__(self):
        super().__init__()
        print("Child Constructor")
    
    def career (self, a, b):
        print("Youtuber")
        super().career (10)

obj = Child()
obj.career (20, 30)
