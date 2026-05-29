

class Demo:

    a = 10                                                  # class var

    def __new__(cls):
        print("in new")
        cls.b = 20                                          # b : in new obj
        c = 30                                              # c : local or Temp var 
        return super().__new__(cls)

    def __init__(self):
        print("in init")
        self.d = 40                                         # d : in init obj
        e = 50                                              # e : local or temp 

    def instFun(self):
        print("in instance")
        f = 60                                              # f :  in instFun 
        self.g = 70                                         #

    @classmethod
    def classFun(cls):
        print("in class")
        cls.h = 80                                          #   
        i = 90                                              # i : local or temp

    @staticmethod
    def staticFun():
        print("in static")
        j = 100                                             # j : local or Temp

obj = Demo()

