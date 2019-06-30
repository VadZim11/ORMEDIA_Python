import random

number_1 = random.randint(1, 25)

gvest = 0

while gvest < 5:
    print("Enter a number from 1 to 25")
    number_2 = int(input())
    gvest += 1

    if gvest == 5:
        print("LOSER. Number was: " + str(number_1))
        break
    if number_2 == number_1:
        print("WIN")
        break