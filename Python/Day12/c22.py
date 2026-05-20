

def fun(listObj):

    print("in fun : ",listObj)      # [10,20,30,40]

    listObj[2] = 70                 # 70

    print("in fun after update : ",listObj)         # [10,20,70,40]

listObj = [10,20,30,40]

print("in main : ",listObj)     # [10,20,30,40]

fun(listObj)

print("in main after fun call : ",listObj)          # [10,20,70,40]
