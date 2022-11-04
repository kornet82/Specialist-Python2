print(sum([45, 23, 27, 89]))

sum = 5
# print(sum([45, 23, 27, 89]))

# del sum
def some_sum(arg):
    if hasattr(some_sum, 'counter'):
        some_sum.counter += 1
    else:
         some_sum.counter = 1
    return arg + 10

print(some_sum(4))
# some_sum.counter = 0
print(some_sum(4))
print(some_sum(10))
if some_sum.counter > 2:
    del some_sum
# print(some_sum(10)) # Error


# from builtins import *
# from builtins import sum
#
# print(sum([45, 23, 27, 89]))
# print(sum([45, 13, 7, 89]))

