

def outerFunc():

    print("in outer function")

    x = 20

    def innerFunc():

        print("in inner function")

    return innerFunc

retVal = outerFunc()

print(retVal)
