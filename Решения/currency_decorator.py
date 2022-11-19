'''
Напишите функцию декоратор, которая переводит значение декорируемой функции
в рублях, в доллары (курс: 1$ = 70 рубля) или в евро (курс: 1€  = 81 руб).
Для тех, кто хочет добавить знак валюты:
chr(36) -> '$'
chr(8364) -> '€'
chr(8381) -> '₽'
'''
def decorator(func):
    def wrapper(*args, **kwargs):
        result = float(func(**kwargs)[:-1])
        result_in_USD = round(result/70, 2)
        result_in_EURO = round(result/81, 2)
        result_in_currency = f'{result_in_USD:.2f}' + chr(36) + '\n'
        result_in_currency += f'{result_in_EURO:.2f}' + chr(8364) + '\n'
        return  result_in_currency
    return wrapper

@decorator
def summa(count: float, price: float) -> str:
    return f'{round(count * price, 2)}₽'

print(summa(count=int(input('Введите количество:')),
            price=int(input('Введите курс:'))))



