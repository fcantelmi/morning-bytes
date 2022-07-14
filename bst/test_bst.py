import unittest

from bst import BinarySearchTree


class TestBinarySearchTree(unittest.TestCase):

    def test_add(self):
        expected_word = 'bat'
        bst = BinarySearchTree()
        self.assertNotIn(expected_word, bst)
        bst.add(expected_word)
        self.assertIn(expected_word, bst)

    def test_add_two_words(self):
        expected1 = 'cat'
        expected2 = 'dog'
        bst = BinarySearchTree()
        self.assertNotIn(expected1, bst)
        self.assertNotIn(expected2, bst)
        bst.add(expected1)
        bst.add(expected2)
        self.assertIn(expected1, bst)
        self.assertIn(expected2, bst)

    def test_len(self):
        expected1 = 'cat'
        expected2 = 'dog'
        bst = BinarySearchTree()
        bst.add(expected1)
        self.assertIn(expected1, bst)
        self.assertEqual(1, len(bst))
        bst.add(expected2)
        self.assertIn(expected2, bst)
        self.assertEqual(2, len(bst))

    def test_max(self):
        # empty tree
        bst = BinarySearchTree()
        self.assertIsNone(bst.max())

        # one node tree
        bst = BinarySearchTree([514])
        self.assertEqual(514, bst.max())

        # root without right child is the max
        bst = BinarySearchTree([514, 426])
        self.assertEqual(514, bst.max())

        # root with right child requires recursion
        bst = BinarySearchTree([426, 514])
        self.assertEqual(514, bst.max())

    @unittest.skip("min not implemented yet")
    def test_min(self):
        # empty tree
        bst = BinarySearchTree()
        self.assertIsNone(bst.min())

        # one node tree
        bst = BinarySearchTree([514])
        self.assertEqual(514, bst.min())

        # root with left child requires recursion
        bst = BinarySearchTree([514, 426])
        self.assertEqual(426, bst.min())

        # root without left child is the min
        bst = BinarySearchTree([426, 514])
        self.assertEqual(426, bst.min())


if __name__ == '__main__':
    unittest.main()
