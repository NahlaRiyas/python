class Rectangle:
    def __init__(self, l, b):
        self.area = l * b

l1, b1 = map(int, input("Rect1 length breadth: ").split())
l2, b2 = map(int, input("Rect2 length breadth: ").split())

r1, r2 = Rectangle(l1, b1), Rectangle(l2, b2)

print("R1 larger" if r1.area > r2.area else
      "R2 larger" if r2.area > r1.area else
      "Equal area")

