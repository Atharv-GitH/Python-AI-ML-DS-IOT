#wrong format

def outerFunc(funcRef):

    def innerFunc():

        print("start inner function")

        funcRef()

        print("end inner function")

    return innerFunc

def run():

    print("in run")

retRef = outerFunc(run)

print(hex(id(run)))

print(retRef.__closure__)

retRef()
