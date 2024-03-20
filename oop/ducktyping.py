"""Polymorphism"""


class TextBox:
    """text box class"""

    def draw(self):
        """text box draw mthod"""
        print("Textbox draw")


class DropDownList:
    """Dropdwpm class class"""

    def draw(self):
        """Dropdown class draw method"""
        print("Dropdown draw")


def draw(controls):
    """draw function"""
    for control in controls:
        control.draw()


ddl = DropDownList()
text_box = TextBox()
# print(isinstance(ddl, UIControl))
draw([ddl, text_box])
