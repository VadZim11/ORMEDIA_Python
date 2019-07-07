# Создадим пустую функцию которая ничего не возвращает

def none_func():
    pass

# Написать функцию, которая принимает число, возвращает его значение умноженное на два

def duble_func(x):
    return x*2

print(duble_func(8))

# Напишем функцию, которая определяет параметр на чётность. Если чётное число принтим (‘yes’) в ином случае (‘no’)

def chet_nechet_fun(x):
    if x % 2 != 1 :
        print("Yes")
        return x
    else:
        print("No")
        return x

chet_nechet_fun(1415)
chet_nechet_fun(1000)

# Пишем функцию, принимающую два аргумента. После чего проверим, если первое число больше 10, принтим (‘да’). Если меньше(‘нет’)

def ten_fun(a, b):
    if a > 10 :
        return print("Yes")
    else: return print("No")

ten_fun(15, 1)
ten_fun(4, 25)

# Написать лямбда функцию, которая делит по модулю(%) два аргумента

lumd = lambda x, y : x % y

print(lumd(10,2))
print(lumd(2563,81))

# Создадим функцию с простыми командами. Обернём её в декоратор, который бы дополнял возможности функции

def decor(func):
    def wrap():
        print("Python. ", end="", flush=True)
        func()
        print("world!")
    return wrap

@decor
def show():
    print("Hello ",end="", flush=False) # Пропуск ввода

show()

# Использовать функцию map и filter

list_1 = [1, 2, 6, 8, 78, 52]
print("List: " + str(list_1))

list_2 = list(map(duble_func, list_1))
print("List afte map: " + str(list_2))

list_2 = list(filter(chet_nechet_fun, list_1))
print("List afte filter: " + str(list_2))

# Создадим чистую и нечистую функцию

def clean_fun(x):
    a = 2
    return x*a

a = 3
def no_clean_fun(x):
    return x*a

# Сделать функцию поиска минимума и максимума в списке

def max_fun(list_fun):
    a = list_fun[0]
    for i in list_fun:
        if i > a:
            a = i
    return a  

def min_fun(list_fun):
    a = list_fun[0]
    for i in list_fun:
        if i < a:
            a = i
    return a  

list_test = [1, 23, 52, 8, 65, 32, 21]

print("Test list: " + str(list_test))
print("Max in list: " + str(max_fun(list_test)))
print("Min in list: " + str(min_fun(list_test)))

# Написать функцию, которая определяет, является ли год високосным. Пользователь вводит год, если он високосный, то функция возвращает True. Если нет, то False

