#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    add = 0
    i = 1
    if len(sys.argv) - 1 == 0:
        add = 0
    while i <= len(sys.argv) - 1:
        add = add + int(sys.argv[i])
        i = i + 1
    print("{:d}".format(add))
