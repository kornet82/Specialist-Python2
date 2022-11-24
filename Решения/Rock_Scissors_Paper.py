"""Реализация игры Камень-ножницы-бумага"""
import random
class Thing(object):
    pass

class Rock(Thing):
    def __str__(self):
        return 'Камень'


class Scissors(Thing):
    def __str__(self):
        return 'Ножницы'


class Paper(Thing):
    def __str__(self):
        return 'Бумага'


def beats(x,y):
    if isinstance(x, Rock):
        if isinstance(y, Rock):
            return None # Нет победителя
        elif isinstance(y, Paper):
            return y
        elif isinstance(y, Scissors):
            return x
        else:
            raise TypeError('Unknown Second Thing')
    elif isinstance(x, Scissors):
        if isinstance(y, Scissors):
            return None
        elif isinstance(y, Paper):
            return x
        elif isinstance(y,Rock):
            return y
        else:
            raise TypeError('Unknown Second Thing')
    elif isinstance(x, Paper):
        if isinstance(y, Paper):
            return None
        elif isinstance(y, Scissors):
            return y
        elif isinstance(y, Rock):
            return x
        else:
            raise TypeError('Unknown Second Thing')

rock, paper, scissors = Rock(), Paper(), Scissors()
lst = [rock,paper,scissors]
i = 0
while i < 10:
    first_hand = random.choice(lst)
    second_hand = random.choice(lst)
    print(f'{first_hand} vs {second_hand} --> '
          f'{beats(first_hand,second_hand)} is win')
    i += 1
