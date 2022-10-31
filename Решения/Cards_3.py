import random


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit    # Масть карты
        # Меняем название масти на значок(юникод символ)
        suits = {'Diamonds': '\u2666', 'Hearts': '\u2665', 'Spades': '\u2660', 'Clubs': '\u2663'}
        for key, value in suits.items():
            if self.suit == key:
                self.suit = value

    def __repr__(self):
        return f'{self.value}{self.suit}'

    def __eq__(self, other_card):
        if self.suit == other_card.suit and self.value == other_card.value:
            return True
        return False

    def __gt__(self, other_card):
        # создаем 2 словаря: значения и масти
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['\u2665', '\u2666', '\u2663', '\u2660']
        # находим индексы значений карт
        for i in range(len(values)):
            if self.value == values[i]:
                v1 = i
                break
        for i in range(len(values)):
            if other_card.value == values[i]:
                v2 = i
                break
        # сравниваем значения карт
        if v1 > v2:
            return True
        elif v1 < v2:
            return False
        # если значения совпали, находим индексы мастей
        else:
            for i in range(len(suits)):
                if self.suit == suits[i]:
                    s1 = i
                    break
            for i in range(len(suits)):
                if other_card.suit == suits[i]:
                    s2 = i
                    break
            # сравниваем карты по масти
            if s1 < s2:
                return True
            return False

    def __lt__(self, other_card):
        return not self > other_card


class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['\u2665', '\u2666', '\u2663', '\u2660']

        self.cards = []
        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def __getitem__(self, index):
        return self.cards[index]

    def __repr__(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        return f"cards[{len(self.cards)}]: {', '.join(item.__repr__() for item in self.cards)}"

    def draw(self, x):
        # Принцип работы данного метода прописан в 00_task_deck.md
        tmp_lst = []
        for _ in range(x):
            tmp_lst.append(self.cards[0])
            del self.cards[0]
        return tmp_lst

    def shuffle(self):
        # Обратите внимание на: https://www.w3schools.com/python/ref_random_shuffle.asp
        random.shuffle(self.cards)


'''
создадим имитацию одного хода в “Дурака без козырей”:

1. Создайте колоду из 52 карт. Перемешайте ее.
2. Первый игрок берет сверху 10 карт
3. Второй игрок берет сверху 10 карт.
4. Игрок-1 ходит:
    1. игрок-1 выкладывает самую маленькую карту по значению
    2. игрок-2 пытается бить карту, если у него есть такая же масть, но значением больше.
    3. Если игрок-2 не может побить карту, то он проигрывает.
    4. Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
5. Выведите в консоль максимально наглядную визуализацию данного игрового хода.
'''

deck = Deck()
print(deck)
print('=' * 40)

deck.shuffle()
print(deck)
print('=' * 40)

hand_1 = deck.draw(10)
hand_2 = deck.draw(10)

print(f'{hand_1 = }')
print(f'{hand_2 = }')

max_card = Card('A', '\u2665')  # Туз червей

# ход первого игрока, находим карту с минимальным значением

tmp_1 = max_card
for card in hand_1:
    if card < tmp_1:
        tmp_1 = card
print(f"Ход первого игрока: {tmp_1}")

# удаляем карту
for card in hand_1:
    if card == tmp_1:
        hand_1.remove(card)
        break

# ход второго игрока
tmp_2 = max_card
for card in hand_2:
    if tmp_1 < card < tmp_2 and card.suit == tmp_1.suit:
        tmp_2 = card

if tmp_2 in hand_2:
    print(f"Ход второго игрока: {tmp_2}")
    # удаляем карту, если был сделан ход
    hand_2.remove(tmp_2)
    for card in hand_1:
        if card.value == tmp_1.value or card.value == tmp_2.value:
            print(f"Ход первого игрока: {card}")
            hand_1.remove(card)
            break
else:
    print("Второму игроку нечем крыть")
print("Игра окончена")

