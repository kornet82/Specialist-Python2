# Функция полноправный объект в языке Python:
# • может быть создан во время выполнения;
# • может быть присвоен переменной или полю структуры данных;
# • может быть передан функции в качестве аргумента;
# • может быть возвращен функцией в качестве результата.

# def func(text: str) -> str:
#     return text.upper() + '!'
# #
# #
# print(id(func))
# print(func('привет'))
# bar = func
# print(type(bar), bar)
# print(bar('пока'))
# #
# # # Можно удалить func, но bar будет вызываться
# del func
# print(func('textest')) ## Out -> Error
# # # # #
# print(bar('Я работаю'))
# print(bar.__name__)
# print(id(bar))
# # #
# # # ## Можно хранить функции в структурах данных
# funcs = [bar, str.lower, str.capitalize]
# print(funcs)
# # # # #
# # # # # ## Доступ в функциям, хранящимся внутри списка
# for function in funcs:
#     print(function.__name__, '->', function('проверка Работы'))
# #
# # ## Вызов функции как элемента списка по индексу
# print(funcs[0]('первая функция'))


# ## Передача функции в качестве аргумента в другую функцию
# def greet(function):
#     greeting = function('Программа на Python')
#     print(greeting)

# ## Вызов функции greet с аргументом - функцией bar
# greet(bar)
# # greet('hello')  # TypeError
# ## Вторая функция для примера
# def imp_func(text):
#      return text.lower() + '. Done!'
# #
# # ## Вызов функции greet с аргументом - функцией imp_func
# greet(imp_func)

## Функции более высокого порядка(higher-order functions)
## map, filter, reduce
# print(map(bar, ['hello', 'hi', 'привет']))
# print(set(map(bar, ['hello', 'hi', 'привет'])))
#
# # numbers = list(map(int, input("Enter: ").split()))
# # print(numbers)
# strings = list(map(bar, input("Enter: ").split()))
# print(strings)

# def condition(text):
#      return len(text) > 3
# # ## Включаем элемент в итоговый список, если результат работы
# # ## функции condition True
# print(list(filter(condition, ['hello', 'hi', 'привет'])))
# #
# def add_two(a, b):
#     print(f'{a = }')
#     print(f'{b = }')
#     return a + b
# # #
# from functools import reduce
# print(reduce(add_two, ['hello', 'hi', 'привет']))


## Пример функции zip
## Объединяет элементы с одинаковым индексом
# a = list(range(5))
# b = list(range(11, 17))
# c = list(range(101, 120))
# d = 'hello python'
# print(list(zip(a, b, c, d)))
#
# print(dict(zip([2, 3, 4, 5], (10, 11, 12, 13))))
# # Out: {2: 10, 3: 11, 4: 12, 5: 13}
#
# print(dict(zip('hello', [12, 23, 90, True])))
# # Out: {'h': 12, 'e': 23, 'l': True}
#
# print(dict(zip((1, 45, 11, True), 'abcde')))
# # Out: {1: 'd', 45: 'b', 11: 'c'}
#
# print(dict(zip((True, 45, 11, 1, 2, 3), 'abcde')))
# # Out: {True: 'd', 45: 'b', 11: 'c', 2: 'e'}


# LEGB: Local -> Enclosed -> Global -> Builtin
# a = 10
# # ## Вложенные функции
# def main(text: str):
#     # print(a)
#     a = 5
#     def inner_func(text_1: str) -> str:
#         ## Доступ к переменной a в функции main
#         # nonlocal a
#         ## Доступ к глобальной переменной a
#         # global a
#         print(a)
#         print(locals())  ## Словарь локальных переменных
#         # a += 1  # a = a + 1
#         return text_1.lower() + '...' + f'{a}'
#     return inner_func(text)
#
# print(main('Привет, Всем '))
# print(f'глобальная переменная: {a = }')


# #
# print(inner_func('Может работает?')) # Error
# print(main.inner_func) # Error

