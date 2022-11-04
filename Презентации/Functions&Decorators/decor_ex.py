class DateTime(object):
    def __init__(self, day=10, month=10, year=2000):
        self.day = day
        self.month = month
        self.year = year
    
    def __str__(self):
        return f'{self.day}.{self.month}.{self.year}'
    
    @classmethod
    def from_string(cls, string_date):  # Создаем экземпляр класса с помощью строки
        day, month, year = map(int, string_date.split('-'))
        my_date = cls(day, month, year)
        return my_date
        
    @staticmethod
    def is_valid_date(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999
        

is_valid_date = DateTime.is_valid_date('20-05-1994')
if is_valid_date:
    date_obj = DateTime.from_string('20-05-1994')
    print(date_obj)
date_obj2 = DateTime()
print(date_obj2)
date_obj3 = DateTime(1, 1, 2021)
print(date_obj3)