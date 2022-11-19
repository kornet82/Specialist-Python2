import random


def decor(func):
    def convert(arg1, arg2):
        rub = float(func(arg1, arg2)[:-1])
        usd = rub / 70
        euro = rub / 81
        return random.choice((f"{usd:>0.2f}{chr(36)}",f"{euro:>0.2f}{chr(8364)}"))
    return convert


@decor
def summa(count: float, price: float) -> str:
    return f'{round(count * price, 2)}₽'


print(summa(35, 2))