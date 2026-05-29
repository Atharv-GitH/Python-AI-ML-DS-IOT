

class Demo():

    z = 30

    def __init__(self):

        self.x = 10
        y = 20
        print(locals())         # y is a local variable live in the function’s local namespace (stack frame)

obj = Demo()


print(Demo.__dict__)
print(obj.__dict__)

print(obj.__init__.__dict__)

print(globals())

