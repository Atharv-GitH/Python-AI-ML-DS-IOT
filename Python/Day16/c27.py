

def decorFun1(funRef):

    def innerFun(*args):

        print("start decoration")

        retVal = funRef(*args)

        print("end decoration")

        return retVal

    return innerFun

@decorFun1

def add(x, y):

    print("in add")

    return x + y

retVal = add(10, 50)

print(retVal)

