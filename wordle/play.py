import trie

root = {}

trie.add(root, "foo")
trie.add(root, "bar")
trie.add(root, "baz")
trie.add(root, "bot")

print(trie.to_json(root))
print(trie.startswith(root, 'b'))
print(trie.startswith(root, 'ba'))
print(trie.startswith(root, 'f'))