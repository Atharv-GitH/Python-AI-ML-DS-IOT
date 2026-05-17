

def fun(*args,**kwargs):

    for i in args:

        print(i)

    for i,j in kwargs.items():

        print(i, ":", j)

fun(10,20,30,jerNo = 18,pName="virat",runs=5000)
