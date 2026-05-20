

def fun(a):

    print("in fun before : ",a)

    a = 30
    
    print("in fun after : ",a)

x = 10

print("globals before : ",x)        # 10

fun(x)

print("global after : ",x)


