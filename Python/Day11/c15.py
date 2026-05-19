

def outerFunc():

    print("in outer function")

    def innerFunc1():

        print("in inner1 function")
    
    def innerFunc2():

        print("in inner2 function")
    
    print(innerFunc1)
    print(innerFunc2)

print(outerFunc)

outerFunc()
