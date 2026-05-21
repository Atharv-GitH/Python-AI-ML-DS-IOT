

x = 30

def fun():

    global x

    x = x + 1       

    print("in fun : ",x)        # 31

print(x)            # 30

fun()

print(x)            # 31
