class Animal:

    alive = True

    def __init__(self):
        pass

    def eat(self):
        print("this animal is eating")
    
    def sleep(self):
        print("this animal is sleeping")

class Rabbit(Animal):
    def hop(self):
        print("this rabbit is hopping")
class Fish(Animal):
    def swim(self):
        print("this fish is swimming")
class Hawk(Animal):
    def fly(self):
        print("this hawk is hawking lol")

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()
################
hawk.fly()
fish.swim()
rabbit.hop()


