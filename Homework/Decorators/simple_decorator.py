from datetime import datetime

def time_it(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper


@time_it
def one(x: int):
    # start = datetime.now()
    l = []
    for i in range(x):
        if i % 2 == 0:
            l.append(i)
    # print(datetime.now() - start)
    return l

@time_it
def two(x: int):
    # start = datetime.now()
    l = [i for i in range(x) if i % 2 == 0]
    # print(datetime.now() - start)
    return l

l1 = one(12)
l2 = two(12)
# print(l1)
# print(l2)
