

x = 10

def fun():

    y = 20

    print("in fun")
    print("fun : x",x)      # 10
    print("fun : y",y)      # 20

def gun():

    z = 30

    print("in gun")
    print("gun : x",x)      # 10
    print("gun : z",z)      # 30

gun()
fun()
print(x)
#print(y)                    NameError -> y is not defined
print(z)                     # NameError
