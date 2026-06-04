

from abc import ABC, abstractmethod

class Parent(ABC):

    def __init__(self):
        print("Parent Constructor")

    @abstractmethod
    def fun(self):
        pass

obj = Parent()

'''
TypeError: Can't instantiate abstract class Parent without an implementation for abstract method 'fun'
'''

