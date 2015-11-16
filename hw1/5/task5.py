#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pymorphy2
import csv
import re

def solve(book_name):
    writers = {}
    file = open(book_name, 'r', encoding='utf-8')
    morph = pymorphy2.MorphAnalyzer()
    for line in file.readlines():
        for word in filter(lambda x: x, re.split('[^\wW]', line)):
            for mean in morph.parse(word):
                if mean.score >= 0.1:
                    pos = mean.tag.POS
                    if pos not in writers:
                        file = open('%s.csv', 'wb')
                        writers[pos] = csv.writer(file, delimiter=',')
                    writers[pos].writerow()
                    print('%s %s %f' % (word, mean.tag.POS, mean.score))




if __name__ == '__main__':
    # solve(sys.argv[1])
    solve('decameron_test.txt')