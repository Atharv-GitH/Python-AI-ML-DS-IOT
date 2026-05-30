

class MacD :
    
    def taste(self):
        print("Burger and fries Taste: Same in all outlets")
    
    def price(self):
        print("price: Same in all outlets")

class MacDPune (MacD) :
    
    def __init__(self):
        print("Constructor Pune")
    
    def location (self):
        print("Location: Pune")

class MacDMumbai (MacD) :
    
    def __init__(self):
        print("Constructor Mumbai")
    
    def location(self):
        print("Location: Mumbai")

obj1 = MacDPune()
obj1.taste()
obj1.price()
obj1.location()

obj2 = MacDMumbai()
obj2.taste()
obj2.price()
obj2.location()

