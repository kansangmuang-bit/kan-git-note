
# Abstract class Animal 
class Animal:

    def __inti__(self, legs=None):
        self.num_legs = legs

    def communicate(self):
        raise NotImplementedError("NoOo!")
    
# concrete class Bird
class Bird(Animal):
           
    def __init__(self):
        super().__init__(2)
            
    def communicate(self):
        print("chirp")

a = Animal() # this still works, but isn't ideal
             # should not be able to instantiate abstract classes
b = Bird()
b.communicate()