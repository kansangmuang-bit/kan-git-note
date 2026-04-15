

class Bread:
    
    def __init__(self):
        self.flour = "Wheat"

    def __str__(self):
        return "Bread String Method"

class SaleItem:
    
    def __init_(self):
        self.price = 2.99 

    def __str__(self):
        return "SaleItem String Method"

class HamburgerBun(Bread, SaleItem):
    
    def __init__(self):
        # Use class names explicity to call on super class
        # constructors
        Bread.__init__(self) # must pass in self manually
        SaleItem.__init__(self)

    def __str__(self):
        return "HamburgerBun String Method"
    
h = HamburgerBun()
print(h)