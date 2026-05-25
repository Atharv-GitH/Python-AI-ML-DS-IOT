
def decorFun(funRef):

    def innerFun(*args, **kwargs):

        print("start decoration")

        funRef(*args, **kwargs)

        print("end decoration")

    return innerFun

@decorFun

def add(x, y):

    print("x : ",x)
    print("y : ",y)
    print("add : ",x+y)

#add = decorFun(add)

add(10,20)
