

mult = lambda a,b : print("In mult"), a * b

x = int(input("enter num1 : "))
y = int(input("enter num2 : "))

print(mult(x, y))

# error becz we're trying to use two separate expression in our lambda fun
# print("in mult") and a * b
