

class Player:

    #class variable
    team = "India"
    
    def __init__(self,pName,jerNo):

        print("in constructor")
        self.pName = pName
        self.jerNo = jerNo

print(Player.team)
Player.team = "Bharat"
obj1 = Player("Virat",18)
print(obj1.team)                         # Bharat

obj2 = Player("MSD",7)
print(obj2.team)                         # Bharat

obj3 = Player("Rohit",45)
print(obj3.team)                         # Bharat

