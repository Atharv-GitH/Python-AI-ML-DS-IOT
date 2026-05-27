

class Demo:

    x = 10 

    def __init__(self):

        print("in constructor")

obj = Demo()

print(Demo.x)
print(obj.x)

print(obj.__dict__)
print(Demo.__dict__)
