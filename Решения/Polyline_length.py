import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Hinting (Подсказки типов)
def distance(p1: Point, p2: Point) -> float:
    """     Расстояние между двумя точками     """
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)


point1 = Point(2, 4)
point2 = Point(5, -2)
# Задание: Найдите расстояние между этими точками. Реализовав и используя функцию distance()
print("Расстояние между точками = ", distance(point1, point2))


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии

length = 0
for index in range(len(points) - 1):
    # length = length + distance(points[i], points[i + 1])
    length += distance(points[index], points[index + 1])
    print(f'{length = }')

print("Длина ломаной линии = ",  round(length, 2))
