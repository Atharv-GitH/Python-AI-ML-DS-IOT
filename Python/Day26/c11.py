

from abc import ABCMeta, abstractmethod

class Demo(metaclass = ABCMeta):

    def __init__(self):
        print("Constructor")

    @abstractmethod
    def fun(self):
        pass

print(type(Demo))
print(Demo.__abstractmethods__)
Demo()

'''
<class 'abc.ABCMeta'>
frozenset({'fun'})
TypeError: Can't instantiate abstract class Demo without an implementation for abstract method 'fun'
'''
