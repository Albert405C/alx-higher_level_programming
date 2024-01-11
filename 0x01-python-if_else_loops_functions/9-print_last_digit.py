#!/usr/bin/python3
i = 0
last_digit = abs(i) % 10

def print_last_digit(number):
    for i in range(11):
        print("{}".format(i), end="")
        last_digit = abs(i) % 10
