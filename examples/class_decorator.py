#! /usr/bin/env python3


def my_class_decorator(c):
    print(c)
    c.d = 100.
    return c


@my_class_decorator
class A():
    def __init__(self):
        self.a = 10


def main():
    a = A()
    print(a.a)
    print(a.d)

if __name__ == "__main__":
    main()
