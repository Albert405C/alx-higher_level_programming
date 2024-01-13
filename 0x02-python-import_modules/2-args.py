#!/usr/bin/python3
from sys import argv  
if __name__ == "__main__":
    num_args = len(argv) - 1  

    if num_args == 0:
        print("Number of argument(s): 0.")
    elif num_args == 1:
        print("Number of argument(s): 1.")
    else:
        print("Number of argument(s): {}.".format(num_args))
    if num_args > 0:
        print()
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))
