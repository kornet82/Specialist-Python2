from datetime import datetime
# py - m pip install pytz
import pytz

WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'


class Account:
    def __init__(self, name, balance):
        self.name = name
        # Приватный атрибут
        self.__balance = balance
        # Приватный атрибут
        self._history = []
    
    @staticmethod
    def _get_current_time():
        return pytz.utc.localize(datetime.utcnow())
    
    def deposit(self, amount):
        self.__balance += amount
        self.show_balance()
        self._history.append([amount, self._get_current_time()])
              
    def withdraw(self, amount):
        if self.__balance > amount:
            self.__balance -= amount
            print(f'You spent {amount} units')
            self.show_balance()
            self._history.append([-amount, self._get_current_time()])
        else:
            print('Not enough money')
            self.show_balance()
            
    def show_balance(self):
        print(f'Balance: {self.__balance}')
    
    def show_history(self):
        for amount, date in self._history:
            if amount > 0:
                transaction = 'deposited'
                color = GREEN
            else:
                transaction = 'withdrawn'
                color = RED
            print(f'{color} {amount:+} {WHITE} {transaction} on'
                  f'{date.astimezone()}')        
                
acc = Account('first', 0)
# print(pytz.utc.localize(datetime.utcnow()))
# pytz.utc.localize(datetime.utcnow()).astimezone().isoformat()

acc.deposit(100)
acc.deposit(250)
acc.withdraw(170)
acc.deposit(40)

acc.show_history()
print(acc.__dict__)
# print(acc._get_current_time())
# print(acc.__balance)  ## Error
# print(acc.balance)    ## Error
# print(acc._balance)   ## Error
print(acc._Account__balance)
# print(acc.__dict__)
#
acc._Account__balance = 1000
acc.show_balance()