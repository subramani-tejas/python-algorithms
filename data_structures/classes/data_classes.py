from collections import namedtuple

# data classes hold ONLY data
# can use namedtuple instead - immutable

Point = namedtuple("Point", ["x", "y"])

p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
