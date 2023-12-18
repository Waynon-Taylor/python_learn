#  walrus operator :=

# new to python 3.8
# assignment expression aka walrus operatpor
# assign values to variable as part of a large expression

print(happy := True)
print(happy)  

foods = list()
while food := input("what food do you like?:  "):
    if food == "q": break
    foods.append(food)

print(foods)
