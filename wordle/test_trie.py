import unittest

import trie


class TestTrie(unittest.TestCase):

    def test_add(self):
        expected_word = 'bat'
        root = {}
        self.assertFalse(trie.contains(root, expected_word))
        trie.add(root, expected_word)
        self.assertTrue(trie.contains(root, expected_word))

    def test_add_two_words_same_stem(self):
        root = {}
        expected1 = 'bat'
        expected2 = 'bar'
        self.assertFalse(trie.contains(root, expected1))
        self.assertFalse(trie.contains(root, expected2))
        trie.add(root, expected1)
        trie.add(root, expected2)
        self.assertTrue(trie.contains(root, expected1))
        self.assertTrue(trie.contains(root, expected2))

    def test_all(self):
        root = {}
        self.assertSetEqual(set(), trie.all(root))
        expected1 = 'bat'
        expected2 = 'bar'
        self.assertFalse(trie.contains(root, expected1))
        self.assertFalse(trie.contains(root, expected2))
        trie.add(root, expected1)
        trie.add(root, expected2)

        self.assertSetEqual({expected1, expected2}, trie.all(root))

    def test_startswith(self):
        root = {}
        self.assertSetEqual(set(), trie.all(root))
        expected1 = 'foo'
        expected2 = 'bar'
        expected3 = 'baz'

        trie.add(root, expected1)
        trie.add(root, expected2)
        trie.add(root, expected3)

        self.assertSetEqual({expected2, expected3}, trie.startswith(root, 'ba'))

    def test_startswith_prefix_not_present(self):
        root = {}
        self.assertSetEqual(set(), trie.all(root))
        expected1 = 'foo'
        expected2 = 'bar'
        expected3 = 'baz'

        trie.add(root, expected1)
        trie.add(root, expected2)
        trie.add(root, expected3)

        self.assertSetEqual(set(), trie.startswith(root, 'z'))

    def test_startswith_empty_list(self):
        root = {}
        self.assertSetEqual(set(), trie.all(root))
        self.assertSetEqual(set(), trie.startswith(root, 'z'))


if __name__ == '__main__':
    unittest.main()
