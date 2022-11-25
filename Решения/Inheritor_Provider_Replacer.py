## Класс предок
class Super(object):
    # стандартное поведение
    def method(self):
        print('In Super.method')

    def delegate(self):
        self.action()
        print('покажет или не покажет')

    # Ожидается переопределение метода в потомках
    def first(self):
        assert False, 'first must be defined'

# буквальное наследование метода
class Inheritor(Super):
    pass


# заполнение обязательного метода в Provider.action
class Provider(Super):
    def action(self):
        print('In Provider.action')


class Replacer(Super):
    def method(self):
        print("In Replacer.method")

    def first(self):
        print('first has defined')

# Расширение поведения метода
class Extender(Super):
    def method(self):
    # Начало Extender.method
        print('starting Extender.method...')
        Super.method(self)
        print('ending Extender.method...')
    # конец Extender.method

if __name__ == '__main__':
    # for klass in (Inheritor, Replacer, Extender):
    #     print(klass)
    #     print('\n' + klass.__name__ + '...')
    #     print('*' * 40)
    #     klass().method()
    #     print('*' * 40)


    # print('\n Provider...')
    # p = Provider()
    # p.delegate()


    # i = Inheritor()
    # i.first() # Error

    # r = Replacer()
    # r.first()
    # r.delegate()

    e = Extender()
    e.first() # Error
