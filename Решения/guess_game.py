from random import randint

def guess_game():
    n = randint(1,200)
    i = 1
    print('Папа загадал число от 1 до 200. Попробуйте угадать его. У вас 10 попыток')
    while i <= 15:
        u = int(input(f'{str(i)}-я попытка:'))
        if u > n:
            print('Много!')
        elif u < n:
            print('Мало!')
        else:
            print(f'Вы угадали с {i}-й попытки!')
            break
        i += 1
    else:
        print('Угадать не получилось!')

guess_game()
