from datetime import datetime

def time_it(func):
    def wrapper():
        start = datetime.now()
        result = func()
        print(datetime.now() - start)
        return result
    return wrapper


@time_it
def one():
    # start = datetime.now()
    l = []
    for i in range(10**4):
        if i % 2 == 0:
            l.append(i)
    # print(datetime.now() - start)
    return l

@time_it
def two():
    # start = datetime.now()
    l = [i for i in range(10**4) if i % 2 == 0]
    # print(datetime.now() - start)
    return l

l1 = one()
l2 = two()
print(l1)
print(l2)
