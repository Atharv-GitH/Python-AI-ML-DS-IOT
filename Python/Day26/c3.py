

from abc import ABC, abstractmethod

class Parent(ABC):

    def __init__(self):
        print("Parent Constructor")

    #@abstractmethod
    def fun (self):
        pass

class Child:
    pass

obj = Parent()

'''
Parent Constructor
'''

