# define parent class
class Animal:
    name = 'Unkown'
    weight = 0
    age = 0
    color = 'Unkown'
    breed = 'Unkown'

    # method (function)
    def statistics(self):
        msg = "\nName: {}\nWeight {}\nAge: {}\nColor: {}\nBreed: {}"\
              .format(self.name,self.weight,self.age,self.color,self.breed)
        return msg
    
# define child class 
class Cat(Animal):
    name = 'Sally'
    weight = 400
    age = 7
    color = 'Orange and black'
    catBreed = 'Tiger'
    pawSize = 4

    # method (function)
    def statistics(self):
        msg = "\nName: {}\nWeight {}\nAge: {}\nColor: {}\nCat Breed: {}\nPaw Size: {}"\
              .format(self.name,self.weight,self.age,self.color,self.catBreed,self.pawSize)
        return msg
    
# define child class
class Bird(Animal):
    name = 'Frank'
    weight = 10
    age = 12
    color = 'Unkown'
    birdType = 'Eagle'
    wingSpan = 6.5

    # method (function)
    def statistics(self):
        msg = "\nName: {}\nWeight {}\nAge: {}\nColor: {}\nBird Type: {}\nWing Span: {}"\
              .format(self.name,self.weight,self.age,self.color,self.birdType,self.wingSpan)
        return msg
    

if __name__ == "__main__":
    cat = Cat()
    print(cat.statistics())

    bird = Bird()
    print(bird.statistics())
