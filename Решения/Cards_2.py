import random


suit_tuple = 'Spades', 'Clubs', 'Diamonds', 'Hearts'
value_tuple = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')

SUITS = {'Spades': '\u2660',
         'Hearts': '\u2665',
         'Diamonds': '\u2666',
         'Clubs': '\u2663'}

class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit    # Масть карты

    def __str__(self):
        for key, value in SUITS.items():
            if key == self.suit:
                return f'{self.value}{value}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __gt__(self, other_card):
        if self.value == other_card.value:
            return suit_tuple.index(self.suit) > suit_tuple.index(other_card.suit)
        return self.value > other_card.value

    def __lt__(self, other_card):
        if self.value == other_card.value:
            return suit_tuple.index(self.suit) < suit_tuple.index(other_card.suit)
        return self.value < other_card.value


class Deck:
    def __init__(self):
        self.hand = None
        self.cards = []
        for suit in suit_tuple:
            self.cards += [Card(value, suit) for value in value_tuple]

    def show(self):
        print(f'deck[{len(self.cards)}]:', end=" ")
        for card in self.cards:
            print(card, end=", ")
        print()

    def __str__(self):
        s = f'deck[{len(self.cards)}]: '
        s += ', '.join([str(card) for card in self.cards])
        return s

    def draw(self, x):
        self.hand = self.cards[:x]
        self.cards = self.cards[x:]
        return self.hand
    #
    def shuffle(self):
        random.shuffle(self.cards)


deck = Deck()
print(deck)
# Задачи - реализовать нативную работу с объектами:
# 1. Вывод колоды в терминал:
deck.show()
print('=' * 40)

deck.shuffle()
deck.show()
print('=' * 40)

# 2. Вывод карты в терминал:
hand1 = deck.draw(10)
print('hand1:', *hand1)
hand2 = deck.draw(10)
print('hand2:', *hand2)



# # 3. Сравнение карт:
if hand1[0] > hand2[0]:
    print(f"{hand1[0]} больше {hand2[0]}")
else:
    print(f"{hand1[0]} меньше {hand2[0]}")

print(deck)