#! /usr/bin/env python3

class my_resource(object):
    def __init__(self):
        self.items = [1,2,4,5,6]

    def __enter__(self):
        print('enter section')
        return self

    def free(self):
        self.items = []

    def __exit__(self, type, value, trace):
        print('exit sectoion')
        self.free()
        print(type, value, trace)

    def calc(self):
        print('in calc()')
        result = sum(self.items)
        return result


def main():
    try:
        with my_resource() as my_res:
            my_res.calc()
            raise Exception('oops')
    except:
        print('error')

    print('continue?')



if __name__ == "__main__":
    main()
