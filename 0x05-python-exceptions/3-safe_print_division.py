#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        if result != None:
            print("inside result: {:.0f}".format(result))
        else:
            print("inside result: None")
    return result
