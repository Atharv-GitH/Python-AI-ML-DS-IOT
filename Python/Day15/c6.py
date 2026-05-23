

#wrong format

def fun(x):

    print(x)        # function run at address

    x()

def run():

    print("in run")

fun(run)
