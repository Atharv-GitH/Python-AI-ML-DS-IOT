

def outerFunc():

    print("in outer function")

    x = 10

    def innerFunc():

        print("in inner function")

    innerFunc()

    return outerFunc()
