#! /usr/bin/env python3

import datetime

call_dict = dict()


def get_fun_info(fun):

    if fun not in call_dict:
        raise Exception('Wrong data')
    return call_dict[fun]


def add_to_dict(fun, pair):
    if fun not in call_dict:
        call_dict[fun] = []
    call_dict[fun].append(pair)


def spy(func):
    def wrapper(*args):
        add_to_dict(wrapper, (str(datetime.datetime.now()), args))
        func(args)

    return wrapper


def bond(func):
    yield from get_fun_info(func)


@spy
def foo(*args):
    pass


def main():
    foo('3234')
    foo(324)
    foo('34')
    foo('32')
    foo(23, 3454, 456, 54, 645, 6)

    for (t, p) in bond(foo):
        print(t)
        print(p)


if __name__ == "__main__":
    main()
