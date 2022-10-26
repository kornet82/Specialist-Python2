class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def to_str(self):
        return f'Point ({self.x}, {self.y})'

    def __repr__(self):
        return f'Point ({self.x}, {self.y})'


    def __str__(self):
        return f'Точка с координатами {self.x}, {self.y}'

p1 = Point(5,5)
p2 = Point(3, 4)
print (p1)
print(p1.to_str())
print(p2.to_str())
print('*' * 20)
# Три вызова с одинаковым функционалом
print(str(p2))
print(p2.__str__())
print(Point.__str__(p2))

