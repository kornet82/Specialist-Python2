from pprint import pprint


class People:
    ''' first class for learning '''
    name = "Teachers"


# ## Dot notations
# print(People.__class__)
# ## Встроенный(системный)
# print(People.__name__)
# # Сами создаем в классе
# print(People.name)
# print(id(People))
# p = People()
# print(p)
# print(hex(id(p)).upper())
# #
# # ## class People, создаю новый экземпляр
# new_p = type(p)()  ## new_p = People()
# print(type(p))
# print(new_p)
# print(id(new_p))
# #
# # ## Получаю доступ к классу экземпляра
# print(p.__class__)
# print(new_p.__class__)

#
# # ## Получаю доступ к классу экземпляра
# # ## и затем к имени класса
# print(p.__class__.__name__)  # Out: People
# print(p.name)  # Out: Teachers
# p.__class__.__name__ = "Person"
# print(p.__class__.__name__)
# print(People.__name__)


## Доступ к полям класса
# pprint(People.__dict__)
# People.count = 20
# print(p.count)
# pprint(People.__dict__)
# pprint(p.__dict__)
# print(p.name)
# del People.name
# pprint(People.__dict__)
# print(p.name) ## Error

# p.name = 'Students'
# #
# p.age = 22
# pprint(p.__dict__)

## Функции getattr, setattr, delattr
# print(getattr(People, 'name'))

##  название класса -> имя атрибута -> значение атрибута
# setattr(People, 'course', 'Python')
# pprint(People.__dict__)
# delattr(People, 'course')
# pprint(People.__dict__)

## Экземпляры класса. Класс как Callable объект
# class Student:
#     name = 'First'
#
#
# s1 = Student()
# s2 = Student()
# print(s1.name)
# print(s2.name)
# print(id(Student.name))
# print(id(s1.name))
# print(id(s2.name))
# print(s1.__dict__)
# print(s2.__dict__)
# s1.name = 'Second'
# s2.name = 'Third'
# s2.age = 22
# print(s1.__dict__)
# print(s2.__dict__)
# pprint(Student.__dict__)
# # print(s1.age) ## AttributeError: 'Student' object has no attribute 'age'
# #
# s1 = Student()
# s2 = Student()
# Student.name = 'Last'
# print(s1.name)
# print(s2.name)

# print('*' * 50)

## Методы класса
class StudentBetter:
    def __init__(self, name='John'):
        self.name = name
        self.surname = 'Smith'

    def hello1(self):
        self.name += ' addons'

    def hello3(self):
        print(self.name, self.surname)

    def hello2():
        print('Hello, Student')
# 
# 
print(StudentBetter.hello1)
sb = StudentBetter()
print(sb.hello1)
sb.hello1()
# StudentBetter.hello2() ## Error
StudentBetter.hello1(sb) ## sb.hello1()
sb.hello1()
sb.hello3()
StudentBetter.hello3(sb)
# StudentBetter.hello2(sb)  ## TypeError
# sb.hello2()    ## TypeError
# StudentBetter.hello2()
print(sb.__dict__)
print(sb.hello1.__self__)
# # print(hex(id(sb)))
print(sb.hello1.__func__)
print(type(sb.hello1))