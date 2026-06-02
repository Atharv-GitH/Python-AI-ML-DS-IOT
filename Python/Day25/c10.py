

from abc import abstractmethod, ABC

class Parent(ABC):
    
    def __init__(self):
        print("Parent Constructor")
    
    def career(self):
        print("Doctor")
    
    @abstractmethod
    def marry(self):
        pass

obj = Parent()

'''
TypeError: Can't instantiate abstract class Parent without an implementation for abstract method 'marry'
'''
