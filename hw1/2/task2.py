#! /usr/bin/env python3
from collections import namedtuple

mod = 100000007

Query = namedtuple('Query', ('i1', 'j1', 'h1', 'w1', 'i2', 'j2', 'h2', 'w2'))

import sys

hashes = list()


def create_hashes(n, m, matrix):




def is_submatrix_eq(query):
    if query.h1 != query.h2 or query.w1 != query.w2:
        return 0



def main():
    n, m = (int(x) for x in sys.stdin.readline().split())

    matrix = list()
    i = 0
    while i < n:
        matrix.append([int(x) for x in sys.stdin.readline().split()])
        i += 1
    print(matrix)

    q = int(sys.stdin.readline()[0])

    hashes = create_hashes(n, m, matrix)

    for i in range(q):
        query = Query(*[int(x) for x in sys.stdin.readline().split()])
        print(is_submatrix_eq(query))


if __name__ == '__main__':
    main()
