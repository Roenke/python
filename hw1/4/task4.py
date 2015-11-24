#! /usr/bin/env python3

import random


class Node(object):
    def __init__(self, value):
        levels = 1
        while random.random() >= 0.5:
            levels += 1
        self.height = levels
        self.next = [None] * levels
        self.value = value


class SkipList(object):
    def __init__(self):
        self._head = Node(None)
        self.__size = 0

    def insert(self, item):
        """
        >>> sl = SkipList()
        >>> sl.insert(1), sl.insert(2)
        (True, True)
        >>> sl.insert(1)
        False
        """
        if self.contains(item):
            return False

        current_node = self._head
        new_node = Node(item)
        current_level = min(self._head.height - 1, new_node.height - 1)
        if new_node.height > self._head.height:
            new_level_count = new_node.height - self._head.height
            self._head.height += new_level_count
            self._head.next.extend([new_node] * new_level_count)

        while current_level >= 0:
            next_node = current_node.next[current_level]
            if next_node is None:
                if new_node.height > current_level:
                    current_node.next[current_level] = new_node
                current_level -= 1
                continue
            if next_node.value > item:
                # Move down
                new_node.next[current_level] = next_node
                current_node.next[current_level] = new_node
                current_level -= 1
            else:
                # Move right
                current_node = next_node
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
        if not self.contains(item):
            return False

        current_level = self._head.height - 1
        current_node = self._head
        deleted = None
        while current_level >= 0:
            if current_node.next[current_level] is None:
                current_level -= 1
                continue
            if current_node.next[current_level].value < item:
                current_level -= 1
                continue
            if current_node.next[current_level].value > item:
                current_node = current_node.next[current_level]
                continue
            if not deleted:
                deleted = current_node.next[current_level]
            current_node.next[current_level] = deleted.next[current_level]
            current_level -= 1

        self.__size -= 1
        del deleted
        return True

    def contains(self, item):
        """
        >>> sl = SkipList()
        >>> sl.insert(1), sl.insert(2)
        (True, True)
        >>> sl.contains(1), sl.contains(3)
        (True, False)
        """
        levels = len(self._head.next)
        level = levels - 1
        current = self._head
        while level >= 0:
            if current.next[level] is None:
                level -= 1
                continue
            if current.next[level].value < item:
                current = current.next[level]
                continue
            if current.next[level].value > item:
                level -= 1
                continue
            if current.next[level].value == item:
                return True

        return False

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
        return self.__size

    def __iter__(self):
        def get_next(node):
            while node:
                yield node.value
                node = node.next[0]

        return get_next(self._head.next[0])


def make_skip_list(seq):
    """
    >>> make_skip_list([]).size()
    0
    >>> make_skip_list(range(10)).size()
    10
    >>> make_skip_list([10] * 10).size()
    1
    >>> sum(make_skip_list(range(10**5)))
    4999950000
    """
    skip_list = SkipList()
    for s in sorted(seq, reverse=True):
        skip_list.insert(s)
    return skip_list


def make_list(skip_list):
    """
    >>> make_list(SkipList())
    []
    >>> make_list(make_skip_list(range(3, 0, -1)))
    [1, 2, 3]
    >>> sum(make_list(make_skip_list(range(10**5))))
    4999950000
    """
    return list(skip_list)


if __name__ == '__main__':
    import doctest

    doctest.testmod()
