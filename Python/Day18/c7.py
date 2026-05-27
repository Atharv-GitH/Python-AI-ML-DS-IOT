

class Player:

    team = "India"

    def __new__(cls):

        print("memory allocation")

        return super().__new__(cls)

    def __init__(self):

        self.pName = "Virat"
        self.jerNo = 18

        print("constructor")

print(globals())
