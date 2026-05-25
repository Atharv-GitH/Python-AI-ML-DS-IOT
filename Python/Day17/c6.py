

a = 50

class Demo:

    x = 10

    def disp():

        print("x :",x)

def fun():

    print("in fun")

print(a)            #50

fun()               #in fun

print(Demo.x)       #10

Demo.disp()         # x : error
