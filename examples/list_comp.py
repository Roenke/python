#! /usr/bin/env python3

def main():
    list1 = [(x, y) for x in range(10) 
                         for y in range(10) if x < y]
    print(list1)

    list2 = [(x, y, z) for x in range(10)
                       for y in range(10) if y < x
                       for z in range(10) if z < y]
    print(len(list2))

    # Проблема пободных выражений в том, что они всегда конечны и расходуют
    # ресурсы. Хотелось бы итерироваться по списку, которого в памяти нет.
    # В этом помогутг генераторные выражения

if(__name__ == "__main__"):
    main()
