

class Demo:

    x = 10

    def __init__(self):

        print("constructor")

obj1 = Demo()
obj2 = Demo()

print(obj1.__dict__)
print(obj2.__dict__)

print(obj1.x)
print(obj2.x)

obj1.x = 50

print(obj1.x)
print(obj2.x)

print(obj1.__dict__)
print(obj2.__dict__)
