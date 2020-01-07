# This program processes a credit card number input and identifies what type of credit card it is or if it is INVALID
from cs50 import get_string

while True:

    innum = get_string("Number: ")
    # ensures input is a number with no other characters
    try:
        num = int(innum)
    except ValueError:
        continue

    # save the first two digits of the input
    dig1 = int(innum[0])
    dig2 = int(innum[1])

    # carry out sum of every other number starting from the last number, as per Luhn's Algorithm
    calc = 0
    while (num > 0):
        calc = calc + (num % 10)
        num = int(num / 100)

    num = int(int(innum) / 10)
    # carry out the remaining part of Luhn's Algorithm
    while (num > 0):
        x = (num % 10) * 2

        if x > 9:
            x = (x % 10) + 1

        calc = calc + x
        num = int(num / 100)

    # detects if card number is INVALID, or if it belongs to a specific card type
    if calc % 10 == 0:

        if len(innum) == 15 and (dig1 == 3 and (dig2 == 4 or dig2 == 7)):
            print("AMEX")
            break

        elif len(innum) == 16 and dig1 == 5 and (dig2 > 0 and dig2 < 6):
            print("MASTERCARD")
            break

        elif (len(innum) == 13 or len(innum) == 16) and dig1 == 4:
            print("VISA")
            break

        else:
            print("INVALID")
            break

    elif calc % 10 != 0:
        print("INVALID")
        break

