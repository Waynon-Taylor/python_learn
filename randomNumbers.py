import random

options = ["rock","paper",'sissors']
num = random.randint(0,6)
random.shuffle(options)

x = random.random()
print(num)
print(x)
item = random.choice(options)
print(item)
