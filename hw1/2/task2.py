from collections import namedtuple
import sys

mod = 100000007
p = 1000003
q = 2000029

Query = namedtuple('Query', ('i1', 'j1', 'h1', 'w1', 'i2', 'j2', 'h2', 'w2'))


def create_hashes(n, m, matrix):
    hash_array = [[1] * m for _ in range(n)]
    hash_array[0][0] = matrix[0][0]

    ps = [1] * n
    qs = [1] * m

    for j in range(m - 1):
        qs[j + 1] = (qs[j] * q) % mod
        tmp = (matrix[0][j + 1] * qs[j + 1]) % mod
        hash_array[0][j + 1] = (hash_array[0][j] + tmp) % mod

    for i in range(n - 1):
        ps[i + 1] = (ps[i] * p) % mod
        tmp = (ps[i + 1] * matrix[i + 1][0]) % mod
        hash_array[i + 1][0] = (hash_array[i][0] + tmp) % mod

    for i in range(1, n):
        for j in range(1, m):
            h = (hash_array[i - 1][j] + hash_array[i][j - 1]) % mod
            h = (h - hash_array[i - 1][j - 1] + mod) % mod
            tmp = (qs[j] * ps[i]) % mod
            hash_array[i][j] = (h + (tmp * matrix[i][j]) % mod) % mod

    return ps, qs, hash_array


def eval_hash(i, j, h, w, hashes):
    h, w = h - 1, w - 1
    hs = hashes[i + h][j + w]
    if i > 0:
        hs = (hs - hashes[i - 1][j + w] + mod) % mod
    if j > 0:
        hs = (hs - hashes[i + h][j - 1] + mod) % mod
        if i > 0:
            hs = (hs + hashes[i - 1][j - 1]) % mod
    return hs


def main():
    n, m = (int(x) for x in sys.stdin.readline().split())
    matrix = [[int(a) for a in sys.stdin.readline().split()]
              for _ in range(n)]

    ps, qs, hashes = create_hashes(n, m, matrix)

    count = int(sys.stdin.readline())
    for i in range(count):
        i1, j1, h1, w1, i2, j2, h2, w2 = \
            [int(x) for x in sys.stdin.readline().split()]
        if h1 != h2 or w1 != w2:
            print(0)
            continue

        hs1 = eval_hash(i1, j1, h1, w1, hashes)
        hs2 = eval_hash(i2, j2, h2, w2, hashes)

        hs1 = (((hs1 * ps[i2]) % mod) * qs[j2]) % mod
        hs2 = (((hs2 * ps[i1]) % mod) * qs[j1]) % mod

        if hs1 == hs2:
            print(1)
        else:
            print(0)


if __name__ == '__main__':
    main()
