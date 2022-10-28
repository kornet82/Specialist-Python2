"""
Прямоугольник по двум сторонам
Создать класс прямоугольник:

а) при создании указывается ширина и длина

r = Rect(5, 10)

б) методы для площади и периметра

print(r.area())       # возвращает площадь
print(r.perimeter())  # периметр

в) масштабирование и поворот

r.scale(10) - ширина и длина увеличиваются в 10 раз
r.scale(0.1) - ширина и длина уменьшаются в 10 раз
r.rotate() - меняется местами ширина и длина

г) переопределить магические методы __repr__ и __str__
"""
import random


class Rect:
    def __init__(self, wight, height):
        self.wight = wight
        self.height = height

    def area(self):
        return self.wight * self.height

    def perimeter(self):
        return (self.wight + self.height) * 2

    def scale(self, scale):
        self.wight *= scale
        self.height *= scale

    def rotate(self):
        self.wight, self.height = self.height, self.wight

    def __repr__(self):
        return f'Rect ({self.wight}, {self.height})'

    def __str__(self):
        return f'Прямоугольник с шириной {self.wight} и высотой {self.height}'


## Тестовая часть
r = Rect(5, 10)
print(repr(r))
print("Площадь: ", r.area())
print("Периметр: ", r.perimeter())

if random.randint(0, 1):
    r.scale(10)
    print(f"Увеличение: {r.wight}, {r.height}")
else:
    r.scale(0.1)
    print(f"Уменьшение: {r.wight}, {r.height}")

r.rotate()
print("Rotate: ", r.wight, r.height)
print("Площадь: ", r.area())
print("Периметр: ", r.perimeter())
print(r)
print(repr(r))
