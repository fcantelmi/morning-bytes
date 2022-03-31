import unittest

import word_list


class TestWordList(unittest.TestCase):
    def setUp(self):
        self.words = {'foo', "bar", "baz"}

    def test_add(self):
        expected_word = "bat"
        wl = word_list.WordList(self.words)
        self.assertFalse(wl.contains(expected_word))
        wl.add(expected_word)
        self.assertTrue(wl.contains(expected_word))

    def test_remove(self):
        expected_word = "foo"
        wl = word_list.WordList(self.words)
        self.assertTrue(wl.contains(expected_word))
        wl.remove(expected_word)
        self.assertFalse(wl.contains(expected_word))


if __name__ == '__main__':
    unittest.main()
