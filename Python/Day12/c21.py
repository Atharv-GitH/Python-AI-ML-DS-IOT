

# Call by reference 

def fun(listObj):

    print("in fun : ",listObj)

listObj = [10,20,30,40]

print("in main : ",listObj)         # [10,20,30,40]

fun(listObj)

'''
in main :  [10, 20, 30, 40]
in fun :  [10, 20, 30, 40]
'''
