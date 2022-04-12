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


def find_node(prefix, node):
    if len(prefix) > 0:
        head = prefix[0]
        tail = prefix[1:]
        if head in node:
            return find_node(tail, node[head])
        else:
            return None
    else:
        return node


def startswith_node(words, prefix, node):
    if not node:
        words.add(prefix)
    else:
        for letter, child in node.items():
            startswith_node(words, prefix + letter, child)


class WordList:

    def __init__(self):
        self.trie = {}

    def __str__(self):
        return str(self.trie)

    def add(self, word):
        add_node(word, self.trie)

    def contains(self, word):
        return contains_node(word, self.trie)

    def find_node(self, prefix):
        pass

    def startswith(self, prefix):
        words = set()
        node = find_node(prefix, self.trie)
        if node:
            startswith_node(words, prefix, node)

        return words

    def all(self):
        return self.startswith('')
