
def decorFun1(funRef1):

    def innerFun1():

        print("start decoration1")

        funRef1()

        print("end decoration1")

    return innerFun1

def decorFun2(funRef2):

    def innerFun2():

        print("start decoration2")

        funRef2()

        print("end decoration2")

    return innerFun2

@decorFun1
@decorFun2

def fun():

    print("in fun")

#fun = decorFun1(decorFun2(fun))

fun()
