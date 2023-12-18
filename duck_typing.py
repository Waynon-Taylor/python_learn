# duck_typing = concept where the class of an object is less important than the method/attributes.
# class type is not checked if minimum methods/attribute are present.
# "if it walks like a duck, and it quacks like a duck, then it must be a duck"


class Duck:

    def walk(self):
        print("This duck is walking")

    def talk(self):
        print("this duck is quacking")


class Chicken:

    def walk(self):
        print("This chickenis walking")

    def talk(self):
        print("this chicken is clucking")


class Person():

    def catch(self, duck):
        duck.walk()
        duck.talk()
        print("you caught the critter")


duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)
