import  math, requests, json
from pprint import pprint

class Money:
    def __init__(self, rub:int = 0, kop:int = 0):
        self.kop = rub * 100 + kop

    def __str__(self):
        return f'Деньги: {math.trunc(self.kop - self.kop % 100) / 100} рублей {math.trunc(self.kop % 100)} копеек'

    def __repr__(self):
        return f'Money ({math.trunc(self.kop - self.kop % 100) / 100} {math.trunc(self.kop % 100)})'

    def __eq__(self, other):
        if self.kop == other.kop:
            return True
        return False

    def __lt__(self, other):
        if self.kop < other.kop:
            return True
        return False

    def __gt__(self, other):
        if self.kop > other.kop:
            return True
        return False

    def __add__(self, other):
        temp = self.kop + other.kop
        return Money ((temp - temp % 100) / 100, temp % 100)

    def __ne__(self, other):
        if self.kop != other.kop:
            return True
        return False

    def __sub__(self, other):
        if other.kop > self.kop:
            return Money (kop=(other.kop - self.kop))
        return Money(kop=(self.kop - other.kop))

    def __mod__(self, percent):
        temp = round(self.kop * percent/100, 0)
        return Money ((temp - temp%100)/100, temp%100)

    def convert_currency(self, val: str):
        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        data_dict = json.loads(response.text)
        well = data_dict['Valute'][val]['Value']
        wp = math.trunc(self.kop / 100 / well)
        return f"{wp} {str(val[0])}. {math.trunc(((self.kop - wp * well * 100) / 100) / well * 100)} cents. "

    def convert(self):
        print(self.convert_currency('USD'))
        print(self.convert_currency('EUR'))

# Тестовая часть
money_sum1 = Money(20, 120)
print(money_sum1)
money_sum1 = Money(20, 60)
money_sum2 = Money(10, 45)
money_result = money_sum1 + money_sum2
print(money_result)
money_sum1 = Money(1120, 60)
percent_sum = money_sum1 % 20
print(percent_sum)
print(money_sum1)
money_sum1.convert()



# url = 'https://www.cbr-xml-daily.ru/daily_json.js'
# response = requests.get(url)
# # Variant 1
# data_dict1 = json.loads(response.text)
# # Variant 2
# data_dict2 = response.json()
#
# # pprint(data_dict1)
# # pprint(data_dict2)
# # print(data_dict1['Valute']['EUR']['Value'])
# # print(data_dict2['Valute']['USD']['Value'])