class Car:
    def __init__(self, gas=0, capacity=40, gas_per_km=5, prob=0):
        self.gas = gas  # сколько бензина в баке
        self.capacity = capacity  # вместимость бака
        self.gas_per_km = gas_per_km  # расход топлива на 100 км
        self.prob = prob  # пробег

    def fill(self, litr: float):
        if self.gas + litr <= self.capacity:
            self.gas += litr
            print(f"Залили {litr} литров. В бак {self.gas} литров")
        else:
            print(f"{self.gas + litr - self.capacity} литров лишних!")
            self.gas = self.capacity

    def ride(self, ride_km : float):
        if (self.gas_per_km / 100) * ride_km <= self.gas:
            self.prob += ride_km
            self.gas -= self.gas_per_km * ride_km / 100
            print(f"проехали {ride_km} километров. Потратили {self.gas_per_km * ride_km / 100} литр бензин")
        else:
            print(f"Error: Мало бензина в баке")

    def info(self):
        print("бензин в бак: {} л\nпробег: {} км".format(self.gas, self.prob))


#(self, gas=0, capacity=40, gas_per_km=5)
car1 = Car(10, 50, 10)
print('Первый вызов info')
car1.info()
car1.fill(10)
car1.ride(50)

print('Второй вызов info')
car1.info()
print('*' * 50)
car1.fill(5)
car1.ride(200)

print('Третий вызов info')
car1.info()

car1.fill(75)
car1.ride(600)
print('4-й вызов info')
car1.info()