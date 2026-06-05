

class Parent:

    def __init__(self):
        print("Constructor")

    def __new__(cls, *args, **kwargs):
        print("Memory allocation")
        return super().__new__(cls)

    def __call__(cls, *args, **kwargs):
        print("Parent call method")

obj = Parent()

"""
Parent():
    type (Parent).__call__(Parent)
    type.__call__(Parent)
    Parent.__new__(Parent)
    Parent.__init__(obj)
"""

'''
op :
Memory allocation
Constructor
'''
