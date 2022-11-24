class Super:
    def __init__(self):
        self._age = 30
        self.__name = 'Python'

    def one(self):
        print('In Super.one')

    def _two(self):
        print('In "_two" method')


class Sub(Super):
    def three(self):
        print('my "three" method')

    def one(self):
        # Переопределение метода
        print('Запуск Sub.one')
        Super.one(self)
        # Запустить стандартное действие
        print('Отработал Sub.one')


if __name__ == '__main__':
    super_obj = Super()  # Создать экземпляр Super
    super_obj.one() # Выполняется Super.method
    print('=' * 40)
    sub_obj = Sub()
    sub_obj.one() # Выполняется Sub.method
    print(sub_obj._age)
    print(sub_obj._Super__name)
    sub_obj._two()
    super_obj.one()
    print(sub_obj.__class__.__bases__) # Получаем класс предок
    print(sub_obj.__class__.__mro__) # method resolution order, показать всех предков







