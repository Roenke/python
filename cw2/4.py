#! /usr/bin/env python3

decorated_functions = dict()


def runner(func, *args, **kwargs):
    found = False
    for (function, test_func) in decorated_functions[func]:
        if test_func(*args, **kwargs):
            return function(*args, **kwargs)
    if not found:
        return func(*args, **kwargs)


def apply(func, testFunc):
    if "__modified__" not in func.__dict__:
        def wrapper(*args, **kwargs):
            return runner(func, *args, **kwargs)

        setattr(wrapper, "__modified__", func)
        globals()[func.__name__] = wrapper
    else:
        func = func.__modified__

    def decorator(f):
        if func not in decorated_functions:
            decorated_functions[func] = list()
        decorated_functions[func].append((f, testFunc))
        return f

    return decorator


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
