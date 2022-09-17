import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1, p2):
    """     Расстояние между двумя точками     """
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y)**2)


# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты

point_max = Point(0, 0)
max_len = 0
for point in points:
    # point = Point(2, 7)
    # point = Point(12, 7)
    current_distance = distance(Point(0,0), point)
    if current_distance > max_len:
        max_len = current_distance
        point_max = point
        print(f'{max_len = }, Point({point.x},{point.y})')

print("Координаты наиболее удаленной точки = Point({},{})".format(point_max.x, point_max.y))


