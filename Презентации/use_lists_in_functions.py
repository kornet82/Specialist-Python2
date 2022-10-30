def bad_func(a, b=[]):
    b.append(a)
    return b
#
# ## Как правильно работать со списком в
# ## качестве аргумента функции
def good_func(a, b=None):
    if b is None:
        b = []
    b.append(a)
    return b
#
lst = [4, 5, 8]
res_1 = bad_func(111, lst)
print(res_1)
res_2 = bad_func(222, res_1)
print(res_2)

res_3 = bad_func(333)
print(res_3)

# res_4 = bad_func(444, ['hello', 'hi'])
# print(res_4)

print('Неправильная работа функции')
res_5 = bad_func(555)
print(f'{res_5}')  # Out: [555]
res_6 = bad_func(666)
print(f'{res_6}') # Out [666]
# #
print('Правильная работа функции')
good_res_3 = good_func(333)
print(good_res_3)
good_res_4 = good_func(444)
print(good_res_4)
good_res_5 = good_func(555)
print(good_res_5)
#
good_res_6 = good_func(999, lst)
print(good_res_6)



