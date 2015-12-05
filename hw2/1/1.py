#! /usr/bin/env python3

def final(func):
    WithFinals.add_final_function(func)


class WithFinals(type):
    __final_methods = set()

    def __call__(cls, *args, **kwargs):
        super(WithFinals, cls)

    @staticmethod
    def add_final_function(func):
        WithFinals.__final_methods.add(func)


class A(metaclass=WithFinals):
    pass


class B(metaclass=WithFinals):
    pass


class C(A, B):
    pass


def main():
    c = C()


if __name__ == "__main__":
    main()
