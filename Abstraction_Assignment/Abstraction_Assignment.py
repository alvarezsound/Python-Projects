from abc import ABC, abstractmethod

#abstract base class
class Animal(ABC):
    
    #parent abstract method
    @abstractmethod
    def sound(self):
        pass
    
#subclass 
class Pig(Animal):
    #child method
    def sound(self):
        print("Oink")

#subclass 
class Tiger(Animal):
    #child method
    def sound(self):
        print("Roar")
        
#subclass
class Snake(Animal):
    #child method 
    def sound(self):
        print("Hiss")

#subclass 
class Dog(Animal):
    #child method 
    def sound(self):
        print("Bark")

#create objects utilizings both the parent/child methods   
P = Pig()
P.sound()
 
T = Tiger()
T.sound()
 
S = Snake()
S.sound()

D = Dog()
D.sound()
