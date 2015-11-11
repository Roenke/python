#! /usr/bin/env python3

def main():
    print('Raw strings, no escape: ', r'\t')

    # строки не изменяемы

    # можно проверить на вхождение подстроки
    print('find substring:', 'sub' in 'find substring:')

    # отличие index от find в том, что index 
    # выбрасывает исключение в случае неуспеха

    print("%s %s %s this string" % ('you', 'can', 'format'))

    # Есть много функций для модификации строк, например:
    # upper, lower, [l|r]strip
    # Все они возвращают новую строку

    # Со строками можно делать split() и join()
    # В join элементы списка обязаны иметь строковый тип

if(__name__ == "__main__"):
    main()
