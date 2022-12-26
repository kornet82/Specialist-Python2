def qsort(x):
    if len(x) < 2:
        return x
    else:
        pivot = x[0]
        print(f'{pivot =}')
        less = [i for i in x[1:] if i <= pivot]
        print(f'{less =}')
        greater = [i for i in x[1:] if i > pivot]
        print(f'{greater =}')
        return qsort(less) + [pivot] + qsort(greater)

arr = [54, 1, 2, 3, 52, 3, 1, 2, 4, 5, 3, 67, 2, 253]
print(qsort(arr))

