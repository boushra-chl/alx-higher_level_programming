#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv) - 1
    print(f"{num_args} {'arguments.' if num_args == 0 else 'arguments:'}")
    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
