

def decorFun(funRef):
 
        print("start decoration")

        funRef()

        print("end decoration")
'''

    def innerFunc():

        print("start decoration")

        funRef()

        print("end decoration")

    return innerFunc
'''

# @decorFun
def fun():

    print("in fun")

decorFun(fun)
