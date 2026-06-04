

from abc import ABCMeta, abstractmethod

class Demo(metaclass = ABCMeta):

    def __init__(self):
        print("Constructor")

    #@abstractmethod
    def fun(self):
        pass

print(type(Demo))
print(Demo.__abstractmethods__)
Demo()

'''
<class 'abc.ABCMeta'>
frozenset()
Constructor
'''
