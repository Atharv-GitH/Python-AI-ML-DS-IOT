

def outerFunc():

    print("in outer function")

    def innerFunc():

        print("in inner function")

    return innerFunc

retVal = outerFunc()

print(type(retVal))
