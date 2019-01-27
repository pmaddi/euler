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
print(max(len(w) for w in words))
