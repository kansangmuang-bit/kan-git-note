
class Fruit:
    
    # class variables
    MIN_SWEET = 0
    MAX_SWEET = 1
    
    def __init__(self, color="Orange"):
        # instance vars
        # 0 is not sweet 
        # 1 is max sweet
        self._sweetness = None
        self.color = color
        self.shape = "round"
        self.weight = 0.5  # in pounds
        
    @property
    def sweetness(self):
        return self._sweetness
    
    @sweetness.setter
    def sweetness(self, value):
        if value < Fruit.MIN_SWEET:
            self._sweetness = Fruit.MIN_SWEET
        elif value > Fruit.MAX_SWEET:
            self._sweetness = Fruit.MAX_SWEET 
        else:
            self._sweetness = value
            
    def rot(self):
        self.color = "brown"
        self.shape = "flat"
    
    def __str__(self):
        return f"Shape: {self.shape}\nColor: {self.color}"
    

class Juice:
    pass 

class Orange(Fruit):
    
    def __init__(self):
        # do one of these for inheritance
        super().__init__("Orange")
        # Fruit.__init__(self, "Orange") 
        self.juice = Juice()
        

    

f = Fruit()
f2 = Fruit("red")
print(f)
print(f.__dict__)

o = Orange()
print(o.shape)