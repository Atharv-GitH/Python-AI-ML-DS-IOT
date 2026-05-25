

def decorFun(funRef):

    def innerFunc():

        print("start decoration")

        funRef()

        print("end decoration")

    return innerFunc

@decorFun
def fun():

    print("in fun")

fun()
