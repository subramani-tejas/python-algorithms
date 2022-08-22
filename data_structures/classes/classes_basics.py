from collections import namedtuple


class Point:

    # class level attributes
    # they stay the same throughout the class
    # accessible/modified thru class or instance
    default_color = "red"

    # x, y are instance attributes
    # they change according to instances
    #
    # magic methods: called by py interpreter automatically
    # ex1. __init__ called when an object is created
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        print(f"self is: {self}")

    # ex2. __str__ called when object is converted to string
    def __str__(self):
        return f"({self.x}, {self.y})"

    # ex3. __eq__ default behavior == (compared references/addresses)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # class method: factory method to spit out an
    # initializeed instance of the class
    # ex. Point(0, 0)
    @classmethod
    def zero(cls):
        return Point(0, 0)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point(2, 3)
point.draw()

point_0 = Point.zero()
point_0.draw()

point_0.x = 2
point_0.y = 3

print("Comparing:", point == point_0)


# data classes
# abstract? classes that contain only data - no methods/logic
AbstractPoint = namedtuple("AbstractPoint", ["x", "y"])

# immutable objects (individual values can't be changed later)
p1 = AbstractPoint(x=1, y=2)

# we can change the reference
p1 = AbstractPoint(x=1, y=22)
p2 = AbstractPoint(x=1, y=2)

# compares the individual values
print(p1 == p2)
