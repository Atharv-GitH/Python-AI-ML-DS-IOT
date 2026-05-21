

x = 10

def fun():

    y = 20

    print("in fun")

    print("fun : x",x)          # 10
    print("fun : y",y)          # 20

fun()

print(x)                        # 10
print(y)                        # NameError
