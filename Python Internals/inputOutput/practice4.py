

print(type(input))              # <class 'builtin_function_or_method'>

'''

1. input function object ultimately has a constructor because it is also an object in Python

2. But not in the same way as normal class instances we create.

input is a built-in function object created internally by the Python interpreter CPython, not by Python code.

3. Internally, CPython creates these built-in function objects using C structures and constructor-like mechanisms in C code.

4. c does not has classes and object cpp have.

5. input, print are created internally by CPython before our program starts.

6.input and print is an object
  its type is builtin_function_or_method
  that type itself is created by Python internals
  therefore there is an internal constructor mechanism behind it, but not a normal Python __init__ we directly use.

'''
