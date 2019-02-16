from pathlib import Path


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


def get_words_anas():
    return anagrams(
            Path('p098_words.txt').read_text().replace('"', '').split(','))


def word_anagrams():
    for k, v in get_words_anas().items():
        for i in v:
            for j in v:
                if i == j:
                    continue
                yield(i, j, repositionings(i, j))


def digit_anagrams(max_digits):
    rng = range(int((10 ** max_digits) ** .5) + 1)
    a = anagrams(rng, keyfn=lambda x: str(x ** 2), valuefn=lambda x: x ** 2)
    for k, v in a.items():
        for i in v:
            for j in v:
                if i == j:
                    continue
                yield(i, j, repositionings(str(i), str(j)))


def comb():
    wor = list(word_anagrams())
    max_digits = max(len(i) for i in get_words_anas().keys())
    dig = list(digit_anagrams(max_digits))
    for w in wor:
        for d in dig:
            if w[2] == d[2]:
                yield(max(d[0:2]))


if __name__ == '__main__':
    print(max(list(comb())))
