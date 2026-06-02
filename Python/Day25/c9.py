

from abc import abstractmethod, ABC

class Parent():
    
    def __init__(self):
        print("Parent Constructor")
    
    def career(self):
        print("Doctor")
    
    @abstractmethod
    def marry(self):
        pass

obj = Parent()
