#multiple inheritance = when a child class is derived from than one parent class


class Prey:

    def flee(self):
        print("This animal flees")


class Predator:

    def hunt(self):
        print("this animal is hunting")


class Rabbits(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

fish = Fish()
print(fish.flee())
print(fish.hunt())
