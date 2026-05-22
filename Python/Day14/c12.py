
def fun ():

    x = 30
    
    print("fun x : ",x)                               

    def gun():

        nonlocal x

        x = x + 1

        print("gun x : ",x)
    
    def run():

        nonlocal x

        x = x + 1

        print("run x : ",x)

    return gun,run

retRef = fun()

for data in retRef:

    data()
