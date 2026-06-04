

from abc import ABC, abstractmethod

class Parent(ABC):

    def __init__(self):
        print("Parent Constructor")

    #@abstractmethod
    def fun (self):
        pass

obj = Parent()

'''
Parent Constructor
'''
