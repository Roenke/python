#! /usr/bin/env python3

def main():
    # Все отличия от списочных встраиваний заключаются в том,
    # вместо квадратных скобок используются круглые и слудющий элемент
    # вычисляется лениво

    iter1 = (x**2 for x in range(10))

    print(next(iter1))
    print(next(iter1))

if(__name__ == "__main__"):
    main()
