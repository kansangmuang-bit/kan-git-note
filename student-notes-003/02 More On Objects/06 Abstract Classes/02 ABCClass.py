from abc import ABC, abstractmethod


# Abstract class Animal 
class Animal(ABC):

    def __inti__(self, legs=None):
        self.num_legs = legs

    def communicate(self):
        """Implementation intended for subclasses"""    

# concrete class Bird
class Bird(Animal):
           
    def __init__(self):
        super().__init__(2)
            
    def communicate(self):
        print("chirp")

a = Animal() # this causes an error since Animal is abstract
b = Bird() # without implementing communciate, this line cause an error
b.communicate()