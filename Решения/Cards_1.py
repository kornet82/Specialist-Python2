import random

# все масти в белом цвете
suits_1 = ('\u2664','\u2667','\u2662','\u2661')  # ('♤', '♧', '♢', '♡')
# все масти в черном цвете
suits_2 = ('\u2660','\u2663','\u2666','\u2665')  # ('♠', '♣', '♦', '♥')
name_suits = 'Spades ', 'Clubs', 'Diamonds', 'Hearts'  # для кортежа круглые скобки необязательны
suits_names2int = {name_suits[k]: k for k in range(4)} # {'Spades ': 0, 'Clubs': 1, 'Diamonds': 2, 'Hearts': 3}

card_values = dict(zip(list(range(14)), list(str(i) for i in range(2, 11)) + ['J','Q','K','A'] ))
card_values2int = dict((v, k) for k, v in card_values.items())

# Белые или черные цвета мастей
def icon_of_player(suit, player: int = 1):
    if type(suit) == str:
        suit = suits_names2int[suit]
    if player == 1:
        return suits_1[suit]
    elif player == 2:
        return suits_2[suit]
    return None


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit    # Масть карты

    def to_str(self, player=1):
        return self.value + icon_of_player(self.suit, player)

    def __str__(self, player=1):
        return self.value + icon_of_player(self.suit, player)

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def more(self, other_card):
        my_value = card_values2int[self.value]  # Число от 0 до 13
        other_value = card_values2int[other_card.value] # Число от 0 до 13

        if my_value > other_value:
            return True
        if my_value < other_value:
            return False
        # Если у нас равны значения и масти, выкидываем исключение
        if self.equal_suit(other_card):
            raise Exception('Краплёные!!!')

        my_suit = suits_names2int[self.suit]   # Число от 0 до 3
        other_suit = suits_names2int[other_card.suit]  # Число от 0 до 3
        return my_suit > other_suit

    def less(self, other_card):
        return not self.more(other_card)

    def __lt__(self, other_card):
        return self.less(other_card)

    def __gt__(self, other_card):
        return self.more(other_card)

class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = [Card(card_values[j], name_suits[i]) for i in range(4) for j in range(13)]

    def show(self, player=1):
        str_return = f"deck[{len(self.cards)}]: "
        for i in range(len(self.cards)):
            str_return += self.cards[i].to_str(player) + ', '
        str_return = str_return.removesuffix(', ')
        return str_return

    def draw(self, x):
        # Variant 1
        # new_deck = Deck()
        # new_deck.cards = self.cards[:x]
        # self.cards = self.cards[x:]

        # Variant 2
        new_deck = Deck()
        drawn_cards = [self.cards[i] for i in range(x)]
        new_deck.cards = drawn_cards
        self.cards= [self.cards[i] for i in range(x, len(self.cards))]
        return new_deck

    def shuffle(self):
        # Обратите внимание на: https://www.w3schools.com/python/ref_random_shuffle.asp
        random.shuffle(self.cards)

    def copy_with_suit(self, suit):
        new_deck = Deck()
        matched_cards = [self.cards[i] for i in range(len(self.cards)) if self.cards[i].suit == suit]
        new_deck.cards = matched_cards
        return new_deck




# ===========================================================================
# Проверка работы методов to_str() и __str__()
# hearts_cards = [Card(card_values[i],'Diamonds') for i in range(13)]
# # TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
# for card in hearts_cards:
#     print(card.to_str(), end=' ')
#
# print()
# print(*hearts_cards)
# ============================================================================
print('Старт игры!')
print('=' * 40)
deck = Deck()
print(deck.show())

print('=' * 40)
deck.shuffle()
print(deck.show())
print('=' * 40)

# Вернуть первые 10 карт из перемешанной колоды, осталось 42 карты
hand1 = deck.draw(10)
print(hand1.show(1))
print('=' * 40)

# Вернуть первые 10 карт из перемешанной колоды, осталось 32 карты
hand2 = deck.draw(10)
print(hand2.show(2))
print('=' * 40)

print('Остаток: '+ deck.show())  # осталось 32 карты
print('=' * 40)

game = 0
player = 1
while True:
    if len(hand1.cards) == 0:
        print('Ничья')
        break
    game += 1
    player = player ^ 1
    print(f'Ход {game}, игрок {player + 1}:')

    min1 = min(hand1.cards)
    print(min1.to_str(1))
    hand1.cards.remove(min1)

    # Ищем карты указанной масти для второго игрока для возможности отбиться
    hand2_answer = hand2.copy_with_suit(min1.suit)
    if len(hand2_answer.cards) == 0:
        print(f'{player} игрок проиграл')
        break

    # Сортируем, чтобы отбиться минимально возможной
    hand2_answer.cards.sort()

    min2 = None
    for i in range(len(hand2_answer.cards)):
        if hand2_answer.cards[i] > min1:
            min2 = hand2_answer.cards[i]
            break

    if min2 is None: # id(min2) == id(None)
        print(f'{player} игрок проиграл')
        break

    print(min2.to_str(2))
    hand2.cards.remove(min2)

    print('Смена игроков')
    hand1, hand2 = hand2, hand1

print('*' * 20)
print('Осталось на руках: ')
print(hand1.show(1))
print(hand2.show(2))