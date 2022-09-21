# if it walks like a duck and quacks like a duck
# it is a duck


from abc import ABC, abstractmethod
from typing import Text


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# py is dynamically typed - it doesn't check for object type
# here if its iterable, its good enough
def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
tb = TextBox()
draw([ddl, tb])
