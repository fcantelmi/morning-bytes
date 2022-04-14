def add_node(node, word):
    if len(word) > 0:
        head = word[0]
        tail = word[1:]
        if head not in node:
            node[head] = {}
        add_node(node[head], tail)


def find_node(node, prefix):
    if len(prefix) > 0:
        head = prefix[0]
        tail = prefix[1:]
        if head in node:
            return find_node(node[head], tail)
        else:
            return None
    else:
        return node


def contains_node(node, word):
    if find_node(node, word) is None:
        return False
    else:
        return True


def startswith_node(node, words, prefix):
    if not node:
        words.add(prefix)
    else:
        for letter, child in node.items():
            startswith_node(child, words, prefix + letter)


class WordList:

    def __init__(self):
        self.trie = {}

    def __str__(self):
        return str(self.trie)

    def add(self, word):
        add_node(self.trie, word)

    def contains(self, word):
        return contains_node(self.trie, word)

    def startswith(self, prefix):
        words = set()
        node = find_node(self.trie, prefix)
        if node:
            startswith_node(node, words, prefix)

        return words

    def all(self):
        return self.startswith('')
