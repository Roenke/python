#! /usr/bin/env python3

class node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __iter__(self):
        return inorder(self)

def inorder(t):
    if t:
        yield from inorder(t.left)
        yield t.value
        yield from inorder(t.right)


def main():
    n1 = node(7)
    n2 = node(3)
    n3 = node(1)
    n4 = node(7)
    n5 = node(5, n1, n2)
    n6 = node(2, n3, n4)
    n7 = node(4, None, n6)
    root = node(1, n5, n7)
    result = list(root)
    print(result)

if(__name__ == "__main__"):
    main()
