#! /usr/bin/env python3


class ClassBase(type):
    __attributes = dict()

    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)

        attrs = []
        with open(cls.__name__ + '.txt') as attr_file:
            for line in attr_file.readlines():
                var, value = line.split(':', 1)
                attrs.append((var, value))

        ClassBase.__attributes[cls] = attrs

    def __call__(cls, *args, **kwargs):
        instance = super().__call__(*args, **kwargs)

        for attr in ClassBase.__attributes.get(cls):
            setattr(instance, attr[0], attr[1])

        return instance


class A(metaclass=ClassBase):
    pass


def main():
    instance = A()
    print(instance.x)
    print(instance.c == 'sdklhsldf')


if __name__ == "__main__":
    main()
