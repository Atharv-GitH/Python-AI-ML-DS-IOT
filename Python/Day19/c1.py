

class Player:

    #class variable
    team = "India"

    def __new__(cls,*args,**kwargs):

        print("memory allocation")

        return super().__new__(cls)

    def __init__(self,pName,jerNo):

        print("in constructor")

        self.pName = pName
        self.jerNo = jerNo

obj1 = Player("Virat",18)
obj2 = Player("MSD",7)
obj3 = Player("Rohit",45)
