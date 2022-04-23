import json


def add(node, word):
    if len(word) > 0:
        head = word[0]
        tail = word[1:]
        if head not in node:
            node[head] = {}
        add(node[head], tail)


def find(node, prefix):
    if len(prefix) > 0:
        head = prefix[0]
        tail = prefix[1:]
        if head in node:
            return find(node[head], tail)
        else:
            return None
    else:
        return node


def contains(node, word):
    if find(node, word) is None:
        return False
    else:
        return True


def count(node):
    if node is None:
        return 0
    elif node == {}:
        return 1
    else:
        s = 0
        for child in node.values():
            s += count(child)
        return s


def traverse_children(node, words, word):
    if node == {}:
        words.add(word)
    else:
        for letter, child in node.items():
            traverse_children(child, words, word + letter)


def startswith(root, prefix):
    node = find(root, prefix)

    if root == {} or node is None:
        return set()
    elif node == {}:
        return {prefix}
    else:
        words = set()
        traverse_children(node, words, prefix)
        return words


def everything(root):
    return startswith(root, '')


def to_json(node):
    return json.dumps(node, indent=2)
