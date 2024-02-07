#!usr/bin/python3
def safe_print_list(my_list=[], x=0):
    for n in my_list:
        print("{%d}".format(n), end="")
        x++
    return x
