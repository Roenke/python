#! /usr/bin/env python3

import sys

def decorate_print(fun):
    def wrapper(*args, sep=' ', end='\n', file=None):
        fun('I made it. This is my new print function')
        fun(*args, sep=' ', end='\n', file=None)
    return wrapper

print = decorate_print(print)


def main():
    sys.stdout.write('test:\n')
    print('some text')


if __name__ == "__main__":
    main()
