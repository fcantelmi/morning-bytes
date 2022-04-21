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


def all(root):
    return startswith(root, '')


def to_json(node):
    return json.dumps(node, indent=2)


if __name__ == '__main__':

    scrabble_two_letter_words = """
    aa, ab, ad, ae, ag, ah, ai, al, am, an, 
    ar, as, at, aw, ax, ay, ba, be, bi, bo, 
    by, da, de, do, ed, ef, eh, el, em, en, 
    er, es, et, ew, ex, fa, fe, gi, go, ha, 
    he, hi, hm, ho, id, if, in, is, it, jo, 
    ka, ki, la, li, lo, ma, me, mi, mm, mo, 
    mu, my, na, ne, no, nu, od, oe, of, oh, 
    oi, ok, om, on, op, or, os, ow, ox, oy, 
    pa, pe, pi, po, qi, re, sh, si, so, ta, 
    te, ti, to, uh, um, un, up, us, ut, we, 
    wo, xi, xu, ya, ye, yo, za"""

    r = {}
    s = {}
    for w in scrabble_two_letter_words.split(','):
        add(r, w.strip())
        add(s, w.strip()[::-1])

    print(sorted(startswith(r, 'a')))
    print(sorted(startswith(r, 'c')))
    print(sorted(startswith(r, 'y')))
    print(sorted(startswith(r, 'ye')))
    print(sorted(startswith(r, 'z')))
    print(sorted(startswith(r, '')))
    print(len(startswith(r, '')))
    print()
    print(to_json(r))
    print(to_json(s))
    print()

    wordle_202201 = "LIGHT,WRUNG,COULD,PERKY,MOUNT,WHACK,SUGAR,KNOLL,CRIMP,WINCE,PRICK,ROBOT,POINT,PROXY,SHIRE,SOLAR," \
                    "PANIC,TANGY,ABBEY,FAVOR,DRINK,QUERY,GORGE,CRANK,SLUMP,BANAL,TIGER,SIEGE,TRUSS,BOOST,REBUS "

    rt = {}
    for w in wordle_202201.split(','):
        add(rt, w.lower())

    print(to_json(rt))
    print(startswith(rt, 'p'))
    print(startswith(rt, 'pr'))
    print(startswith(rt, 'pro'))
    print(to_json(find(rt, 'c')))
    print(to_json(find(rt, 'crank')))
    print(to_json(find(rt, 'cranz')))
    print(to_json(find(rt, 's')))

    top = {}
    add(top, 'she')
    add(top, 'sells')
    add(top, 'sea')
    # add(top, 'shells')
    print(to_json(top))
