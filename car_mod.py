class Car:
#class variables
    wheels = 4

    def __init__(self,make,model,year,color):
        #instance variables
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    
    def drive(self):
        print("this {0} is driving".format(self.model))
        
    def stop(self):
        print("this {0} has stopped".format(self.model))
