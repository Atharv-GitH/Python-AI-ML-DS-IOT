

def outerFunc():

    print("in outer function")

    def innerFunc():
    
        print("in inner function")

    innerFunc()

    print("end outer")

outerFunc()

