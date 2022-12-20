'''
## 2.1 Квадрат
сделать класс Square - квадрат, который наследуется от пр-ка
Класс Point(x: int, y: int)
Класс Rect(p1, p2)

rect = Rect(p1: Point, p2: Point)
p1 = left_bottom -> (1, 1)  # левая нижняя
p2 = right_top -> (4, 5)    # правая верхняя
methods: area, perimeter


class Square(Rect):
    def __init__(self, p1, size):
        # ...

    # добавить метод вычисления диагонали

sq = Square(p1, 5)  # Квадрат 5x5
print(sq.area())
print(sq.perimeter())
print(sq.diag())
'''

class Point(object):
    def __init__(self, x: int, y:int):
        self._x = x
        self._y = y

    def __str__(self):
        return f'Point ({self._x}, {self._y})'

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value



class Rect:
    def __init__(self, p1: Point, p2: Point):
        self.p1 = p1  #left_bottom
        self.p2 = p2  #right_top
        self.lenght = abs(self.p1.x - self.p2.x)
        self.height = abs(self.p1.y - self.p2.y)

    def __str__(self):
        return f'Rect {self.lenght}x{self.height}'

    def area(self):
        return f'Area = {self.height * self.lenght}'

    def perimeter(self):
        return f'Perimeter = {(self.lenght + self.height) * 2}'


class Square(Rect):
    def __init__(self, p1: Point, size):
        Rect.__init__(self, p1, Point(p1.x + size, p1.y + size))

    def __str__(self):
        return f'Square {self.height}x{self.lenght}'

    def diag(self):
        return f'Diagonale = {round(self.height * 2 ** 0.5, 2)}'


# Проверочный блок

p1 = Point(1,1)
p2 = Point(4,5)
print(p1,p2)

rect1 = Rect(p1,p2)
print(f'{rect1} - {rect1.area()}, {rect1.perimeter()} ')

sq1 = Square(p1, 5)
print(f'{sq1} - {sq1.diag()}')
print(f'{sq1} - {sq1.area()}, {sq1.perimeter()} ')



