

from abc import ABCMeta

class Parent(metaclass = ABCMeta):
    
    def __init__(self):
        print("Parent Constructor")

class Parent2():
    
    def __init__(self):
        print("Parent2 Constructor")

print(type(Parent))
print(type(Parent2))

'''
<class 'abc.ABCMeta'>
<class 'type'>
'''
