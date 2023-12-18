#Prevents a User from creating and object of that class
# + compels a  user to override methods in a child class

#abstract class = a class which contains one or more abstract mwthods.
#abstract method = a method that has a declaration but does  not have an implementation.


from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    
    def go(self):
        print("going")

    def stop(self):
        print("stoping")

class Motorcycle(Vehicle):

    def go(self):
        print("bike going")

    def stop(self):
        print("bike stoping")
