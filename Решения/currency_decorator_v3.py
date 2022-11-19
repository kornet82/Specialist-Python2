'''
Напишите функцию декоратор, которая переводит значение декорируемой функции
в рублях, в доллары (курс: 1$ = 70 рубля) или в евро (курс: 1€  = 81 руб).
Для тех, кто хочет добавить знак валюты:
chr(36) -> '$'
chr(8364) -> '€'
chr(8381) -> '₽'
'''


a = chr(36)
b = chr(8364)
c = chr(8381)


def switch(func):
    def inner(count, price):
        original_result = float(func(count, price)[:-1])
        x = int(input(f'В какой валюте? 1:{a} 2:{b} 3:{c} '))
        if x == 1:
            print(f'Kypс 1$ = 70{c}')
            original_result /= 70
        elif x == 2:
            print(f'Kypс 1€ = 81{c}')
            original_result /= 81
            """Вывод одной строчкой без input в комменте"""
        return f'{round(original_result, 2)}{(a,b,c)[x - 1]}'
    return inner


@switch
def summa(count: float, price: float) -> str:
    return f'{round(count * price, 2)}₽'


print(summa(35, 2))