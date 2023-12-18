#multi_level inheritance when a derived child class inherits another derived child class.

class Organism:
    alive = True

class Animal(Organism):
    def eat(self,animal_name):
        print("this {0} is eating".format(animal_name))

class Dog(Animal):

    def __init__(self,name):
        self.name=name

    def bark(self):
        print("this" + self.name + "is barking")
        self.eat(self.name)


dog = Dog("pitbull")
dog.bark()