## Результат работы функции main это идентификатор на функцию,
## которая выбирается в зависимости от значения аргумента
# def main_imp(size: int):
#     def foo(text):
#         return text.lower() + '...'
#
#     def bar(text):
#         return text.upper() + '!!!'
#
#     if size > 5:
#         return foo
#     else:
#         return bar
# # # # #
# print(main_imp(3)) ## out-> function main_imp.<locals>.bar
# print(main_imp(7)) ## out-> function main_imp.<locals>.foo
# some_name = main_imp(1)
# print(some_name, type(some_name))
# print(some_name('привет'))
# # В одну строчку
# print(main_imp(10)('test'))
# print(main_imp(3)('Student'))

## Используем область видимости Enclosed
# def main_imp_2(size: int, text='default'):
#     def foo():
#         return text.lower() + '...'
#
#     def bar():
#         return text.upper() + '!!!'
#
#     if size > 5:
#         return foo
#     else:
#         return bar
#
# print(main_imp_2(10, 'test')())  # test...
# print(main_imp_2(3)())           # DEFAULT!!!


# ## Лямбды. Нельзя делать связывание в теле функции
## Возвращает только одно значение
# # # ### Вызов лямбды с аргументами
# print((lambda x, y: x + y)(10, 16))
#
# add = lambda x, y: x + y
# print(add(2, 3), type(add))
# # # #
# # Можно, но не нужно
# print((lambda *args, **kwargs: (args, kwargs))(4, 5, 9, b='hello', c='hi'))

# # Сортировка по второму значению кортежей
# list_of_tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
# print(sorted(list_of_tuples))
# print(sorted(list_of_tuples, key=lambda x: x[1]))
# # # # # #
# print(sorted(range(-5, 6), key=lambda x: x * x))
# print(sorted(range(5, -6, -1), key=lambda x: x * x))
# result = set(map(lambda x: x.replace('5', '*'), input('Enter: ').split()))
# print(result)


# ## Декораторы
# def null_decorator(func):
#     return func
#
# def greet():
#     return 'Привет!'
#
# print(greet())

# ## Механизм работы декоратора
# greet = null_decorator(greet)
# # #
# print(greet())
#
# ## Функция декоратор
# def uppercase(func):
#     def wrapper():
#         original_result = func()
#         modified_result = original_result.upper()
#         return modified_result
#     return wrapper


# # ## Декоратор
# @uppercase  ## тоже самое, что и greet_eng = uppercase(greet_eng)
# def greet_eng() -> str:
#     return 'Hello!'
# # # #
# print(greet_eng()) ## out -> HELLO!
# # # # #
# print(greet)
# print(null_decorator(greet))
# print(uppercase(greet))
#
# change_func = uppercase(greet)
# print(greet())
# print(change_func())
#
# # # # ## Применение нескольких декораторов
# def strong(func):
#     def wrapper():
#         return '<strong>' + func() + '</strong>'
#     return wrapper
# #
# def emphasis(func):
#     def wrapper():
#         return '<em>' + func() + '</em>'
#     return wrapper
# # #
# ## Порядок применения снизу вверх
# @strong
# @emphasis
# def greet2():
#     return 'Привет!'
# # #
# print(greet2())
# from pprint import pprint
# Функция декоратор
def trace(func):
    def wrapper(*args, **kwargs):
        print(f'ТРАССИРОВКА: вызвана {func.__name__}() '
              f'с {args}, {kwargs}')
        original_result = func(*args, **kwargs)
        print(f'ТРАССИРОВКА: {func.__name__}() '
              f'вернула {original_result!r}')
        return original_result + '!!!!'
    return wrapper

@trace
def say(name, line):
    return f'{name * 3}: {line}'

print(say('hi', line='Hello'))
print('*' * 30)
print(say(100, 5.2))
print('*' * 30)
print(say(line='time', name='third'))

# Заново создаем недекорированную функцию
def say(name, line):
    return f'{name * 3}: {line}'
print(say(100, 5.2))
