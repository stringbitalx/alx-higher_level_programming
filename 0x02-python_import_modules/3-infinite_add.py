#!/usr/bin/python3

if __name == "__main__":
    """Print the addition of all arguments"""
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sys.argv[1 + 1])
    print("{}".format(total))
