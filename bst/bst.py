import collections.abc
from typing import Iterator


class BinarySearchTree(collections.abc.MutableSet):

    def __init__(self, iterable=None):
        self.key = None
        self.left = None
        self.right = None
        if iterable is not None:
            for key in iterable:
                self.add(key)

    def __contains__(self, key) -> bool:
        return key in self.everything()

    def __len__(self) -> int:
        return len(self.everything())

    def __iter__(self):
        return iter(self.everything())

    def add(self, key):
        if self.key is None:
            self.key = key
        elif key < self.key:
            if self.left is None:
                self.left = BinarySearchTree({key})
            else:
                self.left.add(key)
        elif key > self.key:
            if self.right is None:
                self.right = BinarySearchTree({key})
            else:
                self.right.add(key)
        else:
            pass  # duplicate key

    def discard(self, key):
        pass

    def max(self):
        if self.right is None:
            return self.key
        else:
            return self.right.max()

    def collect(self, keys):
        if self.left:
            self.left.collect(keys)

        keys.append(self.key)

        if self.right:
            self.right.collect(keys)

    def everything(self):
        keys = []
        self.collect(keys)
        return keys


class SortedSet(collections.abc.Set):

    def __contains__(self, x: object) -> bool:
        pass

    def __len__(self) -> int:
        pass

    def __iter__(self) -> Iterator:
        pass


def main():
    root = BinarySearchTree()
    root.add('cat')
    root.add('bunny')
    root.add('dog')
    root.add('dog')
    root.add('parrot')
    root.add('monkey')
    print(root.everything())
    print(root.max())

    for key in root:
        print(key)

    print(len(root))

    ts = BinarySearchTree()
    ts.add(0)
    ts.add(-1)
    ts.add(1)
    print(ts.everything())


if __name__ == '__main__':
    main()
