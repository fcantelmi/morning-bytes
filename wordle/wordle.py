from string import ascii_lowercase

import trie

wordle_202201 = "LIGHT,WRUNG,COULD,PERKY,MOUNT,WHACK,SUGAR,KNOLL,CRIMP,WINCE,PRICK,ROBOT,POINT,PROXY,SHIRE,SOLAR," \
                "PANIC,TANGY,ABBEY,FAVOR,DRINK,QUERY,GORGE,CRANK,SLUMP,BANAL,TIGER,SIEGE,TRUSS,BOOST,REBUS"
wordle_202202 = "CHOKE,CHANT,SPILL,VIVID,BLOKE,TROVE,THORN,OTHER,TACIT,SWILL,DODGE,SHAKE,CAULK,AROMA,CYNIC,ROBIN," \
                "ULTRA,ULCER,PAUSE,HUMOR,FRAME,ELDER,SKILL,ALOFT,PLEAT,SHARD,MOIST,THOSE"
wordle_202203 = "LOWLY,STOVE,SHALL,FOUND,NYMPH,EPOCH,DEPOT,CHEST,PURGE,SLOSH,THEIR,RENEW,ALLOW,SAUTE,MOVIE,CATER," \
                "TEASE,SMELT,FOCUS,TODAY,WATCH,LAPSE,MONTH,SWEET,HOARD,CLOTH,BRINE,AHEAD,MOURN,NASTY,RUPEE"

root = {}

for w in wordle_202201.split(','):
    trie.add(root, w.lower())
for w in wordle_202202.split(','):
    trie.add(root, w.lower())
for w in wordle_202203.split(','):
    trie.add(root, w.lower())

# print(trie.to_json(root))
print(trie.startswith(root, 's'))
print(trie.to_json(trie.find(root, 's')))
print(trie.count(root))
print()
counts = {}
for letter in ascii_lowercase:
    counts[letter] = trie.count(trie.find(root, letter))

print(counts)
