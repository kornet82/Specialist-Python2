'''
Наследование подразумевает, что дочерний класс содержит все атрибуты
родительского класса, при этом некоторые из них могут быть переопределены
или добавлены в дочернем
'''


# class Student:
#     def __init__(self, name: str, surname: str, birth_date: str, school: int, class_room: str):
#         self.name = name
#         self.surname = surname
#         self.birth_date = birth_date
#         self.school = school
#         self._class_room = {'class_num': int(class_room.split()[0]),
#                             'class_chair': class_room.split()[1]}
#
#     @property
#     def class_room(self):
#         return "{} {}".format(self._class_room['class_num'], self._class_room['class_chair'])
#
#     def next_class(self):
#         self._class_room['class_num'] += 1
#
#     def get_full_name(self):
#         return '{} {}'.format(self.name, self.surname)
#
#     def set_name(self, new_name):
#         self.name = new_name
#
#
# class Teacher:
#     def __init__(self, name, surname, birth_date, school, teach_classes):
#         self.name = name
#         self.surname = surname
#         self.birth_date = birth_date
#         self.school = school
#         self.teach_classes = list(map(self.convert_classes, teach_classes))
#
#     def convert_classes(self, class_room):
#         """
#         '<class_num> <class_room>' --> {'class_num': class_num, 'class_chair': class_chair}
#         """
#         return {'class_num': int(class_room.split()[0]),
#                 'class_chair': class_room.split()[1]}
#
#     def get_full_name(self):
#         return self.name + ' ' + self.surname
#
#     def set_name(self, new_name):
#         self.name = new_name
#
#
# student1 = Student('Иван', 'Петров', '11.01.1987', 112, '11 А')
# print(student1.class_room)
# student1.next_class()
# print(student1.class_room)
# print(student1._class_room)
#
# teacher1 = Teacher('Петр', 'Петров', '12.09.1982', 111, ['11 A', '8 Б'])
# print(teacher1.teach_classes)


class Person(object):
    def __init__(self, name, surname, birth_date, school):
        self.name = name
        self.surname = surname
        self.birth_date = birth_date
        self.school = school

    @property
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def set_name(self, new_name):
        self.name = new_name


class Student(Person):
    def __init__(self, name: str, surname: str, birth_date: str, school: int, class_room: str):
        Person.__init__(self, name, surname, birth_date, school)
        self._class_room = {'class_num': int(class_room.split()[0]),
                            'class_chair': class_room.split()[1]}

    @property
    def class_room(self):
        return "{} {}".format(self._class_room['class_num'], self._class_room['class_chair'])

    def next_class(self):
        self._class_room['class_num'] += 1


class Teacher(Person):
    def __init__(self, name:str, surname:str, birth_date:str, school:int, teach_classes: str):
        Person.__init__(self,name, surname, birth_date, school)
        self.teach_classes = list(map(self.convert_classes, teach_classes))

    def convert_classes(self, class_room):
        """
        '<class_num> <class_room>' --> {'class_num': class_num, 'class_chair': class_chair}
        """
        return {'class_num': int(class_room.split()[0]),
                'class_chair': class_room.split()[1]}


student1 = Student('Ivan', 'Ivanov', '11.01.2001', 111, '7 A')
print(student1.class_room)
print(student1.get_full_name)
student1.set_name('Alexey')
print(student1.get_full_name)
print('=' * 40)
teacher1 = Teacher('Petr', 'Petrov', '12.05.1996', 111, ['2 B', '3 a', '3 b'])
print(teacher1.teach_classes)
print(teacher1.convert_classes('2 B'))


