
def decorFun(funRef):

    def innerFun(**kwargs):

        print("start decoration")

        funRef(**kwargs)

        print("end decoration")

    return innerFun

@decorFun

def add(x, y):

    print("x : ",x)
    print("y : ",y)
    print("add : ",x+y)

add(y = 50, x = 20)
