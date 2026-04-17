from abc import ABCMeta, abstractclassmethod


# abstract class Animal
class Animal(metaclass=ABCMeta):
    
    def __init__(self, legs=None):
        self.num_legs = legs 
    
    @abstractclassmethod
    def communicate(self):
        """Implementation intended for subclasses""" 
    

# concrete class Bird  
class Bird(Animal):
    
    def __init__(self):
        super().__init__(2)
        
    # def communicate(self):
    #     print("chirp!")

# a = Animal() # this causes an error since Animal is abstract
b = Bird() # without implementing communicate, this line causes an error
# b.communicate()