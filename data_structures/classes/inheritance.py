# "object" is the base class for all py classes


class Animal:
    def __init__(self) -> None:
        print("animal constructor")
        self.age = 1

    def eat(self):
        print("Animal eats")


class Mammal(Animal):
    # this overrides base class constructor w/o super()
    def __init__(self) -> None:
        print("mammal constructor")
        self.weight = 2
        super().__init__()

    def walk(self):
        print("Mammal walks")


class Fish(Animal):
    def swim(self):
        print("Fish swims")


# driver
tiger = Mammal()
