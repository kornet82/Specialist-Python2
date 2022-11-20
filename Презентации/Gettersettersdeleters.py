class StudentA:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print('From get_name()')
        return self._name

    def set_name(self, value):
        print('From set_name()')
        self._name = value

    def del_name(self):
        self._name = ''
        # del self._name

    name = property(fget=get_name, fset=set_name, fdel=del_name)

student = StudentA('First')
print(student.__dict__)
print(student.name)



