

def fun(x,y):

    print("fun data", x,y)

    x = 50
    y = 100

    print("fun data after update :",x,y)

x = 10
y = 20

print("main data :",x,y)

fun(x,y)

print("main data after fun call : ",x,y)

'''
op :
main data : 10 20
fun data 10 20
fun data after update : 50 100
main data after fun call :  10 20
'''
