

class Employee:

    def __init__(self,empId,empName):

        self.empid = empId
        self.empName = empName

obj1 = Employee(10,"kanha")         #__init__(obj1,10,kanaha)   
obj2 = Employee(15,"Ashish")        #__init__(obj2,15,Ashish)

print(obj1.empid)
print(obj1.empName)

print(obj2.empid)
print(obj2.empName)
