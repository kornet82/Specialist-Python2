"""
Используем класс Rect() с длиной и шириной в качестве атрибутов
Дополнительные задания на magic methods:
1) __repr__() - отобразить в виде текста

2) __str__() - отобразить в виде текста

3) r1 * 5 (__mul__()) - обе стороны станут в 5 раз больше

4) r1 < r2, r1 == r2, r1 <= r1 и т.п.

Шесть методов для сравнения:
__lt__() -> '<'
__gt__() -> '>'
__le__() -> '<='
__ge__() -> '>='
__eq__() -> '=='
__ne__() -> '!='
Сравнить по площади.

def __gt__(self, other):
	# ...
	# return True/False
"""

class Rect:
    def __init__(self, lenght, wight):
        self.wight = wight
        self.lenght = lenght

    def area(self):
        return self.wight * self.lenght

    def perimeter(self):
        return (self.wight + self.lenght) * 2

    def scale(self, scale):
        self.wight *= scale
        self.lenght *= scale

    def rotate(self):
        self.wight, self.lenght = self.lenght, self.wight

    def __repr__(self):
        return f'Rect ({self.lenght}, {self.wight})'

    def __str__(self):
        return f'Прямоугольник с шириной {self.wight} и длиной {self.lenght}'

    def __mul__(self, factor):
        return Rect(self.lenght * factor, self.wight * factor)

    def __eq__(self, other):
        return self.lenght == other.lenght and self.wight == other.wight

    def __ne__(self, other):
        return not (self.lenght == other.lenght and self.wight == other.wight)

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __ge__(self, other):
        return self.area() >= other.area()

#Тестовая часть
r1 = Rect(5, 15)
r2 = Rect(8, 10)
r3 = r1 * 5

print (f'{r1!s}')
print (f'{r1!r}')
print (f'{r2!s}')
print (f'{r2!r}')
print (f'{r3!s}')
print (f'{r3!r}')

print(r1<r2)
print(r1>r2)
print(r1<=r2)
print(r1>=r2)
print(r1!=r2)
print(r1>r3)
print(r1<r3)
print(r1!=r3)




    
