#! /usr/bin/env python3
import itertools


class Singleton(type):
    __instances = dict()

    def __call__(cls, *args, **kwargs):
        arg_id = (args, tuple(kwargs.items()))
        if arg_id in Singleton.__instances:
            return Singleton.__instances[arg_id]
        instance = super().__call__(*args, **kwargs)
        Singleton.__instances[arg_id] = instance
        return instance


class A(metaclass=Singleton):
    def __init__(self, *args, **kwargs):
        pass


def main():
    a = A(2)
    b = A(2)
    c = A(3)
    d1 = A(2, arg1='sdfjsd', arg2='dfkjg;df')
    d2 = A(2, arg1='sdfjsd', arg2='dfkjg;df')
    d3 = A(3, arg1='sdfjsd', arg2='dfkjg;df')
    d4 = A(3, arg1='sdfjs', arg2='dfkjg;df')
    d5 = A(2, arg1='sdfjs', arg2='dfkjg;df')
    # Tests. All must be True.

    print(a is b)
    print(d1 is d2)

    different = [a, c, d1, d3, d4, d5]
    for (f, s) in itertools.combinations(different, 2):
        print(not (f is s))


if __name__ == "__main__":
    main()
