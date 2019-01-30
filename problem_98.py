'''
Generating all the pairs of words that are anagrams:
    go through each word and scan. n^2, but only 2k words.

Need to generate the square number anagrams too?

Then go through each pair and each square of the right length and see if the
mapping works??

2000^2 *

'''

from pathlib import Path

words = Path('p098_words.txt').read_text().replace('"', '').split(',')
a = {}

def word_anagrams():
    # Word anagrams
    for w in words:
        k = ''.join(sorted(w))
        v = a.get(k, [])
        v += [w]
        a[k] = v
    b = {}
    mlen = 0
    for k, v in a.items():
        if len(v) > 1:
            if len(v[0]) == 9:
                print(v)

def digit_anagrams():
    a = {}
    for i in range(int((10 ** 8) ** .5), int((10 ** 9) ** .5) + 1):
        sq = i ** 2
        sqstr = ''.join(sorted(str(sq)))
        v = a.get(sqstr, [])
        v += [sqstr]
        a[sqstr] = v
    cnt = 0
    for k, v in a.items():
        if len(v) > 1:
            if len(v[0]) == 9:
                if len(set(v[0])) == 9:
                    print(v)
                    cnt += 1
    print(cnt)
if __name__ == '__main__':
    digit_anagrams()
