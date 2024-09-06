#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add
    a = 10
    b = 5
    result = add(a, b)
    print("{} + {} = {}".format(a, b, result))
    print("{} - {} = {}".format(a, b, result))
    print("{} * {} = {}".format(a, b, result))
    print("{} / {} = {}".format(a, b, result))
