'''
5+add(4)
    4+add(3)
        3+add(2)
            2+add(1)
                Базовый случай == 1 -> 1
'''

def add(n):
    if n == 1:
        print(n)
        return 1
    else:
        print(n)
        return n + add(n - 1)
print ('Рекурсивная сумма =', add(int(input("Введите число для подсчета рекурсивной суммы:"))))
