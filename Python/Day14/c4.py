
x = 10

def fun ():

    x = 30

    print("fun x : ",x)               

    def gun():

        print("gun x : ",x)

    return gun

retRef = fun()

retRef()

print(x)
