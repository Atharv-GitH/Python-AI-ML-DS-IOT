

def outerFunc():

    print("in outer function")

    def innerFunc():

        print("in inner function")
    
    print(innerFunc)

print(outerFunc)

