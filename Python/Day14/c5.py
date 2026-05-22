
x = 10

def fun ():

    x = 20

    print("fun x : ",x)                

    def gun():

        nonlocal x

        x = x + 1

        print("gun x : ",x)

        def run():

            print("run x : ",x)

        return run

    return gun

retGun = fun()

retRun = retGun()

retRun()

print(x)
