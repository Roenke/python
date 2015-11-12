#! /usr/bin/env python3
import random
class random_iterator:
    def __init__(self, n):
        self.count = 0
        self.n = n
        random.seed()

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            self.count += 1
            return int(random.random() * self.n)
        raise StopIteration


def merge(list1, list2):
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            yield list1[i]
            i+=1
        else:
            yield list2[j]
            j+=1
    if i < len(list1):
        for x in list1:
            yield x
    if i < len( list2):
        for x in list2:
            yield x


def main():
    it = random_iterator(10)
    for r in random_iterator(10):
        print(r, end=' ')

    print('')
    for r in merge([1, 4, 5, 7, 9], [2, 3, 5, 78]):
        print(r, end=' ')




if __name__ == "__main__":
    main()
