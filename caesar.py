# this program cyphers a code using Caesar's Encription
from cs50 import get_int, get_string
import sys

# ensures correct amount of command line arguments
if len(sys.argv) != 2:
    print("Usage: python caesar.py key")
    sys.exit(1)

try:
    key = int(sys.argv[1]) % 26
except ValueError:
    print("Usage: python caesar.py key")
    sys.exit(1)

plaintext = get_string("plaintext: ")

i = 0
ctext = plaintext
for c in plaintext:
    # Converts each character only if it is a letter of the alphabet
    if c.isalpha() == True:

        newc = ord(c) + key

        if (ord(c) < 91 and newc > 90) or (ord(c) < 123 and newc > 122):

            newc = newc - 26

    else:

        newc = ord(c)

    ctext = ctext[:i] + chr(newc) + ctext[i + 1:]

    i = i + 1
# Prints final output
print(f"ciphertext: {ctext}")
sys.exit(0)
