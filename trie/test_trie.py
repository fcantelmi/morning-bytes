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

    def test_everything(self):
        root = {}
        self.assertSetEqual(set(), trie.everything(root))
        expected1 = 'bat'
        expected2 = 'bar'
        self.assertFalse(trie.contains(root, expected1))
        self.assertFalse(trie.contains(root, expected2))
        trie.add(root, expected1)
        trie.add(root, expected2)

        self.assertSetEqual({expected1, expected2}, trie.everything(root))

    def test_startswith(self):
        root = {}
        self.assertSetEqual(set(), trie.everything(root))
        expected1 = 'foo'
        expected2 = 'bar'
        expected3 = 'baz'

        trie.add(root, expected1)
        trie.add(root, expected2)
        trie.add(root, expected3)

        self.assertSetEqual({expected2, expected3}, trie.startswith(root, 'ba'))
        self.assertSetEqual(set(), trie.startswith(root, 'z'))

    def test_startswith_empty_list(self):
        root = {}
        self.assertSetEqual(set(), trie.everything(root))
        self.assertSetEqual(set(), trie.startswith(root, 'z'))

    # @unittest.skip("count not implemented yet")
    def test_count(self):
        root = {}

        self.assertEqual(0, trie.count(root))
        trie.add(root, 'a')
        self.assertEqual(1, trie.count(root))
        trie.add(root, 'b')
        self.assertEqual(2, trie.count(root))
        trie.add(root, 'c')
        self.assertEqual(3, trie.count(root))
        trie.add(root, 'd')
        self.assertEqual(4, trie.count(root))

    @unittest.skip("prefix words are not implemented yet")
    def test_she_shells(self):
        root = {}
        self.assertSetEqual(set(), trie.everything(root))

        expected1 = 'she'
        expected2 = 'sells'
        expected3 = 'sea'
        expected4 = 'shells'

        trie.add(root, expected1)
        trie.add(root, expected2)
        trie.add(root, expected3)
        trie.add(root, expected4)

        self.assertSetEqual({expected1, expected2, expected3, expected4}, trie.everything(root))


if __name__ == '__main__':
    unittest.main()
