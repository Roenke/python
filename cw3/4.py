stack = list()
level = 0


def test1(num):
    return (num == 1)


def test2(num):
    return (num > 3)


def foo(num):
    print('Original')
    test1(num)


def foo2(num):
    foo(num)
    test1(num)


def printStack():
    for level, name, args, kwargs in stack:
        print('\t' * level + name
              + '(' + ', '.join([str(x) for x in list(args)])
              + ', '.join([str(x) for x in list(kwargs.items())]) + ')')


def add_all():
    glob = globals().copy()
    for record in glob:
        if hasattr(glob[record], '__call__'):
            def external_wrapper(name, *args, **kwargs):
                def wrapper(*args, **kwargs):
                    globals()['level'] += 1
                    stack.append((globals()['level'], glob[name].__name__, args, kwargs))
                    glob[name](*args, **kwargs)
                    globals()['level'] -= 1
                return wrapper

            globals()[record] = external_wrapper(record)


def main():
    add_all()
    foo2(1)
    foo(2)
    printStack()


if __name__ == "__main__":
    main()
