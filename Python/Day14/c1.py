def fun ():

    x = 10

    print("fun x : ",x)                 # 10

    def gun():

        #nonlocal x

        x = x + 1

        print("gun x : ",x)

    return gun

retRef = fun()

retRef()
