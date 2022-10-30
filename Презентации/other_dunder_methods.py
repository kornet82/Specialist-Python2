class Vector:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]

    def __add__(self, other):
        return Vector((self.x + other.x, self.y + other.y))

    def as_point(self):
        return self.x, self.y

    def __str__(self):
        return "V x:{}, y:{}".format(self.x, self.y)

# Тест
v1 = Vector((10,15))
v2 = Vector((5,3))
v3 = v1 + v2
print (v3)

# Эквивалент этого ->
v3 = v1.__add__(v2)
#Но благодаря перезагрузке оператора __add__ мы можем делать это просто "+"

class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return 'Point ({}{})'.format(self.x, self.y)

    def __eq__(self, other):
        """Перегрузка оператора == """
        if type(other) == Point:
            return self.x == other.x and self.y == other.y
        else:
            raise TypeError ('Пришел не класс Point')

    def __lt__(self, other):
        '''Перегрузка оператора < (меньше). Меньше та точка,
        у которой меньше х. При одинаковых x меньше та, у которой меньше y'''
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    def __gt__(self, other):
        '''Перегрузка оператора > (больше). Больше та точка,
        у которой больше х. При одинаковых x больше та, у которой больше y'''
        if self.x == other.x:
            return self.y > other.y
        return self.x > other.x




def test():
    p0 = Point(3,5)
    p1 = Point(3,5)
    p2 = Point(-1,7)
    p3 = Point(3,1.17)

    print('p0=', p0)
    print('p1=', p1)
    print('p2=', p2)
    print('p3=', p3)
    print('*'* 20)
    print("p0=p1 ", p0 == p1) # True
    print("p0=p1 ", p0.__eq__(p1)) # True (the same)
    assert p0 == p1
    print("p1=p2", p1 == p2) # False
    assert not p1 == p2

    print("p0 != p1 ", p0 != p1)  # False
    print("__ne__" in dir(p1)) # Проверяем наличие оператора в словаре объекта
    assert not (p0 != p1)
    print("p1 != p2", p1 != p2) # True
    assert p1 != p2

    print('p2 < p1', p2 < p1)  # True
    assert p2 < p1
    print('p1 < p2', p1 < p2)  # False
    assert not (p1 < p2)

    print('p3 < p1', p3 < p1)

    a = [p0,p1,p2,p3]
    pmin = min(a)
    pmax = max(a)
    print('pmin=', pmin)
    print('pmax=', pmax)
    assert p2 == pmin
    b = sorted(a)
    print(*b)
    assert (b == [p2,p3,p0,p1])










