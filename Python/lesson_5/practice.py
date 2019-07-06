def null_function():
    print("Hello!")

def too(x):
    print(x*2)

def chet_nechet(x):
    if x % 2 == 1 :
      print("no")
    else: print("yes")

def max_10(x, y):
    if x > 10:
        print("yes")
    else: print("no")

x = int(input())

y = x + 2

null_function()
too(x)
chet_nechet(x)
max_10(x, y)