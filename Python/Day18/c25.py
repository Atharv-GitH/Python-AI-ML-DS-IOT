

class Employee:

    def __init__(self):

        self.empid = 10 
        self.empName = "kanha"

obj1 = Employee(10,"kanha")             # Error
obj2 = Employee(15,"Ashish")

print(obj1.empid)
print(obj1.empName)

print(obj2.empid)
print(obj2.empName)
