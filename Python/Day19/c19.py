

class Demo :

    x = 10
    y = 20

    @classmethod
    def fun(cls):

        x = 80

        print("in class method")
        print(cls.x)
        print(Demo.y)
        print(x)                # 80

Demo.fun()

