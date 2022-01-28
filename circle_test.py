import math

class Circle:
    color = "red"

    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def area(self):
        return self.radius * self.radius * math.pi

    def center(self):
        return self.x, self.y

print("원의 정보를 입력하세요")
radius = int(input("반지름:"))
cx = int(input("x 좌표:"))
cy = int(input("y 좌표:"))
circle1 = Circle(radius, cx, cy)

print("원의 넓이:", circle1.area())
print("중심 좌표:", circle1.center())