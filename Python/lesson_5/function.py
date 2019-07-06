def func(a):
    a += 1
    return a

print(func(3))

def add(x, y):
    summa = x + y
    return summa

def too_add(x, y):
    return add(add(x, y), add(x, y))

print(too_add(5, 6))