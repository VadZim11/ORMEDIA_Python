import random

number_1 = random.randint(1, 100)

gvest = 0

while gvest < 7:
    print("Enter a number from 1 to 100")
    number_2 = int(input())
    gvest += 1

    if number_2 < number_1:
        print("Too low, try again")
    if number_2 > number_1:
        print("So high, try again")
    if number_2 == number_1:
        print("WIN.")
        break
else:
    print("LUSER. Number was: " + str(number_1))
