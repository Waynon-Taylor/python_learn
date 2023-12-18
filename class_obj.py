from car_mod import Car

car_1 = Car("chevy","corvette",2021,"blue")
car_2 = Car("honda","honda",1998,"red")

car_2.wheels = 2

print(car_2.wheels)
print(car_1.wheels)
print(car_1.drive())
print(car_2.stop())
