import collections.abc


class BinarySearchTree(collections.abc.MutableSet):

    def __init__(self, iterable=None):
        self.key = None
        self.left = None
        self.right = None
        if iterable is not None:
            for key in iterable:
                self.add(key)

    def __contains__(self, key) -> bool:
        # __contains__ is invoked by the "in" operator.
        # It should return True if the key is present in the set, else False.
        #
        # We always say make it work, make it right, make it fast (I think Ken Dodd was the originator).
        # This implementation of __contains__ works by building a list with every key in the list.
        # This is very inefficient because we touch every element to find a single element.
        #
        # Let's rewrite this method to leverage the binary search tree property: the key value for the node
        # is greater than the key value for the left child node and less than the key of the right child.
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

    def min(self):
        # use the binary search tree property to implement to implement min.
        # for any node in a binary search, the key value for the node is less than the right child and
        # greater than the left child (unless there is no left child...).
        pass

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
    print([key for key in root])

    ts = BinarySearchTree()
    ts.add(0)
    ts.add(-1)
    ts.add(1)
    print(ts.everything())


if __name__ == '__main__':
    main()
