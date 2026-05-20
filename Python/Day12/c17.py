

def fun(x):

    print("in fun before : ",x)         # 10

    x = 30
    
    print("in fun after : ",x)         # 30

x = 10

print("global before : ",x)             # 10

fun(x)

print("global after : ",x)             # 10
