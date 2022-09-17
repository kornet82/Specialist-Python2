import random

class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """  Подбрасывание монетки """
        self.side = random.choice(['heads','tails'])

heads = tails = 0
n = int(input('Сколько монеток подбросить?'))

lst_of_coins = [Coin() for _ in range(n)]

for coin in lst_of_coins:
    coin.flip()
    if coin.side == 'heads':
        heads += 1
    else:
        tails += 1

heads = round(heads / n * 100 , 2)
tails = round(tails / n * 100 , 2)

print (f'Выпавших орлов {heads}%')
print (f'Выпавших решек {tails}%')

# Задание: создайте список из n-монеток. Подбросьте(flip) все монетки.
# выведите соотношение выпавших орлов и решек в процентах
