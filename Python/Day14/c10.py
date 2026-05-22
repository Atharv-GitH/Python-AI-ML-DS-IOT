
def fun ():

    x = 10
    y = 20
    z = 30

    print("fun x : ",x)                
    print("fun y : ",y)                
    print("fun z : ",z)                

    def gun():

        x = 40
        y = 50
        z = 60

        print("gun x : ",x)
        print("gun y : ",y)
        print("gun z : ",z)

    return gun

retRef = fun()

retRef()

print(retRef.__closure__)
