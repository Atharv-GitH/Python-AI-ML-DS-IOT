

class Employee:

    def __new__(cls,*args,**kwargs):

        print("memory allocation")

        return super().__new__(cls)

    def __init__(self,empId,empName):

        self.empid = empId
        self.empName = empName

obj1 = Employee(10,"kanha")         #__init__(obj1,10,kanaha)   
#1.__new__(Employee,10,"kanha")
#2.__init__(obj1,10,"kanha")

obj2 = Employee(15,"Ashish")        #__init__(obj2,15,Ashish)
#1.__new__(Employee,15,"Ashish")
#2.__init__(obj1,15,"Ashish")

print(obj1.empid)                   # 10
print(obj1.empName)                 # kanha

print(obj2.empid)                   # 15
print(obj2.empName)                 # Ashish
