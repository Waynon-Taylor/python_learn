#super()  =  Function used to give access to the methods of a parent class Returns a temporary object of a parent class when used. 

class Rectangle:
    def  __init__(self,length,width):
        self.width=width
        self.length = length

class Square(Rectangle):
    def __init__(self,width,length):
        super().__init__(width,length)

    def area(self):
        return self.width*self.length

class Cube(Rectangle):

    def __init__(self, length, width,height):
        super().__init__(length, width)
        self.height = height

    def volume(self):
        return self.width*self.length*self.height


square = Square(8,8)
cube = Cube(3,3,3)

print(cube.volume())
print(square.area())
