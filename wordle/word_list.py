def add_node(word, node):
    if len(word) > 0:
        head = word[0]
        tail = word[1:]
        if head not in node:
            node[head] = {}
        add_node(tail, node[head])


def contains_node(word, node):
    if len(word) > 0:
        head = word[0]
        tail = word[1:]
        if head in node:
            return contains_node(tail, node[head])
        else:
            return False
    else:
        return True


class WordList:

    def __init__(self):
        self.trie = {}

    def __str__(self):
        return str(self.trie)

    def add(self, word):
        add_node(word, self.trie)

    def contains(self, word):
        return contains_node(word, self.trie)
