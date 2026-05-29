

class Demo:

    a = 10

    def __new__(cls):
        print("in new")
        cls.b = 20                                  # in new obj
        x = 100                                     # x : local or Temp var 
        print("=> new locals : ",locals())
        return super().__new__(cls)

    def __init__(self):
        print("in init")
        self.c = 30                             # in init obj
        u = 400                                 # local or temp 
        print("=> init locals : ",locals())

    def instFun(self):
        print("in instance")
        d = 40                                   # d :  in instFun 
        self.y = 200                             #
        print("=> instFun locals : ",locals())

    @classmethod
    def classFun(cls):
        print("in class")
        cls.e = 50                               #   
        z = 300                                  # z : local or temp
        print("=> classFun locals : ",locals())

    @staticmethod
    def staticFun():
        print("in static")
        f = 60                                  # local or Temp
        print("=> staticFun locals : ",locals())

obj = Demo()

#print(globals())

print("=> Demo dict : ",Demo.__dict__)
print("\n")

print("=> obj dict : ",obj.__dict__)
print("\n")

obj.instFun()
print("=> Demo.instFun.dict : ",Demo.instFun.__dict__)
print("=>obj.instFun.dict : ",obj.instFun.__dict__)
print("\n")

obj.classFun()
print("=> Demo.classFun.dict : ",Demo.classFun.__dict__)
print("=> obj.classFun.dict : ",obj.classFun.__dict__)
print("\n")

obj.staticFun()
print("=> Demo.staticFun.dict : ",Demo.staticFun.__dict__)
print("=> obj.staticFun.dict : ",obj.staticFun.__dict__)

