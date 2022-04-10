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


if __name__ == '__main__':
    unittest.main()
