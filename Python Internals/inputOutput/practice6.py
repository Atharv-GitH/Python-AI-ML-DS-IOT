

jerNo1 = input("Enter jer NO : ")
print(jerNo1)
print(type(jerNo1))

jerNo = int(input("Enter your jer no : "))

print(jerNo)
print(type(jerNo))

'''
*** internal ***

1. input by defaut returns string we have to type cast/conversion to ex int, float ...

2. Here int is actually a class/type constructor.

3. a. input("Enter number: ")
   b. int("25")

4. Python creates a different object.
   a. original string object - "25"
   b. new integer object - 25

5. Python does not modify the original string object into an int object

'''
