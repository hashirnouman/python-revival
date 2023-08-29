"""Polymorphism"""
from abc import ABC, abstractmethod


class UIControl(ABC):
    """UI control abstract class"""
    @abstractmethod
    def draw(self):
        """draw abstract method"""


class TextBox(UIControl):
    """ text box class"""

    def draw(self):
        print('Textbox draw')


class DropDownList(UIControl):
    """ Dropdwpm class class"""

    def draw(self):
        print('Dropdown draw')


def draw(controls):
    """draw function"""
    for control in controls:
        control.draw()


ddl = DropDownList()
text_box = TextBox()
# print(isinstance(ddl, UIControl))
draw([ddl, text_box])
