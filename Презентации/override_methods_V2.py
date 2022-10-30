# =============================
#    Перегрузка операторов
# =============================

from math import sqrt


class Vector:
    """ docstring for Vector """
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        txt = "<" + str(self.x) + ","
        txt += str(self.y) + ","
        txt += str(self.z) + ">"
        return txt

    def __add__(self, obj):
        t = Vector()
        t.x = self.x + obj.x
        t.y = self.y + obj.y
        t.z = self.z + obj.z
        return t

    def __iadd__(self, obj): # +=
        self = self + obj
        return self

    def __mul__(self, p): # v1 * v2; v1 * 5
        if type(p) == Vector:
            res = self.x * p.x + self.y * p.y + self.z * p.z
            return res
        else:
            self.x *= p
            self.y *= p
            self.z *= p
            # Возвращаем тот же самый объект, но значение атрибутов будут новые
            return self   # v1 = v1 * 3

    def __rmul__(self, p): # 5 * v1
        return self * p

    def __neg__(self):  ## -5, -7.1
        return Vector(-self.x, -self.y, -self.z)

    def __sub__(self, obj):
        return -obj + self

    def __isub__(self, obj): # -=
        self = -obj + self
        return self

    def __abs__(self):
        return sqrt(self * self)

    def __truediv__(self, p):  # реализуем через * (__mul__)
        return self * (1 / p)

    def __eq__(self, obj):
        return self.x == obj.x and self.y == obj.y and self.z == obj.z

    def __ne__(self, obj):
        return not self == obj

    def __lt__(self, obj):
        # return abs(self) < abs(obj)  # можно и так
        if abs(self) < abs(obj):
            return True
        return False

    def __gt__(self, obj):
        if abs(self) > abs(obj):
            return True
        return False

    def __le__(self, obj):
        if abs(self) <= abs(obj):
            return True
        return False

    def __ge__(self, obj):
        if abs(self) >= abs(obj):
            return True
        return False

    def __invert__(self):   # ~
        self.x = 10 - self.x
        self.y = 10 - self.y
        self.z = 10 - self.z
        return self


# Vectors
print("Vectors:")
a = Vector(1, 2, -1)
b = Vector(1, -1, 3)
c = ~Vector(9, 8, 11)
print("a =", a)
print("b =", b)
print("c =", c)

print("Abs of Vectors:")
print("|a| =", abs(a))
print("|b| =", abs(b))
print("|c| =", abs(c))

print("Vectors comparation:")
print("a == b ->", a == b)
print("a != b ->", a != b)
print("a == c ->", a == c)
print("a < b ->", a < b)
print("a > b ->", a > b)
print("a <= b ->", a <= b)
print("a >= b ->", a >= b)

print("Vectors operations:")
print("Vectors sum:")
print("a + b =", a + b)
c += a
print("a += c ->", c)
print("Vectors sub:")
print("a - b =", a - b)
c -= a
print("a -= c ->", c)
print("Vector mul:")
print("a * b =", a * b)
print(f'Before: {id(a) = }')
print("a * 3 =", a * 3)
print(f'After: {id(a) = }')
print("a =", a)
print("2 * b =", 2 * b)
print("b =", b)
print("-b =", -b)
print("b =", b)
print("a / 3 =", a / 3)
print("a =", a)


