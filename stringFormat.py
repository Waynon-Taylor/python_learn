#str.format()= optional method that gives users 
#more control when displaying output

animal ="cow"
item ="moon"
print("The {} jumped over the {}".format(animal,item))
#positional arguments
print("The {1} jumped over the {1}".format(animal,item))
#keyword argument
print("The {animal} jumped over the {item}".format(animal="cow",item="moon"))

text="The {} jumped over the {}"
print(text.format(animal,item))

#add padding
print("The {1} jumped over the {0:^11} the end".format(animal,item))
print("The {1} jumped over the {0:>11} the end".format(animal,item))
# format nimber 
print("The number is {:.2f}".format(1.4254))
