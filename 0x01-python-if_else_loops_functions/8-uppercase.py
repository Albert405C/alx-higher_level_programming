#!/usr/bin/python3
def uppercase(str):
    for char in input_str:
        if ord(char) >= 97 and ord(char) <= 122:
            char = char.upper()
        print("{}".format(char), end="")
    print()
