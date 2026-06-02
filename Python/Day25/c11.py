

from abc import abstractmethod, ABC

class Parent(ABC):
    
    def __init__(self):
        print("Parent Constructor")

    
    def career(self):
        print("Doctor")

    @abstractmethod
    def marry(self):
        pass

class Child(Parent):
    
    def __init__(self):
        super().__init__()
        print("Child Constructor")

    def marry(self):
        print("Disha Patni")

obj = Child()
obj.career()
obj.marry()
