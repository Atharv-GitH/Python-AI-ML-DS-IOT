
# wrong format

def decorFun(funRef):

    def innerFun():

        print("start decoration")

        funRef()

        print("end decoration")

    return innerFun

#@decorFun

def fun():

    print("in fun")

print(fun)
