#! /usr/bin/env python3

def get_value(x, y, n):
    if n % 2 == 1:
        if y >= abs(x - n // 2) and y < -abs(x - n // 2) + n:
            return "1"
    elif y >= -x + (n / 2) - 1 and y > x - (n / 2) - 1 \
        and y < -x + 3 * n / 2 and y < x + (n / 2) + 1:
            return "1"
    return "0"

def main():
    N = int(input())
    result = ((get_value(i, j, N) for j in range(N)) for i in range(N))
    for line in result:
        for value in line:
            print(value, end=' ')
        print('')

if(__name__ == "__main__"):
    main()
