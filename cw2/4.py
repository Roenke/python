#! /usr/bin/env python3

decorated_functions = list()

def apply(func, testFunc):
    func = testFunc(2)
    def my_decorator(fun):
        decorated_functions.append((fun, testFunc))
        def wrapper(*args):
            found = False
            for f, test in decorated_functions:
                if f == func and test(args):
                    f(args)
                    found = True
            if not found:
                fun(args)
        return wrapper

    return my_decorator


def test1(num):
    return num == 1


def test2(num):
    return num > 3


def foo(num):
    print('Original')


@apply(foo, test1)
def foo2(num):
    print('Modified')


@apply(foo, test2)
def foo3(num):
    print('Magic')


def main():
    foo(-1)
    foo(1)
    foo(2)
    foo(4)


if __name__ == "__main__":
    main()
