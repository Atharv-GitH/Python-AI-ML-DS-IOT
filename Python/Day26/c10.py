

from abc import ABCMeta, abstractmethod

class Demo (metaclass = ABCMeta):

    def __init__(self):
        print("Constructor")

    def fun(self):
        pass

print(type (Demo))
Demo()

'''
<class 'abc.ABCMeta'>
Constructor
'''
