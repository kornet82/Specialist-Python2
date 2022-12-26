def recursion(a,b):
    if a > b:
        #Шаг рекурсии / рекурсивное условие
        return str(a) + ">" + recursion(a - 1, b)
    else:
        # Базовый случай
        if a == b:
            return str(a)
        #Шаг рекурсии / рекурсивное условие
        return str(a) + '<' + recursion(a + 1, b)


print(recursion(20,15)) # Out -> 20>19>18>17>16>15
print(recursion(10,15)) # Out -> 10<11<12<13<14<15
