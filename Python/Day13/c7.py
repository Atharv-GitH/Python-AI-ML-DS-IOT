

x = 30

def fun():

    x = x + 1           # Error : unboundedLocalError

    print("in fun : ",x)

fun()

print(x)
