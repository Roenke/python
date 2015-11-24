#! /usr/bin/env python3

class my_iterator:
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        self

    def __next__(self):
        self.counter += 1
        return self.counter

# Простой пример на итератор в Python
def main():
    iterrator = my_iterator()
    print(next(iterrator))
    print(next(iterrator))
    print(next(iterrator))
    print(next(iterrator))

if(__name__ == "__main__"):
    main()
    