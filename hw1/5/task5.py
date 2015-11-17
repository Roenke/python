#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import re

import pymorphy2
import sys


def solve(book_name):
    file = open(book_name, 'r', encoding='utf-8')
    morph = pymorphy2.MorphAnalyzer()
    results = dict()
    for line in file.readlines():
        for word in filter(lambda x: x, re.split("[^\wW]", line)):
            for mean in morph.parse(word):
                if mean.score >= 0.1 and mean.tag.POS is not None:
                    pos = mean.tag.POS
                    if pos not in results:
                        results[pos] = dict()
                    if mean.normal_form not in results[pos]:
                        results[pos][mean.normal_form] = 0
                    results[pos][mean.normal_form] += 1

    for pos, words in results.items():
        with open('%s.csv' % pos, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for word, freq in sorted(words.items(), key=lambda x: x[1], reverse=True)[:10]:
                csv_writer.writerow([word, freq])


if __name__ == '__main__':
    solve(sys.argv[1])
