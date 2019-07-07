def decor(func):
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

@decor
def show():
    print("now!")

show()