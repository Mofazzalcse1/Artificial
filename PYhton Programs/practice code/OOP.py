"""
0.5*base*height

base*height
"""


class Triangle:
    base = ""
    height = ""

    def __init__(self, base, height):
        self.base = base
        self.height = height

    def display(self):
        print(f"Triangle Area :{0.5 * self.base * self.height}")
        print(f"Area: {self.base * self.height}")


T1 = Triangle(10, 20)
T1.display()

