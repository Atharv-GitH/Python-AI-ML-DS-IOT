

class Player:

    #class variable
    team = "India"
    
    def __init__(self,pName,jerNo):

        print("in constructor")
        self.pName = pName
        self.jerNo = jerNo

obj1 = Player("Virat",18)
print(obj1.team)                         # India
obj1.team = "Eng"
print(obj1.team)                         # Eng

obj2 = Player("MSD",7)
print(obj2.team)                         # India

obj3 = Player("Rohit",45)
print(obj3.team)                         # India

