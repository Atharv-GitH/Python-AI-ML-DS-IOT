

print("ATHARV")

lastName = input("Enter last name : ")

print(lastName)

lastName = lastName.upper()

print(lastName)

'''

** Internal ***

1. print and input are built-in functions even though python internally labels it as "builtin_function_or_method", input is used as a    function because it is called directly 

2. A method belongs to an object/class - like lastName.upper() belongs to the string object lastName

3. You cannot call it independently like upper()

4. input and print are designed to work globally in Python, not with a specific object.

5. You can call them directly because Python already provides them as built-in functions.

6. print and input are function object

'''
