#! /usr/bin/env python3

import itertools

def main():
    student_list = [
        ('Дима', 'bi'),
        ('Оля', 'bi'),
        ('Максим', 'se'),
        ('Андрей', 'cs'),
        ('Вася', 'se'),
        ('Саша', 'se'),
        ('Юля', 'bi'),
        ('Наташа', 'cs'),
        ('Петр', 'bi')
    ]

    print(student_list)

    grouped = itertools.groupby(student_list, lambda x: x[0])
    print(grouped)

if(__name__ == "__main__"):
    main()
