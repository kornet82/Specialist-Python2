"""
class Money

Напишите класс для работы с денежными суммами.
"""
import json
import random

import requests

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
data_dict = json.loads(response.text)

class Money:
    def __init__(self, integer=0, decimal=0):
        self.integer = integer + decimal // 100
        self.decimal = decimal % 100
        self.total_decimal = self.integer * 100 + self.decimal

    def __str__(self):
        return f'{self.integer:>6} руб {self.decimal:0>2} коп'

    def __add__(self, other_sum):
        return Money(self.integer + other_sum.integer, self.decimal + other_sum.decimal)

    def __sub__(self, other_sum):
        return Money(self.integer - other_sum.integer, self.decimal - other_sum.decimal)

    def __mul__(self, rate):
        return Money(self.integer * rate, self.decimal * rate)

    def __truediv__(self, rate):
        return Money(0, int(round(self.total_decimal * (1/rate), 0)))

    def __gt__(self, other_sum):
        return self.total_decimal > other_sum.total_decimal

    def __lt__(self, other_sum):
        return self.total_decimal < other_sum.total_decimal

    def __eq__(self, other_sum):
        return self.total_decimal == other_sum.total_decimal

    def __ne__(self, other_sum):
        return not self == other_sum

    def __mod__(self, percent):
        return Money(0, round(self.total_decimal * percent / 100))

    def convert(self, currency):
        exchange = self.total_decimal * 0.01 / currency
        return round(exchange, 2)


# Реализовать:
# *   сложение
# *   вычитание
# *   умножение на целое число
# *   сравнение (больше, меньше, равно, не равно)
#
# денежной суммы.
# При всех операциях, сумма должна преобразовываться к сумме с минимальным количеством копеек.

# Примеры:
# Создаем сумму из 20 рублей и 120 копеек
money_sum1 = Money(20, 120)
money_sum2 = Money(0, 101)
money_sum3 = Money(0, 99)
# Выводим сумму, с учетом минимального кол-ва копеек
print(money_sum1)  # 21руб 20коп
print(money_sum2)
print(money_sum3)
print()

# Создаем две денежные суммы
money_sum1 = Money(20, 60)
money_sum2 = Money(20, 60)
# money_sum2 = Money(10, 45)

# Складываем суммы
money_result = money_sum1 + money_sum2
print(money_result)  # 31руб 05коп
print(money_sum1 - money_sum2)
print(money_sum1)
print(money_sum2 * 5)
print(money_sum2 / 5)
print()
print(money_sum1 > money_sum2)
print(money_sum1 < money_sum2)
print(money_sum1 == money_sum2)
print(money_sum1 != money_sum2)
print()

currency_name = random.choice(['EUR', 'USD'])
currency = data_dict['Valute'][currency_name]['Value']
print(f'{currency_name}: {currency}')
money_sum5 = Money(200, 60)
print(f'{money_sum5!s} -> {money_sum5.convert(currency)} {currency_name}')