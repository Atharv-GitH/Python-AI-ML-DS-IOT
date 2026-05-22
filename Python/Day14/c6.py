
def fun ():

    x = 20

    print("fun x : ",x)                

    def gun():

        print("gun x : ",x)

    return gun

retRef = fun()

retRef()

print(retRef.__closure__)         # object  
