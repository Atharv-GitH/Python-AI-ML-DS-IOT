

from abc import ABC, abstractmethod

class Parent():

    def __init__(self):
        print("Parent constructor")

    @abstractmethod
    def fun (self):
        pass

class Child:
    pass

Parent()
Child()

print(type (Parent))            # <class 'type'>
print(type (Child))             # <class 'type'>
