

class Demo:

    x = 10

    def __init__(self):

        print("in constructor")

        self.a = 20
        self.b = 30

obj = Demo()

# class variable access
print(Demo.x)
print(obj.x)

# instance variable
print(obj.a)
print(obj.b)

print(Demo.a)       # Error
print(Demo.a)
