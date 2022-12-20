def selection_sort(a):
    '''Сортировка выбором при помощи FOR'''
    lenght = len(a)
    for i in range (lenght - 1):
        idx_min = i
        for j in range (i+1, lenght):
            if a[j] < a[idx_min]:
                idx_min = j
        a[idx_min], a[i] = a[i], a[idx_min]


def selection_sort_via_while(a):
    '''Сортировка выбором при помощи WHILE'''
    print ('Before sort', a)
    i = 0
    while i < len(a) - 1:
        m = i
        j = i + 1
        while j < len(a):
            if a[j] < a[m]:
                m = j
            j += 1
        a[i], a[m] = a[m], a[i]
        i+=1

array_ = [32, 13, 56, 4, 4, 33, -4, 7, 89]
selection_sort(array_)
print(array_)

array_2 = [32, 13, 56, 4, 4, 33, -4, 7, 89, 15, 22, 333]
selection_sort_via_while(array_2)
print(array_2)