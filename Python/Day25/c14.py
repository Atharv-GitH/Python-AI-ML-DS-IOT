

from abc import ABCMeta

class Parent1(metaclass = ABCMeta):
    
    def __init__(self):
        print("Parent1 Constructor")

class Parent2():
    
    def __init__(self):
        print("Parent2 Constructor")

Parent1()
Parent2()

print(type(Parent1))
print(type(Parent2))
