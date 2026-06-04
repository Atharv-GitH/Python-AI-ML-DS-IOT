

from abc import ABC, abstractmethod

class Parent():

    def __init__(self):
        print("Parent Constructor")

    #@abstractmethod
    def fun (self):
        pass

class Child:
    pass

obj = Parent()

print(type (Parent))
print(type (Child))

'''
Parent Constructor
<class 'type'>
<class 'type'>
'''
