import re


class WordList:

    @classmethod
    def parse(cls, csv):
        no_whitespace = re.sub(r'\s+', "", csv)
        values = [int(val) if val in '123456789' else None for val in no_whitespace]

        return cls([])

    def __init__(self, words):
        self.words = set(words)

    def __str__(self):
        return str(self.words)

    def add(self, word):
        self.words.add(word)

    def remove(self, word):
        self.words.remove(word)

    def contains(self, word):
        return word in self.words
