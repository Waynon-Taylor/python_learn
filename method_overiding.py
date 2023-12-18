class Vehicle:
    def drive(self):
        print("this car is driving")


class Bike(Vehicle):
    def drive(self):
        print("this bike is driving")
    pass

bike = Bike()
bike.drive()
