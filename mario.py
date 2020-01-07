# This code prints a symetrical tower of blocks (represented by '#'s), whos size depends on user input
from cs50 import get_int

while True:
    height = get_int("Height: ")
    # This section will skip to the next while iteration if the user input isn't correct
    if (height < 1 or height > 8):
        continue
    # Printing of the blocks
    for i in range(1, height + 1):
        print(' ' * (height-i) + '#' * i + '  ' + '#' * i)

    if (height > 0 and height < 9):
        break