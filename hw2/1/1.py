#! /usr/bin/env python3


def final(func):
    WithFinals.add_final_function(func)
    return func


class WithFinals(type):
    __final_methods = set()
    __class_finals_map = dict()

    def __new__(mcs, name, bases, fields):
        cl = super(WithFinals, mcs).__new__(mcs, name, bases, fields)
        parents = [x for x in cl.mro()
                   if isinstance(x, WithFinals) and not (x is cl)]
        for key, value in fields.items():
            for parent in parents:
                if key in WithFinals.__class_finals_map[parent.__name__]:
                    raise Exception("Wrong")

        WithFinals.__class_finals_map[name] = list()
        for key, value in fields.items():
            if value in WithFinals.__final_methods:
                WithFinals.__class_finals_map[name].append(key)

        return cl

    @staticmethod
    def add_final_function(func):
        WithFinals.__final_methods.add(func)


class A(metaclass=WithFinals):
    @final
    def __add__(self, other):
        pass

    @final
    def my_final_method(self):
        pass


class B(metaclass=WithFinals):
    def my_final_method(self):
        pass


class C(A, B):
    pass


class D(C):
    def my_final_method(self):
        pass


def main():
    pass


if __name__ == "__main__":
    main()
