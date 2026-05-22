
a = 10

b = 20

def fun ():

    x = 10
    y = 20
    
    print("fun x : ",x)                               
    print("fun y : ",y)                               

    def gun():

        x = 50

        print("gun x : ",x)
        print("gun y : ",y)
    
        def run():

            nonlocal y

            y = y + 1

            print("run x : ",x)
            print("run y : ",y)

        return run

    return gun

retGun = fun()

print(retGun.__closure__)

retRun = retGun()

print(retRun.__closure__)

retRun()
