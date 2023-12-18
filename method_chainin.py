from cgitb import reset


class Car:
    def __init__(self,color,name):
        self.color = color
        self.name = name

    def car_data(self):
        print("{0} {1} car".format(self.color,self.name))
        return self

    def drive(self):
        print("driving")
        return self

    def stop(self):
        print("stoping")
        return self

    def switch_off(self):
        print("switch off")

car = Car('red',"honda")
car.car_data().drive().stop().switch_off()
