

x = 30

def fun():

    global x

    x = 20     

    print("in fun : ",x)        # 20

print(x)            # 30

fun()

print(x)            # 20
