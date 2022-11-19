'''
Написать программу для удаления всех повторяющихся элементов в списке
'''


start_list = [{"key1": "value1"},
         {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {},
         {"key1": "value1"}, {"key1": "value1"},
         {"key2": "value2"}]

for item in start_list:
    if start_list.count(item) > 1:
        start_list.remove(item)

print(start_list)




