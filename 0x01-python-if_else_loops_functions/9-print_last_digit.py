#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -1 * number
    r = number % 10
    while r > 10:
        r = r % 10
    print("{:d}".format(r), end="")
    return r
