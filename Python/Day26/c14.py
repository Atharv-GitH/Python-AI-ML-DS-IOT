

from abc import ABCMeta, abstractmethod

class Demo(metaclass = ABCMeta):

    def __init__(self):
        print("Demo Constructor")

    @abstractmethod
    def fun(self):
        pass

class DemoChild(Demo):

    def __init__(self):
        super().__init__()
        print("DemoChild constructor")

    def fun(self):
        print("DemoChild fun")

print(type(Demo))
print(Demo.__abstractmethods__)
print(type(DemoChild))
print(DemoChild.__abstractmethods__)
DemoChild().fun()

'''
<class 'abc.ABCMeta'>
frozenset({'fun'})
<class 'abc.ABCMeta'>
frozenset()
Demo Constructor
DemoChild constructor
DemoChild fun
'''
