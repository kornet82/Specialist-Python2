class Car:
    def __init__(self, gas, capacity, gas_per_km, mileage):
        self.gas = gas   # Сколько бензина в баке
        self.capacity = capacity  # Вместимость бака
        self.gas_per_km = gas_per_km  # Расход бензина
        self.mileage = mileage
    def fill(self, litr : float):
        if self.gas + litr <= self.capacity:
            self.gas += litr
            print(f"Залили {litr} литров. В баке {self.gas} литров. \n"
                  f"Можем проехать {self.gas / self.gas_per_km} километров")
        else:
            print(f"Залили {litr} литров до полного! Лишних {self.gas + litr - self.capacity} литров")
            self.gas = self.capacity
            

    def ride(self, km : int):
        print(f"Едем {km} километров!")
        if km * self.gas_per_km <= self.gas:
            self.mileage += km
            self.gas -= km * self.gas_per_km
            return f"Проехали {km} километров. В баке еще {self.gas} литров"
        else:
            tmp = self.gas / self.gas_per_km
            self.mileage += tmp
            self.gas = 0
            print(f"Проехали {tmp} километров. Бензин кончился. ")

    def info(self):
        print (f"Бензина в баке: {self.gas} л\nПробег: {self.mileage} км")


# car1 = Car(5, 100, 10, 0)
# print(car1.info())
# print('*' * 40)
# # метод fill: "залить столько-то литров в бак"
# car1.fill(5)
# print(car1.info())
# print('*' * 40)
# # метод ride: "проехать сколько-то км"
# car1.ride(50)
# print(car1.info())
# print('*' * 40)
# # метод info: "количество бензина в баке и пробег"
# car1.fill(150)
# print(car1.info())
# print('*' * 40)
# car1.ride(1300)
# print(car1.info())


"""
## Автомобиль

Описать класс Car
``` python
class Car:
  ...
  
car1 = Car()
```

а) У машины должны быть атрибуты
* "сколько бензина в баке" (gas)
* "вместимость бака" - сколько максимум влезаем бензина (capacity)
* "расход топлива на 100 км" (gas_per_km)

б) метод "залить столько-то литров в бак"

``` python
car1.fill(5)  # залили 5 литров
```

должна учитываться вместительность бака
если пытаемся залить больше, чем вмещается, то заполняется полностью +
print'ом выводится сообщение о лишних литрах

в) метод "проехать сколько-то км"

``` python
car1.ride(50)  # едем 50 км (если хватит топлива) 
```

выведет сообщение "проехали ... километров"
в результате поездки потратится бензин
Машина едет пока хватает бензина

г) добавить атрибут с пробегом, который увеличивается в результате ride
реализовать метод: car1.info() (количество бензина в баке и пробег)
"""
