
def greet():
    print("Hello")

x = greet

x()     

print(type(x))          # <class 'function'>

class cricPlayer :
    pass

print(type(cricPlayer))            # <class 'type'>

'''

*** internal ***

1. functions are objects
   classes are objects
   instances are objects

2. Student is an object created by the metaclass type

3. So when we say "print is a function", it means :

   print is a built-in function object
