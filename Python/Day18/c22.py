

class Demo:

    x = 10

    def __init__(self):

        print("in constructor")

obj1 = Demo()
obj2 = Demo()

print(obj1.x)       # 10
print(obj2.x)       # 10

Demo.x = 50

print(obj1.x)       # 50
print(obj2.x)       # 50
