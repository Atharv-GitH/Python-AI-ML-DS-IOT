

class Demo:

    x = 10
    y = 50

    def __init__(self):

        self.x = 20
        y = 30
        print(y)        # 30

obj = Demo()

print(obj.x)            # 20
print(Demo.x)           # 10
print(obj.y)            # 50
