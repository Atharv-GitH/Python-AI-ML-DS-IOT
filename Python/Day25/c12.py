

from abc import ABC

class Parent(ABC):
    
    def __init__(self):
        print("Parent Constructor")

class Parent2():
    
    def __init__(self):
        print("Parent2 Constructor")

print(type(Parent))             # <class 'abc.ABCMeta'>
print(type(Parent2))            # <class 'type'>
