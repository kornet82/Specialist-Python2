class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name} {self.age}'

jack = Person('Jack', 19)
adam = Person('Adam', 43)
becky = Person('Becky', 23)
ada = Person('Ada', 28)
adam2 = Person('Adam', 34)
people = [jack, adam, becky, ada, adam2]
print(jack == adam) #False
# a = sorted(people) #TypeError: '<' not supported between instances of 'Person' and 'Person'
print(people)

def by_name_key(obj):
    return obj.name
###
a = sorted(people, key=by_name_key)
print(a) # [Ada 28, Adam 43, Adam 34, Becky 23, Jack 19]

def by_age_key(obj):
    return obj.age

# a = sorted(people, key=by_age_key)
# print(a) # [Jack 19, Becky 23, Ada 28, Adam 34, Adam 43]

c = sorted(people, key=lambda x: x.age)
print(c)

print(sorted(people, key=lambda x: (ord(x.name[0]), x.age))) # [Ada 28, Adam 34, Adam 43, Becky 23, Jack 19]



