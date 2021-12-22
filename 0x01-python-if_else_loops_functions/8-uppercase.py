#!/usr/bin/python3
def uppercase(str):
    for upper in str:
        if ord(upper) >= 97 and ord(upper) <= 122:
            letter = ord(upper) - 32
        else:
            letter = ord(upper)
        print("{}".format(chr(letter)), end="")
    print("")
