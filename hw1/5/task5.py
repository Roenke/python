#! /usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import defaultdict, Counter

import csv
import re

import pymorphy2
import sys


def solve(book_name):
    morph = pymorphy2.MorphAnalyzer()
    results = defaultdict(Counter)
    with open(book_name, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            for word in filter(lambda x: x, re.split("[^\wW]", line)):
                for mean in morph.parse(word):
                    if mean.score >= 0.1 and mean.tag.POS is not None:
                        pos = mean.tag.POS
                        results[pos][mean.normal_form] += 1

    for pos, words in results.items():
        with open('%s.csv' % pos, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            key = lambda x: x[1]
            for word, fr in sorted(words.items(), key=key, reverse=True)[:10]:
                csv_writer.writerow([word, fr])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: task5.py book_name')
        exit(1)
    solve(sys.argv[1])
