

# wrong format

def decorFun(funRef):

    def innerFun():

        print("start decoration")

        funRef()

        print("end decoration")

    return innerFun


def fun():

    print("in fun")

fun = decorFun(fun)

print(fun.__closure__)

fun()
