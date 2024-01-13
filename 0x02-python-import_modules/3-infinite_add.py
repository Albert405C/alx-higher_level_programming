#!/usr/bin/python3
if __name__ == "__main__":
    """print arguments"""
    arguments = argv[1:]
    result = sum(int(arg) for arg in arguments)
    print(result)
