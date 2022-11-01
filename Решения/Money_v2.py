import requests
import json
from pprint import pprint


class Money:
    def __init__(self, rub: int = 0, kop: int = 0):
        self.rub = rub + kop // 100
        self.kop = kop % 100

    def __str__(self):
        return f'Money({self.rub} руб, {self.kop:0>2} коп)'

    def __eq__(self, other):
        if self.rub == other.rub and self.kop == other.kop:
            return True
        return False

    def __lt__(self, other):
        if self.rub == other.rub:
            return self.kop < other.kop
        return self.rub < other.rub

    def __gt__(self, other):
        if self.rub == other.rub:
            return self.kop > other.kop
        return self.rub > other.rub

    def __add__(self, other):
        """Операция сложения"""
        return Money(self.rub + other.rub, self.kop + other.kop)

    def __ne__(self, other):
        if self.rub != other.rub or self.kop != other.kop:
            return True
        return False

    def __sub__(self, other):
        """Операция вычитания"""
        self_kop = self.rub * 100 + self.kop
        other_kop = other.rub * 100 + other.kop
        if other_kop > self_kop:
            return Money(kop=(other_kop - self_kop))
        return Money(kop=(self_kop - other_kop))

    def __mul__(self, amount):
        """Умножение суммы на целое число"""
        return Money(self.rub * amount, self.kop * amount)

    def __mod__(self, percent):
        """Остаток от деления (x % y)"""
        summa = ((self.rub * 100 + self.kop) * percent / 100)
        return Money(round(summa // 100), round(summa % 100))

    def convert(self, currency):
        """Конвертация """
        url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        response = requests.get(url)
        data_dict = json.loads(response.text)
        value = data_dict['Valute'][currency]['Value']
        print(f'Kypс {currency}: {value}')
        return round((self.rub + self.kop * 0.01) / value, 2)



# =================================================================================================

money_sum0 = Money(20, 120)
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)
money_result = money_sum1 + money_sum2
sub_money = money_sum1 - money_sum2
multy_sum = money_sum1 * 3
percent_sum = (money_sum1 % 20)
# =================================================================================================
print(40 * '~')
#
print(f'money_sum0: ', money_sum0)
print(f'money_sum1: ', money_sum1)
print(f'money_sum2: ', money_sum2)

print(40 * '~')
print(f'money_sum1 + money_sum2:  ',  money_result)
print(40 * '~')
print(f'money_sum1 == money_sum2: ', money_sum1 == money_sum2)
print(40 * '~')
print(f'money_sum1 < money_sum2:  ', money_sum1 < money_sum2)
print(40 * '~')
print(f'money_sum1 > money_sum2:  ', money_sum1 > money_sum2)
print(40 * '~')
print(f'money_sum1 != money_sum2: ', money_sum1 != money_sum2)
print(40 * '~')
print(f'money_sum1 - money_sum2:  ', sub_money)
print(40 * '~')
print(f'money_sum1 * 3:           ', multy_sum)
print(40 * '~')
print(f' 20% от суммы money_sum1: ', percent_sum)
print(40 * '~')
m = Money(750)
print(f"Перевод {m} в USD: {m.convert('USD')}")

print(40 * '~')
print(f'money_sum2 - money_sum1:  ', money_sum2 - money_sum1)