#! /usr/bin/env python3

import random


class Node(object):
    def __init__(self, value, left=None, right=None):
        self.__left = left
        self.__right = right
        self.__value = value

    def __iter__(self):
        if self.__left:
            yield from self.__left

        yield self.__value

        if self.__right:
            yield from self.__right

    def __contains__(self, item):
        if self.__value == item:
            return True
        if item > self.__value:
            return item in self.__right
        return item in self.__left

    def __add__(self, value):
        if value == self.__value:
            return self
        if value < self.__value:
            if not self.__left:
                self.__left = Node(value)
            else:
                self.__left += value
        else:
            if not self.__right:
                self.__right = Node(value)
            else:
                self.__right += value
        return self


class Tree(object):
    def __init__(self):
        self.__root = None

    def __add__(self, value):
        if isinstance(value, int) or isinstance(value, float):
            if self.__root:
                self.__root += value
            else:
                self.__root = Node(value)
        
        if isinstance(value, Tree):
            for node in value:
                self.__root += node

        return self

    def __contains__(self, item):
        return item in self.__root

    def __iter__(self):
        yield from self.__root


def main():
    tree = Tree()

    for i in range(30):
        tree += int(random.uniform(1, 100))

    dfs = list(tree)

    print('|'.join([str(x) for x in dfs]))


if __name__ == "__main__":
    main()
