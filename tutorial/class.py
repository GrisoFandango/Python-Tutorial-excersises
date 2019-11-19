class Point:
    defaul_color = "Red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def draw(self):
        print(f"Point {self.x}, {self.y}")


ciccio = Point.zero()
ciccio.z = 10
ciccio.draw()
print(ciccio.defaul_color)
print(Point.defaul_color)
print(ciccio.z)
