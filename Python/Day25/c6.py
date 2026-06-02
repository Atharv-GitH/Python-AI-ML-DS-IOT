

class Parent :
    
    def __init__(self):
        print("Parent Constructor")
    
    def career(self):
        print("Doctor")

class Child (Parent):
    
    def __init__(self):
        super().__init__()
        print("Child Constructor")
    
    def career(self):
        print("Youtuber")

obj = Child()
obj.career()
