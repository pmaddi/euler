'''
Generating all the pairs of words that are anagrams:
    go through each word and scan. n^2, but only 2k words.

Need to generate the square number anagrams too?

Then go through each pair and each square of the right length and see if the
mapping works??

2000^2 *

'''

from pathlib import Path


DIGITS = 5


def repositionings(a, b):
    '''The new indexes of elements in a mapped to b'''
    out = ""
    for c in a:
        out = out + str(b.index(c))
    return out


def test_repositionings():
    assert(repositionings('abc', 'cba') == '210')
    assert(repositionings('', '') == '')


def identity(x):
    return x


def anagrams(items, keyfn=identity, valuefn=identity):
    a = {}
    for i in items:
        key = ''.join(sorted(keyfn(i)))
        v = a.get(key, [])
        v += [valuefn(i)]
        a[key] = v
    return {k: v for k, v in a.items() if len(v) > 1}


def test_anagrams():
    assert(anagrams(['abc', 'a', 'd']) == {})
    assert(len(anagrams(['abc', 'cba', 'd'])) == 1)


def word_anagrams():
    # Word anagrams
    words = Path('p098_words.txt').read_text().replace('"', '').split(',')
    a = anagrams(words)
    for k, v in a.items():
        if len(v[0]) != DIGITS:
            continue
        for i in v:
            for j in v:
                if i == j:
                    continue
                yield(i, j, repositionings(i, j))


def digit_anagrams():
    rng = range(int((10 ** (DIGITS - 1)) ** .5), int((10 ** DIGITS) ** .5) + 1)
    a = anagrams(rng, keyfn=lambda x: str(x ** 2), valuefn=lambda x: x ** 2)
    for k, v in a.items():
        if len(str(v[0])) != DIGITS:
            continue
        for i in v:
            for j in v:
                if i == j:
                    continue
                yield(i, j, repositionings(str(i), str(j)))


def comb():
    dig = list(digit_anagrams())
    wor = list(word_anagrams())
    for w in wor:
        for d in dig:
            if w[2] == d[2]:
                print(w, d)


if __name__ == '__main__':
    comb()
