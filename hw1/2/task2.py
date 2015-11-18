#! /usr/bin/env python3
from collections import namedtuple

mod = 100000007
p = 1000003
q = 2000029
Query = namedtuple('Query', ('i1', 'j1', 'h1', 'w1', 'i2', 'j2', 'h2', 'w2'))

import sys

Hashes = namedtuple('Hashes', ('p', 'q'))
pow_q = list([1])
pow_p = list([1])


def create_hashes(n, m, matrix):
    hash_array = list()
    line = [0] * m
    for i in range(n):
        hash_array.append(line[0:])

    prev = 1
    for i in range(n - 1):
        pow_p.append((prev * p) % mod)
        prev = pow_p[-1]

    prev = 1
    for i in range(m - 1):
        pow_q.append((prev * q) % mod)
        prev = pow_q[-1]

    hash_array[0][0] = matrix[0][0]
    for i in range(m - 1):
        hash_array[0][i + 1] = (hash_array[0][i] + pow_q[i + 1] * matrix[0][i + 1]) % mod

    for i in range(n - 1):
        hash_array[i + 1][0] = (hash_array[i][0] + pow_p[i + 1] * matrix[i + 1][0]) % mod

    for i in range(n - 1):
        row = i + 1
        for j in range(m - 1):
            col = j + 1
            tmp = (pow_p[row] * pow_q[col] * matrix[row][col]) % mod
            hash_array[row][col] = (hash_array[i][col] + hash_array[row][j] - hash_array[i][j] + tmp) % mod

    return hash_array


def eval_hash(x1, x2, y1, y2, hashes):
    result = hashes[x2][y2]
    if x1 > 0:
        result -= hashes[x1 - 1][y2]
    if y1 > 0:
        result -= hashes[x2][y1 - 1]
        if x1 > 0:
            result += hashes[x1 - 1][y1 - 1]
    return result


def is_sub_matrix_eq(query, hashes):
    if query.h1 != query.h2 or query.w1 != query.w2:
        return 0

    h1 = eval_hash(query.i1, query.i1 + query.h1 - 1, query.j1, query.j1 + query.w1 - 1, hashes)
    h2 = eval_hash(query.i2, query.i2 + query.h2 - 1, query.j2, query.j2 + query.w2 - 1, hashes)
    if (h1 * pow_p[query.i2] * pow_q[query.j2]) % mod == (h2 * pow_p[query.i1] * pow_q[query.j1]) % mod:
        return 1

    return 0


def main():
    f = open('max_test.in', 'r')
    sys.stdin = f
    n, m = (int(x) for x in sys.stdin.readline().split())

    matrix = list()
    i = 0
    while i < n:
        matrix.append([int(x) for x in sys.stdin.readline().split()])
        i += 1

    q = int(sys.stdin.readline().split()[0])

    hashes = create_hashes(n, m, matrix)

    count = 0
    for i in range(q):
        query = Query(*[int(x) for x in sys.stdin.readline().split()])
        # print()
        if is_sub_matrix_eq(query, hashes) == 1:
            count += 1

    print(count)


if __name__ == '__main__':
    main()
