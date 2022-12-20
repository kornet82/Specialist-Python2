from random import randint

def guess_game():
    n = randint(1,1000)
    i = 1
    print('Компьютер загадал число от 1 до 1000. Попробуйте угадать его. У вас 10 попыток')
    while i <= 10:
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
