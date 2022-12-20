def bubble_sort(a):
    '''Сортировка пузырьком'''
    lenght = len(a)
    for k in range(1, lenght):
        for i in range(lenght - k):
            if a[i] > a [i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
    return a

array_ = [54, 1, 2, 3, 4, 32, 12, 56, 45, 67, 222, 34, -1]
print('Before sort', array_)
print('After sort', bubble_sort(array_))
