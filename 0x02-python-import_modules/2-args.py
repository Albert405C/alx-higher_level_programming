#!/usr/bin/python3
if __name__ == "__main__":
    # Get the number of arguments
    num_args = len(argv) - 1  # Subtract 1 to exclude the script name itself

    # Print the number of arguments
    if num_args == 0:
        print("Number of argument(s): 0.")
    elif num_args == 1:
        print("Number of argument(s): 1.")
    else:
        print("Number of argument(s): {}.".format(num_args))

    # Print the list of arguments
    if num_args > 0:
        print()
        for i, arg in enumerate(argv[1:], start=1):
            print("{}: {}".format(i, arg))

