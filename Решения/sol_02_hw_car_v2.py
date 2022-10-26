class Car:
    """ class for car """
    def __init__(self, gas=0, capacity=0, gas_per_km=0, mileage=0):
        # сколько бензина в баке
        self.gas = gas
        # вместимость бака
        self.capacity = capacity
        # расход топлива на 1 км
        self.gas_per_km = gas_per_km / 100
        # пробег
        self.mileage = mileage

    # заполняем бак
    def fill(self, x):
        # проверяем не превышает ли количество заливаемых литров объем бака
        if self.gas + x <= self.capacity:
            self.gas += x
            return f"В баке {self.gas} л"
        # если превышает приравниваем количество заливаемых литров к вместимости
        else:
            tmp = self.gas
            self.gas = self.capacity
            return f"Осталось {tmp + x - self.capacity} лишних литров."

    def ride(self, x):
        # находим количество бензина необходимого для поездки
        # проверяем хватит ли бензина на поездку
        if x * self.gas_per_km <= self.gas:
            self.mileage += x
            self.gas -= x * self.gas_per_km
            return f"Проехали {x} км"
        # если не хватило
        else:
            # находим количество км на преодоление которых хватает бензина
            tmp = self.gas / self.gas_per_km
            self.mileage += tmp
            self.gas = 0
            return f"Проехали {tmp} км"

    def info(self):
        return f"Бензина в баке: {self.gas} л\nПробег: {self.mileage} км"


# создаем объект класса
car1 = Car(5, 100, 10, 0)
print(car1.info())
print('*' * 40)
# метод fill: "залить столько-то литров в бак"
print(car1.fill(5))
print(car1.info())
print('*' * 40)
# метод ride: "проехать сколько-то км"
print(car1.ride(50))
print(car1.info())
print('*' * 40)
# метод info: "количество бензина в баке и пробег"
print(car1.fill(150))
print(car1.info())
print('*' * 40)
print(car1.ride(1300))
print(car1.info())