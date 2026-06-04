

from abc import ABCMeta, abstractmethod

class Demo (metaclass = ABCMeta):

    @abstractmethod
    def fun(self):
        pass

print(type (Demo))
Demo ()

'''
<class 'abc.ABCMeta'>
TypeError: Can't instantiate abstract class Demo without an implementation for abstract method 'fun'
'''

