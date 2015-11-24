#! /usr/bin/env python3

import random


class Node(object):
    def __init__(self, value):
        levels = 1
        while random.random() >= 0.5:
            levels += 1
        self.levels = [None] * levels
        self.value = value


class SkipList(object):
    def __init__(self):
        self._head = Node(None)
        self.__size = 0

    def _find_last_less(self, item, level):
        node = self._head
        while node.levels[level] and node.levels[level].elem < item:
            node = node.levels[level]
        return node

    def insert(self, item):
        """
        >>> sl = SkipList()
        >>> sl.insert(1), sl.insert(2)
        (True, True)
        >>> sl.insert(1)
        False
        """
        update = self._path_to_less(item)
        if self.__size > 0 and update[0].next[0] is not None and \
                update[0].next[0].elem == item:
            return False
        height = self._random_height()
        new = self._SkipNode(item, height)
        min_height = min(len(update), height)
        for level in range(min_height):
            new.next[level] = update[level].next[level]
            update[level].next[level] = new
        self.head.next += [new] * (height - self.head.height())
        self.__size += 1
        return True


    def remove(self, item):
        """
        >>> sl = SkipList()
        >>> sl.insert(1), sl.insert(2)
        (True, True)
        >>> sl.remove(1), sl.remove(1), sl.remove(3)
        (True, False, False)
        """
        pass

    def contains(self, item):
        """
        >>> sl = SkipList()
        >>> sl.insert(1), sl.insert(2)
        (True, True)
        >>> sl.contains(1), sl.contains(3)
        (True, False)
        """
        pass

    def size(self):
        """
        >>> sl = SkipList()
        >>> sl.size()
        0
        >>> sl.insert(1), sl.insert(1)
        (True, False)
        >>> sl.size()
        1
        >>> sl.insert(2)
        True
        >>> sl.size()
        2
        """
        pass

    def __iter__(self):
        pass


def make_skip_list(seq):
    """
    >>> make_skip_list([]).size()
    0
    >>> make_skip_list(range(10)).size()
    10
    >>> make_skip_list([10] * 10).size()
    1
    >>> sum(make_skip_list(range(10**6)))
    499999500000
    """
    pass


def make_list(skip_list):
    """
    >>> make_list(SkipList())
    []
    >>> make_list(make_skip_list(range(3, 0, -1)))
    [1, 2, 3]
    >>> sum(make_list(make_skip_list(range(10**6))))
    499999500000
    """
    return list(skip_list)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
