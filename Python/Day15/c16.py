
# Sugar Syntax:

def outerFunc(funcRef):

    def innerFunc():

        print("start inner function")

        funcRef()

        print("end inner function")

    return innerFunc

@outerFunc

def run():

    print("in run")

run()

#retRef = outerFunc(run)

#retRef()
