#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    tmp = -1 * number
if number > 0:
    tmp = number
if 0 < tmp < 10:
    r = tmp
    if r > 5:
        print(f"Last digit of {number} is {r} and is greater than 5")
    elif r == 0:
        print(f"Last digit of {number} is {r} and is 0")
    elif 0 < r <= 6:
        print(f"Last digit of {number} is {r} and is less than 6 and not 0")
elif 10 <= tmp < 100:
    r = tmp % 10
    if r > 5:
        print(f"Last digit of {number} is {r} and is greater than 5")
    elif r == 0:
        print(f"Last digit of {number} is {r} and is 0")
    elif 0 < r <= 6:
        print(f"Last digit of {number} is {r} and is less than 6 and not 0")
elif 100 <= tmp < 1000:
    r = tmp % 100
    r = r % 10
    if r > 5:
        print(f"Last digit of {number} is {r} and is greater than 5")
    if r == 0:
        print(f"Last digit of {number} is {r} and is 0")
    elif 0 < r <= 6:
        print(f"Last digit of {number} is {r} and is less than 6 and not 0")
elif 1000 <= tmp < 10000:
    r = tmp % 1000
    r = r % 100
    r = r % 10
    if r > 5:
        print(f"Last digit of {number} is {r} and is greater than 5")
    elif r == 0:
        print(f"Last digit of {number} is {r} and is 0")
    elif 0 < r <= 6:
        print(f"Last digit of {number} is {r} and is less than 6 and not 0")
