import unittest

import word_list


class TestWordList(unittest.TestCase):

    def setUp(self):
        self.wl = word_list.WordList()

    def test_add(self):
        expected_word = 'bat'
        self.assertFalse(self.wl.contains(expected_word))
        self.wl.add(expected_word)
        self.assertTrue(self.wl.contains(expected_word))

    def test_add_two_words_same_stem(self):
        expected1 = 'bat'
        expected2 = 'bar'
        self.assertFalse(self.wl.contains(expected1))
        self.assertFalse(self.wl.contains(expected2))
        self.wl.add(expected1)
        self.wl.add(expected2)
        self.assertTrue(self.wl.contains(expected1))
        self.assertTrue(self.wl.contains(expected2))

    def test_all(self):
        # self.assertSetEqual(set(), self.wl.all())

        expected1 = 'bat'
        expected2 = 'bar'
        self.assertFalse(self.wl.contains(expected1))
        self.assertFalse(self.wl.contains(expected2))
        self.wl.add(expected1)
        self.wl.add(expected2)

        self.assertSetEqual({expected1, expected2}, self.wl.all())

    def test_startswith(self):
        self.assertSetEqual(set(), self.wl.all())
        expected1 = 'foo'
        expected2 = 'bar'
        expected3 = 'baz'

        self.wl.add(expected1)
        self.wl.add(expected2)
        self.wl.add(expected3)

        self.assertSetEqual({expected2, expected3}, self.wl.startswith('ba'))

    def test_startswith_prefix_not_present(self):
        self.assertSetEqual(set(), self.wl.all())
        expected1 = 'foo'
        expected2 = 'bar'
        expected3 = 'baz'

        self.wl.add(expected1)
        self.wl.add(expected2)
        self.wl.add(expected3)

        self.assertSetEqual(set(), self.wl.startswith('z'))

    def test_startswith_empty_list(self):
        self.assertSetEqual(set(), self.wl.all())
        self.assertSetEqual(set(), self.wl.startswith('z'))


if __name__ == '__main__':
    unittest.main()
