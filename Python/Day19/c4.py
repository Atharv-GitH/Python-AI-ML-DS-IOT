

class Player:

    #class variable
    team = "India"
    
    def __init__(self,pName,jerNo):

        print("in constructor")
        print(self)
        # 1000 2000 3000

        self.pName = pName
        self.jerNo = jerNo

obj1 = Player("Virat",18)
print(obj1)                         # 1000
obj2 = Player("MSD",7)
print(obj2)                         # 2000
obj3 = Player("Rohit",45)
print(obj3)                         # 3000
